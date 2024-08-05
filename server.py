import asyncio
import websockets

# Set of connected clients
connected_clients = set()

# Function to handle each client connection
async def handle_client(websocket, path):
    # Add the new client to the set of connected clients
    connected_clients.add(websocket)
    print(f"New client connected: {websocket.remote_address}")

    try:
        # Listen for messages from the client
        async for message in websocket:
            print(f"Received message from {websocket.remote_address}: {message}")
            # Broadcast the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
                    print(f"Sent message to {client.remote_address}")
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")
    finally:
        # Remove the client from the set of connected clients
        connected_clients.remove(websocket)

# Main function to start the WebSocket server
async def main():
    server = await websockets.serve(handle_client, 'localhost', 12345)
    print("Server started on ws://localhost:12345")
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    asyncio.run(main())