from flask import Flask,jsonify,request

app = Flask(__name__)
'''
用户微服务的api
    创建用户 POST /users
    删除用户 DELETE /users/:user_id
    更新用户信息 PUT /users/:user_id
    获取用户列表 GET /users
    获取用户某个用户详情 GET /users/:user_id
users
    id name 
    1  jack
    2 rose
    3 fred
'''
# 存放数据类
class data:
    # 数据位置
    db = []
    # 初始用户id，使用全局id，避免删除用户后出现id重复
    uid = 0


# 创建用户
@app.route('/api/users',methods=['POST'])
def create_user():
    user = request.json
    if user is not None:
        name = user['name']
        data.uid = data.uid + 1
        data.db.append({"id":data.uid,"name":name})
        print(data.db,data.uid)
        return jsonify({"msg":"success","id":data.uid,"name":name})
    else:
        return jsonify({"msg":"user is required"})


# 获取所有用户
@app.route('/api/users',methods=['GET'])
def get_users():
    print(data.db,data.uid)
    return jsonify(data.db)

# 获取用户某个用户详情 GET /users/:user_id
@app.route('/api/users/<int:user_id>',methods=['GET'])
def get_users_with(user_id):
    if user_id is not None:
        for user in data.db:
            if user["id"] == user_id:
                return jsonify({"id":user_id,"name":user["name"]})            
        return jsonify({"msg":"data not found"})


# 更新用户信息 PUT /users/:user_id
@app.route('/api/users/<int:user_id>',methods=['PUT'])
def update_users(user_id):
    user_info = request.json
    if user_info is not None:
        for user in data.db:
            if user["id"] == user_id:
                user["name"] = user_info["name"]
                return jsonify(user)
        return jsonify({"msg":"data not found"})
    else:
        return jsonify({"msg":"user is required"})


# 删除用户 DELETE /users/:user_id
@app.route('/api/users/<int:user_id>',methods=['DELETE'])
def del_user(user_id):
    for user in data.db:
        if user["id"] == user_id:
            i = data.db.index(user)   # 返回对应user信息在db中的索引值
            del data.db[i]            # 删除对应user
            return jsonify({'msg':"delete success"})
    return jsonify({"msg":"data not found"})


if __name__ == "__main__":
    app.run(debug=True)