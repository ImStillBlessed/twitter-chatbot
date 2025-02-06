import os
from bot import bot_config
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ai_response(tweet_text):
    try:
        response = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": bot_config.get_system_prompt()},
                {"role": "user", "content": tweet_text,}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )
        ai_response = response.choices[0].message.content
        print(f"Generated AI Response: {ai_response}")
        return ai_response
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "I'm unable to generate a response at the moment."

def generate_default_response():
    keywords_str = ", ".join(bot_config.keywords.copy())
    
    default_prompt = f"generate a tweet from these keywords: {keywords_str}"
    return generate_ai_response(default_prompt)
