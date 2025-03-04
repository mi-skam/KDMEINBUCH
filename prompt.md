<scope>
Create an app that allows thu user to switch between different characters which alter the style of the response to the question "Kennst du das Buch?" Basically it's a different persona per image. 
</scope>

<specs>
- The app should be a frontend application that has 8 different characters as a tile in the upper part
- the system prompts of the characters and the whole application should be german
- each tile represents a different system prompt for a character, e.G. a pirate that speaks in pirate slang
- each tile should have a predefined system prompt
- on clicking on the tile one can see / edit the system prompt, which can be saved and the tile flyies back
- each tile has a image matching the character
- on the lower part, we have a chat window where the user's question and the answer of the llm is gathered
- we should have a sidebar where we can configure the app (e.G. configuring ollama, selecting the llm backend)
- ollama configuration:
  - server and port
  - model
- anthropic configuration:
  - api key (taken from .env)
  - model (get the list)
- make the configuration stick
</specs>

<your_task>
Create the chat app with the above specs. 
Create test files, so that you can test features without me copying code and re-run the python interpreter (make `python ./run.py` not as needed) 
</your_task>

<rules>
- Use Python >= 3.13
- Use streamlit for creating an interactive data science app
- Use ollama to access the different models
- Use anthropic to access the different models
- design should be clear cut and functional
</rules>