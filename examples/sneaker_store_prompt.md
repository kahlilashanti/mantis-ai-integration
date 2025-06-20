# Example: Sneaker Store Prompt → Mantis Agent Tools

## 🗣️ User Prompt

> "Build a 3D storefront for a sneaker brand called 'SneakerLab'.  
> Add a product called 'StreetGlow 7s' with this image: https://example.com/sg7.jpg and this GLB: https://example.com/sg7.glb.  
> Navigate to the product spotlight scene and swap the sponsor logo to Adidas."

---

## 🤖 Agent Calls (Mapped to Mantis Tools)

1. **Create the experience**
```json
{
  "function": "load_experience",
  "arguments": {
    "url": "https://mantisxr.com/sneakerlab"
  }
}

Navigate to product spotlight scene
{
  "function": "go_to_scene",
  "arguments": {
    "sceneId": "spotlight"
  }
}


update logo in scene

{
  "function": "update_scene",
  "arguments": {
    "data": {
      "logo": "https://adidas.com/logo.png"
    }
  }
}

