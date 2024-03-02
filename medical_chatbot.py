# !pip install openai==0.28
# !pip install gradio

import openai
import gradio
# openai.api_key = "Token-from_OpenAI"
openai.api_key = "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"
def initialize_messages():
    return [{"role": "system",
             "content": "You are a doctor of a multispecialty hospital and you should give medical advice, also suggest appropriate medications"}]
messages = initialize_messages()
def CustomChatGPT(user_input, history):
    global messages

    messages = initialize_messages()  # Reset the entire conversation history
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(response)
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    return ChatGPT_reply
iface = gradio.ChatInterface(CustomChatGPT,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a medical question"),
                     title="DocBot",
                     description="Chat bot for medical assistance",
                     theme="hard",
                     examples=["hi","How to stay healthy", "What to do in cases of a cardiac arrest"],
                     cache_examples=True,
                     retry_btn=None,
                     undo_btn="Delete Previous",
                     clear_btn="Clear",
                     )
iface.launch(share=True)








