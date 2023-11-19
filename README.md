# CUHK-Wired-Network-Auto-Login

## Background

I have no idea why the wired network in CUHK requires manual authentication every 12 hours while the wireless network does not. This annoyed me so much that I wanted to write a program to monitor the network status, authenticate and reconnect automatically when the network disconnects.

![Alt text](/media/login_page.png)

## Idea

- Regularly checking the connection status between the Google DNS server and the local machine.
- Do a POST request with a pre-filled form to the login page directly if network disconnection is detected.

## How to install and run

1. Install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management.

   You may change the configuration of the location of the virtual environment to be in the project folder.

   ```bash
   poetry config virtualenvs.in-project true
   ```

2. Install dependencies. Poetry will automatically create a virtual environment.

   ```bash
   poetry install --no-root
   ```

   check if the dependencies are installed correctly.

   ```bash
   poetry show --tree
   ```

3. Activate the virtual environment.

   ```bash
   poetry shell
   ```
   or just activate it in the Python way.

4. Run the program.

   ```bash
   python "cuhk wired network auto login.py"
   `````

## How to use

Fill in the "credential/credential.json" file. Then run the program~

```
{
  "username": "<CUHK Email>",
  "password": "<Your Password>"
}
```

## To-do List

- [ ] Let the program run in the background instead of opening a terminal every time. (Maybe make it a tray icon?)