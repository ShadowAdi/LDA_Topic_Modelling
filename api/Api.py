from fastapi import FastAPI,HTTPException
from .Classes import ResearchArticles,NewsArticles
from gensim import models
from utils import textTransform
from utils.topicDict import topic_dict,lang_dict
import numpy as np
from typing import Dict, Any

app = FastAPI()
Lda_Model_Research=models.LdaModel.load("models\lda_model_research_articles.gensim")


@app.get('/')
def index():
    return {'message': "This is  an lda model api it can provide you topic modelling on news and research articles"}



@app.post("/news")
def predict_news_topics(data: NewsArticles):
    text = data.text
    minimum_probability = data.minimumProbability

    # Ensure minimum_probability is within the valid range
    if minimum_probability < 0.01 or minimum_probability > 0.90:
        raise HTTPException(status_code=400, detail="minimumProbability must be between 0.01 and 0.90")

    topics = textTransform.get_topics(text)
    valid_topic_found = False
    response = []

    # Convert numpy types to native types
    for topic_num, prob in topics:
        if isinstance(prob, np.float32):
            prob = float(prob)  # Convert numpy float to Python float
        
        if prob > minimum_probability:
            valid_topic_found = True
            topic_name = topic_dict.get(topic_num, f"Topic {topic_num}")
            response.append({
                "News-Topic-Name": topic_name,
                "probability": prob
            })

    if not valid_topic_found:
        return {
            "message": 'No topics found. Maybe you should try to change the minimum probability of the topic or maybe your given news was not related to the dataset the model is trained on.',
            "status": 400
        }

    # If only one topic is found, return it as a single object
    if len(response) == 1:
        return response[0]

    # Otherwise, return the list of topics
    return response

        



@app.get("/get-news-dictionary")
def get_news_dictionary()->Dict[str,Any]:
      return {
            "message":"This dictionary Consist those news related topics in which my model is going to predict.Remember this topic name are given by me. So maybe they are not that accurate",
            "articles":topic_dict,
      }
    
@app.get("/get-research-dictionary")
def get_research_dictionary()->Dict[str,Any]:
      return {
            "message":"This dictionary Consist those article recommendation topics in which my model is going to predict.",
            "articles":lang_dict,
      }
    


@app.post("/research")
def predict_research_topic(data: ResearchArticles):
    text = data.text
    minimum_probability = data.minimumProbability

    # Ensure minimum_probability is within the valid range
    if minimum_probability < 0.01 or minimum_probability > 0.90:
        raise HTTPException(status_code=400, detail="minimumProbability must be between 0.01 and 0.90")

    topics = textTransform.get_research_article(text)
    valid_topic_found = False
    response = []

    # Convert numpy types to native types
    for topic_num, prob in topics:
        if isinstance(prob, np.float32):
            prob = float(prob)  # Convert numpy float to Python float
        
        if prob > minimum_probability:
            valid_topic_found = True
            topic_name = lang_dict.get(topic_num, f"Topic {topic_num}")
            response.append({
                "Research-Article-Name": topic_name,
                "probability": prob
            })

    if not valid_topic_found:
        return {
            "message": 'No topics found. Maybe you should try to change the minimum probability of the topic or maybe your given research article was not related to the dataset the model is trained on.',
            "status": 400
        }

    # If only one topic is found, return it as a single object
    if len(response) == 1:
        return response[0]

    # Otherwise, return the list of topics
    return response
