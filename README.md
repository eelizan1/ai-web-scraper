# ai-web-scraper

# Overview
This project is an AI-powered web scraping toolkit that leverages Ollama, BrightData, Selenium, and other modern libraries to intelligently extract data from the web. Designed for efficiency and scalability, it combines traditional scraping techniques with LLM-assisted decision-making to navigate complex sites, bypass anti-bot measures, and parse data in a structured, adaptable format.

Key Features:

🤖 AI-Assisted Scraping using Ollama to understand context, interpret page structures, and guide scraping logic dynamically.

🌐 BrightData Integration for robust proxy management and geo-targeted scraping.

🕸️ Selenium Automation for interacting with JavaScript-heavy or dynamic content.

🧠 Intelligent retry logic, headless browsing, and customizable workflows.

📦 Modular architecture that makes it easy to plug in new targets, extractors, or AI models.

### Setup
To get started, set up a virtual environment and install dependencies:

```bash
python3 -m venv ai
pip install -r requirements.txt
```

### Ollama - llama3
This will use a local instance of the Ollamma LLM. Download Ollama for mac or windows and use model llama3. Then run: 
```bash
ollama #runs the llm
ollama pull llama3.1 # pulls the model
ollama run llama3
```

### To Run 
```bash
streamlit run main.py
