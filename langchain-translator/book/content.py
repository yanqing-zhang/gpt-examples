import pandas as pd
from enum import Enum, auto
from PIL import Image as PILImage
from utils import LOG
from io import StringIO

class ContentType(Enum):
    TEXT = auto()
    TABLE = auto()
    IMAGE = auto()

class Content:
    """
    Content对象就是一页pdf中的具体内容了，
    某个页面中可能包含文本内容，可能包含表格内容，也可能包含图像内容
    """
    def __init__(self, content_type, original, translation=None):
        """
        :param content_type: 待翻译的pdf内容类型:TEXT、TABLE、IMAGE
        :param original:原始内容(没翻译的)
        :param translation:翻译后的内容
        """
        self.content_type = content_type
        self.original = original
        self.translation = translation
        self.status = False

    def set_translation(self, translation, status):
        if not self.check_translation_type(translation):
            raise ValueError(f"Invalid translation type. Expected {self.content_type}, but got {type(translation)}")
        self.translation = translation
        self.status = status
    def check_translation_type(self, translation):
        """
        isinstance(translation, str):该函数判断translation这个参数是否是str字符串类型，如果是返回True否则False
        :param translation:
        :return:
        """
        if self.content_type == ContentType.TEXT and isinstance(translation, str):
            return True
        elif self.content_type == ContentType.TABLE and isinstance(translation, list):
            return True
        elif self.content_type == ContentType.IMAGE and isinstance(translation, PILImage.Image):
            return True
        return False
    def __str__(self):
        return self.original

class TableContent(Content):
    def __init__(self, data, translation=None):
        df = pd.DataFrame(data)
        if len(data)!=len(df) or len(data[0]) != len(df.columns):
            raise ValueError("The number of rows and columns in the extracted table data and DataFrame object do not match.")
        super().__init__(ContentType.TABLE, df)
    def set_translation(self, translation, status):
        try:
            if not isinstance(translation, str):
                raise ValueError(f"Invalid translation type. Expected str, but got {type(translation)}")
            LOG.debug(f"[translation]\n{translation}")
            header = translation.split("]")[0][1:].split(", ")
            data_rows = translation.split("] ")[1:]
            data_rows = [row[1:-1].split(", ") for row in data_rows]
            translated_df = pd.DataFrame(data_rows, columns=header)
            LOG.debug(f"[translated_df]\n{translated_df}")
            self.translation = translated_df
            self.status = status
        except Exception as e:
            LOG.error(f"An error occurred during table translation:{e}")
            self.translation = None
            self.status = False