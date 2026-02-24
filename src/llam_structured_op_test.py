from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Initialize Ollama model
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


# System behavior instructions
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """You are a biomedical research agent.

You must use tools when necessary.

Rules:
- If disease ID is unknown, call resolve_disease.
- If user asks for drugs and disease ID is known, call fetch_known_drugs.
- Never invent ontology IDs.
- Do not hallucinate.
"""),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

chain = prompt | llm
print(chain.invoke({"input": "I am interested in breast cancer related drugs."}))
