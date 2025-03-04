import streamlit as st
import asyncio
from models.character import AppConfig
from utils import ollama, anthropic
from utils.config import load_config, save_config


def sidebar_config() -> AppConfig:
    """
    Display sidebar with configuration options.
    
    Returns:
        Updated AppConfig
    """
    st.sidebar.title("Konfiguration")
    
    # Load current config
    config = load_config()
    
    # Backend selection
    st.sidebar.subheader("Backend")
    backend = st.sidebar.radio(
        "Wähle einen Backend-Anbieter:",
        options=["ollama", "anthropic"],
        index=0 if config.backend == "ollama" else 1
    )
    
    # Ollama configuration
    if backend == "ollama":
        st.sidebar.subheader("Ollama Einstellungen")
        
        # Server and port
        ollama_server = st.sidebar.text_input(
            "Server",
            value=config.ollama_server
        )
        
        ollama_port = st.sidebar.number_input(
            "Port",
            min_value=1,
            max_value=65535,
            value=config.ollama_port
        )
        
        # Model selection
        try:
            available_models = asyncio.run(ollama.list_models(ollama_server, ollama_port))
            if available_models:
                ollama_model = st.sidebar.selectbox(
                    "Modell",
                    options=available_models,
                    index=available_models.index(config.ollama_model) if config.ollama_model in available_models else 0
                )
            else:
                ollama_model = st.sidebar.text_input(
                    "Modell",
                    value=config.ollama_model,
                    help="Konnte keine Modelle vom Server abrufen. Bitte manuell eingeben."
                )
        except Exception as e:
            st.sidebar.warning(f"Fehler beim Abrufen der Modelle: {e}")
            ollama_model = st.sidebar.text_input(
                "Modell",
                value=config.ollama_model
            )
        
        # Update config
        config.backend = backend
        config.ollama_server = ollama_server
        config.ollama_port = ollama_port
        config.ollama_model = ollama_model
    
    # Anthropic configuration
    elif backend == "anthropic":
        st.sidebar.subheader("Anthropic Einstellungen")
        
        # API Key from .env
        api_key_status = st.sidebar.empty()
        import os
        if os.getenv("ANTHROPIC_API_KEY"):
            api_key_status.success("API-Schlüssel in .env gefunden")
        else:
            api_key_status.error("API-Schlüssel fehlt! Bitte in .env-Datei eintragen: ANTHROPIC_API_KEY=...")
        
        # Model selection
        available_models = anthropic.list_models()
        anthropic_model = st.sidebar.selectbox(
            "Modell",
            options=available_models,
            index=available_models.index(config.anthropic_model) if config.anthropic_model in available_models else 0
        )
        
        # Update config
        config.backend = backend
        config.anthropic_model = anthropic_model
    
    # Save config
    save_config(config)
    
    return config 