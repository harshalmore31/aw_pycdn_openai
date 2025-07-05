# all_in_one_client.py (Corrected)
# This client demonstrates using multiple different packages
# from the single, all-in-one Appwrite PyCDN function.
#
# Local requirements: pip install pycdn python-dotenv

import os
import pycdn
from dotenv import load_dotenv

# --- Setup ---
load_dotenv()
APPWRITE_FUNCTION_URL = "https://685e19a20010ac4f850e.fra.appwrite.run/" # Your endpoint
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    print("🚀 Testing the All-in-One PyCDN Server")
    print("-" * 40)

    if not OPENAI_API_KEY:
        print("❌ OpenAI API key not found. Skipping OpenAI test.")
        return

    try:
        # Connect to your single, powerful Appwrite function
        print(f"🔗 Connecting to PyCDN at {APPWRITE_FUNCTION_URL}...")
        cdn = pycdn.pkg(APPWRITE_FUNCTION_URL)
        print("✅ Connected!")

        # --- Example 1: Use the 'openai' package (This part was already working) ---
        print("\n--- Testing OpenAI ---")
        from cdn.openai import OpenAI
        
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Hello from an all-in-one PyCDN!"}]
        )
        print("🤖 OpenAI Response:", response.choices[0].message.content)

        # --- Example 2: Use the 'requests' package (Corrected) ---
        print("\n--- Testing Requests ---")
        from cdn.requests import get

        # The 'get' function is executed on the server.
        # It returns a *proxy object* that represents the real `requests.Response` on the server.
        req_response_proxy = get("https://httpbin.org/get?param=pycdn")

        # *** THE FIX IS HERE ***
        # Instead of calling .json() on the local proxy, we tell the remote object to execute its .json() method.
        # PyCDN handles this remote method call seamlessly.
        # The server runs `response.json()` and sends back the resulting dictionary.
        data = req_response_proxy.json()
        
        print(f"🌍 Requests Response from httpbin.org (via server):")
        print(f"   Origin IP (the server's IP): {data['origin']}")
        print(f"   Query Param: {data['args']['param']}")


        # --- Example 3: Use the 'cryptography' package (This should work as is) ---
        print("\n--- Testing Cryptography ---")
        from cdn.cryptography.hazmat.primitives import hashes
        from cdn.cryptography.hazmat.backends import default_backend

        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(b"PyCDN is the future of package management!")
        hashed_value = digest.finalize()
        print(f"🔒 SHA256 Hash (calculated on server): {hashed_value.hex()}")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
        print("   Please check your Appwrite function URL and ensure it's deployed correctly.")

if __name__ == "__main__":
    main()