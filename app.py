import streamlit as st

st.title("Title -->Hello  Geeks,Welcome to GeeksForGeeks") #title 
st.header("Header --> GeeksforGeeks")#header
st.subheader("Subheader--> GeeksforGeeks")
st.text("text-->GeeksforGeeks")

st.markdown('Hi')
st.markdown('#Hi')
st.markdown('##Hi')
st.markdown('###Hi')
st.markdown('####Hi')
st.markdown('Hi\n')

st.success('Success')
st.info("Information")
st.warning("Waring")
st.error("Error")

# exp = ZeroDivisionError('Divison not possible with 0')
# st.exception(exp)

st.exception(ZeroDivisionError('Divison not possible with 0'))
st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))

st.write("1+2+3")
st.write(1+2+3)

st.code("x = 10\n"
        "for i in range(x):\n"
        "    print(i)")

st.checkbox("Male")
st.checkbox("Female")

if (st.checkbox("Adult")):
    st.write("You are an adult")

st.radio('Select  :',('Male','Female'))
radioButton =st.radio('Select  :',('Male1','Female1'))
if radioButton =="Male1":
    st.write("You are a Male")


st.subheader("Select Box")
selectBox = st.selectbox("Data Science :", ["Data Science", "Web Scraping", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision", "Image Processing"])

st.write("You make selected",selectBox)

st.subheader("MultiSelet box")
multiselect = st.multiselect("Data Science :", ["Data Science", "Web Scraping", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision", "Image Processing"])

st.write("you've selected:",multiselect,len(multiselect) )


st.subheader("button")
if st.button("Click me"):
    st.write("You clicked the button")

st.subheader("Slider")
vol = st.slider("Slecet the level",1,10,step=1)
st.write("the volume is",vol)

st.subheader("user input")
name = st.text_input("Name: ")
# st.write("hi the name is",name)
if name:
    st.write("Hi, ",name)

st.subheader("Username input")
username = st.text_input('Username:')
password = st.text_input("Password:",type = "password")
if username:
    st.write("Hi, ",username)

st.subheader("text area")
textArea = st.text_area("Write about yousrself 20 words:" )
st.write(textArea)

st.subheader("Input of Number:")
st.number_input("select your age:",18,110)

st.subheader("Input Date:")
st.date_input("Date")

st.subheader("Input time:")
st.time_input("time")

