from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient
import os
from dotenv import load_dotenv

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

load_dotenv()

# Ai Processing
def aiProcess(command) :

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(os.getenv("TOKEN")),
    )
    response = client.complete(
        messages=[
            {
                "role": "assistant",
                "content": "you personal assistant and give short responses like real human",
            },
            {
                "role": "user",
                "content": command
            }

        ],
            temperature=1,
            top_p=1,
            model=model
    )

    return(response.choices[0].message.content)
