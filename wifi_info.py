import json
import subprocess

result = subprocess.run(['termux-wifi-connectioninfo'], capture_output=True, text=True)
data = json.loads(result.stdout)

print(f"network: {data['ssid']}")
print(f"ipaddress: {data['ip']}")
print(f"signal: {data['rssi']} dBm")

if data['rssi'] >= -40:
    print ("network status: Amazing")
elif data['rssi'] >= -60:
    print ("network status: good")
elif  data['rssi'] >= -80:
    print ("network status: bad")
else:
    print ("network status: worst")

subprocess.run(['termux-notification', '--title', 'wi-fi status', '--content', f"signal: {data['rssi']} dBm"])
