import asyncio
import websockets
from flask import Flask, redirect, url_for, request, render_template
from chat import start_chat_server
import multiprocessing

from flaskapp import app
from chat import start_chat_server

def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    runFlask = multiprocessing.Process(target = run_flask)
    runChat = multiprocessing.Process(target = start_chat_server)
    runFlask.start()
    runChat.start()
    runFlask.join()
    runchat.join()