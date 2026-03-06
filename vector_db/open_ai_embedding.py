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

# Collect embeddings into a list for easier processing
embeddings = [d.embedding for d in response.data]

# number of embeddings returned (should match number of inputs)
num_embeddings = len(embeddings)
# length of a single embedding vector (embedding dimension)
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
    # Initialize n x n distance matrix with zeros
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(vectors[i], vectors[j])
            dist[i][j] = d
            dist[j][i] = d
    return dist


# Compute all pairwise L2 (Euclidean) distances between embeddings
distance_matrix = pairwise_l2_distances(embeddings)

print("pairwise L2 distance matrix (num_embeddings x num_embeddings):")
for row in distance_matrix:
    # format each row to a compact string with 4 decimal places
    print("[" + ", ".join(f"{v:.4f}" for v in row) + "]")

