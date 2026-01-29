from pypdf import PdfReader

def extract_text(pdf_file):
    try:
        # Reset stream position (VERY IMPORTANT)
        pdf_file.stream.seek(0)

        reader = PdfReader(pdf_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        # If PDF has no readable text
        if not text.strip():
            return "Demo content: This PDF appears to be scanned or image-based."

        return text

    except Exception:
        # Any PDF error → safe fallback
        return "Demo content: Unable to read this PDF. Using fallback notes."

def study_ai(content, question, lang):
    if lang == "hindi":
        return "📘 डेमो उत्तर: यह विषय छात्रों के लिए सरल भाषा में समझाया गया है।"
    else:
        return "📘 Demo Answer: This concept is explained in simple Hinglish for students."
