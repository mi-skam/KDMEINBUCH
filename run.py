#!/usr/bin/env python3
"""
Test script for KDMeinBuch application.
This allows testing features without restarting the application.
"""
import os
import argparse
import subprocess
import sys
import asyncio
from utils import ollama, anthropic
from models.character import ChatMessage, AppConfig


def test_ollama_connection(server: str, port: int) -> None:
    """Test connection to Ollama server."""
    print(f"Testing Ollama connection to {server}:{port}...")
    try:
        models = asyncio.run(ollama.list_models(server, port))
        if models:
            print(f"✅ Successfully connected to Ollama. Available models: {', '.join(models)}")
        else:
            print("❌ Connected to Ollama but no models found.")
    except Exception as e:
        print(f"❌ Failed to connect to Ollama: {e}")


def test_anthropic_connection() -> None:
    """Test connection to Anthropic API."""
    print("Testing Anthropic API connection...")
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found in environment variables.")
        return
    
    try:
        models = anthropic.list_models()
        print(f"ℹ️ Available Anthropic models: {', '.join(models)}")
        
        # Test a simple completion
        print("Testing API with a simple completion...")
        messages = [ChatMessage(role="user", content="Hello, testing 1-2-3")]
        response = asyncio.run(anthropic.generate_response(
            messages=messages,
            system_prompt="You are a helpful assistant. Keep it short.",
            model="claude-3-haiku-20240307"
        ))
        
        if "Error:" in response:
            print(f"❌ Failed to get response from Anthropic: {response}")
        else:
            print(f"✅ Successfully received response from Anthropic: {response[:50]}...")
    except Exception as e:
        print(f"❌ Error testing Anthropic API: {e}")


def create_sample_images() -> None:
    """Create sample placeholder images for characters."""
    from PIL import Image, ImageDraw, ImageFont
    import random
    
    print("Creating sample character images...")
    os.makedirs("data/images", exist_ok=True)
    
    character_ids = [
        "pirat", "philosoph", "dichter", "wissenschaftler", 
        "kind", "alien", "ritter", "detektiv"
    ]
    
    for char_id in character_ids:
        img_path = f"data/images/{char_id}.png"
        if os.path.exists(img_path):
            print(f"Image for {char_id} already exists, skipping.")
            continue
        
        # Create a colored image with character name
        img = Image.new('RGB', (200, 200), color=(
            random.randint(100, 240), 
            random.randint(100, 240), 
            random.randint(100, 240)
        ))
        d = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("Arial", 24)
        except IOError:
            font = ImageFont.load_default()
        
        d.text((40, 80), char_id.capitalize(), fill="black", font=font)
        img.save(img_path)
        print(f"Created image for {char_id}")


def run_streamlit_app() -> None:
    """Run the Streamlit application."""
    print("Starting Streamlit application...")
    subprocess.run(["streamlit", "run", "app.py"])


def run_tests() -> None:
    """Run all tests."""
    print("Running tests...")
    subprocess.run([sys.executable, "tests/run_tests.py"])


def main():
    """Main entry point for the test script."""
    parser = argparse.ArgumentParser(description="Test script for KDMeinBuch application")
    parser.add_argument("--test-ollama", action="store_true", help="Test Ollama connection")
    parser.add_argument("--test-anthropic", action="store_true", help="Test Anthropic API connection")
    parser.add_argument("--create-images", action="store_true", help="Create placeholder images for characters")
    parser.add_argument("--run-app", action="store_true", help="Run the Streamlit application")
    parser.add_argument("--run-tests", action="store_true", help="Run all tests")
    
    args = parser.parse_args()
    
    # If no arguments are provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    if args.test_ollama:
        config = AppConfig()
        test_ollama_connection(config.ollama_server, config.ollama_port)
    
    if args.test_anthropic:
        test_anthropic_connection()
    
    if args.create_images:
        create_sample_images()
    
    if args.run_tests:
        run_tests()
    
    if args.run_app:
        run_streamlit_app()


if __name__ == "__main__":
    main() 