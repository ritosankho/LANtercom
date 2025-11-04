import asyncio
import websockets
from flask import Flask, redirect, url_for, request, render_template
from chat import start_chat_server
import multiprocessing

from flaskapp import app
from chat import start_chat_server

if __name__ == "__main__":
    runFlask = multiprocessing.Process(target = app.run)
    runChat = multiprocessing.Process(target = start_chat_server)
    runFlask.start()
    runChat.start()
    runFlask.join()
    runchat.join()