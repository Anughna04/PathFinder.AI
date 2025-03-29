import streamlit as st
from model3 import generate_career_recommendations,generate_learning_path

#Streamlit UI enhancements.Change it according to your likings
st.markdown("""
        <h1 style='text-align: center; 
            font-size: 50px;
            font-weight: bold;
            color: #D8BFD8; 
            text-shadow: 10px rgba(230, 204, 255, 0.8);'>
            PathFinder.AI 🎯
        </h1>
        """,unsafe_allow_html=True)
st.markdown(""" <h6 style='texr-align:center;margin-left:80px;
            font-size:25px;color:white;'>
            <i>Find Your Perfect Career Path with AI Precision!<i>
            </h6>
        """,unsafe_allow_html=True)
st.write('---')

#defining the input fields for user details
name = st.text_input("Enter your name:📝 ")
skills = st.text_area("Enter your skills (comma-separated):⚡️")
interests = st.text_area("Enter your interests (comma-separated):🚀")

#if the user want career recommendations
if st.button("Get Career Recommendations"):
    if name and skills and interests:
        recommendations = generate_career_recommendations(name, skills, interests)
        st.subheader("Recommended Career Paths:")
        st.write(recommendations)
    else:
        st.warning("Please fill in all fields!")

st.divider()

st.subheader("Generate Learning Path 📚")
career_choice = st.text_input("Enter your chosen career:")

#to generate the learning path according to the user's career choice
if st.button("Get Learning Path"):
    if career_choice:
        learning_path = generate_learning_path(career_choice)
        st.subheader(f"Learning Path for {career_choice}:")
        st.write(learning_path)
    else:
        st.warning("Please enter a career!")










