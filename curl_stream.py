# import requests

# url = "http://192.168.31.242:1212/stream"
# headers = {
#     "Host": "localhost:8001",
#     "User-Agent": "python-requests/2.24.0",
#     "Accept": "*/*",
#     "Content-Type": "application/json"
# }
# data = {
#     "query": "你好，你是谁",
#     "history": []
# }

# response = requests.post(url, headers=headers, json=data)
# print(response.text)  # 输出响应的JSON数据

import requests
from sseclient import SSEClient
import json

url = "http://192.168.31.242:1212/stream"
headers = {
    "Host": "localhost:8001",
    "User-Agent": "python-requests/2.24.0",
    "Accept": "*/*",
    "Content-Type": "application/json"
}
data = {
    "query": "你好，你是谁",
    "history": []
}

# 发送POST请求
response = requests.post(url, headers=headers, json=data)

# 从响应中获取conversation_id和服务器返回的SSE事件流URL
conversation_id = response.json().get('conversation_id')
sse_url = response.json().get('stream')

# 创建SSE客户端对象，并连接到服务器端的SSE事件流地址
if sse_url:
    response = requests.get(sse_url, stream=True)
    client = SSEClient(response)

    for event in client.events():
        # 将事件流数据转换为Python字典对象
        data = json.loads(event.data)
        # 按需求进行数据处理和分析
        if "delta" in data:
            delta_text = data['delta']
            response_text = data['response']
            print(f"用户输入：{response_text}{delta_text}")
else:
    print("获取SSE地址失败！")
