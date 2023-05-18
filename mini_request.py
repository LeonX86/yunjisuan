import requests
import time,sys
import json
import os
import platform

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'

def stream_out(text):
    for shuo in text:
        sys.stdout.write(shuo)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write('\n')

def build_prompt(history):
    prompt = ""
    # for query, response in history[-1]:
    # prompt += f"\n\n用户：{history[-1][0]}"
    prompt += f"\n\nChatGLM-6B：{history[-1][1]}"
    return prompt

# url = "http://172.30.7.253:1212"
# url = "http://192.168.31.242:1212"
url = "http://172.30.7.253:1722"
# url = "http://192.168.31.133:1722"


"""
chatGLM模型的post请求格式为
curl -X POST "http://127.0.0.1:8000" \
     -H 'Content-Type: application/json' \
     -d '{"prompt": "你好", "history": []}'
返回结果格式为json
{
  "response":"你好👋！我是人工智能助手 ChatGLM-6B，很高兴见到你，欢迎问我任何问题。",
  "history":[["你好","你好👋！我是人工智能助手 ChatGLM-6B，很高兴见到你，欢迎问我任何问题。"]],
  "status":200,
  "time":"2023-03-23 21:38:40"
}
基于上面的内容写一个简单的微信小程序，要求在index页面直接实现连续的对话框，界面美观大气
"""


"""
{
    "response":"你好👋！我是人工智能助手 ChatGLM-6B，很高兴见到你，欢迎问我任何问题。",
    "history":[],
    "status":200,
    "time":"2023-03-23 21:38:40"
}
"""

def main():
    print("欢迎使用 ChatGLM-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
    history = []
    while True:
        query = input("\n用户：")
        if query == "stop":
            break
        if query == "clear":
            history = []
            os.system(clear_command)
            print("欢迎使用 ChatGLM-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
            continue
        else:
            data = {"prompt": query, "history": history}
            headers = {"Content-Type": "application/json"}
            
            response = requests.post(url, headers=headers, json=data)
            response_dict = json.loads(response.text)
            
            response_text = response_dict.get("response")
            response_time = response_dict.get("time")
            
            history.append([query, response_text])
            
            stream_out(build_prompt(history))
            stream_out("time : "+response_time)
        
if __name__ == '__main__':
    main()

























