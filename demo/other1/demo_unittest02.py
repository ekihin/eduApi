import unittest


class Unittest02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup类方法")

    def test01(self):
        print("测试用例01")

    @unittest.skip('未执行原因')
    def test02(self):
        print("测试用例02")

    def test03(self):
        print("测试用例03")

    def test04(self):
        print("测试用例04")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown类方法")
