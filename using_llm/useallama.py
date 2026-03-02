import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# 1. Load your documents
# Ensure you have a folder named 'data' with some .txt or .pdf files
documents = SimpleDirectoryReader("./data").load_data()

# 2. Build the Index
# By default, this uses OpenAI (GPT-3.5/4) and OpenAI Embeddings
index = VectorStoreIndex.from_documents(documents)

# 3. Create a Query Engine
query_engine = index.as_query_engine()

# 4. Ask a question
response = query_engine.query("What is the main topic of these documents?")
print(response)