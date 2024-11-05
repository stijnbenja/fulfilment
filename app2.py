import streamlit as st
from fun_opslag import formaten_naar_klasse, klasse_naar_prijs

with st.sidebar:
    st.header('Suite')

st.title('Opslag kosten')

with st.container(border=True):
    st.subheader('Formaten')
    
    afmeting1 = st.number_input('Afmeting 1 (cm)', step=1)
    afmeting2 = st.number_input('Afmeting 2 (cm)', step=1)
    afmeting3 = st.number_input('Afmeting 3 (cm)', step=1)
    
col1, col2 = st.columns(2)

klasse = formaten_naar_klasse([afmeting1, afmeting2, afmeting3])

col1.metric("Klasse", klasse)
col2.metric("Kosten", klasse_naar_prijs(klasse))
