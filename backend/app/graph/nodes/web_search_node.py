from app.graph.state import GraphState
from app.tools.web_search import web_search_tool
from app.ai.llm import llm
from app.ai.gateway.llm_gateway import llm_gateway
from app.ai.gateway.llm_task import LLMTask

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
        answer = llm_gateway.generate_response(prompt,
                                               task=LLMTask.WEB_SEARCH)

        state["answer"] = answer
        state["sources"] = [search_results]
        state["evaluation"] = {}

        return state
    
web_search_node = WebsearchNode()