import requests
import json
r=requests.post("https://pxxzbut94j.execute-api.ap-south-1.amazonaws.com/prod/api-gpt-ml",data=json.dumps({"input": "Drinking less water leads to"}))
print(r.content)
