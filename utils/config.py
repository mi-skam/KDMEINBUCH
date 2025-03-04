import json
import os
import streamlit as st
from models.character import AppConfig, Character
from data.default_characters import DEFAULT_CHARACTERS
from typing import List, Dict, Any


def load_config() -> AppConfig:
    """
    Load app configuration from session state or initialize with defaults.
    
    Returns:
        AppConfig object
    """
    if "config" not in st.session_state:
        st.session_state.config = AppConfig()
    
    return st.session_state.config


def save_config(config: AppConfig) -> None:
    """
    Save app configuration to session state.
    
    Args:
        config: AppConfig object to save
    """
    st.session_state.config = config


def load_characters() -> List[Character]:
    """
    Load characters from session state or initialize with defaults.
    
    Returns:
        List of Character objects
    """
    if "characters" not in st.session_state:
        st.session_state.characters = DEFAULT_CHARACTERS
    
    return st.session_state.characters


def save_character(character: Character) -> None:
    """
    Save or update a character in the session state.
    
    Args:
        character: Character object to save
    """
    characters = load_characters()
    
    # Find and update existing character or add new one
    for i, char in enumerate(characters):
        if char.id == character.id:
            characters[i] = character
            st.session_state.characters = characters
            return
    
    # Character not found, add new one
    characters.append(character)
    st.session_state.characters = characters 