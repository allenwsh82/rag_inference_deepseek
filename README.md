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
   
2) Create a new environment for this project:
   ```
   python -m venv rag_env
   ```
   
3) You should be able to see a new folder called rag_env inside the folder of rag_inference_deepseek
<br/>
            <img width="500" alt="rag_inference_deepseek folder" src="https://github.com/user-attachments/assets/1c17b444-3144-46b7-8139-bed9a4984c1e" />
<br/>


4) Activate the environment:
   ```
   source rag_env/bin/activate
   ```

5) Setup the environment with all the dependencies:
   ```
   pip install -r requirements.txt
   ```

6) Don't forget to include huggingface-cli login token into your current environment:
   ```
   huggingface-cli login --token "hf_xxxxxxxxxxxxxxxxxxxx"
   ```
   
7) Run the demo script by this command:
   ```
   streamlit run inference.py
   ```

8) Open a browser and type the following Port:8501 at the local URL:
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



  

