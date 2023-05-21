import requests

import requests
r = requests.get('https://securelogin.net.cuhk.edu.hk/cgi-bin/login')
print (r.text)
print (r.status_code)
print (type(r.text))

# if (r.content)