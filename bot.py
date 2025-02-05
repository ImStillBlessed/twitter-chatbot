import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    def __init__(self):
        self.keywords = ["AI", "chatbot"]
        self.custom_prompt = None
        self.username = ""
        self.default_system_prompt = "You are a helpful assistant responding to tweets."

    def set_keywords(self, keywords):
        """Set keywords to scan for in tweets"""
        self.keywords = keywords

    def set_custom_prompt(self, prompt):
        """Set a custom system prompt for AI responses"""
        self.custom_prompt = prompt

    def get_system_prompt(self):
        """Get current system prompt"""
        return self.custom_prompt or self.default_system_prompt
    
    def set_username(self, username):
        """Set Twitter username to scan for tweets"""
        self.username = username

# Initialize bot configuration
bot_config = BotConfig()
