from langchain.tools import tool

@tool
def load_experience(url: str) -> str:
    """Load a Mantis 3D storefront experience by URL."""
    # Placeholder: Simulates postMessage to iframe
    return f"Loaded experience from {url}"

@tool
def go_to_scene(sceneId: str) -> str:
    """Navigate to a specific scene in the Mantis experience."""
    return f"Navigated to scene {sceneId}"

@tool
def update_scene(data: dict) -> str:
    """Update elements in the current scene (e.g., logo, video)."""
    return f"Updated scene with {data}"

@tool
def get_current_scene() -> str:
    """Returns the current scene (stubbed)."""
    return "current-scene-id"
