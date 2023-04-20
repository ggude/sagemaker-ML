
#### How to test after deploy API :
```
>>> import requests
>>> import json
>>> r=requests.post("https://pxxzbut94j.execute-api.ap-south-1.amazonaws.com/prod/api-gpt-ml",data=json.dumps({"input": "Drinking less water leads to"}))
>>> r.content
b'{"statusCode": 200, "output": "[{\'generated_text\': \'Drinking less water leads to more heart disease, diabetes, and cancer.\\\\n\\\\nThe study,\'}]"}'
```



