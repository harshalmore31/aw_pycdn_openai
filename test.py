# basic_openai_server.py
# Prerequisite: pip install pycdn openai

from pycdn.server import CDNServer

def main():
    """Starts a basic PyCDN server configured to serve the OpenAI package."""
    print("🚀 Starting PyCDN Server for OpenAI...")
    print("This server will allow remote execution of the 'openai' package.")
    print("Ensure the 'openai' package is installed in this server's environment.")
    
    # Configure the server to allow the 'openai' package.
    # For security, it's best to explicitly list allowed packages.
    # Setting allowed_packages=None would allow any importable package.
    server = CDNServer(
        host="localhost",
        port=8000,
        debug=True,
        allowed_packages=["openai"]
    )
    
    print("\n🌐 Server running at http://localhost:8000")
    print("📦 Allowed packages: ['openai']")
    print("💡 Press Ctrl+C to stop the server.")
    
    try:
        # Start the server and wait for requests
        server.run()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")

if __name__ == "__main__":
    main()