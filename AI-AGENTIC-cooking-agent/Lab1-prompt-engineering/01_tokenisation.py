import tiktoken


def num_tokens_from_string(string: str, encoding_name: str = "o200k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(string))


encoding = tiktoken.encoding_for_model("gpt-4o")
print("Encoding utilise:", encoding.name)

system_message = """
Perform Sentiment analysis of the review presented in the user message.
The result should be positive or negative.
Do not justify your response.
"""

tokens = encoding.encode(system_message)

print("Nombre de tokens du prompt system:", len(tokens))
print("Liste des tokens:", tokens)
print("Reconstruction token par token:")
for token in tokens:
    print(encoding.decode_single_token_bytes(token).decode("utf-8", errors="ignore"), end="")

print("\n")
print("Exemple simple:", num_tokens_from_string("tiktoken is great!"))
