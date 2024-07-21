import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en_core_web_sm',disable=["parser","ner"])
nlp.Defaults.stop_words.add("say")




def basic_filter(tokenized_doc):
    return [t.lemma_ for t in tokenized_doc if t.is_alpha and t.text not in STOP_WORDS and t.pos_ in ["NOUN", "VERB", "ADJ"]]



    