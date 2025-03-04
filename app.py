import streamlit as st
from models.character import Character
from utils.config import load_characters, load_config
from components.character_tiles import character_tiles
from components.chat import chat_ui, clear_chat_button
from components.sidebar import sidebar_config
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="KDMeinBuch - Charakter-Chat",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
<style>
    .stButton button {
        width: 100%;
    }
    .character-tile {
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .character-tile:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)


def main():
    """Main application function."""
    st.title("KDMeinBuch - Charakter-Chat")
    
    # Configure sidebar
    config = sidebar_config()
    
    # Initialize selected character in session state if not exists
    if "selected_character_id" not in st.session_state:
        st.session_state.selected_character_id = None
    
    # Load characters
    characters = load_characters()
    
    # Character tiles section
    selected_id = character_tiles(characters, st.session_state.selected_character_id)
    
    # Update selected character if changed
    if selected_id is not None and selected_id != st.session_state.selected_character_id:
        st.session_state.selected_character_id = selected_id
        # Clear messages when character changes
        if "messages" in st.session_state:
            st.session_state.messages = []
        st.rerun()
    
    # Divider
    st.divider()
    
    # Get selected character
    selected_character = None
    if st.session_state.selected_character_id:
        for character in characters:
            if character.id == st.session_state.selected_character_id:
                selected_character = character
                break
    
    # Chat UI
    col1, col2 = st.columns([5, 1])
    with col1:
        chat_ui(selected_character, config)
    
    with col2:
        clear_chat_button()


if __name__ == "__main__":
    main() 