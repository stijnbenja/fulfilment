import streamlit as st
from fun import sales_naar_bedrag
from fun_opslag import formaten_naar_klasse, klasse_naar_prijs

st.title('Fulfilment centrum kosten')
st.write('voor Nederland')


    
   
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
    
    coller = st.columns(2)
    
    with coller[0]:
        with st.container(border=True):
            st.subheader('Afzet')
            afzet = st.number_input('Afzet per week', step=1, min_value=1, value=1)
            
            
    with coller[1]:
        with st.container(border=True):
            st.subheader('Opslag')
            opslag = st.number_input('Opslag per week', step=1, min_value=1, value=1)
            
 
output = sales_naar_bedrag(afmetingen=[afmeting1, afmeting2, afmeting3], gewicht=gewicht, afzet=afzet)            


with st.container(border=True):
    st.subheader('Fulfilment')
    col1, col2, col3 = st.columns(3)


col1.metric("Klasse", output['klasse'])
col2.metric("Week kosten (€)", output['totaal'])
col3.metric("Per product (€)", output['per_product'])


with st.container(border=True):
    st.subheader('Opslag')
    colk1, colk2, colk3 = st.columns(3)

klasse = formaten_naar_klasse([afmeting1, afmeting2, afmeting3])

colk1.metric("Klasse", klasse)

colk2.metric("Week kosten (€)", round(klasse_naar_prijs(klasse) * opslag,2))

colk3.metric("Per product (€)", klasse_naar_prijs(klasse))


