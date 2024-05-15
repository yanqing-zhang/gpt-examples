import unittest
from config.configurations import get_api_key

class ApiKeyTestCase(unittest.TestCase):
    """
    openai`s api_key获取函数测试
    """
    def test_get_api_key(self):
        api_key = get_api_key()
        print(f'api_key:{api_key}')
