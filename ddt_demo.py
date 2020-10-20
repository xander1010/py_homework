import unittest
from ddt import ddt,data,unpack,file_data

@ddt
class Testwork(unittest.TestCase):

    # 单一数据参数的用例，在data中每个逗号就是一个用例数据
    @data(1,2,3)
    def test_1(self,value):
        print(value)

    @data((1,2,3),(4,5,6))
    def test_2(self,value):
        print(value)

    # 用例参数有多个的，且分成几组数据时，需要用unpack拆分数据，每条数据需要包装起来为可迭代的形式
    @data([1,2,3],[4,5,6])
    @unpack    #拆分数据，其实就是拿每个逗号分开的参数里的数据作为参数，而不是和单一参数一样直接按逗号分隔拿用例数据,只有一组数据的不适用
    def test_3(self,value1,value2,value3):
        print(value1,value2,value3)

    





if __name__ == "__main__":
    unittest.main()