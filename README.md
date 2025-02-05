# Twitter AI Chatbot

A Python-based Twitter bot that scans user timelines for keywords and generates AI-powered responses using Groq API.

## Features

- 🔍 Scan Twitter timelines for specific keywords
- 🤖 Generate AI responses using Groq API
- 🎯 Customizable response prompts
- ⚙️ Flexible configuration options

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ImStillBlessed/twitter-chatbot.git
    cd twitter-chatbot
    ```

2. Create virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create *.env* file with your API keys:

    ```js
    TWITTER_API_KEY=your_key
    TWITTER_API_SECRET=your_secret
    TWITTER_ACCESS_TOKEN=your_token
    TWITTER_ACCESS_SECRET=your_secret
    TWITTER_BEARER_TOKEN=your_bearer
    GROQ_API_KEY=your_groq_key
    ```

5. Run bot:

    ```bash
    python main.py
    ```

## Configuration

### Available Options

0. Set Twitter username to monitor
1. Set keywords to scan for
2. Configure AI response prompts
3. View current settings
4. Start bot
5. Exit

#### Bot Settings

- **Username**: Twitter account to monitor
- **Keywords**: Terms to scan for (comma-separated)
- **Prompt Templates**:
  - Professional (business-focused)
  - Casual (friendly tone)
  - Technical (detailed analysis)
  - Custom (user-defined)

## Usage Examples

1. Basic Setup:

    ```bash
    # Start configuration
    python main.py

    # Set target username
    Choose option: 0
    Enter username: techuser123

    # Set keywords
    Choose option: 1
    Enter keywords: AI, Python, ML

    # Set response style
    Choose option: 2
    Select template: 1
    ```

2. Custom Prompt:

    ```bash
    Choose template (1-4): 4
    Enter your custom prompt: Respond with helpful tech tips and resources
    ```

## File Structure

```bash
twitter-chatbot/
├── main.py          # Entry point
├── bot.py           # Core config
├── handler.py       # Twitter API
├── groqsdk.py      # AI generation
├── .env            # Credentials
└── README.md       # Documentation
```

## API Reference

### BotConfig Class

- set_keywords(keywords): Set scan keywords
- set_custom_prompt(prompt): Set AI response prompt
- get_system_prompt(): Get current prompt
- set_username(username): Set target Twitter user

### Twitter Interactions

```bash
scan_timeline(username, keywords)  # Scan tweets
post_to_twitter(text)             # Post response
```

### AI Generation

```bash
generate_ai_response(tweet)    # Generate response
generate_default_response()    # Fallback response
```

## Troubleshooting

### Common issues

- "Error fetching tweets": Verify Twitter API credentials
- "Unable to generate response": Check Groq API key
- "Invalid choice": Follow menu options 0-5

### Debug Steps

- Verify .env file exists
- Check API key format
- Confirm internet connection
- Check console output

## Requirements

- Python 3.8+
- Tweepy
- Groq SDK
- python-dotenv

## License

MIT License - See LICENSE file
