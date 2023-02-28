import streamlit as st

st.set_page_config(page_title='Data App')
st.title(":red[Hello Everyone] :wave: ")
st.header("I am :green[Tushar Goel] and I welcome you to my :blue[first web application]")
st.subheader("This is a streamlit webapp for Data Analysis and Visualization of the :orange[Palmer Archipelago (Antarctica) Penguin Dataset]")
st.subheader("This app allows you to create different plots and to explore and analyze datasets using visualizations and the best part is you can choose your desired X_axis and Y_axis.")

st.subheader(":green[Feel free to connect with me :]")

link = '[![Title](https://camo.githubusercontent.com/5e3d78e5310a41c0667e07077cf93596229de398b154b83885dc068874ed5365/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d2532333145373742352e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/tushar-goel04/)'
st.markdown(link,unsafe_allow_html=True)

link2 = '[![Title](https://camo.githubusercontent.com/b2d1ae072c968dbeaf2232f0e1071ae5a7b218b11caec1ae5c69c10ef370a3cc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333234323932652e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/TusharGoel13)'
st.markdown(link2,unsafe_allow_html=True)

st.balloons()