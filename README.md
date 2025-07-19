# Sunscreen advisor API

## Self-hosted setup

You can quickly get this up and running by following these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/victoralensai/sunscreen
   ```
2. Navigate into the cloned directory:
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set the `PYTHONPATH` environment variable:
    For linux/macOS:
    ```bash
    export PYTHONPATH=$(pwd)
    ```
    For Windows (PowerShell):
    ```powershell
    $env:PYTHONPATH = (Get-Location).Path
    ```
    For Windows (Command Prompt):
    ```cmd
    set PYTHONPATH=%cd%
    ```
5. (optional) Run the API:
   ```bash
   fastapi dev api/main.py
   ```
   _By default, it uses my public API : https://f1.vctor.me but be aware of the usage limits if many use it._
6. Create a `.env` file in the root directory and add your API key:
   ```
   api_key=your_api_key_from_weatherapi.com
   ```
7. changes the value in `app.py` and run the main script:
   ```bash
   python app.py
   ```

## Get notifications on a device
Download the [ntfy](https://ntfy.sh/) app on your device and subscribe to a topic with the format `<random_string>_location`. The topic is explicitly given when running the main loop.

## Work with the API
once your inside the repository folder, you can run the following commands to set up and run the API:

```bash
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
fastapi dev main.py
```

inside a .env file, you **have to** set the following variable:

```bash
api_key=your_api_key_from_weatherapi.com
```

# TODOs
- [ ] remove useless api function that were just for testing
- [x] Use ntfy with the API to send notifications to your subject (eg. "<random_string_for_you>&location=<location>) and the ntfy server will send you a notification with the UV index and a message telling you if you should put sunscreen or not to the subject.
- [x] Easy config file/startup file for the app.py _(sort of, it is just changing the values in app.py)_