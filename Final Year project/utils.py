# utils.py
from PyPDF2 import PdfReader
import replicate
from langchain.prompts import PromptTemplate
import pandas as pd
import re
import os
from dotenv import load_dotenv

load_dotenv()

def get_pdf_text(pdf_file):
    text = ""
    try:
        with pdf_file as f:
            pdf_reader = PdfReader(f)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        print("Error occurred while extracting text from PDF:", e)
    return text

def extracted_data(pages_data):
    template = """Extract all the following values : invoice no., Description, Quantity, date, 
        Unit price , Amount, Total, email, phone number and address from this data: {pages}

        Expected output: remove any dollar symbols {{'Invoice no.': '1001329','Description': 'Office Chair','Quantity': '2','Date': '5/4/2023','Unit price': '1100.00','Amount': '2200.00','Total': '2200.00','Email': 'Santoshvarma0988@gmail.com','Phone number': '9999999999','Address': 'Mumbai, India'}}
        """
    prompt_template = PromptTemplate(input_variables=["pages"], template=template)

    replicate_api_key = os.getenv("REPLICATE_API_TOKEN")

    output = replicate.run('meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e',
                           input={"prompt": prompt_template.format(pages=pages_data),
                                  "temperature": 0.1, "top_p": 0.9, "max_length": 512, "repetition_penalty": 1},
                           api_key=replicate_api_key)

    full_response = ''
    for item in output:
        full_response += item

    return full_response

def create_docs(user_pdf_list):
    df = pd.DataFrame(columns=['Invoice no', 'Description', 'Quantity', 'Date', 'Unit price', 'Amount', 'Total', 'Email', 'Phone number', 'Address'])

    for pdf_file in user_pdf_list:
        raw_data = get_pdf_text(pdf_file)
        llm_extracted_data = extracted_data(raw_data)

        pattern = r"'Invoice\s*no\.?':\s*'([^']+)',\s*'Description':\s*'([^']+)',\s*'Quantity':\s*'([^']+)',\s*'Date':\s*'([^']+)',\s*'Unit\s*price':\s*'([^']+)',\s*'Amount':\s*'([^']+)',\s*'Total':\s*'([^']+)',\s*'Email':\s*'([^']+)',\s*'Phone\s*number':\s*'([^']+)',\s*'Address':\s*'([^']+)'"  

        match = re.search(pattern, llm_extracted_data)

        data_dict = {}  

        if match:
            data_dict = {
                'Invoice no': match.group(1),
                'Description': match.group(2),
                'Quantity': match.group(3),
                'Date': match.group(4),
                'Unit price': match.group(5),
                'Amount': match.group(6),
                'Total': match.group(7),
                'Email': match.group(8),
                'Phone number': match.group(9),
                'Address': match.group(10)
            }
        else:
            print("No match found.")

        df = pd.concat([df, pd.DataFrame(data_dict, index=[0])], ignore_index=True)

    return df
