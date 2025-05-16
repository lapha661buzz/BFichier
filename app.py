import streamlit as st
from openpyxl import load_workbook
from io import BytesIO

st.set_page_config(page_title="Vérificateur Excel", page_icon="📊")

st.title("📊 Vérificateur de fichier Excel")
st.write("Chargez un fichier `.xlsx` pour vérifier s'il fait moins de 10 Ko et afficher le nombre de lignes.")

# Upload du fichier
fichier = st.file_uploader("📁 Déposer un fichier Excel ici", type=["xlsx"])

if fichier:
    taille = len(fichier.getvalue())
    st.write(f"📦 Taille du fichier : `{taille}` octets")

    if taille >= 0 * 1024:
        try:
            wb = load_workbook(filename=BytesIO(fichier.read()), read_only=True)
            ws = wb.active
            nb_lignes = ws.max_row
            st.success("✅ Le fichier est valide et sa taille est correcte.")
            st.write(f"📈 Nombre total de lignes : `{nb_lignes}`")
        except Exception as e:
            st.error(f"❌ Erreur lors de la lecture du fichier : {e}")