import os
from dotenv import load_dotenv
import tweepy
from groq import Groq

def test_connections():
    load_dotenv()
    
    # Test Twitter
    try:
        client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
            bearer_token=os.getenv("TWITTER_BEARER_TOKEN")
        )
        me = client.get_me()
        print("✅ Twitter connection successful")
    except Exception as e:
        print(f"❌ Twitter Error: {e}")

    # Test Groq
    try:
        groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": "Test"}],
            model="mixtral-8x7b-32768"
        )
        print("✅ Groq connection successful")
    except Exception as e:
        print(f"❌ Groq Error: {e}")

if __name__ == "__main__":
    test_connections()