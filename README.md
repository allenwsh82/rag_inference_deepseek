# rag_inference_deepseek

<img width="800" alt="deepseek_chatbot" src="https://github.com/user-attachments/assets/a8ced19a-cfd3-4431-a95f-e9f39dc1f930" />

Testing Setup:
Platform: Intel® Tiber™ AI Studio
 
 Hardware:
 🖥️ One Bare Metal Machine Intel Xeon 5th Gen (8592-64C) with 1TB of Memory
 
 Software Packages:
 <br/>
 🛠️ LlamaIndex
 <br/>
 🛠️ Intel OpenVINO
 <br/>
 🛠️ optimum-intel
 <br/>
 🛠️ transformers
 <br/>
 
Testing Configuration:
<br/>
Model: DeepSeek-R1-Distill-Llama-8B
<br/>
Toolkit:  OpenVINOLLM API function
<br/>
Frameworks:⚙️ LlamaIndex
<br/>
RAG Application: PDF Document Input
<br/>

<img width="1024" alt="AI_ChatBot_DeepSeek" src="https://github.com/user-attachments/assets/7a0a81a9-b009-45d3-aff3-43d07afca8e0" />

Key Components / Features:
 <br/>
 <br/>
reader = SimpleWebPageReader Reader API used to simplify data ingestion from multiple sources which include webpages for processing and data extraction. Follow this URL: https://lnkd.in/e-_yEFZk
 <br/>
 <br/>
query_engine = index.as_query_engine query engine API takes in natural language query and generates a rich response to the user. It has built in one or many indexes capacities as retrievers which simplify the process of building a AI ChatBot with RAG capabilities. Follow this URL: https://lnkd.in/ezpK-RF9
 <br/>
 <br/>
index = VectorStoreIndex.from_documents Vector Stores are key component in RAG and you can easily call out this function from LlamaIndex to load a set of documents and build an index from them using from_documents. Follow this URL: https://lnkd.in/evJQsj-M
 <br/>
 <br/>
ov_llm = OpenVINOLLM ( )
 <br/>
 <br/>
OpenVINO LLMs is an open-source toolkit for optimizing and deploying AI inference. OpenVINO™ Runtime can enable running the same model optimized across various hardware devices. Accelerate your deep learning performance across use cases like: language + LLMs, computer vision, automatic speech recognition, and more.
 <br/>
 <br/>
How to run llm with QnA ChatBot with RAG Demo:
 <br/>
1) Clone the project:
   ``` 
   git clone https://github.com/allenwsh82/rag_inference_deepseek
   ```
   <br/>
   <img width="500" alt="github_rag_2" src="https://github.com/user-attachments/assets/75a5e07c-5b71-4842-b50b-1ec2eb1a04ff" />
   <br/>
   
2) Create a new environment for this project:
   ```
   python -m venv rag_env
   ```
   <br/>
   <img width="500" alt="github_rag_3" src="https://github.com/user-attachments/assets/7e72aef9-0f42-4309-bb94-9193e044c5ae" />
   <br/>
   
3) You should be able to see a new folder called rag_env inside the folder of rag_inference_deepseek
   
   <br/>
   <img width="500" alt="rag_inference_deepseek folder" src="https://github.com/user-attachments/assets/1c17b444-3144-46b7-8139-bed9a4984c1e" />
   <br/>


5) Activate the environment:
   ```
   source rag_env/bin/activate
   ```
   <br/>
   <img width="500" alt="github_rag_4" src="https://github.com/user-attachments/assets/70ef065d-1772-48ae-ac53-a81976ccaa7f" />
   <br/>

6) Make sure all .py file is in executable:
   ```
   chmod u+x *.py
   ```
   <br/>
   <img width="500" alt="github_rag_6png" src="https://github.com/user-attachments/assets/f6d63d3b-1df2-4976-8bef-79138dba6a9c" />
   <br/>

7) Setup the environment with all the dependencies:
   ```
   pip install -r requirements.txt
   ```
   <br/>
   <img width="500" alt="github_rag_5" src="https://github.com/user-attachments/assets/23254544-9dda-4482-a6d3-447301dcf4d0" />
   <br/>


8) Don't forget to include huggingface-cli login token into your current environment:
   ```
   huggingface-cli login --token "hf_xxxxxxxxxxxxxxxxxxxx"
   ```
   <br/>
   ![github_rag_8](https://github.com/user-attachments/assets/f91d36d1-df97-4d08-84fa-ef8b8630ecbd)
   <br/>
   
9) Run the demo script by this command:
   ```
   streamlit run inference.py
   ```
   <br/>
   <img width="500" alt="github_rag_9" src="https://github.com/user-attachments/assets/adcf8540-45df-4682-bb5e-f701bb6246c9" />
   <br/>

10) Open a browser and type the following Port:8501 at the local URL:
   ```
   http://localhost:8501/
   ```

<br/>

You should be seeing the following streamlit UI as shown below:

<br/>

<img width="959" alt="image_1" src="https://github.com/user-attachments/assets/07636445-63b0-4767-b7d3-825c025e935c" />

<br/>
<br/>

Once you have upload your pdf document, basically, we can prompt the LLM model for any questions related to the pdf document 

<br/>

<img width="950" alt="image_2" src="https://github.com/user-attachments/assets/6adbdc99-f9e0-4af7-8197-7dcfcfe2aa4e" />

<br/>



  

