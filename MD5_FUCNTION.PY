import hashlib
import json
import requests

# f1e069787ece74531d112559945c6871

def make_post(result, value, course_uri):
    
    payload = {
        "banner": "B00946176",
        "result": result,
        "arn": "arn:aws:lambda:us-east-1:637592602151:function:MD5_FUCNTION",
        "action": "md5",
        "value": value
    }
    
    headers = {
        "Content-Type": "application/json"  
    }
    
    print(payload)
    
    response = requests.post(course_uri, data=json.dumps(payload), headers=headers)
    
    print(response)
    return response

def lambda_handler(event, context):
    
    print(event)
    course_uri = event['course_uri']
    print(course_uri)
    
    VALUE = event['value']
    print(VALUE)
    
    md5_String = hashlib.md5(VALUE.encode('utf-8')).hexdigest()
    print(md5_String)
    
    request = make_post(md5_String, VALUE, course_uri)
    
    if request.status_code == 200:
        print("POST request successful.")
    else:
        print(f"POST request failed with status code: {request.status_code}")
    
    return {
        'statusCode': 200,
        'body': md5_String
    }

# reference:
# [1] 	suman_709, "MD5 hash in Python," [Online]. Available: https://www.geeksforgeeks.org/md5-hash-python/. [Accessed 16 07 2023].