# AI-Generated Content Detection

This code is designed to analyze a PDF document and determine the percentage of AI-generated content within the text. It utilizes the PyPDF2 library to extract the text from each page of the PDF and the NLTK library to check for AI-generated words.


## Requirements

1. Python 3.x
2. PyPDF2 library
3. NLTK library


## Setup

**Install Python: If you don't have Python installed, download and install the latest version from the official [Python website](https://www.python.org/).

Install dependencies: Open the command prompt or terminal and run the following commands to install the required libraries:


```python
pip install PyPDF2
pip install nltk
```
Download NLTK corpus: Before running the code, you need to download the words corpus from NLTK. In the code, there is a line nltk.download('words') that will initiate the download. After running the code for the first time, NLTK will prompt you to download the corpus. Follow the instructions to complete the download.



## Usage
1. Place the PDF file you want to analyze in the same directory as the code file.

2. Open the code file and modify the following lines if necessary:
with open('sample.pdf', 'rb') as pdf_file: Replace 'sample.pdf' with the filename of your PDF file.
with open('output.txt', 'w') as text_file: Replace 'output.txt' with the desired filename for the output text file.

3. Run the code: Open the command prompt or terminal, navigate to the directory containing the code file, and execute the following command:

```python
python filename.py
```
Replace filename.py with the actual name of the code file.

4. The code will extract the text from each page of the PDF, remove non-alphanumeric characters, convert the text to lowercase, and save it in the specified output text file.

5. After processing the text, the code will calculate the percentage of AI-generated content within the text and display it in the console as follows:
```css
AI-generated content percentage: X.XX%

```
The value X.XX represents the percentage of AI-generated content detected.

## Notes 
1. The code assumes that the PDF file contains readable text. It may not work properly with scanned documents or files that only contain images.
2. The accuracy of AI-generated content detection depends on the quality of the NLTK word corpus. False positives or false negatives may occur.
3. It is recommended to review the extracted text and AI-generated content percentage to validate the results.

## References


[PyPDF2](https://pythonhosted.org/PyPDF2/)

[NLTK](https://www.nltk.org/)


## License
[MIT](https://choosealicense.com/licenses/mit/)
