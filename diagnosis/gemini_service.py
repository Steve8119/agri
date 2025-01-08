import os
import google.generativeai as genai

# Configure the API
genai.configure(api_key="AIzaSyAVHrRr52geDnzxxru2fQrJxPinwA3BC0g")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

def diagnose_problem(problem_description):
    """Send a message to the Gemini API and return the response."""
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(problem_description)
    return response.text
