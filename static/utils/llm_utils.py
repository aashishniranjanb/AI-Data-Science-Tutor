import google.generativeai as genai
import os

def get_llm(prompt: str) -> str:
    """
    Sends the user's prompt to Google's Gemini 1.5 Pro 
    model and returns the AI-generated response.
    """
    # Ensure the API key is available
    api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyBVOM4Pct30jaUcFUiXpbMy4hVOv2f3kKk")
    if not api_key:
        return "⚠️ API key not found. Please set GOOGLE_API_KEY in your environment."
    
    try:
        genai.configure(api_key=api_key)
        
        # Instantiate the Gemini model
        model = genai.GenerativeModel("gemini-1.5-pro")
        
        # Generate response
        response = model.generate_content(prompt)
        
        if response and hasattr(response, 'text'):
            return response.text
        else:
            return "Sorry, I couldn't generate a response at this time."
    
    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"
