from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
import json
from typing import Dict, List
import uvicorn
from pathlib import Path

app = FastAPI()
html_file = Path(__file__).parent / "index.html"


active_connections: Dict[str, WebSocket] = {}


class IncomingMessage(BaseModel):
    text: str = Field(..., min_length=1, max_length=200)


class OutgoingMessage(BaseModel):
    type: str  # "message", "system", "error", "private"
    user: str = ""
    text: str = ""
    ts: str = ""
    detail: str = ""


async def send_json(websocket: WebSocket, message: OutgoingMessage):
    await websocket.send_text(message.model_dump_json())


async def broadcast_system(message_text: str):
    online_count = len(active_connections)
    system_msg = OutgoingMessage(
        type="system",
        text=f"{message_text} (online: {online_count})",
        ts=datetime.now().isoformat()
    )
    for client in active_connections.values():
        await send_json(client, system_msg)

@app.get("/")
async def get_chat():
    HTML_TEMPLATE = html_file.read_text(encoding="utf-8")
    return HTMLResponse(content=HTML_TEMPLATE)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str = None):

    if not username:
        await websocket.close(code=1008, reason="Username required")
        return


    if username in active_connections:
        await websocket.close(code=1008, reason="Username already taken")
        return

    await websocket.accept()
    active_connections[username] = websocket


    await broadcast_system(f"{username} joined")

    try:
        while True:

            raw_data = await websocket.receive_text()


            try:
                data = json.loads(raw_data)
                incoming = IncomingMessage(**data)
            except (json.JSONDecodeError, ValidationError) as e:
                error_msg = OutgoingMessage(
                    type="error",
                    detail="Invalid message format or validation failed (1-200 chars)",
                    ts=datetime.now().isoformat()
                )
                await send_json(websocket, error_msg)
                continue

            text = incoming.text.strip()
            if not text:
                error_msg = OutgoingMessage(
                    type="error", detail="Message cannot be empty", ts=datetime.now().isoformat()
                )
                await send_json(websocket, error_msg)
                continue


            if text.startswith("/w "):
                parts = text.split(" ", 2)
                if len(parts) < 3:
                    error_msg = OutgoingMessage(type="error", detail="Usage: /w username message")
                    await send_json(websocket, error_msg)
                    continue
                target_user = parts[1]
                private_text = parts[2]

                if target_user not in active_connections:
                    error_msg = OutgoingMessage(type="error", detail=f"User {target_user} not online")
                    await send_json(websocket, error_msg)
                    continue


                private_msg = OutgoingMessage(
                    type="private",
                    user=username,
                    text=private_text,
                    ts=datetime.now().isoformat()
                )
                await send_json(active_connections[target_user], private_msg)


                confirm_msg = OutgoingMessage(
                    type="system",
                    text=f"Private to {target_user}: {private_text}",
                    ts=datetime.now().isoformat()
                )
                await send_json(websocket, confirm_msg)
                continue


            broadcast_msg = OutgoingMessage(
                type="message",
                user=username,
                text=text,
                ts=datetime.now().isoformat()
            )
            for user, conn in active_connections.items():
                await send_json(conn, broadcast_msg)

    except WebSocketDisconnect:

        del active_connections[username]
        await broadcast_system(f"{username} left")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)