import time
import json
import os
import base64
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options # Make sure you import Options if you're using them
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

def read_json(file_name):
  # --- Read and Parse the JSON File ---
  try:
    with open(file_name, 'r', encoding='utf-8') as f:
      # json.load() reads the file and converts the JSON structure to a Python dictionary
      data = json.load(f)
      return data
          
  except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

def read_content_and_save_pdf(driver, link):
  driver.get(link)
  # 2. Get the PDF as a Base64 string
  # You can pass options like 'orientation' (landscape/portrait) and 'printBackground'
  pdf_base64 = driver.print_page() 

  # 3. Decode and Save the PDF
  pdf_bytes = base64.b64decode(pdf_base64)
  file_path = "output_page.pdf"

  with open(file_path, "wb") as f:
      f.write(pdf_bytes)
      
  print(f"Successfully saved PDF to {file_path}")

load_dotenv()
my_file_path = os.environ.get('MY_FILE_PATH')
print(my_file_path)

# 1. Define the correct raw path (assuming this is fixed from before)
data = read_json("secrets.json")
print(data['my_file_path'])
# PATH = r'C:\Users\andre\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# service = Service(executable_path=PATH)
# options = Options()
# driver = uc.Chrome(use_subprocess=True, service=service, options=options)
# driver.get("https://learnify.sdacademy.ro/")
# link = "https://learnify.sdacademy.ro/lesson/pytorch-by-facebook-10/"

# element = driver.find_element(By.LINK_TEXT, "Continue with Google")
# element.click()

# time.sleep(40)

# read_content_and_save_pdf(driver=driver, link=link)

# time.sleep(10)