# Example: Sneaker Store Prompt → Mantis Agent Tools

## 🗣️ Sample User Prompt

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
```

2. **Navigate to product spotlight scene**
```json
{
  "function": "go_to_scene",
  "arguments": {
    "sceneId": "spotlight"
  }
}
```

3. **Update logo in scene**
```json
{
  "function": "update_scene",
  "arguments": {
    "data": {
      "logo": "https://adidas.com/logo.png"
    }
  }
}
```

---

## 🔍 Why This Matters

AI tools (LangChain, GPT-4o, v0.dev, etc.) use natural language to call these functions.  
This file shows **how to structure your requests** or agent instructions to work seamlessly with Mantis.

Want more examples? Add them here.
