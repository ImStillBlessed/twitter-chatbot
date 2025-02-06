from bot import BotConfig
from handler import scan_timeline

def configure_bot():
    config = BotConfig()
    
    while True:
        print("\n=== Twitter Bot Configuration ===")
        # print("0. Set Twitter username")
        print("1. Set keywords")
        print("2. Set custom prompt")
        print("3. View current settings")
        print("4. Start bot")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        # if choice == "0":
        #     username = input("Enter Twitter username: ")
        #     config.set_username(username)
        #     print(f"Username set: {username}")
        
        if choice == "1":
            keywords = input("Enter keywords (comma-separated): ").split(",")
            keywords = [k.strip() for k in keywords if k.strip()]
            config.set_keywords(keywords)
            print(f"Keywords set: {keywords}")
            
        elif choice == "2":
            print("\nPrompt Templates:")
            print("1. Professional: 'Respond professionally with industry insights'")
            print("2. Casual: 'Generate friendly, casual responses'")
            print("3. Technical: 'Provide technical analysis'")
            print("4. Custom prompt")
            
            prompt_choice = input("Choose template (1-4): ")
            
            if prompt_choice == "4":
                custom_prompt = input("Enter your custom prompt: ")
                if custom_prompt.strip():
                    config.set_custom_prompt(custom_prompt)
                    print("Custom prompt set successfully")
            else:
                templates = {
                    "1": "Respond professionally with industry insights",
                    "2": "Generate friendly, casual responses",
                    "3": "Provide technical analysis"
                }
                if prompt_choice in templates:
                    config.set_custom_prompt(templates[prompt_choice])
                    print(f"Template prompt set: {templates[prompt_choice]}")
                    
        elif choice == "3":
            print(f"\nCurrent Settings:")
            print(f"Keywords: {config.keywords}")
            print(f"Prompt: {config.get_system_prompt()}")
            # print(f"Username: {config.username}")
            
        elif choice == "4":
            # if not config.username:
            #     print("Error: Please set a Twitter username.")
            #     continue
            if not config.keywords:
                print("Error: Please set keywords to scan for.")
                continue
            print("\nStarting bot...")
            scan_timeline(config.keywords)
            
        elif choice == "5":
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    configure_bot()