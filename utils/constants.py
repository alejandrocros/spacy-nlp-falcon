"""
In this file, invariant variables used throughout the project are defined.
"""

# Dictionary containing Spacy - CoreNLP tag correspondences (makes Gandalf Processing easier)
DICTIONARY_OF_VALID_TAGS = {
    'NOUN':'NOUN',
    'PROPN':'PNOUN',
    'VERB':'VERB',
    'ADV':'ADV',
    'ADJ':'ADJ'
}

# Dictionary of Spacy model to be loaded for each language (for future additions)
DICTIONARY_OF_MODELS = {
    'pt':'pt_core_news_sm'
}
