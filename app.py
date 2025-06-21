from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLO WORLD !!"

def run_app():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    t = threading.Thread(target=run_app)
    t.start()
    time.sleep(5)   # Run for 5 seconds
    print("✅ Flask app ran for 5 seconds, exiting now...")
