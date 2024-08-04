import threading
from flask import Flask, render_template
import socket
from waitress import serve
env = 'dev'  
host_ip = socket.gethostbyname(socket.gethostname())
from Mainapp import app




if __name__ == '__main__':
    if env == "production":
        print("WSGI SERVER")
        serve(app, host=host_ip, port=2000, threads=18, url_scheme='https')
    else:
        app.run(host=host_ip, port=2500, debug=True)
