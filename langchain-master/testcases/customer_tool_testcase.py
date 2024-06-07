import unittest
from agents.customer_tool import CustomTool
class TestCustomerTool(unittest.TestCase):

    def test_get_stu_info(self):
        c = CustomTool()
        ret = c.get_student_info("李四")
        print(ret)

    def test_get_max_score_stu_info(self):
        c = CustomTool()
        ret = c.get_max_score_stu_info()
        print(ret)