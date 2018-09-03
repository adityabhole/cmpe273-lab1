import asyncio 
import requests 
 
async def main(name, timee):
    for i in range(timee):
          r = requests.get('https://webhook.site/9107990a-a9d4-4111-9b9a-3c2deeda3321')  
          print(name, r.headers['Date']) 
          await asyncio.sleep(0.0001)
loop = asyncio.get_event_loop() 
loop.run_until_complete(asyncio.gather(
     main("Request 1 :",2),
     main("Request 2 :",1), 
     main("Request 3 :",4) 
))
