import multiprocessing
from flaskapp import app
from chat import chatServer

server = chatServer("0.0.0.0", 8765)

def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    runFlask = multiprocessing.Process(target = run_flask)
    runChat = multiprocessing.Process(target = server.start)
    runFlask.start()
    runChat.start()
    runFlask.join()
    runchat.join()