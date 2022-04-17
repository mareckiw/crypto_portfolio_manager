from apps import home, CryptoNews_app, gainers_losers_app
from multiapp import MultiApp
import streamlit as st
from streamlit_autorefresh import st_autorefresh

app = MultiApp()

st.set_page_config(layout="wide")

st.image(
    "https://c.tenor.com/7VzBpq5zYR8AAAAd/eth.gif",
    width=500,)

#st_autorefresh(interval= 1 * 30 * 1000, key="crypto_prices_refresh")

# Add all your application here
app.add_app("📈 Home", home.app)
app.add_app("🔎 Crypto News", CryptoNews_app.app)
app.add_app("🔥 Gainers and Losers", gainers_losers_app.app)

# The main app
app.run()

st.write("")
st.write("")
st.write("")
st.write("")
st.info('Created by')
# Add Link to your repo
st.markdown('''José Caloca''')
'''
    [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/josecaloca) 
    [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josecaloca/)
'''
st.markdown("<br>",unsafe_allow_html=True)

st.markdown('''Jiyoung Kim''')
'''
    [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jiyoungkimcr) 
    [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jykcr/)
'''
st.markdown("<br>",unsafe_allow_html=True)