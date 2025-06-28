import streamlit as st

st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.text("I love AI VIET NAM")

st.divider()

st.markdown("# Heading 1")
st.markdown("[AI VIET NAM](https://aivietnam.edu.vn/)")
st.markdown("""
    1. Machine Learning
    2. Deep Learning""")
st.markdown(r"$\sqrt{2x+2}$")
st.latex(r"\sqrt{2x+2}")

st.badge("New")
st.badge("Success", 
         icon=":material/check:", 
         color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] \
    :orange-badge[⚠️ Needs review] \
    :gray-badge[Deprecated]"
)

st.divider()

st.code("""
    import torch
    data = torch.Tensor([1, 2, 3])
    print(data)
""", language="python")

st.divider()

st.write('I love AI VIET NAM')
st.write('## Heading 2')
st.write(r'$ \sqrt{2x+2} $')
st.write('1 + 1 = ', 2)

st.divider()

def get_user_name():
    return 'Thai'
with st.echo():
    st.write('This code will be printed')
    def get_email():
        return 'thai@gmail.com'
    user_name = get_user_name()
    email = get_email()
    st.write(user_name, email)

# st.divider()

# st.logo('./logo.png')

# st.image(
#     './dogs.jpeg',
#     caption='Funny dogs.'
# )

# st.audio('./audio.mp4')

# st.video('./video.mp4')

st.divider()

def get_name():
    st.write("Thai")
agree = st.checkbox("I agree",on_change=get_name)
if agree:
    st.write("Great!")

st.radio(
    "Your favorite color:",
    ['Yellow', 'Bleu'],
    captions = ['Vàng', 'Xanh']
)

option = st.selectbox(
    "Your contact:",
    ("Email", "Home phone", "Mobile phone"))

st.write("Selected:", option)

options = st.multiselect(
    "Your favorite colors:",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

st.write("You selected:", options)

color = st.select_slider(
    "Your favorite color:",
    options=["red", "orange", "violet"])

st.write("My favorite color is", color)

st.divider()

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

st.link_button(
    "Go to Google", 
    "https://www.google.com.vn/")

st.divider()
title = st.text_input(
    "Movie title:", "Life of Brian"
)
st.write("The current movie title is", title)

st.divider()

number = st.number_input("Insert a number")
st.write("The current number is ", number)

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

st.divider()

# messages = st.container(height=200)
# if prompt := st.chat_input("Say something"):
#     messages.chat_message("user").write(prompt)
#     messages.chat_message("assistant").write(f"Echo: {prompt}")


st.divider()

uploaded_files = st.file_uploader(
    "Choose files", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)


st.divider()
with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last Name')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name, " - Last Name:", l_name)

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(7, 5), 
    columns=("col %d" % i for i in range(5))
)

st.dataframe(df)  # Same as st.write(df)

st.divider()

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)

st.divider()
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(10, 3), 
    columns=["a", "b", "c"]
)

st.bar_chart(chart_data)

st.divider()
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(10, 3), 
    columns=["a", "b", "c"]
)

st.line_chart(chart_data)

st.divider()

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.divider()
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

if 'key' not in st.session_state:
    st.session_state.key = 'value'
st.write(st.session_state.key)
st.rerun()
st.write(st.session_state.key)
