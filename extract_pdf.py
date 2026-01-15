import os
from pypdf import PdfReader

pdf_files = [
    "Docker LAMP+WORDPRESS.pdf",
    "ISMAEL BERMÚDEZ CASO DOCKER CON PORTAINER.pdf",
    "ISMAEL BERMÚDEZ WORDPRESS + MARIADB.pdf"
]

output_file = "extracted_content.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            try:
                reader = PdfReader(pdf_file)
                f.write(f"--- START OF {pdf_file} ---\n\n")
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        f.write(text)
                        f.write("\n\n")
                f.write(f"--- END OF {pdf_file} ---\n\n")
                print(f"Successfully extracted {pdf_file}")
            except Exception as e:
                f.write(f"Error extracting {pdf_file}: {e}\n")
                print(f"Error extracting {pdf_file}: {e}")
        else:
            print(f"File not found: {pdf_file}")
