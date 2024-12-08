import streamlit as st
from streamlit_option_menu import option_menu

# Données des comptes utilisateurs
lesDonneesDesComptes = {
    'root': {
        'name': 'root',
        'password': 'rootMDP',
        'email': 'admin@gmail.com',
        'role': 'administrateur'
    },
    'utilisateur': {
        'name': 'utilisateur',
        'password': 'utilisateurMDP',
        'email': 'utilisateur@gmail.com',
        'role': 'utilisateur'
    }
}

# Initialisation de l'état de session
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = ""

# Fonction d'authentification
def authenticate(username, password):
    user = lesDonneesDesComptes.get(username)
    if user and user["password"] == password:
        return True, user["name"]
    return False, None

# Page de connexion
if not st.session_state.authenticated:
    st.title("Page de connexion")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    login_button = st.button("Se connecter")

    if login_button:
        authenticated, name = authenticate(username, password)
        if authenticated:
            st.session_state.authenticated = True
            st.session_state.username = name
            st.success(f"Connexion réussie ! Bienvenue, {name}.")
        else:
            st.error("Identifiants incorrects. Veuillez réessayer.")

# Page principale après connexion
if st.session_state.authenticated:
    # Barre latérale avec menu
    with st.sidebar:
        st.title("Menu")
        st.write(f"Bienvenue, **{st.session_state.username}**")
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Photos", "Déconnexion"]
        )

    # Gestion du menu
    if selection == "Accueil":
        st.title("Bienvenue sur ma page de requins d'Afrique du Sud")
        st.image(
            ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrufUn1Y36TFYgZ263QJAWMkeO2m1zEeajmw&s"], 
            caption=["Carte de l'Afrique"]
        )
        st.write("Ceci est la page d'accueil.")
    elif selection == "Photos":
        st.title("Bienvenue sur mon album photo")
        st.write("Voici des photos spécifiques de requins en Afrique du Sud :")
        st.image(
            [
                "https://cloudfront-eu-central-1.images.arcpublishing.com/leparisien/OHCWAPYBHJAGW62NT3FWF6TFB4.jpg",  # Image 1
                "https://ultramarina.com/thumb/ar__x/f__jpg/h__512/q__60/w__1280/zc__1/src/fichier/p_entete/29084/entete_img_afrique_du_sud_plongee_tiger_shark_with_blacktip_sharks_shutterstock_fiona_ayerst_207019243.jpg",  # Image 2
                "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1tOOZTN_qEEAik803eW_7uIS9UN7_24dUkSyCpzcZ0zG9YXcaD2YFXamAqHTLB3ItJ_ndY9-tPc9UHJkbTryz4iB6REmA2laYlohii_p0i6jrJUOBDta6q1_f934O6I-N_R8c_VpGJeY/s1600/les-grands-requins-blancs-ont-disparu-dune-celebre-baie-au-large-du-cap.jpg"  # Image 3
            ],
            caption=["Requin 1", "Requin 2", "Requin 3"]
        )
    elif selection == "Déconnexion":
        st.session_state.authenticated = False
        st.session_state.username = ""

        # Message de déconnexion
        st.warning("Vous avez été déconnecté. Rechargez la page pour revenir à la connexion.")

