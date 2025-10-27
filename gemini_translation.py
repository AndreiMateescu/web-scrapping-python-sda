from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

text_to_translate = """
  Key Features of PyTorch
These features make PyTorch a powerful and flexible tool for developing, training, and deploying machine learning models, catering to both research and production environments:


Eager & Graph Execution
PyTorch runs computations immediately and dynamically, but through TorchScript, it can also optimize and export static computational graphs for production deployment.

Dynamic Neural Networks
Neural networks are being built dynamically, allowing to introduce changes to the network architecture on the fly, which is particularly useful for variable-length inputs.

Distributed Training
It supports distributed training across multiple GPUs and nodes, enabling scalable training for large datasets and models using libraries like torch.distributed.

Hardware Accelerated Inference
It leverages NVIDIA GPUs with CUDA and cuDNN, and other hardware accelerators, to provide fast and efficient inference and training.

Simplicity Over Complexity
PyTorch emphasizes code readability and simplicity, with a design that mimics Python programming paradigms, making it accessible and easy to learn for developers and researchers.
"""

API_KEY = os.environ.get("GEMINI_API_KEY")

# print(API_KEY)
client = genai.Client(api_key=API_KEY)

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Translate in Romanian the following content: " + text_to_translate
# )
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Summarize following content: " + text_to_translate
)
print(response.text)