from pydantic import BaseModel
from typing import Optional, List


class Character(BaseModel):
    """Model for a character with a system prompt."""
    id: str
    name: str
    description: str
    system_prompt: str
    image_path: str
    
    
class ChatMessage(BaseModel):
    """Model for a chat message."""
    role: str  # 'user' or 'assistant'
    content: str
    character_id: Optional[str] = None


class AppConfig(BaseModel):
    """Model for app configuration."""
    ollama_server: str = "http://localhost"
    ollama_port: int = 11434
    ollama_model: str = "llama3"
    anthropic_model: str = "claude-3-sonnet-20240229"
    backend: str = "ollama"  # "ollama" or "anthropic" 