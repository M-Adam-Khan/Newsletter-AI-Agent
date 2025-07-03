from langgraph.graph import StateGraph
from newsletter_ai.schema import AppState
from newsletter_ai.nodes import research_node, formatting_node, display_node

def build_graph():
    builder = StateGraph(AppState)
    builder.add_node("research", research_node)
    builder.add_node("format", formatting_node)
    builder.add_node("display", display_node)

    builder.set_entry_point("research")
    builder.add_edge("research", "format")
    builder.add_edge("format", "display")
    builder.set_finish_point("display")

    return builder.compile()
