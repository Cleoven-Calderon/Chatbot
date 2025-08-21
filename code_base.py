import gradio as gr
import ollama

MODEL = "qwen2.5-coder:3b"  # Current available models: qwen2.5-coder:3b, llama3.2:1b, qwen3:4b

simple_css = """

.gradio-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    min-height: 100vh;
    padding: 20px;

}
"""
system_prompt = ("You are a helpful assistant that provides concise, direct answers. "
                 "Keep responses brief and to the point. Avoid unnecessary explanations and wordiness.")


def chat_with_ollama(message, history):
    """Correct function signature for ChatInterface"""

    # Convert Gradio history format to Ollama format
    messages = []
    for human_msg, ai_msg in history:
        messages.append({"role": "user", "content": human_msg})
        if ai_msg:  # Add AI response if it exists
            messages.append({"role": "assistant", "content": system_prompt})
    messages.append({"role": "user", "content": message})

    # Stream the response
    partial_response = ""
    stream = ollama.chat(
        model=MODEL,
        messages=messages,
        stream=True
    )

    # Yield each token as it arrives
    for chunk in stream:
        if 'message' in chunk and 'content' in chunk['message']:
            token = chunk['message']['content']
            partial_response += token
            yield partial_response


# Create the interface
demo = gr.ChatInterface(
    chat_with_ollama,
    title="Qwen-Codify 2.5",
    description="Local Ai assistant feat. qwen2.5",
    theme="soft",
    css=simple_css,
    examples=[["Hello!"], ["How LLMs work?"], ["Need help with Python code."]],
    example_labels=[
        "👋 Greetings!",
        "🧠 Explain LLMs.",
        "🐍 Help me program."],

    chatbot=gr.Chatbot(
        height=500,
        avatar_images=(
            "llama logo.png",
            "qwen.png"
        )
    )
)

demo.launch(share=False)
