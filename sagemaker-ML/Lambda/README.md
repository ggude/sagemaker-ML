# Lambda function:
In AWS SageMaker, a Lambda function is a serverless compute service that allows you to run code in response to events. 
Here you invoke model endpoint and check functionality of the model.Endpoint is created in sagemaker where the model is defined.
```
import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    sagemaker_runtime = boto3.client('sagemaker-runtime')

    # specify the name of the endpoint and the content type of the input
    endpoint_name = 'GPT2'
    #content_type = "application/json"
    content_type = "text/csv"

    # get the input text from the event
    input_text = event['input']
    #input_data = "Working with SageMaker makes machine learning"

    # invoke the SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType=content_type,
        Body=input_text
    )

    # get the response from the endpoint
    output_text = response['Body'].read().decode('utf-8')

    # return the output
    return {
        'statusCode': 200,
        'output': output_text
    }
```
#### Create a Test event where you give input string/data and test lambda.

```
{
  "input": "Drinking less water leads to"
}
```
#### Deploy it.



