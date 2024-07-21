import streamlit as st
from gensim import models, corpora
from utils.textTransform import get_topics
from utils.topicDict import topic_dict
lda_model = models.LdaModel.load("models\lda_model.gensim")
dictionary = corpora.Dictionary.load("models\lda_model.gensim.id2word")
import time


st.header("News Topic Modeling")

st.write("This is A Topic Modelling Project. You provide an input and it will give you the topic which can belong to. For Example if you read a news That news can be divided into various topics. Maybe it is a sports news, or Fashion News. This project can help You Identify it. I Use Concept of LDA To do this task.")

st.divider()


with st.expander("Dictinary of Topics"):
    st.write('''
        This Dictionary Is created by me not with help of model. Based on this dictionary My model try to predict the News you provide that in which catergory the given news Belongs to. The name given in this dictinary are not that Perfect
    ''')
    st.write(topic_dict)


st.markdown("""
<style>
.custom-margin {
    margin: 80px 0;
}
</style>
            
""", unsafe_allow_html=True)

st.write("Just Provide us the news you want to Classify in the below input field. And We Will Give you the predicted topic")

news=st.text_input("Provide us the news")
st.markdown("""
<style>
.custom-margin {
    margin: 80px 0;
}
</style>
            
""", unsafe_allow_html=True)
possibility_minimum=st.slider("Minimum Possibility of topic",0.05,0.85,0.30,0.01)
st.markdown("""
<style>
.custom-margin {
    margin: 80px 0;
}
</style>
            
""", unsafe_allow_html=True)
btn=st.button("Predict the topic")

if btn:
    if news:
        with st.spinner('Wait for it...'):
            time.sleep(2)
        topics=get_topics(news)

        valid_topic_found = False

        for topic_num, prob in topics:
                print(topics)
                if prob>possibility_minimum:
                    valid_topic_found = True
                    topic_name = topic_dict.get(topic_num, f"Topic {topic_num}") 

                    st.success(f"Topic: {topic_name}, Probability: {prob:.4f}")
                else:
                     continue
        
        if not valid_topic_found:
            st.warning('No topics found. Maybe you should try to change the Minimum Possibility of the topic or maybe your given news was not related to the dataset the model is trained on.')

    else:
        st.warning('Please enter some news to proceed.')
     



    


