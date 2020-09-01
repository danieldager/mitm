import json
import requests
import mitmproxy

# mitmproxy --view-filter 'google\.com/search\?q' --ignore-hosts '^(?![0-9\.]+:)(?!([^\.:]+\.)*google\.com:)'

import re
from mitmproxy.io import FlowReader


filename = 'flows.mitm'

with open(filename, 'rb') as fp:
    reader = FlowReader(fp)

    for flow in reader.stream():
        url_string = flow.request.url
        match = re.search("(?=google\\.com/search\\?q)", url_string)
        if match:
            print(url_string)
