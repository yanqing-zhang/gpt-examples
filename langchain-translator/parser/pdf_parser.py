from book import Book,Content,TableContent,Page,ContentType
from typing import Optional
import pdfplumber
from utils import LOG
from utils.exceptions import PageOutOfRangeException

class PDFParser:
    def parse(self, pdf_file_path:str, pages:Optional[int]=None) -> Book:
        """
        解析pdf文件
        :param pdf_file_path:
        :param pages:
        :return:
        """
        book = Book(pdf_file_path)
        with pdfplumber.open(pdf_file_path) as pdf:
            if pages is not None and pages > len(pdf.pages):
                raise PageOutOfRangeException(len(pdf.pages), pages)
            if pages is None:
                pages_to_parse = pdf.pages
            else:
                pages_to_parse = pdf.pages[:pages]

            for pdf_page in pages_to_parse:
                page = Page()
                """
                调用pdfplumber抽取文本和表格数据
                """
                raw_text = pdf_page.extract_text()
                tables = pdf_page.extract_tables()
                """
                处理表格数据：
                解释：raw_text.replace(cell, "", 1)
                cell：你要在 raw_text 中查找并替换的子串。
                ""：你要替换 cell 子串的新子串，在这个例子中是空字符串，意味着 cell 子串将被删除。
                1：这个参数指定替换的最大次数。在这个例子中，它被设置为 1，意味着只有第一个出现的 cell 子串会被替换。
                """
                for table_data in tables:
                    for row in table_data:
                        for cell in row:
                            raw_text = raw_text.replace(cell, "", 1)
                """
                处理文本数据：
                """
                if raw_text:
                    """
                    根据不同的结束符将原数据进行拆分
                    如：raw_text = "第一行\n第二行\r第三行\r\n第四行"，处理后为['第一行', '第二行', '第三行', '第四行']
                    [line.strip() for line in raw_text_lines if line.strip()]为循环中检查line
                    在进行前后去空后是否为空串，如不为空串，则把line.strip()前后去空后返回赋值给cleaned_raw_text_lines
                    """
                    raw_text_lines = raw_text.splitlines()
                    cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                    cleaned_raw_text = "\n".join(cleaned_raw_text_lines) # 在处理完空格后再次用回行符进行拼装数据
                    text_content = Content(content_type=ContentType.TEXT, original=cleaned_raw_text)
                    page.add_content(text_content)
                    LOG.debug(f"cleaned_raw_text:\n{cleaned_raw_text}")

                if tables: # 把表格内容组装到页面
                    table = TableContent(tables)
                    page.add_content(table)
                    LOG.debug(f"table:\n{table}")
            book.add_page(page) # 把页面组装到book
            return book
