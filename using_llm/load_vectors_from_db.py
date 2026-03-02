from llama_index.core import load_index_from_storage, StorageContext

from using_llm.useallama import query_engine

storage_context = StorageContext().from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("What is the main topic of these documents?")
print(response)


