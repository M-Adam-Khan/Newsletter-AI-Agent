from pydantic import BaseModel

class NewsletterRequest(BaseModel):
    topic: str

class NewsletterResponse(BaseModel):
    newsletter: str
    filename: str