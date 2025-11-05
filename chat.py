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

        # Notify others
        await self.handle_join(ws, nickname)

        try:
            async for msg in ws:
                full = f"{nickname}: {msg}"
                print(full)
                await self.broadcast(full)
        finally:
            await self.handle_leave(ws)

    # ------------------------------
    # --------- Start server -------
    # ------------------------------

    async def main_async(self):
        async with websockets.serve(self.handler, self.host, self.port):
            print(f"Chat server running at ws://{self.host}:{self.port}")
            await asyncio.Future()  # Run forever

    def start(self):
        asyncio.run(self.main_async())
