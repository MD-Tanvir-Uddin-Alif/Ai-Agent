from agent import agent_executor

def run_deal_finder():
    print("\n🔍 Welcome to the AI Deal Finder!")
    print("Ask anything like:\n - Find the best iPhone 15 deals\n - Cheapest gaming laptops under $1000\n - Best smartphone deals on Daraz\n")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("🧠 you: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Tata ;)")
            break
        
        try:
            print("\n🤖 Searching for the best deals...\n")
            result = agent_executor.invoke({"input": user_input})
            
            if isinstance(result, list):
            
                for idx, deal in enumerate(result, 1):
                    print(f"{idx}. 📦 {deal['title']}")
                    print(f"   💰 Price: {deal['price']}")
                    print(f"   🌟 Rating: {deal['rating']}")
                    print(f"   🔗 Link: {deal['link']}\n")
            else:
                print("-" * 60 + "\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")


if __name__ == "__main__":
    run_deal_finder()