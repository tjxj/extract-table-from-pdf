import gradio as gr

def image_classifier(inp):
    pass  # image classifier model defined here
gr.Interface(fn=image_classifier, inputs="image", outputs="label")