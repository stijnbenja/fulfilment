import streamlit as st
from fun import sales_naar_bedrag

st.title('Fulfilment kosten')


    
   
cols = st.columns(2)

with cols[0]:
    with st.container(border=True):
        st.subheader('Afmetingen')
        afmeting1 = st.number_input('Afmeting 1 (cm)', step=1)
        afmeting2 = st.number_input('Afmeting 2 (cm)', step=1)
        afmeting3 = st.number_input('Afmeting 3 (cm)', step=1)
with cols[1]:
    with st.container(border=True):
        st.subheader('Gewicht')
        gewicht = st.number_input('Gewicht (kg)')
with cols[1]:
    with st.container(border=True):
        st.subheader('Afzet')
        afzet = st.number_input('Afzet per week', step=1)
            
 
output = sales_naar_bedrag(afmetingen=[afmeting1, afmeting2, afmeting3], gewicht=gewicht, afzet=afzet)            


with st.container(border=True):
    col1, col2, col3 = st.columns(3)


col1.metric("Klasse", output['klasse'])
col2.metric("Totaal bedrag (€)", output['totaal'])
col3.metric("Per product (€)", output['per_product'])