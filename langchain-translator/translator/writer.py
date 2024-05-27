from book.book import Book
from utils.logger import LOG
from book import Book, ContentType
import os
from reportlab.lib import colors, pagesizes, units
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)

class Writer:
    """
    pip install reportlab -i https://pypi.tuna.tsinghua.edu.cn/simple
    """
    def __int__(self):
        pass
    def save_translated_book(self, book:Book, output_file_format: str):
        LOG.debug(output_file_format)
        if output_file_format.lower() == "pdf":
            output_file_path = self._save_translated_book_pdf(book)
        elif output_file_format.lower() == "markdown":
            output_file_path = self._save_translated_book_markdown(book)
        else:
            LOG.error(f"不支持的文件类型:{output_file_format}")
            return ""
        LOG.info(f"翻译完成,文件保存到:{output_file_path}")
        return output_file_path

    def _save_translated_book_pdf(self, book:Book, output_ifle_path: str = None):
        output_ifle_path = book.pdf_file_path.replace(".pdf", f"_translated.pdf")
        LOG.info(f"开始导出:{output_ifle_path}")

        font_path = "../fonts/simsun.ttc"
        pdfmetrics.registerFont(TTFont("SimSun", font_path))
        simsun_style = ParagraphStyle("SimSun", fontName="SimSun", fontSize=12, leading=14)
        doc = SimpleDocTemplate(output_ifle_path, pagesize=pagesizes.letter)
        styles = getSampleStyleSheet()
        story = []

        for page in book.pages:
            for content in page.contents:
                if content.status:
                    if content.content_type == ContentType.TEXT:
                        text = content.translation
                        para = Paragraph(text, simsun_style)
                        story.append(para)
                    elif content.content_type == ContentType.TABLE:
                        table = content.translation
                        table_style = TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'SimSun'),  # 更改表头字体为 "SimSun"
                            ('FONTSIZE', (0, 0), (-1, 0), 14),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('FONTNAME', (0, 1), (-1, -1), 'SimSun'),  # 更改表格中的字体为 "SimSun"
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)
                        ])
                        pdf_table = Table(table.values.tolist())
                        pdf_table.setStyle(table_style)
                        story.append(pdf_table)
                if page != book.pages[-1]:
                    story.append(PageBreak())
        doc.build(story)
        return output_ifle_path

    def _save_translated_book_markdown(self, book: Book):
        output_file_path = book.pdf_file_path.replace(".pdf", f"_translated.md")
        LOG.info(f"开始导出:{output_file_path}")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            for page in book.pages:
                for content in page.contents:
                    if content.status:
                        if content.content_type == ContentType.TEXT:
                            text = content.translation
                            output_file.write(text + "\n\n")
                        elif content.content_type == ContentType.TABLE:
                            table = content.translation
                            header = "| " + " | ".join(str(column) for column in table.columns) + " |" + "\n"
                            separator = '| ' + ' | '.join(['---'] * len(table.columns)) + ' |' + '\n'
                            # body = '\n'.join(['| ' + ' | '.join(row) + ' |' for row in table.values.tolist()]) + '\n\n'
                            body = '\n'.join(['| ' + ' | '.join(str(cell) for cell in row) + ' |' for row in
                                              table.values.tolist()]) + '\n\n'
                            output_file.write(header + separator + body)
                if page != book.pages[-1]:
                    output_file.write("---\n\n")
        return output_file_path