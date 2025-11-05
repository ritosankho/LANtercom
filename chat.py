import asyncio
import websockets

class chatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}
    def start(self):
           # Empty dictionary to store nickname info

        async def handler(ws):
            await ws.send("Enter your nickname for this chat:")  # Ask for nickname (Asyncronous function)

            
            nickname = await ws.recv()        # Receive nickname (Async function)
            self.clients[ws] = nickname
            print(f"{nickname} connected")

        
            join_msg = f"{nickname} has joined the chat!"      # Announce join
            await asyncio.gather(*[
                c.send(join_msg) for c in self.clientslients
            ])

            try:
                async for msg in ws:
                    full_msg = f"{nickname}: {msg}"
                    print(full_msg)

                    
                    await asyncio.gather(*[
                        c.send(full_msg) for c in self.clients     # Brodcast to everyone 
                    ])
            finally:
                leave_msg = f"{clients[ws]} has left the chat."        #Leaving chat
                print(leave_msg)

                del clients[ws]

                await asyncio.gather(*[
                    c.send(leave_msg) for c in self.clients
                ])

        async def main_async():
            async with websockets.serve(handler, self.host, self.port):
                print(f"WebSocket server running at ws://{self.host}:{self.port}")
                await asyncio.Future()

        asyncio.run(main_async())


