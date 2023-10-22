import requests
import json
import socket
from time import sleep
from datetime import datetime, timedelta
from win11toast import toast
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


def print_message(message, toast_title=None, need_toast=True):
    # show the timestamps for the corresponding status code
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # print timestamps with the message
    print(formatted_datetime, "|", message)

    if need_toast is True:
        threading.Thread(
            target=toast,
            # need to provide a tuple for arguments to correctly unpack in the function
            args=(
                toast_title,
                message,
            ),
            kwargs={"duration": "short"},
        ).start()


def get_expiry_time():
    expiry_time = datetime.now() + timedelta(hours=12)

    expiry_time_str = expiry_time.strftime("%Y-%m-%d %H:%M:%S")
    return expiry_time_str


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
            print_message(
                toast_title="Network disconnected",
                message=f"Reconnecting as <{credentials['username']}>...",
                need_toast=True,
            )

            response = requests.post(login_url, data=form_data)
            # print (response.text)

            if is_internet_connected():
                print_message(
                    toast_title="Login successful",
                    message=f"It will expire at around {get_expiry_time()}.",
                    need_toast=True,
                )
            else:
                print_message(
                    toast_title=f"Login failed",
                    message=f"Please check your credentials in the json file.",
                    need_toast=True,
                )
        else:
            cnt += 1
            # print the network status every 1 minute
            if cnt == 12:
                print_message(
                    toast_title=default_toast_title,
                    message="Network is already connected to Internet. :D",
                    need_toast=False,
                )
                cnt=0
                
            # monitor the network status every 5 seconds
            sleep(5)
