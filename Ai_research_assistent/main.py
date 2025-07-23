from agents.reader_agent import ReaderAgent
from agents.summarizer_agent import SummarizerAgent
from agents.explainer_agent import ExplainerAgent

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="AI Research Assistant")
    parser.add_argument("--file", required=True, help="Path to PDF file")
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print("[ERROR] File not found.")
        return
    
    print("\n🚀 Starting AI Research Assistant\n")
    
    reader = ReaderAgent(args.file)
    chunks = reader.run()
    
    if not chunks:
        print("[❌] No content extracted from PDF.")
        return
    
    summarizer = SummarizerAgent()
    summary = summarizer.run(chunks)

    print("\n📄 === Research Paper Summary ===\n")
    print(summary)
    
    while True:
        concept = input("\n❓ Want an explanation for any term? (type or press Enter to exit): ").strip()
        if not concept:
            break

        explainer = ExplainerAgent()
        explanation = explainer.run(concept)

        print("\n📘 === Explanation ===\n")
        print(explanation)

    print("\n✅ All done. Goodbye!\n")

if __name__ == "__main__":
    main()