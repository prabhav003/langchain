from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

image = client.text_to_image(
    prompt="A futuristic city at sunset, ultra realistic, 8k",
    model="black-forest-labs/FLUX.1-schnell"
)

image.save("output.png")
print("Image saved!")