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

