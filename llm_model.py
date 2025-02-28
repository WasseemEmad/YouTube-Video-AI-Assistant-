import requests
from langchain.llms import HuggingFaceEndpoint
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
import os
import re

API_KEY = ""
MODEL2_ID = "mistralai/Mistral-7B-Instruct"
os.environ['HUGGINGFACEHUB_API_TOKEN'] = API_KEY

import re

def clean_summary(summary: str) -> str:
    """Cleans and properly formats the summary."""
    summary = summary.strip()  # Remove leading/trailing spaces/newlines
    summary = re.sub(r"\*\*(.*?)\*\*", r"\1", summary)  # Remove **bold**
    summary = summary.replace("\n - ", "\n• ")  # Format bullet points
    return summary

def LLM_model(MODEL_ID, temperature=0.7):
    llm = HuggingFaceEndpoint(
        repo_id=MODEL_ID,
        temperature=temperature,
        task="text-generation" 
        )
    return llm

def Summarize(llm,content):
    prompt = f"""
    **Task:** Summarize the transcript while preserving its key meaning and emotions.

    **Instructions:**
    1. The summary should be significantly shorter than the transcript (around 40-50% of the original length).
    2. Retain key themes, emotions, and significant metaphors (e.g., supernatural elements, love-related imagery).
    3. Ensure the summary is coherent, well-structured, and naturally flowing.
    4. Avoid unnecessary repetition or over-explaining.
    

    **Transcript:**

    {content}
    """

    # Create the model instance with explicit task specification
    llm = llm

    # Generate response
    response = llm.invoke(prompt)
    response = response.replace("\\n", "\n")   
    return response

def initialize_search_agent(llm):
    search_tool = DuckDuckGoSearchRun()
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent

def ask_agent(agent,transcript, question):
    input_text = f"""
    You are an AI assistant that answers questions **ONLY** based on the provided transcript.
    If the transcript does not contain enough information, search the internet

    **Transcript:**
    {transcript}

    **Question:** {question}

    **Answer:**
    """
    agent = agent
    # Run the agent with the formatted input
    response = agent.invoke({"input": input_text})

    # Extract response
    output = response.get("output", "").strip()

    # Prevent empty or hallucinated responses
    if not output or "is it is it" in output.lower():
        return "I don't know."

    return output

