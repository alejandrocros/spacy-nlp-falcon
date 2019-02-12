from utils.constants import DICTIONARY_OF_VALID_TAGS

def pos_tagger(model, text):
    """
    This function receives a Spacy model and a string, calls 
    tag_normalizer and returns a list of (token, gandalf-tag) tuples  
    """
    text = model(text)
    return tag_normalizer(text)
    
def tag_normalizer(tokenized_text):
    """
    This function receives the tokenized text and 
    returns a list of (token, gandalf-tag) tuples
    """
    tagged_text = []
    for token in tokenized_text:
        if token.pos_ in DICTIONARY_OF_VALID_TAGS:
            tagged_text.append((token.text, DICTIONARY_OF_VALID_TAGS[token.pos_]))
    return tagged_text