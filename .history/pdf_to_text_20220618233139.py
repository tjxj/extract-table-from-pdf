from gtts import gTTS
from pdfminer.high_level import extract_text
import gradio as gr

def pdf_to_text(file_obj):
   text = extract_text(file_obj.name)
   myobj = gTTS(text=text, lang='en', slow=False)
   myobj.save("output.wav")
   return 'output.wav'

iface = gr.Interface(
   fn = pdf_to_text,
   inputs = 'file',
   outputs = 'audio'
   )
iface.launch()