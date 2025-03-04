import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.character import Character, ChatMessage, AppConfig
from data.default_characters import DEFAULT_CHARACTERS


def test_character_model():
    """Test the Character model."""
    character = Character(
        id="test",
        name="Test Character",
        description="A test character",
        system_prompt="This is a test system prompt",
        image_path="test.png"
    )
    
    assert character.id == "test"
    assert character.name == "Test Character"
    assert character.description == "A test character"
    assert character.system_prompt == "This is a test system prompt"
    assert character.image_path == "test.png"
    
    print("✅ Character model test passed")


def test_chat_message_model():
    """Test the ChatMessage model."""
    message = ChatMessage(
        role="user",
        content="Test message",
        character_id="test"
    )
    
    assert message.role == "user"
    assert message.content == "Test message"
    assert message.character_id == "test"
    
    print("✅ ChatMessage model test passed")


def test_app_config_model():
    """Test the AppConfig model."""
    config = AppConfig()
    
    assert config.ollama_server == "http://localhost"
    assert config.ollama_port == 11434
    assert config.ollama_model == "llama3"
    assert config.anthropic_model == "claude-3-sonnet-20240229"
    assert config.backend == "ollama"
    
    print("✅ AppConfig model test passed")


def test_default_characters():
    """Test the default characters."""
    assert len(DEFAULT_CHARACTERS) == 8
    
    character_ids = [c.id for c in DEFAULT_CHARACTERS]
    expected_ids = ["pirat", "philosoph", "dichter", "wissenschaftler", "kind", "alien", "mittelalter", "detektiv"]
    
    for expected_id in expected_ids:
        assert expected_id in character_ids, f"Expected character ID '{expected_id}' not found"
    
    print("✅ Default characters test passed")


if __name__ == "__main__":
    print("Running model tests...")
    test_character_model()
    test_chat_message_model()
    test_app_config_model()
    test_default_characters()
    print("All tests passed!") 