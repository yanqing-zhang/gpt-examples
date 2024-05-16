import unittest
from translator.pdf_translator import PDFParser
from book.content import ContentType
class PdfTestCase(unittest.TestCase):

    def test_pdf_parse(self):
        file_name = "../datas/test.pdf"
        pdf_parser = PDFParser()
        book = pdf_parser.parse_pdf(file_name)
        page_list = book.pages
        for page in page_list:
            contents = page.contents
            for content in contents:
                if content.content_type == ContentType.TEXT:
                    original = content.original
                    print(f'original:\n{original}')
                elif content.content_type == ContentType.TABLE:
                    original = content.original
                    print(f'original:\n{original}')