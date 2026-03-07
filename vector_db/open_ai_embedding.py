# vector_db/open_ai_embedding.py
import math
from openai import OpenAI

client = OpenAI()

documents = [
    "Bugs introduced by the intern had to be squashed by the lead developer.",
    "Bugs found by the quality assurance engineer were difficult to debug.",
    "Bugs are common throughout the warm summer months, according to the entomologist.",
    "Bugs, in particular spiders, are extensively studied by arachnologists.",
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

embeddings = [d.embedding for d in response.data]
num_embeddings = len(embeddings)
embedding_dim = len(embeddings[0]) if num_embeddings > 0 else 0

print("type of response:", type(response))
print("num embeddings:", num_embeddings)
print("embedding dim of first:", embedding_dim)
print("shape:", (num_embeddings, embedding_dim))


def euclidean_distance(v1, v2):
    squared_sum = sum((x - y) ** 2 for x, y in zip(v1, v2))
    return math.sqrt(squared_sum)


def pairwise_l2_distances(vectors):
    n = len(vectors)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(vectors[i], vectors[j])
            dist[i][j] = d
            dist[j][i] = d
    return dist


def cosine_similarity(v1, v2):
    dot = sum(x * y for x, y in zip(v1, v2))
    norm1 = math.sqrt(sum(x * x for x in v1))
    norm2 = math.sqrt(sum(y * y for y in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


def pairwise_cosine_similarities(vectors):
    n = len(vectors)
    sim = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            s = cosine_similarity(vectors[i], vectors[j])
            sim[i][j] = s
            sim[j][i] = s
    return sim


distance_matrix = pairwise_l2_distances(embeddings)
print("pairwise L2 distance matrix (num_embeddings x num_embeddings):")
for row in distance_matrix:
    print("[" + ", ".join(f"{v:.4f}" for v in row) + "]")

cosine_sim_matrix = pairwise_cosine_similarities(embeddings)
print("pairwise cosine similarity matrix (num_embeddings x num_embeddings):")
for row in cosine_sim_matrix:
    print("[" + ", ".join(f"{v:.4f}" for v in row) + "]")