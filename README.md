# API

The main program is in main.py. Once the repo is cloned, run the application by executing the command below:
```bash
  python3 /venv/bin/uvicorn main:app --reload
```
The requests for testing the API is made in bash scripting in the file requests.sh. To run the test, ensure your terminal are in the directory containing the script then run the command below on the same terminal:
```bash
    chmod +x requests.sh && ./requests.sh
```
