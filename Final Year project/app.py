# # app.py
# import streamlit as st
# from dotenv import load_dotenv
# from utils import *


# def main():
#     load_dotenv()

#     st.set_page_config(page_title="Invoice Extraction Bot")
#     st.title("Invoice Extraction .....💁 ")
#     st.subheader("I can help you in extracting invoice data")

#     # Upload the Invoices (pdf files)
#     pdf_files = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

#     submit = st.button("Extract Data")

#     if submit and pdf_files:
#         with st.spinner('Wait for it...'):
#             df = create_docs(pdf_files)
#             if df is not None and not df.empty:
#                 st.write(df.head())

#                 data_as_csv = df.to_csv(index=False).encode("utf-8")
#                 st.download_button(
#                     "Download data as CSV",
#                     data_as_csv,
#                     "invoice_data.csv",
#                     "text/csv",
#                     key="download-tools-csv",
#                 )
#                 st.success("Data extraction completed! 🎉")
#             else:
#                 st.error("No data extracted from the provided PDF files.")


# # Invoking main function
# if __name__ == '__main__':
#     main()


# app.py

# import streamlit as st
# from dotenv import load_dotenv
# from utils import *
# from flask import Flask, request, redirect

# # Function to check if the custom URL parameter 'loggedIn' is set to 'true'
# def check_logged_in():
#     if st.experimental_get_query_params().get('loggedIn', [''])[0] == 'true':
#         return True
#     else:
#         return False

# def main():
#     load_dotenv()

#     st.set_page_config(page_title="Invoice Extraction Bot")
#     st.title("Invoice Extraction .....💁 ")
#     st.subheader("I can help you in extracting invoice data")

#     # Upload the Invoices (pdf files)
#     pdf_files = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

#     submit = st.button("Extract Data")

#     if submit and pdf_files:
#         with st.spinner('Wait for it...'):
#             df = create_docs(pdf_files)
#             if df is not None and not df.empty:
#                 st.write(df.head())

#                 data_as_csv = df.to_csv(index=False).encode("utf-8")
#                 st.download_button(
#                     "Download data as CSV",
#                     data_as_csv,
#                     "invoice_data.csv",
#                     "text/csv",
#                     key="download-tools-csv",
#                 )
#                 st.success("Data extraction completed! 🎉")
#             else:
#                 st.error("No data extracted from the provided PDF files.")

# if __name__ == '__main__':
#     app = Flask(__name__)

#     @app.route('/')
#     def root():
#         # Check if 'loggedIn' parameter is not present in the query parameters
#         if 'loggedIn' not in request.args:
#             # Redirect to Streamlit app with the custom URL parameter
#             return redirect('/streamlit?loggedIn=true')
#         else:
#             return 'Already redirected'

#     @app.route('/streamlit')
#     def streamlit_redirect():
#         if request.args.get('loggedIn') == 'true':
#             return redirect('/')  # Redirect to the root URL where Streamlit app is running
#         else:
#             return 'Not logged in'

#     app.run(port=8080)  # Adjust the port as needed



# import streamlit as st
# from flask import Flask, request, redirect
# from dotenv import load_dotenv
# from utils import *

# # Function to check if the custom URL parameter 'loggedIn' is set to 'true'
# def check_logged_in():
#     if st.experimental_get_query_params().get('loggedIn', [''])[0] == 'true':
#         return True
#     else:
#         return False

# def main():
#     load_dotenv()

#     st.set_page_config(page_title="Invoice Extraction Bot")
#     st.title("Invoice Extraction .....💁 ")
#     st.subheader("I can help you in extracting invoice data")

#     # Upload the Invoices (pdf files)
#     pdf_files = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

#     submit = st.button("Extract Data")

#     if submit and pdf_files:
#         with st.spinner('Wait for it...'):
#             df = create_docs(pdf_files)
#             if df is not None and not df.empty:
#                 st.write(df.head())

#                 data_as_csv = df.to_csv(index=False).encode("utf-8")
#                 st.download_button(
#                     "Download data as CSV",
#                     data_as_csv,
#                     "invoice_data.csv",
#                     "text/csv",
#                     key="download-tools-csv",
#                 )
#                 st.success("Data extraction completed! 🎉")
#             else:
#                 st.error("No data extracted from the provided PDF files.")

# if __name__ == '__main__':
#     app = Flask(__name__)

#     @app.route('/')
#     def root():
#         # Check if 'loggedIn' parameter is not present in the query parameters
#         if 'loggedIn' not in request.args:
#             # Redirect to Streamlit app with the custom URL parameter
#             return redirect('/streamlit?loggedIn=true')
#         else:
#             return 'Already redirected'

#     @app.route('/streamlit')
#     def streamlit_redirect():
#         if request.args.get('loggedIn') == 'true':
#             return redirect('http://localhost:8501')  # Redirect to the root URL where Streamlit app is running
#         else:
#             return 'Not logged in'

#     app.run(port=8502)  # Adjust the port as needed







import streamlit as st
from flask import request, redirect
from dotenv import load_dotenv
from utils import create_docs

load_dotenv()

st.set_page_config(page_title="Invoice Extraction Bot")
st.title("Invoice Extraction .....💁 ")
st.subheader("I can help you in extracting invoice data")

# Upload the Invoices (pdf files)
pdf_files = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

submit = st.button("Extract Data")

if submit and pdf_files:
    with st.spinner('Wait for it...'):
        df = create_docs(pdf_files)
        if df is not None and not df.empty:
            st.write(df.head())

            data_as_csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download data as CSV",
                data_as_csv,
                "invoice_data.csv",
                "text/csv",
                key="download-tools-csv",
            )
            st.success("Data extraction completed! 🎉")
        else:
            st.error("No data extracted from the provided PDF files.")
