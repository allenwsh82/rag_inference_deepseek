# rag_inference_deepseek

<img width="800" alt="deepseek_chatbot" src="https://github.com/user-attachments/assets/a8ced19a-cfd3-4431-a95f-e9f39dc1f930" />

Testing Setup:
Platform: Intel® Tiber™ AI Studio
 
 Hardware:
 🖥️ One Bare Metal Machine Intel Xeon 5th Gen (8592-64C) with 1TB of Memory
 
 Software Packages:
 🛠️ LlamaIndex
 🛠️ Intel OpenVINO
 🛠️ optimum-intel
 
Testing Configuration:
Model: DeepSeek-R1-Distill-Llama-8B
Toolkit” OpenVINOLLM API function 
Frameworks:⚙️ LlamaIndex
RAG Application: PDF Document Input


<img width="1024" alt="AI_ChatBot_DeepSeek" src="https://github.com/user-attachments/assets/7a0a81a9-b009-45d3-aff3-43d07afca8e0" />

Key Components / Features:

reader = SimpleWebPageReader Reader API used to simplify data ingestion from multiple sources which include webpages for processing and data extraction. Follow this URL: https://lnkd.in/e-_yEFZk

query_engine = index.as_query_engine query engine API takes in natural language query and generates a rich response to the user. It has built in one or many indexes capacities as retrievers which simplify the process of building a AI ChatBot with RAG capabilities. Follow this URL: https://lnkd.in/ezpK-RF9

index = VectorStoreIndex.from_documents Vector Stores are key component in RAG and you can easily call out this function from LlamaIndex to load a set of documents and build an index from them using from_documents. Follow this URL: https://lnkd.in/evJQsj-M

ov_llm = OpenVINOLLM ( )
OpenVINO LLMs is an open-source toolkit for optimizing and deploying AI inference. OpenVINO™ Runtime can enable running the same model optimized across various hardware devices. Accelerate your deep learning performance across use cases like: language + LLMs, computer vision, automatic speech recognition, and more.

How to run llm with QnA ChatBot with RAG Demo:

1) Clone the project:
   ``` 
   git clone https://github.com/allenwsh82/rag_inference_deepseek
   ```
   
2) Create a new environment for this project:
   ```
   python -m venv rag_env
   ```
   
3) Activate the environment:
   ```
   source rag_env/bin/activate
   ```
   
4) Setup the environment with all the dependencies:
   ```
   pip install -r requirements.txt
   ```
   
5) Run the demo script by this command:
   ```
   streamlit run rag_deepseek.py
   ```
