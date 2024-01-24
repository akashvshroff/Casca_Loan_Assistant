# Overview

- My solution for the coding challenge relies on a RAG, or retrieval-augmented generation based approach that analyzes the given bank statement to give an initial prognosis and allows me to dig deeper into the statement using natural language in a chat-based method.
- The benefit of using an LLM-based approach is in its understanding of obscure statement details and ability to reason through potential trends in the transactions. Moreover, instead of getting a concrete answer from the model, I instead tried to implement a human-in-the-loop system where it points to key findings from the statement but decision-making rests with a human. In such a system, the LLM is meant to augment human capabilities and increase efficiency by keenly identifying glaring red-flags.
- I leveraged GPT-4 for its reasoning capabilities and versatility and used a vector store devised using the PyMuPDF OCR and an embeddings model from HuggingFace to build the system. The minimal frontend is built using an incredibly lightweight Python library called streamlit.
- A demo of my solution can be seen through the video below.

  https://github.com/akashvshroff/Casca_Loan_Assistant/assets/63399889/4a0460ba-9519-4373-b1f8-f8ab7f466b54

## Installation & Running
- You can use the requirements.txt file to pip install all packages that are needed to run the file and then run `streamlit run main.py` to get the frontend up and running. 
- It will take a non-trivial amount of time during the first boot up to install the necessary embeddings libraries as well as the model dependencies, but every subsequent running should be quite responsive.
- P.S: The constants.py file referenced in the main code simply contains my OpenAI API key as well as a default directory to store the uploaded statements. These are required to run the main code file.
