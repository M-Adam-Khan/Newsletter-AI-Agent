from typing import TypedDict, Optional

class AppState(TypedDict):
    topic: str
    research: Optional[str]
    newsletter: Optional[str]