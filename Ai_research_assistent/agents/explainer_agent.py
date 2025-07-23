import os
from dotenv import load_dotenv
import google.generativeai as genai
from tools.web_search import web_search_tools


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class ExplainerAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    
    def run(self, concept):
        print(f"[ExplainerAgent] Explaining concept: {concept}")
        
        web_context = web_search_tools(concept)
        
        prompt = f"""
            You are an AI explainer assistant.

            Explain the following technical term clearly and simply, as if to a researcher from a different field.

            📌 Term: {concept}

            You can use this background information from the web for accuracy:
            ---
            {web_context}
            ---

            Write a detailed, readable explanation.
            """
        try:
            responce = self.model.generate_content(prompt)
            explanation = responce.text
        except Exception as e:
            explanation = f"[ERROR] Gemini failed: {e}"

        print("[ExplainerAgent] ✅ Explanation ready.")
        return explanation