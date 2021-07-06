#import pyttsx3 Uncomment this line if you are using Ubuntu or any other linux distro.
import PyPDF2
book = open('Sample.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate',100)
page=pdfreader.getPage(6)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()
