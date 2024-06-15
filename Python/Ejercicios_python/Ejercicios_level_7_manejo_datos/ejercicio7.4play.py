import requests
import io
from PyPDF2 import PdfReader  # Necesitas instalar PyPDF2 para manejar PDFs

internet_file = "https://ec.europa.eu/eurostat/documents/15234730/17582411/KS-HA-23-001-EN-N.pdf/5d783d9e-9cb3-897c-8360-5122563ae8f3?version=6.0&t=1700579783008"

def internet_file_word_counter(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Leer el contenido del archivo PDF (o cualquier otro formato)
            with io.BytesIO(response.content) as f:
                pdf_reader = PdfReader(f)
                text = ""
                for page_num in range(pdf_reader.numPages):
                    text += pdf_reader.getPage(page_num).extract_text()
            # Contar palabras en el texto
            words = text.split()
            return len(words)
        else:
            print(f"Error: No se pudo acceder al archivo. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

count = internet_file_word_counter(internet_file)
if count:
    print(f"El número de palabras en el archivo es: {count}")
