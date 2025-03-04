#!/bin/bash
# Installation script for KDMeinBuch application

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d " " -f 2)
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d "." -f 1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d "." -f 2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 11 ]); then
    echo "Python 3.11 or higher is required. You have Python $PYTHON_VERSION."
    exit 1
fi

echo "Creating virtual environment with venv..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies with pip..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env file to add your Anthropic API key if needed."
fi

# Create sample images
echo "Creating sample character images..."
python run.py --create-images

echo "Installation complete! You can now run the application with:"
echo "source venv/bin/activate.fish  # Activate virtual environment (fish)"
echo "source venv/bin/activate  # Activate virtual environment (bash)" 
echo "python run.py --run-app"
echo ""
echo "To test the application components, run:"
echo "python run.py --run-tests"
echo ""
echo "To test Ollama connection, run:"
echo "python run.py --test-ollama"
echo ""
echo "To test Anthropic connection, run:"
echo "python run.py --test-anthropic" 