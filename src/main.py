# main.py
# This is the code for your "All-in-One" PyCDN Appwrite Cloud Function.
# It serves any package listed in requirements.txt.

import asyncio
from pycdn.server import CDNServer

# --- Server Configuration ---
# By setting allowed_packages=None, we tell the PyCDN server to allow
# remote execution for ANY package found in its environment.
# The security and availability are now controlled by what you put
# in your requirements.txt file.
PYCDN_SERVER = CDNServer(
    debug=True,
    allowed_packages=None
)

# Get the underlying ASGI app from the server instance.
# This is done once when the function runtime initializes (on a cold start).
ASGI_APP = PYCDN_SERVER.app

# This is the main entry point for the Appwrite function.
async def main(context):
    """
    An Appwrite function that acts as a generic, all-in-one PyCDN server.
    It translates the Appwrite request into an ASGI request, processes it with
    the PyCDN server, and returns the response.
    """
    context.log(f"All-in-One PyCDN function triggered. All installed packages are available.")

    # 1. Translate the Appwrite request into the standard ASGI 'scope' format.
    scope = {
        "type": "http",
        "http_version": "1.1",
        "method": context.req.method,
        "path": context.req.path,
        "scheme": context.req.scheme,
        "query_string": context.req.query_string.encode(),
        "headers": [(k.lower().encode(), v.encode()) for k, v in context.req.headers.items()],
        "client": ("127.0.0.1", 8000),
        "server": (context.req.host, context.req.port),
    }

    # 2. Define async handlers to capture the response from the ASGI app.
    response_status = 200
    response_headers = {}
    response_body = b''

    async def receive():
        return {"type": "http.request", "body": context.req.body_raw.encode(), "more_body": False}

    async def send(message):
        nonlocal response_status, response_headers, response_body
        if message["type"] == "http.response.start":
            response_status = message["status"]
            response_headers = {k.decode(): v.decode() for k, v in message["headers"]}
        elif message["type"] == "http.response.body":
            response_body += message.get("body", b"")

    # 3. Execute the PyCDN server's ASGI application.
    context.log(f"Executing request: {scope['method']} {scope['path']}")
    await ASGI_APP(scope, receive, send)
    context.log(f"Request finished with status: {response_status}")

    # 4. Return the captured response using the Appwrite context.
    return context.res.binary(
        response_body,
        response_status,
        response_headers
    )