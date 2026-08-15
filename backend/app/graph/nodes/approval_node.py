from langgraph.types import interrupt

class ApprovalNode:

    def execute(
            self,
            state
    ):
        approval = interrupt(
            {
                "type": "approval_required",
                "message": "Do you want to continue with this request?",
                "question": state["question"],
                "intent": state["intent"]
            }
        )

        state["evaluation"] = {
            "approval": approval
        }

        return state
    
approval_node = ApprovalNode()