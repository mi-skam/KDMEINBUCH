import streamlit as st
import os
from typing import List, Optional
from models.character import Character
from utils.config import save_character


def character_tiles(characters: List[Character], selected_character_id: Optional[str] = None) -> Optional[str]:
    """
    Display character tiles and handle character selection.
    
    Args:
        characters: List of Character objects to display
        selected_character_id: Currently selected character ID
        
    Returns:
        Selected character ID or None if no character is selected
    """
    # Check if we need to edit a character
    if "edit_character_id" in st.session_state:
        edit_character_id = st.session_state.edit_character_id
        for character in characters:
            if character.id == edit_character_id:
                edit_character(character)
                return selected_character_id
    
    # Display character tiles
    st.write("### Charaktere")
    
    cols = st.columns(4)
    
    for i, character in enumerate(characters):
        with cols[i % 4]:
            is_selected = character.id == selected_character_id
            tile_style = "border: 3px solid #4CAF50;" if is_selected else "border: 1px solid #ddd;"
            
            # Check if image exists, use placeholder if not
            image_path = character.image_path
            if not os.path.exists(image_path):
                image_path = "https://via.placeholder.com/150?text=" + character.name
            
            # Create clickable tile
            with st.container(border=True, height=180):
                st.image(image_path, width=100)
                st.write(f"**{character.name}**")
                st.write(character.description, help=character.system_prompt[:100] + "...")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Auswählen", key=f"select_{character.id}"):
                        return character.id
                with col2:
                    if st.button("Bearbeiten", key=f"edit_{character.id}"):
                        st.session_state.edit_character_id = character.id
                        st.rerun()
    
    return selected_character_id


def edit_character(character: Character) -> None:
    """
    Display character edit form.
    
    Args:
        character: Character to edit
    """
    st.write(f"### Charakter bearbeiten: {character.name}")
    
    # Create a form for editing the character
    with st.form(key="edit_character_form"):
        name = st.text_input("Name", value=character.name)
        description = st.text_input("Beschreibung", value=character.description)
        system_prompt = st.text_area("System Prompt", value=character.system_prompt, height=200)
        image_path = st.text_input("Bild-Pfad", value=character.image_path)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("Speichern"):
                # Update character
                updated_character = Character(
                    id=character.id,
                    name=name,
                    description=description,
                    system_prompt=system_prompt,
                    image_path=image_path
                )
                
                save_character(updated_character)
                
                # Clear edit state and refresh
                del st.session_state.edit_character_id
                st.rerun()
        
        with col2:
            if st.form_submit_button("Abbrechen"):
                # Clear edit state and refresh
                del st.session_state.edit_character_id
                st.rerun() 