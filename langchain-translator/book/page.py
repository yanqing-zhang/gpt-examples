from .content import Content

class Page:
    """
    pdf文件中一个页面对应这里的一个Page对象，
    一页pdf中的内容有文字的，有图像的，有表格的，这些内容对应Page对象中的content列表contets
    """
    def __init__(self):
        self.contents = []

    def add_content(self, content:Content):
        self.contents.append(content)