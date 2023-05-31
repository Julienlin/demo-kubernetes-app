import requests
import os
import socket

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def info():
    return f"server hostname: {socket.gethostname()} server ip: {request.host.split(':')[0]} client ip: {request.remote_addr}"


