import requests
import os
import socket
import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def info():
    return f"server hostname: {socket.gethostname()} server ip: {request.host.split(':')[0]} client ip: {request.remote_addr}"

@app.route("/fortune")
def tell_fortune():
    fortune = subprocess.run(["fortune"], stdout=subprocess.PIPE).stdout.decode('utf-8')

    return render_template('fortune.html', fortune=fortune)


def main():
    app.run(host="0.0.0.0", port="8080", debug=True)




