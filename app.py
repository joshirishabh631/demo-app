from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    time = datetime.datetime.now()
    return f"""
    <h1>CI/CD SUCCESS BY RISHABH</h1>
    <p><b>Pod Hostname:</b> {hostname}</p>
    <p><b>Deployed At:</b> {time}</p>
    <p><b>Status:</b> Running via ArgoCD + GitHub Actions</p>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
