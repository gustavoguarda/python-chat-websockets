import asyncio
import websockets

async def send_message(websocket):
    while True:
        message = input("Enter message: ")
        await websocket.send(message)
        print(f"Sent message: {message}")

async def receive_message(websocket):
    while True:
        response = await websocket.recv()
        print(f"Received: {response}")

async def chat():
    async with websockets.connect('ws://localhost:12345') as websocket:
        send_task = asyncio.create_task(send_message(websocket))
        receive_task = asyncio.create_task(receive_message(websocket))
        await asyncio.gather(send_task, receive_task)

if __name__ == "__main__":
    asyncio.run(chat())