from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

# Add other endpoints here!
@app.route("/time")
def get_time():
    return "The time is " + datetime.now().strftime("%H:%M:%S")

# count endpoint
count_request = 0

def count():
    global count_requests
    count_requests += 1
    return f"The /count endpoint has been called {count_requests} times."

# Leave this at the bottom of your code
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)
