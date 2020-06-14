from demo.other1.demo_unittest01 import Unittest01
from demo.other1.demo_unittest02 import Unittest02
import unittest
from ClassicHTMLTestRunner import HTMLTestRunner

#suite = unittest.TestSuite()
#suite.addTest(Unittest01("test01"))

#lista = [Unittest01("test01"),Unittest01("test02")]
#suite.addTests(lista)

suite = unittest.defaultTestLoader.discover('demo',pattern='demo_unittest0*.py')
#runner = unittest.TextTestRunner()

#结果查看器 第一种
# runner = unittest.TextTestRunner()
# runner.run(suite)

#结果查看器 第二种
reportFile = open(r'G:/pycharm_workspace/eduApi/report/HTMLReport.html','wb')
runner = HTMLTestRunner(stream=reportFile,verbosity=2,description="用例执行详细信息",title="用例测试报告",tester="ekihin")
runner.run(suite)