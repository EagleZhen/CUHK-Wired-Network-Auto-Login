import requests
import json
import socket
from datetime import datetime, timedelta
from win11toast import toast


def is_internet_connected():
    try:
        # Attempt to establish a connection to
        # the Google DNS server (8.8.8.8) on port 53,
        # with a timeout of 3 seconds
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        print("OSError")
        pass
    return False


def print_message(message):
    # Show the timestamps for the corresponding status code
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Print timestamps with the message
    print(formatted_datetime, "|", message)


def get_expiry_time():
    expiry_time = datetime.now() + timedelta(hours=12)

    expiry_time_str = expiry_time.strftime("%Y-%m-%d %H:%M:%S")
    return expiry_time_str


if __name__ == "__main__":
    toast_title = "CUHK Wired Network Auto Login"

    toast(toast_title, "Detected Network Change")

    login_url = "https://securelogin.net.cuhk.edu.hk/cgi-bin/login"

    # Load the credentials from the json file
    with open("credential/credential.json") as f:
        credentials = json.load(f)

    form_data = {
        "user": credentials["username"],
        "password": credentials["password"],
        "cmd": "authenticate",
    }

    if not is_internet_connected():
        toast(
            toast_title,
            "Network disconnected. Reconnecting as "
            f"<{credentials['username']}>...",
        )

        # Send the POST request
        requests.post(login_url, data=form_data)

        if is_internet_connected():
            toast(
                toast_title,
                "Login successful! It will expire at around "
                f"{get_expiry_time()}",
            )
        else:
            toast("Login failed.")
    else:
        toast("Network is already connected")
