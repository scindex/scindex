# lookup.py
import json
import argparse
import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(vec_a, vec_b):
    #Calc cosine similarity between vectors
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

def main():
    # Setup CLI search query
    parser = argparse.ArgumentParser(description="Look up scindex codes using a natural language query.")
    parser.add_argument("query", type=str, help="The search string to look up.")
    args = parser.parse_args()

    # Load pre-computed embeddings file
    embeddings_file = 'dist/scindex.embeddings.json'
    try:
        with open(embeddings_file, 'r') as f:
            scindex_embeddings = json.load(f)
    except FileNotFoundError:
        print(f"Error: Embeddings file not found at '{embeddings_file}'")
        print("Please run 'python compiler.py --format embeddings' first.")
        return

    # Load  model and embed user's query
    print("Loading model and searching...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vector = model.encode(args.query)

    # Find best match
    best_match = {"id": None, "text": None, "score": -1}
    for item in scindex_embeddings:
        score = cosine_similarity(query_vector, np.array(item["vector"]))
        if score > best_match["score"]:
            best_match = {"id": item["id"], "text": item["text"], "score": score}

    # Print result
    if best_match["id"]:
        print("\n--- Best Match Found ---")
        print(f"ID:    {best_match['id']}")
        print(f"Text:  '{best_match['text']}'")
        print(f"Score: {best_match['score']:.4f}")
    else:
        print("No match found.")

if __name__ == "__main__":
    main()


