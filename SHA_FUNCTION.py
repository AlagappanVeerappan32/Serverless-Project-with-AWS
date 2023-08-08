import json
import hashlib
import requests

def make_post(result, value, course_uri):
    
    payload = {
        "banner": "B00946176",
        "result": result,
        "arn": "arn:aws:lambda:us-east-1:637592602151:function:SHA_FUNCTION",
        "action": "sha256",
        "value": value
    }
    
    headers = {
        "Content-Type": "application/json"  
    }
    
    print(payload)
    
    response = requests.post(course_uri, data=json.dumps(payload), headers=headers)
    
    
    return response
    

def lambda_handler(event, context):
    
    course_uri = event['course_uri']
    
    VALUE = event['value']
    print(VALUE)
    
    sha256_String = hashlib.sha256(VALUE.encode('utf-8')).hexdigest()
    print(sha256_String)
    
    request = make_post(sha256_String, VALUE, course_uri)
    
    if request.status_code == 200:
        print("POST request successful.")
    else:
        print(f"POST request failed with status code: {request.status_code}")
    
    return {
        'statusCode': 200,
        'body': sha256_String
    }
    
    
# reference:
# [1] suman_709, "SHA in Python," [Online]. Available: https://www.geeksforgeeks.org/sha-in-python/. [Accessed 16 07 2023].

