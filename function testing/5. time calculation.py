from datetime import datetime, timedelta

def get_expiry_time():
	current_time = datetime.now()
	expiry_time = current_time + timedelta(hours=12)

	current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
	expiry_time_str = expiry_time.strftime("%Y-%m-%d %H:%M:%S")

	print("Current Time:", current_time_str)
	print("Expiry Time:", expiry_time_str)

get_expiry_time()
