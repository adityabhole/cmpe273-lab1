import requests
import time
r1 = requests.get('https://webhook.site/9107990a-a9d4-4111-9b9a-3c2deeda3321')
a1 =  r1.headers['Date']
print (a1)
r2 = requests.get('https://webhook.site/9107990a-a9d4-4111-9b9a-3c2deeda3321')
a2 =  r2.headers['Date']
print (a2)
r3 = requests.get('https://webhook.site/9107990a-a9d4-4111-9b9a-3c2deeda3321')
a3 =  r3.headers['Date']
print (a3)