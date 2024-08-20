import requests
import sys
import hashlib
from bs4 import BeautifulSoup

if sys.version_info < (3, 6):
	import sha3


message_url = "https://secuweb-web.2024-bq.ctfcompetition.com/message/"

if __name__ == "__main__":
    unknown = []
    not_found = []
    for i in range(0, 50):
        r = requests.get(message_url + hashlib.sha3_256(str(i).encode()).hexdigest())
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'lxml')
            body = soup.find("body")
            print(body)
            print("""
        ________________________________
        """)
        else:
            unknown.append([i, r.status_code])

print(unknown)
    # r = requests.get(message_url + hashlib.sha3_256(str(4).encode()).hexdigest())
    # print(r.status_code)