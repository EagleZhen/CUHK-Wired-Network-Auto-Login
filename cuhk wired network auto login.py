import requests
import json
import socket
from time import sleep
from datetime import datetime

login_url = "https://securelogin.net.cuhk.edu.hk/cgi-bin/login"

# Load the credentials from the json file
with open("credential/credential.json") as f:
	credentials = json.load(f)

form_data = {
	"user": credentials["username"],
	"password": credentials["password"],
	"cmd": "authenticate"
}

def is_internet_connected():
    try:
        # Attempt to establish a connection to the Google DNS server (8.8.8.8) on port 53, with a timeout of 3 seconds
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False

# Keep monitoring the network status with an interval of 5 seconds
interval = 10
while True:
	if (is_internet_connected()==False):
		# Show the timestamps for the corresponding status code
		current_datetime = datetime.now()
		formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
		print(formatted_datetime,end=" | ")

		# Send the POST request
		response = requests.post(login_url, data=form_data)

		# Check the response
		if response.status_code == 200:
			print("Login successful!")
		else:
			print(f"Login failed. Retry {interval} seconds later.")

	sleep(interval)
