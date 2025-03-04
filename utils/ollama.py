import httpx
import json
from typing import List, Dict, Any
from models.character import ChatMessage


async def generate_response(
    messages: List[ChatMessage],
    system_prompt: str,
    server: str,
    port: int,
    model: str
) -> str:
    """
    Generate a response from Ollama API.
    
    Args:
        messages: List of chat messages
        system_prompt: The system prompt to use
        server: Ollama server address
        port: Ollama server port
        model: Ollama model to use
        
    Returns:
        The generated response text
    """
    url = f"{server}:{port}/api/chat"
    
    # Format messages for Ollama API
    formatted_messages = [{"role": "system", "content": system_prompt}]
    
    for msg in messages:
        formatted_messages.append({
            "role": msg.role,
            "content": msg.content
        })
    
    # Prepare the request payload
    payload = {
        "model": model,
        "messages": formatted_messages,
        "stream": False
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, timeout=60.0)
            response.raise_for_status()
            result = response.json()
            return result["message"]["content"]
    except httpx.HTTPStatusError as e:
        return f"Error: HTTP Status Error - {e}"
    except httpx.RequestError as e:
        return f"Error: Request Error - {e}"
    except Exception as e:
        return f"Error: Unexpected error - {e}"


async def list_models(server: str, port: int) -> List[str]:
    """
    List available models from Ollama.
    
    Args:
        server: Ollama server address
        port: Ollama server port
        
    Returns:
        List of available model names
    """
    url = f"{server}:{port}/api/tags"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            result = response.json()
            return [model["name"] for model in result.get("models", [])]
    except Exception as e:
        print(f"Error listing models: {e}")
        return [] 