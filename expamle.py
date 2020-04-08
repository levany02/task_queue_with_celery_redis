import requests
import random

for i in range(100):
    p = {'one': random.randrange(1, 10000000), 'two': random.randrange(1, 1000000000)}
    r = requests.get('http://localhost:8000/v1/test/add', params=p)
    print(r.json())
    gto = r.json()['goto']
    r2 = requests.get("http://localhost:8000/v1/test/result/{}".format(gto))
    print(r2.json()["result"])
