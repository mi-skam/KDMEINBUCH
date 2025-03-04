# KDMeinBuch - Charakter-Chat App

Eine interaktive Streamlit-App, die es ermöglicht, zwischen verschiedenen Charakteren zu wechseln, die die Antwort auf die Frage "Kennst du das Buch?" in unterschiedlichen Stilen präsentieren.

## Funktionen

- 8 verschiedene Charaktere als Kacheln im oberen Bereich
- Jede Kachel repräsentiert einen anderen Systemprompt (z.B. einen Piraten, der im Piratenjargon spricht)
- Anzeige und Bearbeitung des Systemprompts durch Klicken auf die Kachel
- Jede Kachel hat ein passendes Charakterbild
- Chat-Fenster im unteren Bereich für Benutzerfragen und LLM-Antworten
- Konfigurationsoptionen für Ollama und Anthropic in der Seitenleiste

## Installation

1. Python 3.11 oder höher installieren
2. Repository klonen
3. Virtuelle Umgebung mit uv erstellen und Abhängigkeiten installieren:

```bash
./install.sh
```

4. `.env`-Datei erstellen und Anthropic API-Schlüssel hinzufügen:

```
ANTHROPIC_API_KEY=your_api_key_here
```

## Ausführung

```bash
streamlit run app.py --run-app
```

## Tests

Um die Tests auszuführen:

```bash
python run.py --run-tests
``` 