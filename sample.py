from flask import Flask,jsonify, request

app = Flask(__name__)

USERS = [
    {'1': {'name': 'jack'}},
    {'2': {'name': 'rose'}},
    {'3': {'name': 'fred'}},
]

# 创建用户 POST /users
@app.route("/users", methods=['POST'])
def create_user():
    user = request.json
    if user is not None:
        user_id = get_user_id()
        USERS.append({user_id: user})
        return jsonify({user_id: user})
    else:
        return jsonify({'error': 400, 'message': 'post data should not be empty'})

def get_user_id():
    return len(USERS) + 1   #如果删除其中的数据了后再添加时id会重复

# 获取用户列表 GET /users
@app.route("/users", methods=['GET'])
def get_all_users():
    return jsonify(USERS)

if __name__ == '__main__':
    app.run(debug=True)