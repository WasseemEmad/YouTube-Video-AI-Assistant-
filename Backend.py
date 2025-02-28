from fastapi import FastAPI
from pydantic import BaseModel
import youtube_extract 
from llm_model import MODEL2_ID, LLM_model, Summarize, initialize_search_agent, ask_agent,clean_summary


app = FastAPI()


class Video_link(BaseModel):

    link: str
    

class VideoQARequest(BaseModel):
    link: str
    question: str
    

llm_questions = LLM_model(MODEL2_ID, temperature=0.5)
agent = initialize_search_agent(llm_questions)

@app.post("/summary")
async def chatbot_response(data: Video_link):
    try:
        transcript = youtube_extract.get_youtube_transcript(data.link)
        summary = Summarize(llm_questions,transcript)
        cleaned_summary = clean_summary(summary)
        print("✅ SUMMARY RESPONSE:", repr(cleaned_summary))
        
        return {"summary": cleaned_summary}
    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"bot_response": "Oops! Something went wrong. Try again."}
    

@app.post("/questions")
async def chatbot_response(data: VideoQARequest):
    try:
        transcript = youtube_extract.get_youtube_transcript(data.link)
        response = ask_agent(agent, transcript, data.question)
        return {"bot_response": response}
    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"bot_response": "Oops! Something went wrong. Try again."}
    
    
