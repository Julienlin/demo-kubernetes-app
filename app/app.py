import requests
import os
import socket
import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)


def info():
    return f"server hostname: {socket.gethostname()} server ip: {os.environ.get('POD_IP', socket.gethostbyname(socket.gethostname()))} client ip: {request.remote_addr}"


@app.route("/")
def tell_info():
    return info()


@app.route("/fortune")
def tell_fortune():
    fortune = subprocess.run(["fortune"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    request_info = info()

    return render_template("fortune.html", info=request_info, fortune=fortune)


@app.route("/fortune/cowsay")
def tell_fortune():
    fortune = subprocess.run(
        ["fortune", "|", "cowsay"], stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    request_info = info()

    return render_template("fortune.html", info=request_info, fortune=fortune)


@app.route("/actuator/health")
def health():
    return "ok"


def main():
    app.run(host="0.0.0.0", port="8080", debug=True)
