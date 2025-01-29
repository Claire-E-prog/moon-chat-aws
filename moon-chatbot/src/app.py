from fastapi import FastAPI, Request
from openai import OpenAI
import os
from mangum import Mangum

app = FastAPI()
client = OpenAI()

# Load the OpenAI API key from environment variables
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/ask")
async def ask_moon_question(request: Request):
    """
    Endpoint to answer questions about the moon at a sixth to eighth grade level.
    """
    try:
        body = await request.json()
        query = body.get("query", "")
        if not query:
            return {"error": "Query is required"}

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a science tutor that answers questions about the moon at a sixth grade level."},
                {
                    "role": "user",
                    "content": query  # Use the query from the request body
                }
            ]
        )

        # access the content of the message
        answer = completion.choices[0].message.content.strip()
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

# Add Mangum handler for AWS Lambda
handler = Mangum(app)