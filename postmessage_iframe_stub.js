// postmessage_iframe_stub.js

// Simulates the Mantis iframe postMessage API
// Use this as a stub or testing utility in dev environments

const mantisIframe = {
    contentWindow: {
        postMessage: (message, targetOrigin = "*") => {
            console.log("[Mantis Iframe Stub] postMessage called:", message);
        }
    }
};

// Simulated command wrappers
function loadExperience(url) {
    mantisIframe.contentWindow.postMessage({
        type: "loadExperience",
        payload: { url }
    });
}

function goToScene(sceneId) {
    mantisIframe.contentWindow.postMessage({
        type: "goToScene",
        payload: { sceneId }
    });
}

function updateScene(data) {
    mantisIframe.contentWindow.postMessage({
        type: "updateScene",
        payload: data
    });
}

function getCurrentScene(callback) {
    // Simulate async return
    setTimeout(() => callback("sample-scene-id"), 300);
}

// Export for test or agent usage
module.exports = {
    loadExperience,
    goToScene,
    updateScene,
    getCurrentScene
};
