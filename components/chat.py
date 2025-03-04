import streamlit as st
from typing import List, Optional
import asyncio
from models.character import Character, ChatMessage, AppConfig
from utils import ollama, anthropic


def init_chat_messages() -> None:
    """Initialize chat messages in session state if they don't exist."""
    if "messages" not in st.session_state:
        st.session_state.messages = []


async def generate_response_async(
    messages: List[ChatMessage],
    character: Character,
    config: AppConfig
) -> str:
    """
    Generate a response from the selected backend.
    
    Args:
        messages: List of chat messages
        character: Selected character
        config: App configuration
        
    Returns:
        Generated response text
    """
    if config.backend == "ollama":
        return await ollama.generate_response(
            messages=messages,
            system_prompt=character.system_prompt,
            server=config.ollama_server,
            port=config.ollama_port,
            model=config.ollama_model
        )
    elif config.backend == "anthropic":
        return await anthropic.generate_response(
            messages=messages,
            system_prompt=character.system_prompt,
            model=config.anthropic_model
        )
    else:
        return "Error: Unknown backend selected"


def chat_ui(character: Optional[Character], config: AppConfig) -> None:
    """
    Display the chat UI.
    
    Args:
        character: The selected character or None
        config: App configuration
    """
    init_chat_messages()
    
    # Display chat header
    if character:
        st.write(f"### Chat mit {character.name}")
    else:
        st.write("### Chat")
        st.write("Bitte wähle einen Charakter aus.")
        return
    
    # Display messages
    for msg in st.session_state.messages:
        role_label = "Benutzer" if msg.role == "user" else character.name
        with st.chat_message(msg.role):
            st.write(f"**{role_label}**: {msg.content}")
    
    # Chat input
    if prompt := st.chat_input("Kennst du das Buch?"):
        # Add user message
        user_message = ChatMessage(role="user", content=prompt, character_id=character.id)
        st.session_state.messages.append(user_message)
        
        # Display user message
        with st.chat_message("user"):
            st.write(f"**Benutzer**: {prompt}")
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.write(f"**{character.name}**: Denkt nach...")
            
            # Generate response
            response = asyncio.run(generate_response_async(
                st.session_state.messages,
                character,
                config
            ))
            
            # Add assistant message
            assistant_message = ChatMessage(role="assistant", content=response, character_id=character.id)
            st.session_state.messages.append(assistant_message)
            
            # Update message placeholder
            message_placeholder.write(f"**{character.name}**: {response}")


def clear_chat_button() -> None:
    """Display a button to clear chat history."""
    if st.button("Chat löschen"):
        st.session_state.messages = []
        st.rerun() 