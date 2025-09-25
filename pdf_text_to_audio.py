import pypdf
from gtts import gTTS
class convert_pdf_audio:
    def __init__(self,filepath,audiopath):
        self.filepath = filepath
        self.audiopath = audiopath
    def Extract_text(self):
        #opening file with rb mode. rb means read binary, to read pdf file,we use rb mode.
        pdf_file = open(self.filepath, 'rb')
        #reading the pdf using PdfReader
        pdf_reader = pypdf.PdfReader(self.filepath)
        #creating variable for an empty string to add all pages text to varialble
        text = ""
        #if we have multiple pages, then we loop it.pdf.reader.pages weill give you how many pages are there in the pdf.
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            #we are adding the data of each page by extracting the data from pdf pages.
            text += page.extract_text()
        pdf_file.close()
        return text


    def text_to_audio(self,text):
        #gTTS wil convert text to audio in the specified language.
        tts = gTTS(text=text, lang='en')
        tts.save(self.audiopath)


    def pdf_audio(self):
        text = self.Extract_text()
        #strip will delete extra spaces at start and end of the string
        if text.strip():
            self.text_to_audio(text)
            print("Audio file saved at: {}".format(self.audiopath))
        else:
            print("No text found in the PDF.")

obj = convert_pdf_audio('file_name and path','audio.mp3')
obj.pdf_audio()