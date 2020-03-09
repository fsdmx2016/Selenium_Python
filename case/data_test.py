import unittest
import sys
import ddt
from Util.operate_excel import operaExcel
from log.user_log import UserLog

# ex=operaExcel()
# data=ex.get_lines()

@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        pass

    def tearDown(self):
        print()
    def test(self):
        self.logger.debug("测试")
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    # @ddt.data(
    #     [1,2],
    #     ["2", "3"]
    # )
    # @ddt.data(*data)
    # def test_case(self,data):



    # @ddt.unpack
    # def test_case(self, a, b):
    #     print(a + b)


