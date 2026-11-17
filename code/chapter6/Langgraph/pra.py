from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages

class SearchState(TypedDict):
    messages: Annotated[list,add_messages]
    user_query: str 