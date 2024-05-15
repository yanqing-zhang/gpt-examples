"""
@author:yanqing.zhang@
@date:2024-04-17
"""
import pandas as pd
import tiktoken
from openai import OpenAI
from config.configurations import get_api_key
def load_data_from_csv():
    """
    从CSV中加载数据
    :return:
    """
    data_path = "../../data/fine_food_reviews_1k.csv"
    df = pd.read_csv(data_path, index_col=0)

    df = df[["Time", "ProductId", "UserId", "Score", "Summary", "Text"]]
    df = df.dropna()
    df["combined"] = (
        "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
    )
    # print(f'df:\n{df.head(2)}')
    # print(f'combined:\n{df["combined"]}') # 打印"combined列"
    return df

model_config = {
    'embedding_model' : "text-embedding-ada-002",
    'embedding_encoding' : "cl100k_base",
    'max_tokens':8000,
}

def max_token_filter(df):
    """
    过滤输入的最大token数，不能大于所用模型的最大输入token数
    :param df:
    :return:
    """
    top_n = 1000
    df = df.sort_values("Time").tail(top_n * 2)
    df.drop("Time", axis=1, inplace=True)
    encoding = tiktoken.get_encoding(model_config.get('embedding_encoding'))
    df['n_tokens'] = df.combined.apply(lambda x: len(encoding.encode(x)))
    df = df[df.n_tokens < model_config.get('max_tokens')].tail(top_n)
    return len(df),df

client = OpenAI(api_key=get_api_key())

def embedding_text(text):
    """
    使用openai的text-embedding-ada-002模型对文本进行embedding
    :param text:
    :return:
    """
    res = client.embeddings.create(input=text, model=model_config.get('embedding_model'))
    return res.data[0].embedding

def save_embedding_to_csv(df,f):
    """
    把生成好的embedding保存到csv的embedding列上
    :param emb: 通过模型生成的embedding
    :return:
    """
    # print(f'df:{df.head(2)}')
    # print(f'embedding:\n{emb}')
    # print(f'combined:\n{df["combined"]}')

    # df.combined.apply(f)，其中df是pandas的dataframe对象，
    # combined是dataframe中的一个列名，f是自定义的函数，用于处理combined列的每个元素。
    # 上面的代码将调用f函数，并将该函数其应用到df.combined中的每个元素上，
    # 所以于f函数的入参就是df.combined列上的数据。
    df["embedding"] = df.combined.apply(f)
    out_csv = "data/fine_food_reviews_with_embeddings_1k_0417.csv"
    df.to_csv(out_csv)
    e0 = df["embedding"][0]
    print(f'e0:{e0}')

if __name__ == '__main__':
    is_execute = False
    if is_execute : # 不要轻易执行，会产生费用
        df = load_data_from_csv()
        max_token,df_text = max_token_filter(df)
        print(max_token)
        save_embedding_to_csv(df,embedding_text)