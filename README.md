DocuQuery AI 🤖📄

An AI-powered document Q&A chatbot built with Python and Google's Gemini API. Upload a text or PDF document, ask questions about it in plain English, and get accurate answers grounded in the document's actual content.

Features
📄 Supports both .txt and .pdf documents
💬 Interactive terminal-based chat interface
🎯 Answers are grounded strictly in the uploaded document (reduces hallucination)
⚡ Powered by Google's Gemini API (free tier)
🔒 API key handled securely via environment variable or runtime prompt
Tech Stack
Language: Python 3
AI Model: Google Gemini (gemini-flash-latest)
Libraries: google-genai, PyPDF2
How It Works
The user provides a document (.txt or .pdf)
The script extracts the full text from the document
When the user asks a question, the script builds a grounded prompt that includes the document content
The prompt is sent to the Gemini API, which generates an answer based only on the document
If the answer isn't found in the document, the bot says so instead of guessing
Setup
1. Install dependencies
bash
pip install google-genai PyPDF2
2. Get a free Gemini API key

Get one from Google AI Studio → "Get API key".

3. Set your API key (optional but recommended)
bash
# Windows
set GEMINI_API_KEY="your_key_here"

# Mac/Linux
export GEMINI_API_KEY="your_key_here"

If not set, the script will prompt you to enter it when it runs.

Usage
bash
python doc_qa_chatbot.py

Then follow the prompts:

Enter your API key (if not already set)
Enter the path to your document (e.g. sample.txt or notes.pdf)
Start asking questions — type exit or quit to stop
Example
Enter the path to your document (.txt or .pdf): sample.txt

Loaded document (142 characters). Ask away!
Type 'exit' or 'quit' to stop.

You: What is this document about?
Bot: Based on the document, it is about a B.Tech graduate in
Electronics and Communication Engineering who is learning Java
and Python with the goal of becoming a software developer.
Project Structure
doc-qa-chatbot/
├── doc_qa_chatbot.py   # Main script
├── README.md           # Project documentation
└── sample.txt          # Example test document
Challenges & Learnings
Migrated from the deprecated google-generativeai package to the newer google-genai SDK after Google's package deprecation
Handled Google's 2026 API key format change (AIza → AQ. auth keys)
Adapted to multiple Gemini model deprecations during development by switching to gemini-flash-latest, an alias that always points to Google's current recommended Flash model — making the code more resilient to future model retirements
Future Improvements
Add a Streamlit-based web UI
Support multi-file document uploads
Add conversation memory for follow-up questions
Chunk large documents for more efficient context use
Author

Mandapalli Tejaswini — GitHub