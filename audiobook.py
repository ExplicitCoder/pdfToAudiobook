#import pyttsx3 Uncomment this line if you are using Ubuntu or any other linux distro.
import PyPDF2
import PyPDF2
import glob

l = glob.glob("*pdf")
for i in range(len(l)):
	print(str(i+1)+'.'+l[i])
print('Please type the index number of the pdf.')
n = int(input())
if n > len(l):
	print('Index out of range. Please rerun the program')
else:
	print('Press Ctrl+C to stop')
	book = open(l[n-1],'rb')
	pdfreader = PyPDF2.PdfFileReader(book)
	pages = pdfreader.numPages
	speaker = pyttsx3.init()
	rate = speaker.getProperty('rate')
	speaker.setProperty('rate',100)
	page=pdfreader.getPage(6)
	text=page.extractText()
	speaker.say(text)
	speaker.runAndWait()
