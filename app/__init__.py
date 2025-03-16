from quart import Quart
import google.generativeai as genai
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables
    load_dotenv()
    
    # Initialize Quart app
    app = Quart(__name__)
    
    # Configure Gemini API
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')
    
    # Store model instance in app config
    app.config['AI_MODEL'] = model
    
    # Import and register routes
    from app.routes import chat_bp
    app.register_blueprint(chat_bp)
    
    return app 