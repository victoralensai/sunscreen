# Sunscreen advisor API

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
- [ ] make an app that uses the api in order to have notification on your phone telling you if you should put sunscreen today, which hour etc.
