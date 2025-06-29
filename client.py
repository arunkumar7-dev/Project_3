from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient
import os
from dotenv import load_dotenv

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

# Loading envoirment varriables
load_dotenv()

# Ai Processing
def aiProcess(command) :

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(os.getenv("TOKEN"))  # Ensure you have set the TOKEN in your .env file,
    )
    response = client.complete(
        messages=[
            UserMessage(command),

        ],
            max_tokens=2048,
            model=model
    )

    return(response.choices[0].message.content)

