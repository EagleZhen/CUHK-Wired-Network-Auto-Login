import infi.systray
from os.path import dirname, join, abspath


def hello(systray):
    print("Hello!")


# Load the tray icon image using relative path to the script directory
script_dir = dirname(abspath(__file__))
icon_path = join(script_dir, "../icon/icon.ico")
# pause(icon_path)

# Create the tray icon menu, each bracket for one menu option
# "Hello": text label for the option
# None: icon for the option
# hello: callback function for the option
menu_options = (("Hello", None, hello),)

# # Create the tray icon object
systray_options = {
    "menu_options": menu_options,
    "icon": icon_path,
    "hover_text": "auto connect cuhk wired network",
}
tray = infi.systray.SysTrayIcon(**systray_options)

# Start the tray icon event loop
tray.start()
