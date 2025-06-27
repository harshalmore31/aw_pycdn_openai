# pycdn_openai_server.py

from pycdn.server import CDNServer
from fastapi import Request
import os
import openai

# Define your OpenAI-based handler function
async def handle_request(request: Request):
    path = request.url.path
    headers = request.headers

    # Setup OpenAI API Key (can be passed from headers or env)
    openai.api_key = headers.get("x-openai-key") or os.getenv("OPENAI_API_KEY")

    if path == "/ping":
        return {"message": "Pong"}

    try:
        # Dummy usage of OpenAI: listing available models
        models = openai.models.list()
        return {
            "total_models": len(models['data']),
            "example_model": models['data'][0]['id'] if models['data'] else None,
            "note": "Successfully fetched model list from OpenAI"
        }
    except Exception as e:
        return {"error": str(e)}

# Launch the PyCDN server with OpenAI support
def main():
    allowed_packages = ["openai"]

    server = CDNServer(
        host="0.0.0.0",
        port=8000,
        debug=True,
        allowed_packages=allowed_packages
    )

    # Register route
    server.app.get("/{path:path}")(handle_request)

    print("🚀 PyCDN Server running on http://localhost:8000")
    print(f"📦 Allowed packages: {allowed_packages}")

    server.run()

if __name__ == "__main__":
    main()
