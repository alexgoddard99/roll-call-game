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
           { getFirestore, doc, setDoc, getDocs, collection },
           { getAnalytics, isSupported, logEvent }] = await Promise.all([
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js"),
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-auth.js"),
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-firestore.js"),
      import("https://www.gstatic.com/firebasejs/11.1.0/firebase-analytics.js"),
    ]);

    const app = initializeApp(cfg);
    const auth = getAuth(app);
    const db = getFirestore(app);
    let analytics = null;
    if (cfg.measurementId) {
      isSupported().then((ok) => { if (ok) analytics = getAnalytics(app); }).catch(() => {});
    }

    let user = null;
    const userListeners = [];
    onAuthStateChanged(auth, (u) => {
      user = u;
      userListeners.forEach((fn) => fn(user));
    });

    expose({
      enabled: true,
      user: () => user,
      onUser(fn) { userListeners.push(fn); fn(user); },
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
      logEvent(name, params) {
        try { if (analytics) logEvent(analytics, name, params); } catch (e) {}
      },
    });
  } catch (e) {
    console.warn("Yea or Nay: cloud layer failed to load", e);
    expose({ enabled: false });
  }
}
