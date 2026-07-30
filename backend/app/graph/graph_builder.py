from langgraph.graph import StateGraph, END

from app.graph.state import GraphState
from app.graph.planner import planner

graph = StateGraph(GraphState)

graph.add_node(
    "planner",
    planner.classify
)

graph.set_entry_point("planner")

workflow = graph.compile()

graph.add_conditional_edges(
    "planner",
    route_function,
    {
        "document_qa": "document_node",
        "general_chat": "general_chat_node",
        "summary": "summary_node",
        "comparison": "comparison_node"
    }
)