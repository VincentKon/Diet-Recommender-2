import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Diet Recommendation System! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    Are you looking to improve your health and well-being through personalized nutrition? Our innovative app leverages advanced machine learning algorithms to provide tailored diet recommendations just for you. By analyzing your unique needs and preferences, we create a custom plan that supports your goals, whether it’s weight loss, muscle gain, or simply maintaining a healthy lifestyle. Join us and embark on a journey to a healthier, happier you with the power of personalized nutrition at your fingertips. Start today and discover the perfect diet for your life!
    """
)
