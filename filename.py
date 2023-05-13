import PyPDF2
import nltk
from nltk.corpus import words

# Download the NLTK words corpus
nltk.download('words')

# Load the PDF file
with open('sample.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Extract the text from each page of the PDF
    text = ""
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        text += page.extractText()

    # Remove non-alphanumeric characters and convert to lowercase
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    text = text.lower()

    # Check for AI-generated content
    word_set = set(words.words())
    words_in_text = text.split()
    num_ai_words = 0
    for word in words_in_text:
        if word not in word_set:
            num_ai_words += 1
    ai_percentage = num_ai_words / len(words_in_text) * 100

    # Write the text to a file
    with open('output.txt', 'w') as text_file:
        text_file.write(text)

    # Print the AI-generated content percentage
    print(f"AI-generated content percentage: {ai_percentage:.2f}%")
