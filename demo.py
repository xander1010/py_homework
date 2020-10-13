import unittest

class test_demo(unittest.TestCase):

    exception_list = []

    def setUp(self):
        print('++++++++++开始++++++++++++')
    def tearDown(self):
        print('++++++++++结束++++++++++++')

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


    def test_1_bool(self):

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

    def test_2_aa(self):
        li = []
        li.append(1)
        li.append(2)
        li.append(3)
        li.append(4)
        print(li)

        li.pop()  # 将元素从列表尾部移除
        print(li)

        li.append(4)
        li[3] = 44
        print(li)
        # 取最后一个值，倒数第一个
        print(li[-1])
        print(li[-2])   # 倒数第二个

        # 获取 li[1]li[2]的值，不包含3
        print(li[1:3])  

        # 不写开头，表示到3之前，不包含3的值
        print(li[:3])
        
        # 从2开始后面所有值，包括2
        print(li[2:])

        # 从第一个开始取值每个加2再取，0，2，4
        print(li[::2])
        
        # 从最后开始取值，每个-1
        print(li[::-1])

        # 取li 1到4的值，不包括4，间隔2
        print(li[1:4:2])
        # 删除列表中的指定值
        del li[0]
        print(li)

        li2 = [3,5,6,7,8]
        li3 = li + li2
        print(li3)
        # 连接其他列表,修改了li的值 
        li.extend(li2)
        print(li)

        # 移除第一个满足条件的值
        li.remove(3)
        print(li)
        # 在第li[1]处添加值 3 
        li.insert(1,3)
        print(li)
        # 返回第一个对应值在列表中的索引值，3 在li中第一个索引是1,即li[1]==3
        print(li.index(3))
        # 返回列表长度
        print(len(li))
        # 将列表排序
        li.sort()
        print(li)

        # 字典
        dict1 = {"one": 1, "two": 2, "three": 3}
        d = dict1.keys()
        print(d)
        print(dict1.values())
        print(dict1.items())  #返回元组形式的列表
        print(dict1.get("one",111)) # 获取一个值，没有时返回设置的值

        # 集合 set(),跟列表差不多，只是不能有重复的项
        some_set = set([1, 2, 2, 3, 4])  #现在等于set([1, 2, 3, 4])
        another_set = set([4, 3, 2, 2, 1])
        some_set & another_set #取交集,用 | 取并集

    def test_3_control(self):

        for animal in ["dog", "cat", "mouse"]:
            print("{1} is an animal {0}".format(animal,"11"))
        
        try:
        # 使用"raise"来抛出异常
            raise IndexError("This is an index error")
        except IndexError as e:
            pass  # Pass就是啥都不做.一般情况下，你会在这里做异常的恢复
        except (TypeError, NameError):
            pass  # 如果需要的话可以一次性处理多个异常
        else:  # else分支是可选的.必须出现在所有的except分支之后
            print("All good!")  # 当且仅当try代码块中没有抛出任何异常时才会运行
        finally:  # 最后一定会执行
            print("We can clean up resources here")

        print(dir(unittest))  # 返回导入的模块下所有的函数和属性以列表形式








if __name__ == "__main__":
    td = test_demo()
    td.div_demo()

    unittest.main()