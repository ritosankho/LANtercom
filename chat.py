import asyncio
import websockets

def start_chat_server(host="0.0.0.0", port=8765):
    clients = {}   # maps websocket -> nickname

    async def handler(ws):
        # Ask for nickname
        await ws.send("Enter your nickname for this chat:")

        # Receive nickname
        nickname = await ws.recv()
        clients[ws] = nickname
        print(f"{nickname} connected")

        # Announce join
        join_msg = f"{nickname} has joined the chat!"
        await asyncio.gather(*[
            c.send(join_msg) for c in clients
        ])

        try:
            async for msg in ws:
                full_msg = f"{nickname}: {msg}"
                print(full_msg)

                # Broadcast to everyone else
                await asyncio.gather(*[
                    c.send(full_msg) for c in clients
                ])
        finally:
            leave_msg = f"{clients[ws]} has left the chat."
            print(leave_msg)

            del clients[ws]

            await asyncio.gather(*[
                c.send(leave_msg) for c in clients
            ])

    async def main_async():
        async with websockets.serve(handler, host, port):
            print(f"WebSocket server running at ws://{host}:{port}")
            await asyncio.Future()

    asyncio.run(main_async())


if __name__ == "__main__":
    #app.run(debug=True)
    start_chat_server()