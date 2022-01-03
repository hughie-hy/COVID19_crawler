# 导入模块
import requests

# 发送请求，获取响应
response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")

print(response) #状态响应码<Response [200]>

# 获取响应数据
# print(response.encoding) #ISO-8859-1
# response.encoding = 'utf-8'
# print(response.text)

print(response.content.decode())