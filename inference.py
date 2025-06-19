#Reference LlamaIndex tutorial document to build this RAG chatbot 
#This code is running on Intel CPU and please email me if you have any difficulties running the source code (allenwsh@gmail.com)

import os
import base64
import gc
import random
import tempfile
import time
import uuid

from IPython.display import Markdown, display

from llama_index.core import Settings
from llama_index.core import PromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.llms.openvino import OpenVINOLLM

import streamlit as st

#Insert Intel Logo (Make sure u point the right path to the logo your save)
st.logo ("Intel_logo.png", link=None, icon_image=None)

#Insert Intel AI Everywhere 
#st.image ("/home/smgailab/data1/AI_Allen/image/Intel_AI.jpg", caption="Intel AI Everywhere!")

if "id" not in st.session_state:
    st.session_state.id = uuid.uuid4()
    st.session_state.file_cache = {}

session_id = st.session_state.id
client = None

def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None
    gc.collect()

# Opening file from file path
def display_pdf(file):
    

    st.markdown("### Preview of the PDF Document Which Was Uploaded!")
    base64_pdf = base64.b64encode(file.read()).decode("utf-8")

    # Display your PDF file   (Can change the width and height size)
    pdf_display = f"""<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="100%" type="application/pdf"
                        style="height:100vh; width:100%"
                    >
                    </iframe>"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

#Define your sidebar to upload your pdf. If other files, you can choose 
with st.sidebar:
    st.header(f"Please upload your documents!")
    
    uploaded_file = st.file_uploader("Choose your `.pdf` file", type="pdf")

    if uploaded_file:
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                file_path = os.path.join(temp_dir, uploaded_file.name)
                
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                
                file_key = f"{session_id}-{uploaded_file.name}"
                st.write("Indexing your document in progress...")

                if file_key not in st.session_state.get('file_cache', {}):

                    if os.path.exists(temp_dir):
                            loader = SimpleDirectoryReader(
                                input_dir = temp_dir,
                                required_exts=[".pdf"],
                                recursive=True
                            )
                    else:    
                        st.error('Could not find the file you uploaded, please check again...')
                        st.stop()
                    
                    docs = loader.load_data()

                    # setup llm & embedding model, setting the timeout as 120 seconds
                    # Using bge-large-en-v1.5 embedding model
                    #llm=Ollama(model="llama3.1", request_timeout=120.0)
                    embed_model = HuggingFaceEmbedding( model_name="BAAI/bge-large-en-v1.5", trust_remote_code=True)


                    #OpenVINOLLM Configuration
                    ov_config = {
                        "PERFORMANCE_HINT": "LATENCY",
                        "NUM_STREAMS": "1",
                        "CACHE_DIR": "",
                    }

                    llm = OpenVINOLLM(
                        model_id_or_path="deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
                        context_window=3900,
                        max_new_tokens=256,
                        model_kwargs={"ov_config": ov_config},
                        generate_kwargs={"temperature": 0.7, "top_k": 50, "top_p": 0.95},
                        #messages_to_prompt=messages_to_prompt,
                        #completion_to_prompt=completion_to_prompt,
                        device_map="cpu",
                    )

                    
                    # Create Index
                    Settings.embed_model = embed_model
                    
                    # Storing the vector database using In Memory from Lamma Index (Using In Memory vector database)
                    index = VectorStoreIndex.from_documents(docs, show_progress=True)

                    # Create the query engine
                    Settings.llm = llm
                    query_engine = index.as_query_engine(streaming=True)

                    # Customise prompt template
                    qa_prompt_tmpl_str = (
                    "Context information is below.\n"
                    "---------------------\n"
                    "{context_str}\n"
                    "---------------------\n"
                    "Given the context information above I want you to think step by step to answer the query in a crisp manner, incase case you don't know the answer say 'I don't know!'.\n"
                    "Query: {query_str}\n"
                    "Answer: "
                    )
                    qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)

                    query_engine.update_prompts(
                        {"response_synthesizer:text_qa_template": qa_prompt_tmpl}
                    )
                    
                    st.session_state.file_cache[file_key] = query_engine
                else:
                    query_engine = st.session_state.file_cache[file_key]

                # Inform the user that the file is processed and Display the PDF uploaded
                st.success("Your AI ChatBot Is Ready to Chat!")
                display_pdf(uploaded_file)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.stop()     

col1, col2 = st.columns([6, 1])

with col1:
    st.header(f"AI ChatBot with RAG using DeepSeek-R1-Distill-Llama-8B with Intel Xeon 5th Gen 8592+")

with col2:
    st.button("Clear ↺", on_click=reset_chat)

# Initialize chat history
if "messages" not in st.session_state:
    reset_chat()


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate stream of response with milliseconds delay
        streaming_response = query_engine.query(prompt)
        
        for chunk in streaming_response.response_gen:
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")

        # full_response = query_engine.query(prompt)

        message_placeholder.markdown(full_response)
        # st.session_state.context = ctx

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
