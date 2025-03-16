# WhatsApp AI Integration

This project integrates Gemini AI with WhatsApp Business API using Quart as the backend framework.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create .env file:
- Copy .env.example to .env
- Add your Gemini API key
- Add your WhatsApp API credentials (when implemented)

## Running the Application

```bash
python -m quart run
```

## Running Tests

```bash
pytest tests/
```

## API Endpoints

- `GET /health`: Health check endpoint
- `POST /chat`: Send message to Gemini AI
  - Request body: `{"message": "Your message here"}`
  - Response: `{"response": "AI response", "status": "success"}`

## Future Implementations

- WhatsApp Business API integration
- Message history management
- User session handling 