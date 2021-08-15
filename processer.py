import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def split_with_eos(f_str: str) -> str:
    sent_tokenize_list = sent_tokenize(f_str)
    text = '\n'.join(sent_tokenize_list)
    return text