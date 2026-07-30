from langgraph.graph import StateGraph, END

from app.graph.state import GraphState
from app.graph.planner import planner
from app.graph.nodes.document_node import document_node
from app.graph.nodes.general_chat_node import general_chat_node

graph = StateGraph(GraphState)

graph.add_node(
    "planner",
    planner.classify
)

graph.add_node(
    "document_node",
    document_node.execute
)
graph.add_node(
    "general_chat_node",
    general_chat_node.execute
)

def route_function(
        state: GraphState
):
    return state["intent"]

graph.set_entry_point("planner")



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

graph.add_edge(
    "document_node",
    END
)

graph.add_edge(
    "general_chat_node",
    END
)

workflow = graph.compile()