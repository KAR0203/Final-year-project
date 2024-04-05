# # server.py

# from flask import Flask, request, redirect

# app = Flask(__name__)

# @app.route('/streamlit')
# def streamlit_redirect():
#     if request.args.get('loggedIn') == 'true':
#         return redirect('http://localhost:8502')  # Replace with your Streamlit app URL
#     else:
#         return 'Not logged in'


# if __name__ == '__main__':
#     app.run(port=5000)  # Adjust the port as needed


# from flask import Flask, request, redirect

# app = Flask(__name__)

# @app.route('/streamlit')
# def streamlit_redirect():
#     if request.args.get('loggedIn') == 'true':
#         return redirect('http://localhost:8502')  # Replace with your Streamlit app URL
#         # return redirect('http://127.0.0.1:8080')  # Replace with your Streamlit app URL
#     else:
#         return 'Not logged in'

# if __name__ == '__main__':
#     app.run(port=5000)  # Adjust the port as needed


# # server.py
# from flask import Flask, request, redirect
# import streamlit as st
# from dotenv import load_dotenv
# from utils import create_docs

# # Initialize Flask app
# app = Flask(__name__)

# # Route for handling the redirection to Streamlit
# @app.route('/streamlit')
# def streamlit_redirect():
#     if request.args.get('loggedIn') == 'true':
#         return redirect('http://localhost:8501')  # Redirect to Streamlit app URL
#     else:
#         return 'Not logged in'

# # Main function to define Streamlit app logic
# def main():
#     load_dotenv()

#     st.set_page_config(page_title="Invoice Extraction Bot")
#     st.title("Invoice Extraction 💁 ")
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

# # Define Flask app root route for initial redirection
# @app.route('/')
# def root():
#     # Check if 'loggedIn' parameter is not present in the query parameters
#     if 'loggedIn' not in request.args:
#         # Redirect to Streamlit app with the custom URL parameter
#         return redirect('/streamlit?loggedIn=true')
#     else:
#         return 'Already redirected'

# # Run Flask app
# if __name__ == '__main__':
#     app.run(port=5002)  # Adjust the port as needed



# from flask import Flask, request, redirect

# app = Flask(__name__)

# @app.route('/streamlit')
# def streamlit_redirect():
#     if request.args.get('loggedIn') == 'true':
#         return redirect('http://localhost:8502')  # Replace with your Streamlit app URL
#     else:
#         return 'Not logged in'

# if __name__ == '__main__':
#     app.run(port=5001)  # Adjust the port as needed



from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/streamlit')
def streamlit_redirect():
    if request.args.get('loggedIn') == 'true':
        return redirect('http://localhost:8502')  # Redirect to your Streamlit app URL
    else:
        return 'Not logged in'

if __name__ == '__main__':
    app.run(port=5001)  # Adjust the port as needed
