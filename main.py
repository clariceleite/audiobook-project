import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
reader = PdfReader(book)
pages = len(reader.pages)

for num in range(pages):
    page = reader.pages[num]
    text = page.extract_text()
    
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Page {num + 1} is empty or could not be read.")