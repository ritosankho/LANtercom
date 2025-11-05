!Warning: This is not for professional use. This is just for educational purposes and a fun weekend project. Do not use it in a public environment.


What is this?
    • This is a chatroom built using websockets and flask, and written in python.
    • It runs a http server on the host specified on the app.run() function, and a websocket server on the specified host and port while declaring the server object, both in main.py
    • Flask serves the lohin.html at the http server using the render_template() function, which asks credentials.
    • If the entered credentials are in the users dictionary (Where username is the key and password is tha value), it serves chatRoom.html. If it is not in the dictionary, it serves the loginFailure.html.
    • ChatRoom.html inputs the ip adress and connects to the websocket server hosted by chat.py.
    • Websocket server asks for a nickname, which is stored later in another dictionary clients, with the corresponding websocket clients.
    • It then handles the messaging.

How to use:
    1. Clone the repo
    2. Install dependencies listed in requirements.txt
    3. Specify host and port in main.py.
    4. Run main.py

What next?
    • Maybe I’ll add a system that periodically generates random 8 digit usernames and passwords and appends them to users.
    • I am looking to integrate the whole system with another piece of code later.
    • Possible microcontroller porting later (ESP32 most likely)
    • Encryption (?)
    • And a lot more...

I am a high school student interested mostly in embedded tech but I also ocassionaly like to tinker with other stuff like this. I am very new  to python. Any suggestions on how to improve, optmise or make this better in any way will be very hepful and highly appreciated.

Contact me:
    • ritosankho@proton.me
    • Instagram: @ritosankhohalder

Thank you for taking time to check out my repo.
