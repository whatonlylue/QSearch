"""
File: SBERTtokenizer.py
Author: Luke Wharton
Date: 4/5/2024
Description: helper script for main.py, contains all the functions for the SBERT algorthym.
@article{DBLP:journals/corr/abs-1910-13461,
  author    = {Mike Lewis and
               Yinhan Liu and
               Naman Goyal and
               Marjan Ghazvininejad and
               Abdelrahman Mohamed and
               Omer Levy and
               Veselin Stoyanov and
               Luke Zettlemoyer},
  title     = {{BART:} Denoising Sequence-to-Sequence Pre-training for Natural Language
               Generation, Translation, and Comprehension},
  journal   = {CoRR},
  volume    = {abs/1910.13461},
  year      = {2019},
  url       = {http://arxiv.org/abs/1910.13461},
  eprinttype = {arXiv},
  eprint    = {1910.13461},
  timestamp = {Thu, 31 Oct 2019 14:02:26 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1910-13461.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

comp_model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)





def doc_encode(document: str) -> list[float]:
    """
    encodes the parameter typically a summarized document
    
    Parameters:

    document (str) : document passed through the summary function

    Returns:

    list[float] : ecoded document summary vector

    """
    doc = "search_document: "+document
    return model.encode(doc)
    

def search_encode(query: str) -> list[float]:
    search = "search_query: "+query
    return model.encode(search)



def similarity(doc_encoded: list[float], search_encoded: list[float]) -> float:
    """
    Uses cosine similarity to compare current document vector against search vector

    Parameters:

    doc_encoded (list[float]) : 2d array of all the encoded document vectors

    search_encoded (list[float]) : search query vector

    Returns:

    float : doc_encoded vector comparied against search_encoded vector
    
    """
    return cosine_similarity([doc_encoded], [search_encoded])[0][0]

    



