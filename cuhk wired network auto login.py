import requests
import json
import socket
from time import sleep
from datetime import datetime

def is_internet_connected():
    try:
        # Attempt to establish a connection to the Google DNS server (8.8.8.8) on port 53, with a timeout of 3 seconds
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False

def print_message(message):
	# Show the timestamps for the corresponding status code
	current_datetime = datetime.now()
	formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
	# Print timestamps with the message
	print(formatted_datetime,"|",message)

login_url = "https://securelogin.net.cuhk.edu.hk/cgi-bin/login"

# Load the credentials from the json file
with open("credential/credential.json") as f:
	credentials = json.load(f)

form_data = {
	"user": credentials["username"],
	"password": credentials["password"],
	"cmd": "authenticate"
}

# Keep monitoring the network status with an interval of 5 seconds
interval = 5
print_message("Network monitoring started...")
while True:
	if (is_internet_connected()==False):
		print_message("Network disconnected.")

		while (is_internet_connected()==False):
			# Send the POST request
			requests.post(login_url, data=form_data)

			if (is_internet_connected()==True):
				print_message("Login successful!")
			else:
				print_message(f"Login failed. Trying to reconnect after a few seconds...")

	# Break between every netowrk status checking
	sleep(interval)