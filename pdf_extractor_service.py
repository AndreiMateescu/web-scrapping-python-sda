# importing required classes
from pypdf import PdfReader


def extract_file_content(file_name):
  content = ""
  reader = PdfReader(f'web-scrapping-python-sda\{file_name}.pdf')
  for i in range(2, len(reader.pages)):
    content = content + " " + reader.pages[i].extract_text()
  return content


# content = extract_file_content("introduction-106")
# print(content)
# # printing number of pages in pdf file
# print(len(reader.pages))

# # creating a page object
# page = reader.pages[2]

# # extracting text from page
# print(page.extract_text())