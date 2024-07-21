import streamlit as st
st.header("LDA Based Projects!!")
st.write("This time i create a nlp based project which you can use to solve a very famous problem of topic modelling in NLP With Help of LDA Model.")
st.write("This topic taught us that every document is comprised of several different topics And each topic is comprised of similar word. For example you are reading about topic related to Football the possibility of words like child labour and murder may be very less or also can be zero. But if you are reading about topics related to crime. They can be found")

st.write("LDA Use the similar approach in this")
st.image("https://miro.medium.com/v2/resize:fit:850/1*VK5R_2YlRx3NbRIMbUxJ8Q.png",caption="LDA Image")

st.write("LDA is an unsupervised learning technique that does not require labeled data and is helpful for tasks such as document classification, information retrieval, and recommender systems.")

st.subheader("Probabilistic graphical models")
st.write("LDA is a probabilistic graphical model that represents the probability distributions of observed and hidden variables and their dependencies using graphs. In LDA, the observed variables are the words in the documents, and the hidden variables are the topics and topic proportions. The graphical representation of LDA allows us to visualize and understand the complex relationships between the variables.")

st.subheader("Dirichlet distributions")
st.write("In LDA, the Dirichlet distribution is used to model the distribution of topics in each document and the distribution of words in each topic.")

st.subheader("Generative process of LDA")
st.write('''The generative process of LDA is a probabilistic model that describes how a corpus of documents is generated. It assumes that each document is a mixture of latent topics, and each topic is a distribution over words. The generative process is as follows:

For each document d in the corpus:
a. Choose a distribution over topics θd from a Dirichlet distribution with parameter α.
b. For each word w in the document:
i. Choose a topic zd from the distribution θd.
ii. Choose a word w from the topic zd.
The generative process assumes that each document is generated independently of the others, and the same set of topics is used across all documents. By assuming a generative process for the data, LDA allows us to infer the latent variables that generate the observed data and discover the underlying topics in the corpus.''')


st.subheader("Preprocessing for LDA")
st.markdown("LDA requires some preprocessing of the raw text data before the model can be trained. Preprocessing steps can significantly affect the quality of the results obtained from LDA. Like **Stop Words Removal**, **Lemmatization and Stemming**, **Tokenization**, **Other techniques for data preparation**")