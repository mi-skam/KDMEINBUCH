import os
import anthropic
from typing import List, Dict, Any
from models.character import ChatMessage
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


async def generate_response(
    messages: List[ChatMessage],
    system_prompt: str,
    model: str
) -> str:
    """
    Generate a response from Anthropic API.
    
    Args:
        messages: List of chat messages
        system_prompt: The system prompt to use
        model: Anthropic model to use
        
    Returns:
        The generated response text
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        return "Error: ANTHROPIC_API_KEY not found in environment variables"
    
    client = anthropic.Anthropic(api_key=api_key)
    
    # Format messages for Anthropic API
    formatted_messages = []
    
    for msg in messages:
        formatted_messages.append({
            "role": msg.role,
            "content": msg.content
        })
    
    try:
        response = client.messages.create(
            model=model,
            system=system_prompt,
            messages=formatted_messages,
            max_tokens=1000
        )
        return response.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"


def list_models() -> List[str]:
    """
    List available models from Anthropic.
    
    Returns:
        List of available model names
    """
    return [
        "claude-3-5-haiku-latest",
        "claude-3-5-sonnet-latest",
        "claude-3-7-sonnet-latest",
    ] 