import os, requests, json


BASE_URL = "http://127.0.0.1:8000/api/contact/"
AUTH_URL = "http://127.0.0.1:8000/api/auth/jwt/"
REGISTER_URL = "http://127.0.0.1:8000/api/auth/register/"

image_path = os.path.join(os.getcwd(), "logo.jpg")


def get_token(method="post"):
    payload = {
        "username":"admin@cimpr.com",
        "password":"admin42"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTc4MTM2NTMxLCJlbWFpbCI6ImFkbWluQGNpbXByLmNvbSIsIm9yaWdfaWF0IjoxNTc4MTM2MjMxfQ.spu2Wdv_Yfqpx0t27XYfBAaXf_QvGDKFIpBvYLdGVvI"
    }
    response = requests.request(method, AUTH_URL, data=payload, headers=headers)
    print(response.text)

def register_user(method="post"):
    payload = {
        "username":"sample_api_1",
        "email":"sample_api_1@test.com",
        "password":"sample_api_1",
        "password2":"sample_api_1"
    }
    headers = {
        "Content-Type": "application/json"
        #"Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTc4MTM2NTMxLCJlbWFpbCI6ImFkbWluQGNpbXByLmNvbSIsIm9yaWdfaWF0IjoxNTc4MTM2MjMxfQ.spu2Wdv_Yfqpx0t27XYfBAaXf_QvGDKFIpBvYLdGVvI"
    }
    response = requests.request(method, REGISTER_URL, data=payload)
    print(response.text)

def do_image(method='post',data={}, id=0, is_json=True, image_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if image_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {'image': image}
            if id != 0:
                response = requests.request(method, BASE_URL+str(id)+"/", data=data, files=file_data, headers=headers)
            else:
                response = requests.request(method, BASE_URL, data=data, files=file_data, headers=headers)

    else:
        response = requests.request(method, BASE_URL, data=data, headers=headers)
    print (response.status_code)
    print (response.text)
    return response


def do(method='get',data={}, id=2, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    response = requests.request(method, BASE_URL, data=data, headers=headers)
    print (response.statusc_code)
    print (response.text)
    return response


#do(data={'id':3})
sample_data = {
    'id':5,
    'user': 1,
    'first_name':"Test_Api_1_Updated",
    'email': "test_api@test.com",
    'type': "M"
}

#get_token()
register_user()
#do_image(method="post", data=sample_data, is_json=False, image_path=image_path)
#do_image(method="put", data=sample_data, id=5, is_json=False, image_path=image_path)
