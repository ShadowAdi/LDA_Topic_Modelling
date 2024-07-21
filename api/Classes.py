from pydantic import BaseModel,Field

class ResearchArticles(BaseModel):
  text:str
  minimumProbability:float = Field(..., ge=0.01, lt=0.90)

  
class NewsArticles(BaseModel):
  text:str
  minimumProbability:float = Field(..., ge=0.01, lt=0.90)