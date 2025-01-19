import json
import requests


r = requests.get("http://localhost:80")
answer = json.loads(r.text)
print(answer)
