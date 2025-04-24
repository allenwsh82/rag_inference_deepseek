# rag_inference_deepseek

![deepresize1-1024x684](https://github.com/user-attachments/assets/1188bd2a-576a-4e7a-81f7-2735c339169b)

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


How to run llm with web scraping with RAG Demo:

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
