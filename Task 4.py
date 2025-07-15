import random
corpus = """
Artificial Intelligence is transforming industries.
Machine Learning is a subset of AI.
Natural Language Processing enables machines to understand human language.
Deep Learning allows neural networks to learn from large amounts of data.
AI applications include healthcare, finance, and transportation.
"""
tokens = corpus.lower().replace('\n', ' ').split()
markov_chain = {}

for i in range(len(tokens) - 1):
    word = tokens[i]
    next_word = tokens[i + 1]
    if word in markov_chain:
        markov_chain[word].append(next_word)
    else:
        markov_chain[word] = [next_word]

last_word = tokens[-1]
if last_word not in markov_chain:
    markov_chain[last_word] = []

def generate_text(seed_text, next_words=30):
    words = seed_text.lower().split()
    
    for _ in range(next_words):
        last_word = words[-1]
        next_candidates = markov_chain.get(last_word, [])
        
        if next_candidates:
            next_word = random.choice(next_candidates)
        else:
            next_word = random.choice(tokens)
        
        words.append(next_word)
    
    return ' '.join(words)

if __name__ == "__main__":
    user_prompt ="Artificial Intelligence"
    generated = generate_text(user_prompt, next_words=30)
    print("\nGenerated Text:\n" + generated.capitalize())
