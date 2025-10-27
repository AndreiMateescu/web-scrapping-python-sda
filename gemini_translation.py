import base64
from google import genai
import os
from dotenv import load_dotenv
from pypdf import PdfReader, PdfWriter
import pdf_extractor_service

load_dotenv()

def save_pdf_gemini_response(pdf_title, content):
  file_path = f"{pdf_title}.pdf"
  # pdf_bytes = base64.b64decode(content)
  res = bytes(content, "utf-8")
  with open(file_path, "wb") as f:
    f.write(res)
    

text_to_translate = pdf_extractor_service.extract_file_content("hyperparameters-in-neural-networks-19")

API_KEY = os.environ.get("GEMINI_API_KEY")

# print(API_KEY)
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Translate in Romanian the following content: " + text_to_translate
)
save_pdf_gemini_response("test_translate", response.text)
# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Summarize following content: " + text_to_translate
# )
# save_pdf_gemini_response("test_summarize", response.text)
print(response.text)