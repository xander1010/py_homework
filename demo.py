import unittest

class test_demo(unittest.TestCase):

    exception_list = []

    def div_demo(self):
        a = 5
        b = 2
        c = a / b   # python3中除法默认有小数
        d = a // b  # ‘//’强制取整除法
        print(c,d)

    def tryEqual(self,a,b,msg=''):
        try:
            self.assertEqual(a,b,msg)
        except AssertionError as e:
            self.exception_list.append(e)
    def tryNotEqual(self,a,b,msg=''):
        try:
            self.assertNotEqual(a,b,msg)
        except AssertionError as e:
            self.exception_list.append(e)


    def test_bool(self):
        print(bool(1))
        print(bool(2))
        if bool(0) is False:
            print('假')
        if bool(1) == True:
            print('真')

        a = bool(0)
        b = bool(1)

        self.tryEqual(a,b,'假和真不相等')
        self.tryNotEqual(a,b,'他们相等')

        print('完成')

        print(self.exception_list)
        # raise Exception(self.exception_list) 





if __name__ == "__main__":
    td = test_demo()
    td.div_demo()

    unittest.main()