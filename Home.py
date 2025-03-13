import time
import streamlit as st
import pandas as pd


def balloons_congrats():
    st.balloons()

@st.dialog("User Sign Up")
def user_sign_up():
    my_container = st.container()
    with my_container:
        user_name = st.text_input("Enter your user name :")
        st.text_input("Enter your email here : ")
        sign_up_button = st.button("Sign up")
        if sign_up_button:
            st.toast(f" {user_name} has been signed up successfully", icon="👍")
            balloons_congrats()
            my_container.empty()



def main():
    st.title("Welcome to Baylens Streamlit app")
    st.header("This is a Tutorial")
    st.subheader("Doing a run through of the basics of Streamlit")
    st.write("Mwah 😚")
    st.caption("I hope this is easy on your eyes?")
    with st.sidebar:
        st.write("This is within the sidebar")



    if st.button("Login"):
        user = user_sign_up()

    else:
        pass
    st.divider()

    terms_conditions = st.checkbox("I have read the terms and conditions and agree to them")
    if terms_conditions:
        st.write("User has agreed to the above terms and conditions")
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
    st.number_input("Enter your age here : ", 18,40,29)
    st.date_input("Enter the date of our anniversary here : ")
    st.time_input("Enter the time  : ")
    st.text_input("Enter my name here")
    st.text_area("In less than 450 words....Im joking, go drink water, now",max_chars=450)

    st.info("Upload a .csv file")
    uploaded_file  = st.file_uploader("Upload your file : ")
    if uploaded_file:
        st.success("You have successfully uploaded a file")
        st.image(uploaded_file)
    else:
        pass
    st.header("Its Picture Time")
    activated = st.toggle("Toggle to take a picture of yourself")
    if activated:
        st.camera_input("Take a photo of yourself")
        balloons_congrats()
        st.write("Thank you for your Picture, you Pretty Strawberry")
    else:
        pass

    with st.expander(label="About her"):
        st.write("Strawberry")
        st.write("Princess")
        st.write("Darling")
        st.write("Mommy")
    with st.spinner("Loading your data..."):
        time.sleep(1)
        st.write("Your personal data has been loaded successfully 😈")




    progress_text = "Processing data"
    my_bar = st.progress(0, text=progress_text)
    for percentile_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percentile_complete +1 , text=progress_text)
    time.sleep(1)
    my_bar.empty()




    st.write("You are doing well, Strawberry 🤗")
    like_dislike = st.feedback()
    # st.write(like_dislike)
    if like_dislike == 0:
        st.write("My baby doesnt like the page?:pleading_face:")
    elif like_dislike == 1:
        st.write("Thank you Darling ")

    stars = st.feedback("stars")
    if stars or stars == 0:
        if stars <= 1:
            st.write("Low Rating")
        elif stars == 2:
            st.write("Medium Rating")
            st.write(":pleading_face:")
        elif stars > 2:
            st.write("High Rating")
            balloons_congrats()


    # callout messages


    st.warning(f"This is the end of my web app, Princess")
    # st.error("Failed to load the image")
    # st.code("""
    #     st.title("This is a title")
    #     st.header("This is a header")
    #     st.subheader("This is a subheader")
    #     st.write("Welcome to my streamlit application built in Python")
    #     st.caption("This is a caption")
    #     a = 24
    #     b = 19
    #     st.write(f"{a} + {b} = {a + b}")
    #     """)

    # with st.echo():
    #     st.write("This code is going to be executed")
if __name__ == "__main__":
    main()

