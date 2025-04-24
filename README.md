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


<img width="900" alt="AI_ChatBot_DeepSeek" src="https://github.com/user-attachments/assets/7a0a81a9-b009-45d3-aff3-43d07afca8e0" />

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
