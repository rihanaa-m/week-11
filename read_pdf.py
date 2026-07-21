import pdfplumber

pdf_path = r'C:\Users\hp\Desktop\week 11\10 Academy - KAIM 9 - Week 11.pdf'
output_path = r'C:\Users\hp\Desktop\week 11\pdf_content.txt'

with pdfplumber.open(pdf_path) as pdf:
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, page in enumerate(pdf.pages):
            f.write(f'--- Page {i+1} ---\n')
            text = page.extract_text()
            if text:
                f.write(text)
            f.write('\n\n')

print(f'PDF content written to {output_path}')
