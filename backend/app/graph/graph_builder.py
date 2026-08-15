from langgraph.graph import StateGraph, END

from app.graph.state import GraphState
from app.graph.planner import planner
from app.graph.nodes.document_node import document_node
from app.graph.nodes.general_chat_node import general_chat_node
from app.graph.nodes.summary_node import summary_node
from app.graph.nodes.web_search_node import web_search_node
from app.graph.nodes.comparison_node import comparison_node
from langgraph.checkpoint.memory import MemorySaver
from app.checkpoint.checkpointer import checkpointer
from app.graph.nodes.approval_node import approval_node
from app.graph.nodes.intent_node import intent_router

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

graph.add_node(
    "summary_node",
    summary_node.execute
)

graph.add_node(
    "web_search_node",
    web_search_node.execute
)

graph.add_node(
    "comparison_node",
    comparison_node.execute
)

graph.add_node(
    "approval_node",
    approval_node.execute
)

graph.add_node(
    "intent_router",
    intent_router.execute
)

def route_function(
        state: GraphState
):
    return state["intent"]

def approval_route(state: GraphState):

    if state["approved"]:
        return "approved"

    return "rejected"

graph.set_entry_point("planner")

graph.add_conditional_edges(
    "approval_node",
    approval_route,
    {
        "approved": "intent_router",
        "rejected": END
    }
)



graph.add_conditional_edges(
    "intent_router",
    route_function,
    {
        "document_qa": "document_node",
        "general_chat": "general_chat_node",
        "summary": "summary_node",
        "web_search": "web_search_node",
        "comparison": "comparison_node"
    }
)

graph.add_edge(
    "planner",
    "approval_node"
)

graph.add_edge(
    "approval_node",
    END
)

graph.add_edge(
    "document_node",
    END
)

graph.add_edge(
    "general_chat_node",
    END
)

graph.add_edge(
    "summary_node",
    END
)

graph.add_edge(
    "web_search_node",
    END
)

graph.add_edge(
    "comparison_node",
    END
)

memory = MemorySaver()

workflow = graph.compile(
    checkpointer=checkpointer
)