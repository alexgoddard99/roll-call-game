/* Yea or Nay — optional cloud layer: Firebase Auth (Google), Firestore sync, GA4.
   Loads only if window.YON_FIREBASE_CONFIG is set; otherwise the game runs
   fully local. Exposes window.YonCloud and fires "yon-cloud-ready". */

const cfg = window.YON_FIREBASE_CONFIG;

function expose(api) {
  window.YonCloud = api;
  window.dispatchEvent(new CustomEvent("yon-cloud-ready"));
}

if (!cfg) {
  expose({ enabled: false });
} else {
  try {
    const [{ initializeApp },
           { getAuth, GoogleAuthProvider, signInWithPopup, signOut, onAuthStateChanged },
           { getFirestore, doc, setDoc, getDoc, getDocs, collection, increment },
           { getAnalytics, isSupported, logEvent, setUserId, setUserProperties }] = await Promise.all([
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js"),
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-auth.js"),
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-firestore.js"),
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-analytics.js"),
    ]);

    const app = initializeApp(cfg);
    const auth = getAuth(app);
    const db = getFirestore(app);
    let analytics = null;
    // GA4 user identity: the Firebase UID (opaque, not PII) so a signed-in player
    // counts as one user across devices and the BigQuery export's user_id joins to
    // the users/{uid} docs. Applied once auth has settled AND analytics is up,
    // whichever comes last; null on sign-out clears it.
    let identityUid = null, identitySettled = false;
    function applyIdentity() {
      if (!analytics || !identitySettled) return;
      try {
        setUserId(analytics, identityUid);
        setUserProperties(analytics, { signed_in: identityUid ? "yes" : "no" });
      } catch (e) {}
    }
    // Analytics initialises asynchronously; events logged before then (the
    // page_open fired at yon-cloud-ready, anything the game queued during
    // boot) are held here and flushed once it is up.
    let analyticsPending = !!cfg.measurementId;
    const pendingEvents = [];
    if (cfg.measurementId) {
      isSupported().then((ok) => {
        analyticsPending = false;
        if (ok) {
          analytics = getAnalytics(app);
          applyIdentity();
          pendingEvents.splice(0).forEach(([n, p]) => logEvent(analytics, n, p));
        } else pendingEvents.length = 0;
      }).catch(() => { analyticsPending = false; pendingEvents.length = 0; });
    }

    let user = null;
    const userListeners = [];
    const settledListeners = []; // fn(user) once auth has resolved, never before
    onAuthStateChanged(auth, (u) => {
      user = u;
      identityUid = u ? u.uid : null; identitySettled = true;
      applyIdentity();
      userListeners.forEach((fn) => fn(user));
      settledListeners.splice(0).forEach((fn) => fn(user));
    });

    expose({
      enabled: true,
      user: () => user,
      onUser(fn) { userListeners.push(fn); fn(user); },
      // true once Firebase has resolved the signed-in/out state (onUser fires
      // with null before that, so UI that must not flash waits on these)
      settled: () => identitySettled,
      onAuthSettled(fn) { if (identitySettled) fn(user); else settledListeners.push(fn); },
      async signIn() {
        await signInWithPopup(auth, new GoogleAuthProvider());
      },
      async signOut() { await signOut(auth); },
      async saveResult(date, data) {
        if (!user) return;
        await setDoc(doc(db, "users", user.uid, "courtResults", date), data, { merge: true });
      },
      async fetchResults() {
        if (!user) return {};
        const snap = await getDocs(collection(db, "users", user.uid, "courtResults"));
        const out = {};
        snap.forEach((d) => { out[d.id] = d.data(); });
        return out;
      },
      // Crowd counters (collection "daily"): open to everyone, rules only
      // permit +1 increments — see firestore.rules.
      async bumpDaily(id, keys) {
        const data = {};
        keys.forEach((k) => { data[k] = increment(1); });
        await setDoc(doc(db, "daily", id), data, { merge: true });
      },
      async fetchDaily(id) {
        const snap = await getDoc(doc(db, "daily", id));
        return snap.exists() ? snap.data() : null;
      },
      logEvent(name, params) {
        try {
          if (analytics) logEvent(analytics, name, params);
          else if (analyticsPending && pendingEvents.length < 50) pendingEvents.push([name, params]);
        } catch (e) {}
      },
    });
  } catch (e) {
    console.warn("Yea or Nay: cloud layer failed to load", e);
    expose({ enabled: false });
  }
}
