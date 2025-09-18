# Copilot Instructions for Ollama3.2 Codebase

## Overview
This project is a set of local AI chatbot interfaces using Gradio and Ollama. It provides multiple UIs for interacting with various Ollama models, supporting real-time streaming responses and custom layouts.

## Architecture & Key Files
- `code_base.py`: Main Gradio chat interface using a system prompt and customizable avatars. Streams responses from Ollama models. Contains model selection and CSS customization.
- `tk_web.py`: Alternative Gradio UI with custom layout, button placement, and streaming chat. Uses a different model and layout logic.
- `test_1.py`: Example/test interface for Qwen model, with custom avatars and CSS. Useful for reference implementations.
- Image files (`llama logo.png`, `qwen.png`, `user.jpg`): Used as avatars in chat interfaces.

## Developer Workflows
- **Run Locally:** Launch any `.py` file directly to start a Gradio web UI. No build step required.
- **Model Management:** Models must be downloaded via the official Ollama site before use. Update the `MODEL` variable in each script to switch models.
- **Testing:** No formal test suite; use `test_1.py` for manual interface validation.
- **Debugging:** Modify the Python files and relaunch. Warnings are suppressed for cleaner output.

## Project-Specific Patterns
- **Gradio ChatInterface:** All chatbots use Gradio's `ChatInterface` with a custom `chat_with_ollama` function. This function converts Gradio history to Ollama format and streams responses.
- **Streaming Responses:** Responses are streamed for a "typing" effect using Ollama's `stream=True` parameter.
- **Avatar Images:** Avatars are set via the `avatar_images` parameter in Gradio's `Chatbot`.
- **CSS Customization:** Custom CSS is used for UI theming. See `simple_css` in each file.
- **System Prompt:** In `code_base.py`, a system prompt guides the assistant's behavior. Other files may use direct AI responses.

## Integration Points
- **Ollama:** All chat logic is handled via the `ollama.chat` API. Ensure models are available locally.
- **Gradio:** Used for all UI components and event handling.

## Conventions
- **Function Signature:** `chat_with_ollama(message, history)` is required for Gradio compatibility.
- **Model Selection:** Change the `MODEL` variable to switch between available models.
- **Suppress Warnings:** Warnings are suppressed globally for a cleaner UI experience.

## Example Patterns
```python
# Streaming response from Ollama
stream = ollama.chat(model=MODEL, messages=messages, stream=True)
for chunk in stream:
    if 'message' in chunk and 'content' in chunk['message']:
        token = chunk['message']['content']
        partial_response += token
        yield partial_response
```

## Quick Start
1. Download desired Ollama models.
2. Run any `.py` file to launch the chatbot UI.
3. Access the Gradio interface in your browser.

---
_If any section is unclear or missing, please provide feedback to improve these instructions._
