# AWS Lambda Python image (stable)
FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for OpenAI API key
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Command to run the Lambda handler
CMD ["app.handler"]