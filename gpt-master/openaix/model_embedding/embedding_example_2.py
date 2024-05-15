import matplotlib.colors
import pandas as pd
import ast
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
"""
    通过TSNE和KMeans分别实现数据图形化
"""

def load_embedded_data():
    """
    加载已通过openai embedding后的数据集
    :return:
    """
    data_path = "../../data/fine_food_reviews_with_embeddings_1k_0417.csv"
    embedded_data = pd.read_csv(data_path, index_col=0)
    # print(f'type:{type(embedded_data["embedding"][0])}')
    # print(f'len:{len(embedded_data["embedding"][0])}')
    return embedded_data

def str_to_vector(embedded_data):
    """
    将字符串转换为向量
    :param embedded_data:
    :return:
    """
    embedded_data["embedding_vec"] = embedded_data["embedding"].apply(ast.literal_eval)
    # print(f'len:{len(embedded_data["embedding_vec"][0])}')
    # print(f'embedded_data:\n{embedded_data.head(2)}')
    return embedded_data

def show_tsne_scatter(embedded_data):
    """
    通过TSNE把数据进行可视化
    :param embedded_data:
    :return:
    """
    assert embedded_data['embedding_vec'].apply(len).nunique() == 1
    matrix = np.vstack(embedded_data['embedding_vec'].values)
    tsne = TSNE(n_components=2, perplexity=15, random_state=42, init='random', learning_rate=200)
    vis_dims = tsne.fit_transform(matrix)
    colors = ["red", "darkorange", "gold", "turquoise", "darkgreen"]
    x = [x for x,y in vis_dims]
    y = [y for x,y in vis_dims]
    color_indices = embedded_data.Score.values - 1
    assert len(vis_dims) == len(embedded_data.Score.values)
    colormap = matplotlib.colors.ListedColormap(colors)
    plt.scatter(x, y, c=color_indices, cmap=colormap, alpha=0.3)
    plt.title("Amazon ratings visualized in language using t-SNE")
    plt.show()

def show_kmeans_scatter(embedded_data):
    """
    通过KMeans把数据进行可视化
    :param embedded_data:
    :return:
    """
    n_clusters = 4
    kmeans = KMeans(n_clusters = n_clusters, init='k-means++', random_state=42, n_init=10)
    matrix = np.vstack(embedded_data['embedding_vec'].values)
    kmeans.fit(matrix)
    embedded_data['Cluster'] = kmeans.labels_
    colors = ["red", "green", "blue", "purple"]
    tsne_model = TSNE(n_components=2, random_state=42)
    vis_data = tsne_model.fit_transform(matrix)
    x = vis_data[:, 0]
    y = vis_data[:, 1]
    color_indices = embedded_data['Cluster'].values
    colormap = matplotlib.colors.ListedColormap(colors)
    plt.scatter(x, y, c=color_indices, cmap=colormap)
    plt.title("Clustering visualized in 2D using t-SN")
    plt.show()


if __name__ == '__main__':
    embedded_data = load_embedded_data()
    embedded_data = str_to_vector(embedded_data)
    show_tsne_scatter(embedded_data)
    show_kmeans_scatter(embedded_data)
