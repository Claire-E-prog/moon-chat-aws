# moon-chatbot/moon-chatbot/README.md

# Moon Chatbot

This project is for my grandmother who always asks me questions about the moon. It was originally developed as a RAG using Langchain and Huggingface but was reconfigured to use OpenAI's API for a more straightforward deployment using ws services.
The chatbot application answers questions about the moon at a sixth to eighth grade level. It is built with FastAPI and can be deployed on AWS Lambda using Docker and API Gateway. 

## Project Structure

```
moon-chatbot
├── src
│   ├── app.py            # Main application code
│   ├── Dockerfile        # Dockerfile for building the application image
│   └── requirements.txt  # Python dependencies
├── .dockerignore         # Files to ignore when building the Docker image
├── .gitignore            # Files to ignore in Git
├── README.md             # Project documentation
└── template.yaml         # AWS SAM template for deployment
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd moon-chatbot
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r src/requirements.txt
   ```

4. Set OpenAI API key in the environment variables:
   ```
   export OPENAI_API_KEY=<your-api-key>  # On Windows use `set OPENAI_API_KEY=<your-api-key>`
   ```

## Usage

To run the application locally, use the following command:
```
uvicorn src.app:app --reload
```

You can then access the API at `http://127.0.0.1:8000/ask` and send POST requests with a JSON body containing the question.

## Deployment

This application can be deployed to AWS Lambda using Docker. Follow these steps:

1. Build the Docker image:
   ```
   ```

2. Push image to AWS ECR:
   ```
   ```
3. Create Lambda function using Docker Image OR Deploy using AWS SAM
   ```
   ```
