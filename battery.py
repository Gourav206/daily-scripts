
import os, json
data = json.loads(os.popen('termux-battery-status').read())
print (f"battery: {data['percentage']}%")
print (f"health: {data['health']}")
print (f"status: {data['status']}")
print (f"temp: {data['temperature']}°C")
if data['percentage'] < 20:
 print ("PLUG UR PHONE")
elif data['percentage'] <60:
 print ("yo might wanna plug in battery getting low")
else:
 print ("all g plenty of charge")
