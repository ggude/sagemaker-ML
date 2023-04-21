#### Create REST API that can be accessed by external applications:
In AWS SageMaker, the API Gateway is a fully managed service that makes it easy to create, deploy, and manage APIs for machine learning models.
# STEPS:
#### create Rest API
#### create Resource
#### create Method (POST here)
#### Test the method - you have to give input string/data here
#### Deploy API - after which provides Invoke URL which is your API


#### How to test after deploy API :
```
>>> import requests
>>> import json
>>> r=requests.post("https://pxxzbut94j.execute-api.ap-south-1.amazonaws.com/prod/api-gpt-ml",data=json.dumps({"input": "Drinking less water leads to"}))
>>> r.content
b'{"statusCode": 200, "output": "[{\'generated_text\': \'Drinking less water leads to more heart disease, diabetes, and cancer.\\\\n\\\\nThe study,\'}]"}'
```



