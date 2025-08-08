# RAG Chatbot Backend (Minimal Viable)

## Setup Instructions
git clone https://github.com/your-username/rag-chatbot-backend.git
cd rag-chatbot-backend

# Install dependencies
pip install -r requirements.txt

# Create .env file
# Copy .env.example to .env and fill in your keys:

OPENAI_API_KEY=your-key
AWS_ACCESS_KEY=your-key
AWS_SECRET_KEY=your-key
S3_BUCKET_NAME=your-bucket

# Run the app
uvicorn main:app --reload

# To run basic tests:
pytest