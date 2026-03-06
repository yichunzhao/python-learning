from sentence_transformers import SentenceTransformer

MODEL_NAME = "paraphrase-MiniLM-L6-v2"


def main():
    documents = [
        "Bugs introduced by the intern had to be squashed by the lead developer.",
        "Bugs found by the quality assurance engineer were difficult to debug.",
        "Bugs are common throughout the warm summer months, according to the entomologist.",
        "Bugs, in particular spiders, are extensively studied by arachnologists.",
    ]

    model = SentenceTransformer(MODEL_NAME)

    embeddings = model.encode(
        documents,
        batch_size=32,
        convert_to_numpy=True
    )

    print("Embedding shape:", embeddings.shape)


if __name__ == "__main__":
    main()