import fitz

class PDFProcessor:
    def extract_text(self, pdf_path: str) -> str:
        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()
        
        document.close()

        return text
    
pdf_processor = PDFProcessor()