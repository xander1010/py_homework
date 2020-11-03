# Python断言方法：assert
* 基本的断言方法提供了测试结果是True还是False。所有的断言方法都有一个msg参数，如果指定msg参数的值，则将该信息作为失败的错误信息返回。
  
| 序号 | 断言方法                                  | 断言描述                               |
| ---- |------------------------------------      | ------------------------------------- |
|  1   | assertEqual(arg1,arg2,msg=None)          | 验证arg1=arg2，不等则fail              |
|  2   | assertNotEqual(arg1,arg2,msg=None)       | 验证arg1 != arg2, 相等则fail           |
|  3   | assertTrue(expr,msg=None)                | 验证expr是true，如果为false，则fail     |
|  4   | assertFalse(expr,msg=None)               | 验证expr是false，如果为true，则fail     |
|  5   | assertIs(arg1,arg2,msg=None)             | 验证arg1、arg2是同一个对象，不是则fail   |
|  6   | assertIsNot(arg1,arg2,msg=None)          | 验证arg1、arg2不是同一个对象，是则fail   |
|  7   | assertIsNone(expr,msg=None)              | 验证expr是None，不是则fail              |
|  8   | assertIsNotNone(expr,msg=None)           | 验证expr不是None，是则fail              |
|  9   | assertIn(arg1,arg2,msg=None)             | 验证arg1是arg2的子串，不是则fail         |
|  10  | assertNotIn(arg1,arg2,msg=None)          | 验证arg1不是arg2的子串，是则fail         |
|  11  | assertIsInstance(obj,cls,msg=None)       | 验证obj是cls的实例，不是则fail           |
|  12  | assertNotIsInstance(obj,cls,msg=None)    | 验证obj不是cls的实例，是则fail           |

