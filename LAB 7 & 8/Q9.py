import re

def hindi_tokenizer(text):
    patterns = [
        (r'\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}', 'DATE'),  # Dates
        (r'https?://\S+|www\.\S+', 'URL'),  # URLs
        (r'[\w.-]+@[\w.-]+\.\w+', 'EMAIL'),  # Emails
        (r'@\w+', 'HANDLE'),  # Social media handles
        (r'\d{1,3}(,\d{2})*(,\d{3})*', 'NUMBER'),  # Indian number format
        (r'\d+\.\d+', 'DECIMAL'),  # Decimal numbers
        (r'\d+/\d+', 'FRACTION'),  # Fractions
        (r'[\u0900-\u097F]+', 'HINDI_WORD'),  # Hindi words (Devanagari script)
        (r'[.,!?;:\"()\[\]{}]', 'PUNCTUATION')  # Punctuation
    ]
    
    tokens = []
    for pattern, label in patterns:
        for match in re.finditer(pattern, text):
            tokens.append((match.group(), label))
    
    return tokens

text = "नाम तनय है और जन्मतिथि 05/04/2007 है। मेरा ईमेल thanaybodda@gmail.com है।"
print(hindi_tokenizer(text))
