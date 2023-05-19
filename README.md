# CUHK-Wired-Network-Auto-Login

## Background

I have no idea why the wired network in CUHK requires authentication every 12 hours while the wireless network does not. This annoyed me so much that I want to write a program to monitor the network status, authenticate and reconnect automatically when the network disconnects.

## Idea

- Regularly checking the connection status between the Google DNS server and the local machine.
- Do a POST request with a pre-filled form to the login page directly if network disconnection is detected.

## Usage

Fill in the "credential.json" file. Then run the program~

## To-do List

### Have some ideas already

- [x] Make a POST request with pre-filled form
- [ ] Let the program run in the background instead of opening a terminal every time. (Maybe make it a tray icon?)

### No idea yet

- [ ] Better monitoring method instead of a while-true loop.