# main.py
from tools import get_price

def detect_intent(user_input: str):
    # Very basic intent detection
    if "btc" in user_input.lower():
        return "BTCUSDT"
    elif "eth" in user_input.lower():
        return "ETHUSDT"
    elif "doge" in user_input.lower():
        return "DOGEUSDT"
    else:
        return None

def run_agent():
    print("🤖 Hello! I can fetch real-time crypto prices.")
    print("Type something like: 'What's the price of BTC?' or type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        symbol = detect_intent(user_input)
        
        if symbol:
            print(get_price(symbol))
        else:
            print("🤖 Sorry, I couldn't understand which coin you want. Try 'BTC', 'ETH', or 'DOGE'.\n")

if __name__ == "__main__":
    run_agent()
