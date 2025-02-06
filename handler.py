import os
from dotenv import load_dotenv
import tweepy
from bot import bot_config
from groqsdk import generate_ai_response, generate_default_response

load_dotenv()

# Authenticate with Twitter API v2
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN")
)

# Function to post to Twitter
def post_to_twitter(response_text):
    try:
        tweet = client.create_tweet(text=response_text, user_auth=True)
        print("Tweet posted successfully!")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

# Scan user timeline for keywords and respond
def scan_timeline(keywords):
    """Scan timeline with configurable keywords"""
    keywords = keywords or bot_config.keywords
    
    try:
        user = client.get_me(user_auth=True)
        # user_id = user.data.id
        tweets = client.get_home_timeline(max_results=10)

        if tweets.data:
            for tweet in tweets.data:
                for keyword in keywords:
                    if keyword.lower() in tweet.text.lower():
                        print(f"Match found: {tweet.text}")
                        ai_response = generate_ai_response(tweet.text)
                        print(f"AI Response: {ai_response}")
                        post_to_twitter(ai_response)  # Post the AI response to Twitter
                        return ai_response

            # If no match found, generate and print default response
            default_response = generate_default_response()
            print(f"Default Response: {default_response}")
            post_to_twitter(default_response)  # Post the default response to Twitter
            return default_response
        else:
            print("No tweets found.")
            default_response = generate_default_response()
            print(f"Default Response: {default_response}")
            post_to_twitter(default_response)  # Post the default response to Twitter
            return default_response
    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")
        return "Error fetching tweets."
