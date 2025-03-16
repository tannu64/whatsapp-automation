from quart import Blueprint, request, jsonify, current_app

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/health', methods=['GET'])
async def health_check():
    return jsonify({'status': 'healthy'}), 200

@chat_bp.route('/chat', methods=['POST'])
async def chat():
    try:
        data = await request.get_json()
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Get model instance from app config
        model = current_app.config['AI_MODEL']
        
        # Generate response using Gemini
        response = model.generate_content(user_message)
        
        return jsonify({
            'response': response.text,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500 