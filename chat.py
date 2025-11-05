import asyncio
import websockets

class chatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        # All connected clients: { websocket : nickname }
        self.clients = {}

    # ------------------------------
    # ---- Helper functionality ----
    # ------------------------------

    async def broadcast(self, msg, exclude=None):
        """Send a message to all clients, optionally excluding someone."""
        targets = [ws for ws in self.clients if ws != exclude]
        if targets:
            await asyncio.gather(*[ws.send(msg) for ws in targets])

    async def handle_join(self, ws, nickname):
        """Announce that someone joined."""
        join_msg = f"{nickname} has joined the chat!"
        print(join_msg)
        await self.broadcast(join_msg)

    async def handle_leave(self, ws):
        """Announce that someone left."""
        nickname = self.clients.get(ws)
        leave_msg = f"{nickname} has left the chat."
        print(leave_msg)
        del self.clients[ws]
        await self.broadcast(leave_msg)

    # ------------------------------
    # --------- Main handler -------
    # ------------------------------

    async def handler(self, ws):
        # Ask nickname
        await ws.send("Enter your nickname:")
        nickname = await ws.recv()

        # Save client
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
