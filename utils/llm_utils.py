import google.generativeai as genai

def get_llm(prompt: str) -> str:
    """
    Sends the user's prompt to Google's Gemini 1.5 Pro 
    model and returns the AI-generated response.
    """
    # Use the global API key set in app.py
    api_key = "AIzaSyBVOM4Pct30jaUcFUiXpbMy4hVOv2f3kKk" 
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel("gemini-1.5-pro")
    
    response = model.generate_content(prompt)
    if response and hasattr(response, 'text'):
        return response.text
    else:
        return "Sorry, I couldn't generate a response at this time."
