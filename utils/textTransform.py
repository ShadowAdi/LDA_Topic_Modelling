import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en_core_web_sm',disable=["parser","ner"])
nlp.Defaults.stop_words.add("say")
from gensim import models
lda_model = models.LdaModel.load('models/lda_model.gensim')
research_model_lda=models.LdaModel.load("models/lda_model_research_articles.gensim")
dictinary_research=research_model_lda.id2word
dictionary = lda_model.id2word






def basic_filter(tokenized_doc):
    return [t.lemma_ for t in tokenized_doc if t.is_alpha and t.text not in STOP_WORDS and t.pos_ in ["NOUN", "VERB", "ADJ"]]



    


nlp = spacy.load('en_core_web_sm',disable=["parser","ner"])
nlp.Defaults.stop_words.add("say")

def get_topics(news):
    article_tokens=list(map(basic_filter,[nlp(news)]))[0]
    article_bow=dictionary.doc2bow(article_tokens)


    topics_distribution = lda_model.get_document_topics(article_bow)
    return topics_distribution

    

def get_research_article(research):
    article_tokens=list(map(basic_filter,[nlp(research)]))[0]
    article_bow=dictinary_research.doc2bow(article_tokens)


    topics_distribution = research_model_lda.get_document_topics(article_bow)
    return topics_distribution

    
