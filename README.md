# Flowbit AI Work Assistant (Flowbit Labs)

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Open Source](https://img.shields.io/badge/open--source-yes-brightgreen.svg)


A minimal, practical AI assistant you can run locally to:
- plan your day (prioritize + time blocks)
- rewrite text (emails/messages/paragraphs)
- close your day (review + carryover plan)

This repo is designed to be easy to understand and easy to extend.

## Demo (What it does)
**Plan my day**
- turns your task dump into Must/Should/Could
- creates a realistic schedule
- gives first steps for top priorities

**Rewrite text**
- makes writing clearer, shorter, and more professional

**End-of-day review**
- summarizes the day
- carries tasks forward
- creates a simple first-30-min plan for tomorrow

## Setup

### 1) Clone
```bash
git clone https://github.com/<your-username>/flowbit-ai-work-assistant.git
cd flowbit-ai-work-assistant 
```

### 2) Install
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### 3) Add your API key
```bash
cp .env.example .env
```

Edit .env:
```bash
OPENAI_API_KEY=YOUR_KEY_HERE
```

(Optional) set a model:
```bash
FLOWBIT_MODEL=gpt-4o-mini
```

### 4) Run
```bash
python assistant.py
```


### Customization ideas
- Add a “meeting prep” mode (agenda + questions + summary)
- Add “weekly review” mode
- Save outputs to markdown files
- Connect to Notion, Google Calendar, or a local notes folder


## Roadmap

Planned features:
- Weekly review mode
- Meeting preparation assistant
- Research summarizer
- Markdown knowledge base
- Calendar integration
- Notion integration
- Local note search

This project is built in public by Flowbit Labs.
Follow along on Medium for tutorials and builds.


## Support the Project

If this project helps you work smarter:
- Give it a ⭐ on GitHub
- Share it with your team
- Follow Flowbit Labs on Medium

This helps us build more tools like this.

