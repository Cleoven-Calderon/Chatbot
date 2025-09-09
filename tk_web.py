import gradio as gr
import ollama


with gr.Blocks(title="🤖 Custom Layout Chatbot", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Ollama Chatbot")
    gr.Markdown("Custom layout with better button placement!")

    chatbot = gr.Chatbot(height=400, label="Conversation")

    # Input row with button NEXT to textbox
    with gr.Row():
        with gr.Column(scale=4):  # 80% width for textbox
            msg = gr.Textbox(
                label="Your message",
                placeholder="Type your message here...",
                show_label=False,
                lines=2,
                max_lines=5
            )
        with gr.Column(scale=1):  # 20% width for button
            send_btn = gr.Button(
                "🚀 Send",
                variant="primary",
                size="lg",
                min_width=100
            )

    clear_btn = gr.Button("🗑️ Clear Chat", variant="secondary")


    def chat_with_ollama(message, history):
        """Correct function signature for ChatInterface"""

        # Convert Gradio history format to Ollama format
        messages = []
        for human_msg, ai_msg in history:
            messages.append({"role": "user", "content": human_msg})
            if ai_msg:  # Add AI response if it exists
                messages.append({"role": "assistant", "content": ai_msg})
        messages.append({"role": "user", "content": message})

        # Stream the response
        partial_response = ""
        stream = ollama.chat(
            model='llama3.2:1b',
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
        title="🤖 Ollama Chatbot",
        description="Real-time streaming chat with local AI",
        theme="soft",
        examples=[["Hello!"], ["How LLMs work?"], ["Tell a joke"]],
    )


    demo.launch()
