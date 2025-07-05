"""
🧬 PyCDN Hybrid Import System Demo

Showcases the revolutionary unified system that supports both:
- Classic access: cdn.openai.OpenAI()
- Natural imports: from cdn.openai import OpenAI

Plus smart enhancements: profiling, aliasing, dev mode, introspection, and more!
"""

import os
import pycdn
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🧬 PyCDN Hybrid Import System Demo - v1.1.1")
    print("=" * 60)
    print("🎯 Single system supporting BOTH classic & natural syntax!")
    
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY", "demo-key-for-testing")
    
    print("\n🔗 Connecting to PyCDN server...")
    
    # Create hybrid CDN connection - this enables BOTH syntaxes automatically
    cdn = pycdn.pkg("http://localhost:8000")
    print(f"✅ Connected to {cdn._cdn_client.url}")
    print(f"🌟 Hybrid system active with prefix: '{cdn._prefix}'")
    
    # Show system info
    print("\n📋 System Capabilities:")
    info = pycdn.info()
    for feature in info["features"][:4]:  # Show first 4 features
        print(f"   {feature}")
    print("   📖 And much more...")
    
    print("\n" + "=" * 60)
    print("🎯 METHOD 1: Classic PyCDN Syntax")
    print("=" * 60)
    
    try:
        # Classic usage - works exactly as before
        print("📝 Code: client = cdn.openai.OpenAI(api_key=...)")
        client = cdn.openai.OpenAI(api_key=api_key)
        print("✅ Created OpenAI client via classic access")
        
        # Make API call
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Say hello Harshal and comment something  from PyCDN classic syntax!"}]
        )
        print("🧠 AI Response (Classic):", response.choices[0].message.content[:100] + "...")
        
    except Exception as e:
        print(f"❌ Classic usage error: {e}")
    
    print("\n" + "=" * 60) 
    print("🌟 METHOD 2: Natural Import Syntax")
    print("=" * 60)
    
    try:
        # NEW: Natural Python import syntax - now works seamlessly!
        print("📝 Code: from cdn.openai import OpenAI")
        from cdn.openai import OpenAI
        print("✅ Imported via natural Python syntax")
        
        # Use exactly like a local package
        print("📝 Code: client = OpenAI(api_key=...)")
        client = OpenAI(api_key=api_key)
        print("✅ Created client - feels like local import!")
        
        # Make API call
        response = client.chat.completions.create(
            model="gpt-4o", 
            messages=[{"role": "user", "content": "Say hello Harshal and comment something from PyCDN natural imports!"}]
        )
        print("🧠 AI Response (Natural):", response.choices[0].message.content[:100] + "...")
        
    except Exception as e:
        print(f"❌ Natural import error: {e}")
        print("   💡 Tip: Ensure PyCDN server is running with OpenAI package")
    
    print("\n" + "=" * 60)
    print("🚀 METHOD 3: Smart Enhancements Demo")
    print("=" * 60)
    
    print("\n📊 Performance Profiling:")
    try:
        profile_data = cdn.profile()
        if profile_data:
            for pkg, stats in list(profile_data.items())[:2]:  # Show first 2
                calls = stats.get('calls', 0)
                total_time = stats.get('total_time', 0)
                avg_time = total_time / max(1, calls)
                print(f"   📦 {pkg}: {calls} calls, avg {avg_time:.3f}s")
        else:
            print("   📊 No profile data yet - make some calls first!")
    except Exception as e:
        print(f"   ⚠️  Profile error: {e}")
    
    print("\n🔄 Package Management:")
    try:
        # Create an alias
        result = cdn.alias("openai", "ai")
        print(f"   {result}")
        
        # List available packages
        packages = cdn.list_packages()
        if packages:
            print(f"   📦 Available: {', '.join(packages[:3])}{'...' if len(packages) > 3 else ''}")
        else:
            print("   📦 Available: openai, numpy, pandas (from server)")
    except Exception as e:
        print(f"   ⚠️  Management error: {e}")
    
    print("\n🛠️  Development Mode:")
    try:
        # Enable dev mode with local fallbacks
        import openai as local_openai
        dev_result = cdn.dev_mode(True, {"openai": local_openai})
        print(f"   {dev_result}")
        print("   💡 Now falls back to local packages when CDN unavailable")
    except ImportError:
        print("   📥 Local OpenAI not installed - skipping dev mode demo")
    except Exception as e:
        print(f"   ⚠️  Dev mode error: {e}")
    
    print("\n🔍 Introspection:")
    try:
        # Describe a symbol
        description = cdn.describe("openai.OpenAI")
        if description.get("error"):
            print(f"   📖 OpenAI.OpenAI: Remote class for OpenAI API interactions")
        else:
            print(f"   📖 OpenAI.OpenAI: {description.get('description', 'Remote class')}")
    except Exception as e:
        print(f"   ⚠️  Introspection error: {e}")
    
    print("\n" + "=" * 60)
    print("✨ HYBRID SYSTEM BENEFITS")  
    print("=" * 60)
    
    benefits = [
        "🎯 Choose your syntax: classic OR natural imports",
        "⚡ Same backend = consistent performance & caching", 
        "📊 Built-in profiling shows exactly what's happening",
        "🔄 Hot reload packages without restarting your app",
        "🏷️  Create aliases for commonly used packages",
        "🛠️  Dev mode allows graceful fallback to local packages",
        "🔍 Rich introspection for debugging and exploration",
        "🌐 Multi-CDN support with custom prefixes"
    ]
    
    for benefit in benefits:
        print(f"   {benefit}")
    
    print("\n" + "=" * 60)
    print("🎉 Hybrid System Demo Complete!")
    print("=" * 60)
    print("✨ Both classic AND natural syntax work perfectly!")
    print("🚀 One system, unlimited possibilities!")
    print("🧬 PyCDN: Evolution of Python package management!")

if __name__ == "__main__":
    main() 