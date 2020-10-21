from  tinydb import TinyDB,Query
from flask import Flask,jsonify,g,request
import uuid,re

app = Flask(__name__)

def get_db():
    db = g.data = TinyDB("./file/db.json")   #数据存放位置
    return db

# 创建任务
@app.route("/api/v1/tasks",methods=["POST"])
def create_task():
    db = get_db()
    task = request.json
    if task is not None and task["title"]:
        task_data = {'title': task['title'], 'done': False, 'id': str(uuid.uuid4())}  #uuid下分uuid1,3,4,5,每个通过不同的方式生成
        db.insert(task_data)                                  #通过insert插入数据
        return jsonify({"id":task_data["id"]})
    else:
        return jsonify({'msg': 'title is required'}), 442


# 获取任务
@app.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    return jsonify(db.all())

# 根据id查询任务
@app.route('/api/v1/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    db = get_db()
    result = db.search(Query().id == task_id)
    if len(result) >= 1:
        return jsonify(result[0])
    else:
        return jsonify({'msg': 'NOT FOUND'}),404

# 模糊匹配任务,基于id
@app.route("/api/v1/tasks/fragment/<fragment>", methods=["GET"])
def get_task_with(fragment):
    db = get_db()
    result = db.search(Query().id.matches(fragment,flags=re.IGNORECASE))
    return jsonify(result)

# 编辑任务,基于id
@app.route("/api/v1/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    db = get_db()
    task = request.json
    Task = Query()
    if task is not None and task["title"]:
        result = db.search(Task.id == task_id)  # 查询对应Id的任务是否存在
        if len(result) >= 1:
            need_updated = result[0]
            need_updated["title"] = task["title"]
            db.update(need_updated,Task.id == task_id)   # 更新对应id的title
            return jsonify({"id":task_id})
        else:
            return jsonify({'msg': 'NOT FOUND'}), 404
    else:
        return jsonify({'msg': 'title is required'}), 422

# 切换任务状态,基于id
@app.route("/api/v1/tasks/<task_id>", methods=["PATCH"])
def toggle_task(task_id):
    db = get_db()
    Task = Query()
    result = db.search(Task.id == task_id)   # 查询对应id
    if len(result) >= 1:
        opposite = not result[0]['done']   # 设置对应结果的done值相反的状态，假和真切换
        db.update({'done': opposite},Task.id == task_id)   # 修改done的值update
        return jsonify({'id': task_id, 'done': opposite})
    else:
        return jsonify({'msg': 'NOT FOUND'}), 404


# 删除任务,基于id
@app.route("/api/v1/tasks/<task_id>", methods=["DELETE"])
def remove_task(task_id):
    db = get_db()
    Task = Query()
    result = db.search(Task.id == task_id) 
    if len(result) >= 1:
        db.remove(Task.id == task_id)  # 通过remove删除对应id的任务
        return jsonify({'msg':"success",'id': task_id})
    else:
        return jsonify({'msg': 'NOT FOUND'}), 404



if __name__ == "__main__":
    app.run()
