import requests
import json
import socket
from time import sleep
from datetime import datetime, timedelta
import threading


def is_internet_connected():
    try:
        # attempt to establish a connection to
        # the Google DNS server (8.8.8.8) on port 53,
        # with a timeout of 3 seconds
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False


def print_message(message, write_to_log=True):
    # show the timestamps for the corresponding status code
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # print timestamps with the message
    print(formatted_datetime, "|", message)

    if write_to_log:
        with open("credential/log.txt", "a") as log:
            log.write(formatted_datetime + " | " + message + "\n")


def get_expiry_time():
    expiry_time = datetime.now() + timedelta(hours=12)

    expiry_time_str = expiry_time.strftime("%Y-%m-%d %H:%M:%S")
    return expiry_time_str

sleep_interval = 5

if __name__ == "__main__":
    default_toast_title = "CUHK ResNet Auto Renew Script"
    login_url = "https://securelogin.net.cuhk.edu.hk/cgi-bin/login"

    # Load the credentials from the json file
    with open("credential/credential.json") as f:
        credentials = json.load(f)

    form_data = {
        "user": credentials["username"],
        "password": credentials["password"],
        "cmd": "authenticate",
    }

    cnt = 0
    while True:
        if not is_internet_connected():
            print_message(message=f"Reconnecting as <{credentials['username']}>...")

            try:
                response = requests.post(login_url, data=form_data)
            except requests.exceptions.RequestException as e:
                print_message(message=f"Request Error:\n{e}\n")

            if is_internet_connected():
                sleep_interval = 5 # restore the sleep interval to 5 seconds
                print_message(message=f"Login succeess: It will expire at around {get_expiry_time()}.")
            else:
                sleep_interval = 1 # allow faster retry to reconnect the network as fast as possible
                print_message(message=f"Login failed: Retry in 1 second.")
        else:
            cnt += 1
            # print the network status every 1 minute
            if cnt == 12:
                print_message(message="Network is already connected to Internet. :D", write_to_log=False)
                cnt = 0

        # monitor the network status every 5 seconds
        sleep(sleep_interval)
