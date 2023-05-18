from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def chat():
    # 解析POST请求中的请求体
    data = request.json
    
    # 处理数据，返回对话响应
    response = "你好👋！我是人工智能助手 ChatGLM-6B，很高兴见到你，欢迎问我任何问题。"
    history = []
    status = 200
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = {
        "response": response,
        "history": history,
        "status": status,
        "time": time
    }
    
    # 将结果转换为JSON格式返回
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1722)
