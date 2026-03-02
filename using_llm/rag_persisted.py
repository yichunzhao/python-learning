from llama_index.core import StorageContext, SimpleDirectoryReader, VectorStoreIndex

#load document from the ./data
documents = SimpleDirectoryReader('./data').load_data()

#Build index
index = VectorStoreIndex.from_documents(documents)

# Persist to disk
index.storage_context.persist(persist_dir="./storage")







