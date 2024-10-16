import streamlit as st 
from library import Biblioteka

biblioteka = Biblioteka()
biblioteka.nuskaityti_knygas()

st.title("Bibliotekos Valdymo Sistema")

menu = ["Prideti knyga", "Perziureti knygas", "Ieskoti knygu", "Isduoti knyga", "Grazinti knyga", "Perziureti veluojancias knygas"]
choise = st.sidebar.selectbox("Pasirinkite veiksma", menu)

if choise == "Prideti knyga":
    st.subheader("Prideti nauja knyga")
    pavadinimas = st.text_input("Knygos pavadinimas")
    autorius = st.text_input("Autorius")
    metai = st.number_input("Isleidimo metai", min_value=1900, max_value=2024)
    zanras = st.text_input("Zanras")
    if st.button ("Prideti knyga"):
        biblioteka.prideti_knyga(pavadinimas, autorius, metai, zanras)

elif choise == "Perziureti knygas":
    st.subheader("Visos knygos")
    biblioteka.perziureti_visas_knygas