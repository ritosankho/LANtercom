!Warning: This is not for professional use. This is just for educational purposes and a fun weekend project. Do not use it in a public environment.



This is a chatroom built using websockets and flask, and written in python.
It runs a http server on the host specified on the app.run() function, and a websocket server on the specified host and port while declaring the server object, both in main.py
Flask serves the lohin.html at the http server using the render_template() function, which asks credentials.
If the entered credentials are in the users dictionary (Where username is the key and password is tha value), it serves chatRoom.html. If it is not in the dictionary, it serves the loginFailure.html.
ChatRoom.html inputs the ip adress and connects to the websocket server hosted by chat.py.
Websocket server asks for a nickname, which is stored later in another dictionary clients, with the corresponding websocket clients.
It then handles the messaging.

How to use:<br>
     1. Clone the repo<br>
     2. Install dependencies listed in requirements.txt<br>
     3. Specify host and port in main.py.<br>
     4. Run main.py<br>

What next?<br>
    1. Maybe I’ll add a system that periodically generates random 8 digit usernames and passwords and appends them to users.<br>
    2. I am looking to integrate the whole system with another piece of code later.<br>
    3. Possible microcontroller porting later (ESP32 most likely)<br>
    4. Encryption (?)<br>
    5 .And a lot more...<br>

I am a high school student interested mostly in embedded tech but I also ocassionaly like to tinker with other stuff like this. I am very new  to python. Any suggestions on how to improve, optmise or make this better in any way will be very hepful and highly appreciated.

Contact me:<br>
    1. ritosankho@proton.me<br>
    2. Instagram: @ritosankhohalder<br>

Thank you for taking time to check out my repo.
