import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


class SummarizerAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        with open("prompts/summarization_prompt.txt", "r", encoding="utf-8") as f:
            self.prompt_template = f.read()
            
    def run(self, chunks):
        print("[SummarizerAgent] Generating structured summary with Gemini...")
        
        combine_text = "\n\n".join([chunk.page_content for chunk in chunks])
        
        prompt = f"{self.prompt_template}\n\n---\n\n{combine_text}"

        response = self.model.generate_content(prompt)

        try:
            summary = response.text
        except Exception as e:
            summary = f"[ERROR] Gemini generation failed: {e}"

        print("[SummarizerAgent] ✅ Summary complete.")
        return summary