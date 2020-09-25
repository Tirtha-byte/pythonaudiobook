import pyttsx3
import PyPDF2
book = open('story.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()


for num in range(1,pages):
 page = pdfReader.getPage(1)
text = page.extractText()

speaker.say(text)
speaker.runAndWait()