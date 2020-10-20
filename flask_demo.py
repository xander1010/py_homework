from flask import Flask,jsonify,g    #jsonify(dict):可以直接将字典转成json格式返回；g：可以通过g.xx定义全局可使用的变量
import copy
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.before_request   #预先处理，类似unittest里的setUp
def set_up_data():
    g.data = [
        {'id': 1, 'title': 'task 1', 'desc': 'this is task 1'},
        {'id': 2, 'title': 'task 2', 'desc': 'this is task 2'},
        {'id': 3, 'title': 'task 3', 'desc': 'this is task 3'},
        {'id': 4, 'title': 'task 4', 'desc': 'this is task 4'},
        {'id': 5, 'title': 'task 5', 'desc': 'this is task 5'}
    ]

    g.task_does_not_exist = {"msg": "task does not exist"}

# 查看所有数据
@app.route("/api/tasks")
def get_tasks():
    return jsonify(g.data)

# 根据id查看指定数据
@app.route("/api/tasks/<int:task_id>")    # 在变量中指定要传参数的类型，只有相同类型的可以被接受
def get_task(task_id):
    if task_id > 0 and task_id <= len(g.data):
        return jsonify(g.data[task_id])
    else:
        return jsonify(g.task_does_not_exist)

# 根据id完成指定任务
@app.route("/api/tasks/<int:task_id>",methods=["PUT"])
def complete_task(task_id):
    if task_id > 0 and task_id <= len(g.data):
        tmp = copy.deepcopy(g.data[task_id])   #复制对应数据后再操作
        tmp["done"] = True
        return jsonify(tmp)
    else:
        return jsonify(g.task_does_not_exist)



if __name__ == "__main__":
    app.run()




'''
1、新增企业删除功能，通过权限点分配。默认只有系统管理员；1
2、导入实名制数据至“高崎污水处理厂”项目；--列表最后一条数据在多页存在
3、优化资料列表，将正在推送中的状态图标默认显示出来；--进度下没有显示
4、优化推送流程，提升推送成功率；1
5、优化进度操作体验；
6、添加项目时通过输入地址定位地图；--填写地址时必须点一下定位地址才可保存
人员导出为excel报500
'''