import numpy as np
from openai import OpenAI
from embedding_example_2 import load_embedded_data,str_to_vector
from config.configurations import get_api_key
def cosine_similarity(a, b):
    """
    相似度计算
    :param a:
    :param b:
    :return:
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

model_config = {
    'embedding_model' : "text-embedding-ada-002",
    'embedding_encoding' : "cl100k_base",
    'max_tokens':8000
}

client = OpenAI(api_key=get_api_key())

def embedding_text(text):
    res = client.embeddings.create(input=text, model=model_config.get('embedding_model'))
    return res.data[0].embedding

def search_reviews(df, product_description, n=3, pprint=True):
    product_embedding = embedding_text(product_description)
    df["similarity"] = df.embedding_vec.apply(lambda x: cosine_similarity(x, product_embedding))
    results = (
        df.sort_values("similarity", ascending=False)
            .head(n)
            .combined.str.replace("Title: ", "")
            .str.replace("; Content:", ": ")
    )
    if pprint:
        for r in results:
            print(r[:200])
            print()
    return results

if __name__ == '__main__':
    embedded_data = load_embedded_data()
    embedded_data = str_to_vector(embedded_data)
    res1 = search_reviews(embedded_data, 'delicious beans', n=3)
    print(f'res1:\n{res1}')
    res2 = search_reviews(embedded_data, 'dog food', n=3)
    print(f'res2:\n{res2}')
    res3 = search_reviews(embedded_data, 'awful', n=5)
    print(f'res3:\n{res3}')