#  AI Service — Compliance Calendar & Tracker

This AI service is part of the **Compliance Calendar and Tracker** project.  
It is built using Flask and integrates with the Groq LLM API to provide intelligent automation features.

---

#  Features

-  Describe user input using AI
-  Generate recommendations
-  Create structured reports
-  Async report processing (background execution)
-  Real-time streaming (SSE)
-  Document analysis (insights & risks)
-  Batch processing (multiple inputs with delay)
-  Unit testing with pytest

---

#  Tech Stack

- Python 3.11
- Flask
- Groq API (LLaMA model)
- JSON APIs
- Pytest

---

#  Prerequisites

Make sure you have:

- Python 3.10 or above
- pip installed
- Git installed
- Groq API key

---

#  Environment Variables

Create a `.env` file inside the project:


---

# Installation

```bash
git clone https://github.com/SurendraMV11/compliance-calendar-tracker.git
cd compliance-calendar-tracker/ai-services

python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt