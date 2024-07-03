import gradio as gr
from chatbot import bot


demo = gr.Interface(fn=bot, inputs="textbox", outputs="textbox")
demo.launch(share=True)