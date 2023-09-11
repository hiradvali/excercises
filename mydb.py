import requests 

import re   

import os   

r = requests.get('https://www.worlddata.info/') 

Content = r.content 

x = re.findall(r"america/{0,}/index.php", Content)

print(x)
