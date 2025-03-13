import time
import streamlit as st
import pandas as pd
@st.dialog("User Sign in")
def user_sign_in():
    users_name = st.text_input("Enter your user name : ")
    users_email = st.text_input("Enter your email here : ")
    return users_name, users_email
def main():
    st.title("This is a title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.write("Welcome to my streamlit application built in Python")
    st.caption("This is a caption")
    with st.sidebar:
        st.write("This is within the sidebar")
    st.code("""
    st.title("This is a title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.write("Welcome to my streamlit application built in Python")
    st.caption("This is a caption")
    a = 24
    b = 19
    st.write(f"{a} + {b} = {a + b}")
    """)

    with st.echo():
        st.write("This code is going to be executed")

    st.divider()
    # st.write("------------------------------")

    # df = pd.read_csv("data.csv")
    # st.dataframe(df)
    #
    # st.table(df.head())
    #
    # edited_df = st.data_editor(df)
    # st.dataframe(edited_df)

    st.metric("Temperature in Degrees Celsius", 26, 2)

    st.metric("Rainfall in mm", 1400, -350)

    if st.button("Submit"):
        st.write("The button has been clicked")

    like_dislike = st.feedback()
    # st.write(like_dislike)
    if like_dislike == 0:
        st.write("You have disliked the content")
    elif like_dislike == 1:
        st.write("You have liked the content")

    stars = st.feedback("stars")
    if stars or stars == 0:
        if stars <= 1:
            st.write("Low Rating")
        elif stars == 2:
            st.write("Medium Rating")
        elif stars > 2:
            st.write("High Rating")

        activated = st.toggle("Activate")

    terms_conditions = st.checkbox("I have read the terms and conditions and agree to them")
    if terms_conditions:
        st.write("The user has agreed to the above terms and conditions")

    gender = st.radio("Select your Gender : ", ["Male", "Female", "Other"])
    if gender == "Male":
        st.write("The men's conference will be held on Saturday")
    elif gender == "Female":
        st.write("The girls' chat will be held on Friday")

    team = st.selectbox("Select your favourite team : ", ["Liverpool", "Arsenal", "Nottingham", "Chelsea"])
    breakfast = st.multiselect("What did you have for breakfast?", ["Eggs", "Tea", "Coffee", "Sausages", "Arrrow roots", "Milk", "Bacon", "Cereal"])

    st.write(breakfast)

    st.write("Any changes made will be effected")
    st.select_slider("Enter your clothing size here : ", ["XS","S","L","XL","XXL","XXL"])
    st.number_input("Enter a number here : ", 18,40,29)
    st.date_input("Enter the date of your appointment here : ")
    st.time_input("Enter the desired time of your appointment : ")
    st.text_input("Enter your name here")
    st.text_area("In less than 450 words, explain why you are deserving of the merit scholarship", 450)
    st.file_uploader("Upload your file : ")
    # st.camera_input("Take a photo of yourself")

    with st.expander(label="About"):
        st.write("This is the first detail")
        st.write("This is the second detail")
        st.write("This is the third detail")
        st.write("This is the fourth detail")
    # with st.spinner("Loading your data..."):
    #     time.sleep(2)
    #     st.write("Your data has been loaded successfully")
    #     st.balloons()

    # for i in range(100):
    #     st.progress(i)
    #     time.sleep(1)
    # progress_text = "Processing data"
    # my_bar = st.progress(0, text=progress_text)
    # for percentile_complete in range(100):
    #     time.sleep(0.01)
    #     my_bar.progress(percentile_complete +1 , text=progress_text)
    # time.sleep(1)
    # my_bar.empty()


    # user_sign_in()
    st.toast("User singed up successfully", icon="👍")
    st.write("You are doing well sir :hot_face: :pensive_face:")


    # callout messages
    st.success("You have successfully uploaded a file")
    st.info("Upload a .csv file")
    st.warning("The directory you are trying to access does not exist")
    st.error("Failed to load the image")
if __name__ == "__main__":
    main()
