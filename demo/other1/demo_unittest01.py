import unittest
from lib.courseLib import *


class Unittest01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        listData = course_list(1,500)
        i=0
        for item in listData['retlist']:
            course_del(item['id'])
            i = i+1
        print("本次初始化删除了"+str(i)+'条课程数据')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDown类方法')

    def test01(self):
        courseNmae = '添加课程自动化' + str(int(time.time() * 1000))
        retDict = course_add(courseNmae, '添加课程自动化描述', 1)
        self.assertEqual(retDict['retcode'],0,"测试不通过")
        #if retDict['retcode'] == 0:
        print(">>>>>>>>>>>新增课程测试通过")
        id = retDict['id']
        retDict2 = course_list(1, 500)
        flag = False
        for dict in retDict2['retlist']:
            if dict['id'] == id:
                print(">>>>>>>>>>>列出课程测试通过：" + str(dict['id']))
                flag = True
                break
        self.assertEqual(flag,True,'>>>>>>>>>>>列出课程测试不通过！')
        print('测试通过')
        # if flag == False:
        #     print(">>>>>>>>>>>列出课程测试不通过！")
        # else:
        #     print(">>>>>>>测试不通过")

    def test02(self):
        print("测试用例02")

    def test03(self):
        print("测试用例03")

    def test04(self):
        print("测试用例04")
