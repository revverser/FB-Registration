import requests,hashlib,hmac,urllib.parse
from uuid import uuid4 as uid
data = {
    'email': 'rev12345@gmail.com',
    'firstname': 'Jack',
    'lastname': 'Smith',
    'gender': 'M',
    'password': 'rev123@@',
    'birthday': '2001-09-25',
    'return_multiple_errors': 'true',
    'attempt_login': 'true',
    'reg_instance': uid(),
    'device_id': uid(),
    'format': 'json',
    'native_preconf': 'true',
    'skip_session_info': 'true',
    'locale': 'en_US',
    'client_country_code': 'UK',
    'method': 'user.register',
    'fb_api_req_friendly_name': 'registerAccount',
    'fb_api_caller_class': 'com.facebook.registration.simplereg.fragment.RegistrationCreateAccountFragment'}
sorted_data = sorted(data.items())
encoded_data = urllib.parse.urlencode(sorted_data)
api_key = "882a8490361da98702bf97a021ddc14d"
sig = hmac.new(api_key.encode(), encoded_data.encode(), hashlib.sha256).hexdigest()
res=requests.get(f'https://b-api.facebook.com/method/user.register?email=rev12345%40gmail.com&firstname=Jack&lastname=Smith&gender=M&password=rev123%40%40&birthday=2001-09-25&return_multiple_errors=true&attempt_login=true&reg_instance={uid()}&device_id={uid()}&format=json&native_preconf=true&skip_session_info=true&locale=en_US&client_country_code=UK&method=user.register&fb_api_req_friendly_name=registerAccount&fb_api_caller_class=com.facebook.registration.simplereg.fragment.RegistrationCreateAccountFragment&api_key=882a8490361da98702bf97a021ddc14d&sig={sig}').content
with open('res.json','a+') as w:
 w.write(str(res))