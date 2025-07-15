# GENERATIVE-TEXT-MODEL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MOHAMMED IBRAHIM SH

*INTERN ID*: CT04DG2681

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

**DESCRIPTION:**

The provided Python script demonstrates a basic Markov chain text generator. Its purpose is to produce new, semi-random text sequences that statistically resemble the style and vocabulary of an original body of text—in this case, a small corpus related to Artificial Intelligence concepts.

Imports and Libraries

The code starts by importing Python’s built-in random module. This module is essential because it allows the program to randomly choose words during text generation, introducing variability and unpredictability into the generated text.

Defining the Corpus

The variable corpus is a multi-line string containing a few short sentences about AI, Machine Learning, Natural Language Processing, and Deep Learning. This text acts as the training data for the Markov model.

Example content includes:


“Artificial Intelligence is transforming industries.”

“Deep Learning allows neural networks to learn from large amounts of data.”

Tokenization and Preprocessing

Before building the Markov chain, the corpus is prepared as follows:

The entire text is converted to lowercase to ensure consistent word matching.

Newline characters (\n) are replaced with spaces.

The processed string is split into individual words (tokens) using .split().

This yields a list of words stored in the variable tokens. The uniform lowercase format helps prevent duplicate keys caused by capitalization differences.

Building the Markov Chain Dictionary

A dictionary named markov_chain is constructed to represent the first-order Markov model. The key concepts are:

Key: A word in the corpus.

Value: A list of words that directly follow that word in the text.

The code loops through the list of tokens (excluding the last word). For each word, it records the word that comes immediately after it. If the word already exists as a key, the new follower word is appended to its list of potential successors. Otherwise, a new key-value pair is created.

Finally, the code ensures the last word in the corpus is added to the dictionary with an empty list, even though it has no words following it in the corpus.

Text Generation Function

The text generation logic is encapsulated in the function generate_text(), which takes two arguments:

seed_text: The initial starting text provided by the user.

next_words: The number of words to generate after the seed text (defaulting to 30).

Inside the function:

The seed text is split into words.

For each iteration in the generation loop:

The last word in the current sequence is identified.

Possible successors are retrieved from the markov_chain dictionary.

If successors exist, one is randomly chosen using random.choice().

If no successors are found, a random word is selected from the entire list of tokens to avoid halting.

The newly selected word is appended to the growing list of words. Once the desired number of words is generated, the list is joined back into a single string, forming the generated text.

Running the Script

The script includes a __main__ block to execute the program directly. It defines user_prompt as "Artificial Intelligence". The generate_text() function is called to produce 30 additional words. The output is printed with capitalization applied to the first letter for better readability.

Summary and Use Case

This script is a simple implementation of a first-order Markov model for text generation. Although the corpus is small and the generated text may lack deep coherence, the code effectively demonstrates the principles behind statistical language modeling. It can be extended to:

Use larger and more diverse corpora.

Implement higher-order Markov models (considering more context).

Enhance text quality and realism.

**OUTPUT:**

