from .page import Page

class Book:
    """
    一个pdf对应的是一个Book对象，实现pdf文件与Book的映射
    一个pdf文件包含多个页面，一个Book对象包含多个page，多个page放在一个list列表pages中
    """
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
        self.pages = []

    def add_page(self, page:Page):
        self.pages.append(page)