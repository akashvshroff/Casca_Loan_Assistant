# Overview

- My solution for the coding challenge relies on a RAG, or retrieval-augmented generation based approach that analyzes the given bank statement to give an initial prognosis and allows me to dig deeper into the statement using natural language in a chat-based method.
- The benefit of using an LLM-based approach is in its understanding of obscure statement details and ability to reason through potential trends in the transactions. Moreover, instead of getting a concrete answer from the model, I instead tried to implement a human-in-the-loop system where it points to key findings from the statement but decision-making rests with a human. In such a system, the LLM is meant to augment human capabilities and increase efficiency by keenly identifying glaring red-flags.
- I leveraged GPT-4 for its reasoning capabilities and versatility and used a vector store devised using the PyMuPDF OCR and an embeddings model from HuggingFace to build the system. The minimal frontend is built using an incredibly lightweight Python library called streamlit.
- A sped-up demo of my solution (where it analyzes [statement4](https://github.com/akashvshroff/Casca_Loan_Assistant/blob/main/statements/statement4.pdf)) can be seen through the video below.

  https://github.com/akashvshroff/Casca_Loan_Assistant/assets/63399889/4a0460ba-9519-4373-b1f8-f8ab7f466b54

- This solution is meant to represent the MVP of the LLM RAG approach - however, there are some clear avenues for improvement. The lowest hanging fruit is to improve the prompting to the LLM itself. Next, we could look at increasing RAG efficiency by using some cache solution or trying to extract relevant parts of the document. To improve reasoning, we could fine-tune a base-model on a Chain-of-Thought financial data regarding loans. Finally, a more cosmetic improvement could seek to use a multi-modal LLM through which we return an annotated version of the bank statement wherein we mark out transactions that are concerning and attach some summary analysis.

## Installation & Running
- You can use the requirements.txt file to pip install all packages that are needed to run the file and then run `streamlit run main.py` to get the frontend up and running. 
- It will take a non-trivial amount of time during the first boot up to install the necessary embeddings libraries as well as the model dependencies, but every subsequent running should be quite responsive.
- P.S: The constants.py file referenced in the main code simply contains my OpenAI API key as well as a default directory to store the uploaded statements. These are required to run the main code file.
