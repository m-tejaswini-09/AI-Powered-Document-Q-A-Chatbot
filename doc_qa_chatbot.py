"""
AI Document Q&A Chatbot
------------------------
Loads a text or PDF document and lets the user ask questions about it
using Google's Gemini API (free tier).
"""

import os
import sys

try:
    from google import genai
except ImportError:
    print("Missing dependency. Run: pip install google-genai")
    sys.exit(1)


def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf_file(path):
    try:
        import PyPDF2
    except ImportError:
        print("Missing dependency. Run: pip install PyPDF2")
        sys.exit(1)

    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def load_document(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)

    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return load_pdf_file(path)
    elif ext == ".txt":
        return load_text_file(path)
    else:
        print("Unsupported file type. Please use a .txt or .pdf file.")
        sys.exit(1)


def get_api_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        key = input("Enter your Gemini API key: ").strip()
    return key


def build_prompt(document_text, question):
    return f"""You are a helpful assistant. Answer the question using ONLY the
information in the document below. If the answer is not in the document,
say "I couldn't find that in the document."

DOCUMENT:
{document_text}

QUESTION:
{question}

ANSWER:"""


def main():
    print("=" * 50)
    print("  AI Document Q&A Chatbot")
    print("=" * 50)

    api_key = get_api_key()
    client = genai.Client(api_key=api_key)

    file_path = input("\nEnter the path to your document (.txt or .pdf): ").strip()
    document_text = load_document(file_path)

    max_chars = 100000
    if len(document_text) > max_chars:
        print(f"Document is large; using the first {max_chars} characters.")
        document_text = document_text[:max_chars]

    print(f"\nLoaded document ({len(document_text)} characters). Ask away!")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        question = input("You: ").strip()
        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        if not question:
            continue

        prompt = build_prompt(document_text, question)
        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )
            print(f"\nBot: {response.text.strip()}\n")
        except Exception as e:
            print(f"Error getting response: {e}\n")


main()