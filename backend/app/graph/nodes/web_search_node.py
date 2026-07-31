from app.graph.state import GraphState
from app.tools.web_search import web_search_tool
from app.ai.llm import llm

class WebsearchNode:
    
    def execute(
            self,
            state: GraphState
    ) -> GraphState:
        
        search_results = web_search_tool.search(
            state["question"]
        )

        prompt = f"""
You are Atlas AI.

Use the following search results to answer the user's question.

Search Results:

{search_results}

Question:

{state["question"]}
"""
        answer = llm.generate_response(prompt)

        state["answer"] = answer
        state["sources"] = [search_results]
        state["evaluation"] = {}

        return state
    
web_search_node = WebsearchNode()