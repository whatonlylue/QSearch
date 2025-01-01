from PIL import Image
import docx
import fitz

INCLUDE = (".txt", ".log", ".md", ".rtf", ".doc", ".docx", ".odt", ".wps", ".pdf", ".jpg", ".jpeg", ".png", ".ppt", ".pptx", ".odp", ".key", ".epub", ".mobi", ".axw3")

def textFile(filename: str):
    
    content = "Null"

    try:
        with open(filename, 'r') as f:
            content = f.read(1000)

    except Exception as e:
        content = f'Could not preview file:\n{e}'

    return content

def docxFile(filename: str):
    content = "Null"
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
        
def picFile(filename: str):
    content = "Null"
    try:
        with open(filename, 'rb') as f:
            content = f.read(1000)
    except Exception as e:
        content = f'Could not preview file:\n{e}'

    return ''.join(format(byte, '08b') for byte in content)

def pdfFile(filename: str):
    doc = fitz.open(filename)
    fullText = ""
    for page in doc:
        fullText += (page.get_text())
    return fullText

def extractSampleText(filename: str):
    TXT = ('.txt', '.log', '.md', '.rtf')
    PIC = ('.png', '.jpg', '.jpeg')
    content = "Error, could not read file"
    if filename.endswith(TXT):
        content = textFile(filename)
    elif filename.endswith(PIC):
        content = picFile(filename)
    elif filename.endswith('.docx'):
        content = docxFile(filename)
    elif filename.endswith('.pdf'):
        content = pdfFile(filename)
    
    return content 
