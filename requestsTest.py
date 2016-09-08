import requests

s = requests.Session()
r = s.get("https://api.toodledo.com/3/account/authorize.php?response_type=code&client_id=kame&state=aaa&scope=basic%20tasks")

payload = {
        "response_type":"code",
        "client_id":"kame",
        "state":"aaa",
        "scope":"basic tasks folders",
        "playground":"0",
        "email":"kameyasu119@gmail.com",
        "pass":"kmnhtmnys",
        "authorized":"Shgn In"}

a = s.post("https://api.toodledo.com/3/account/authorize.php?response_type=code&client_id=kame&state=aaa&scope=basic%20tasks", data=payload)

print(a.url)
print(a.headers)
