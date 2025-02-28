# YouTube Video AI Assistant

This project is an AI-powered assistant that extracts YouTube video transcripts, summarizes them, and answers questions based on the transcript or web search. It leverages advanced language models and search agents to provide meaningful and accurate responses.

## How It Works

1. **Extracting Transcripts:** The application extracts the transcript from a given YouTube video using the youtube-transcript-api.

2. **Summarization:** The transcript is summarized using a large language model (LLM) hosted on Hugging Face.

3. **Answering Questions:** Users can ask questions about the video content.
                            3.1. If the answer is found in the transcript, the system retrieves it.
                            3.2. If not, the AI-powered search agent queries the web for additional information.
                            
4. **Agents and LangChain:** The application utilizes LangChain's initialize_agent function to create an intelligent agent that decides when to rely on the transcript and when to search the web using DuckDuckGo.

## Features

✅ Extracts transcripts from YouTube videos.

✅ Summarizes transcripts using an LLM model.

✅ Answers user questions based on the transcript.

✅ Uses a search agent if the transcript lacks information.

✅ Frontend built with Streamlit.

✅ Backend powered by FastAPI.


## Technologies Used

✅ **Agents** - Intelligent AI-powered reasoning and decision-making using LangChain

✅ **Python**

✅ **FastAPI** - Backend API framework

✅ **Streamlit** - Frontend UI

✅ **LangChain** - LLM integration

✅ **Mistral-7B-Instruct** - Hugging Face LLM

✅ **DuckDuckGo Search** - Web search tool

✅ **YouTube Transcript API** - Extracting transcripts from YouTube

## API Endpoints

### POST /summary
Extracts the transcript from the YouTube video and summarizes it.

**Request Body:**
{
  "link": "https://www.youtube.com/watch?v=your_video_id"
}

**Response:**
{
  "summary": "Summarized text here..."
}

### POST /questions
Answers user questions based on the video transcript or web search.

**Request Body:**
{
  "link": "https://www.youtube.com/watch?v=your_video_id",
  "question": "What is the main topic of the video?"
}

**Response:**
{
  "bot_response": "Answer based on transcript or search."
}

## Future Improvements

Improve response accuracy by using better LLMs.

Add support for multiple LLM backends.

Implement a more interactive UI.

### Example:

https://github.com/user-attachments/assets/b657fcc4-965e-44e8-b414-443901e7fa06


