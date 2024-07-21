import streamlit as st
import time

from utils.topicDict import lang_dict
from utils.textTransform import get_research_article
st.header("Research Topic Modeling")

st.write("This is A Topic Modelling Project. You provide an input and it will give you the research topic which can belong to. For Example if you read a texr That model can be divided into various topics related to research topics. Maybe it is a IT Research, or Or Physics. This project can help You Identify it. I Use Concept of LDA To do this task.")

st.divider()


with st.expander("Dictinary of Topics"):
    st.write('''
        This Dictionary Is created by me not with help of model. Based on this dictionary My model try to predict the info you provide that in which catergory the given text Belongs to. 
    ''')
    st.write(lang_dict)



st.markdown("""
<style>
.custom-margin {
    margin: 80px 0;
}
</style>
            
""", unsafe_allow_html=True)

st.write("Just Provide us the topic you want to do topic labelling in the below input field. And We Will Give you the predicted topic")


research_text=st.text_input("Provide us the Research Topic")

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
    if research_text:
        with st.spinner('Wait for it...'):
            time.sleep(2)
        researchText=get_research_article(research_text)

        valid_topic_found = False

        for topic_num, prob in researchText:
                if prob>possibility_minimum:
                    valid_topic_found = True
                    topic_name = lang_dict.get(topic_num, f"Topic {topic_num}") 

                    st.success(f"Topic: {topic_name}, Probability: {prob:.4f}")
                else:
                     continue
        
        if not valid_topic_found:
            st.warning('No topics found. Maybe you should try to change the Minimum Possibility of the topic or maybe your given news was not related to the dataset the model is trained on.')

    else:
        st.warning('Please enter some news to proceed.')
     



    



