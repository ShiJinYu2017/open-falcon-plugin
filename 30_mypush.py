#!/usr/bin/env python

import requests
import time
import json

ts = int(time.time())
payload = [
    {
        "endpoint": "py-sys-cs-yf00.py",
        "metric": "my_push",
        "timestamp": ts,
        "step": 30,
        "value": 30,
        "counterType": "GAUGE",
        "tags": "idc=lg,loc=beijing",
    },
]

r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

print r.text
