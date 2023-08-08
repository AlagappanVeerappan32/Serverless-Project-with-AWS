import json
import bcrypt
import requests

def make_post(result, value, course_uri):
    
    payload = {
        "banner": "B00946176",
        "result": result.decode('utf-8'),
        "arn": "arn:aws:lambda:us-east-1:637592602151:function:a3",
        "action": "bcrypt",
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
    
    value = event['value']
    print(value)

    bcrypt_value = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())
    print(bcrypt_value)
    
    request = make_post(bcrypt_value, value, course_uri)
    
    if request.status_code == 200:
        print("POST request successful.")
    else:
        print(f"POST request failed with status code: {request.status_code}")
    
    return {
        'statusCode': 200,
        'body': bcrypt_value
    }

# reference:
# [1] chandramauliguptach, "Hashing Passwords in Python with BCrypt," [Online]. Available: https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/. [Accessed 16 07 2023].