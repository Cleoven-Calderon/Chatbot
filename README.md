# Local AI Chat Assistant with Ollama

A lightweight, local AI chatbot interface using Ollama and Gradio. This application allows you to interact with various Ollama models locally without relying on external APIs.

## Features
- **Local AI Processing**: Runs completely offline using Ollama
- **Streaming Responses**: Real-time token streaming for natural conversation flow
- **Customizable UI**: Beautiful gradient interface with avatar support
- **Multiple Model Support**: Easily switch between different Ollama models
- **Conversation History**: Maintains context throughout your chat session

## Prerequisites

1. **Install Ollama**
   - Download and install Ollama from [ollama.ai](https://ollama.ai/)
   - After installation, pull your preferred model:
     ```bash
     ollama pull qwen2.5-coder:3b
     ```

## Installation

### Using requirements.txt
```bash
# Clone or download the project
cd your-project-folder

# Create and activate virtual environment (recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
1. **Start the aplication:**
```bash
python app.py
```
2. **Access the interface:**
   - Open your browser and go to http://localhost:7860
   - The application will be available at this local address
     
3. **Using the chat interface:**
   - ype your message in the text box
   - Press Enter or click "Submit"
   - View streaming responses in real-time
   - Use example prompts to get started quickly
  
## Configuration

### Changing the model:
```bash
MODEL = "llama3.2"  # or any other model you have pulled
```

## Customizing the Interface
**You can modify:**
  - system_prompt in app.py to change assistant behavior
  - CSS styles in the simple_css variable
  - Avatar images (replace llama logo.png and qwen.png with your own images)
  - Example prompts and labels

## Troubleshooting
**Common Issues**
1. "Model not found" error
```bash
# Pull the model first
ollama pull qwen2.5-coder:3b
```
2. Port 7860 is already in use
```bash
# Change the launch port in app.py
demo.launch(server_port=7861, share=False)
```
3. Ollama service not running
```bash
# Start Ollama on CMD (usually runs as a service)
ollama serve
```

## File Structure
```bash
your-project/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── qwen.png           # AI avatar (optional)
└── llama logo.png     # User avatar (optional)
```

## Advanced Features
**Sharing Your Application, to create a public link (lasts 72 hours):**
```bash
demo.launch(share=True)  # Change in app.py
```

## Custom Styling
Edit the **|simple_css|** variable to change colors, padding, or add animations.

## Adding More Examples
Extend the examples and **|example_labels|** lists in the **|gr.ChatInterface()|** call.

## License
[]
