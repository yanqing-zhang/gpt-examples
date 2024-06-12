from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

class CustomChromaVectorStore:

    def search(self):
        raw_doc = TextLoader("../datas/state_of_the_union.txt").load()
        text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
        doc = text_splitter.split_documents(raw_doc)
        print(f"doc:\n{doc}")
        embeddings_model = OpenAIEmbeddings()
        db = Chroma.from_documents(doc, embeddings_model)
        query = "What did the president say about Ketanji Brown Jackson"
        docs = db.similarity_search(query)
        print("-----------------")
        print(f"docs:\n{docs[0].page_content}")
        embeddings_vector = embeddings_model.embed_query(query)
        docs = db.similarity_search_by_vector(embeddings_vector)
        print("-----------------")
        print(f"docs:\n{docs[0].page_content}")

if __name__ == '__main__':
    c = CustomChromaVectorStore()
    c.search()