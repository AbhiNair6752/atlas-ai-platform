from langgraph.types import Command

from app.graph.graph_builder import workflow

thread_id = "approval-test-002"

config = {
    "configurable": {
        "thread_id": thread_id
    }
}

result = workflow.invoke(
    Command(
        resume=True
    ),
    config = config
)

print("Resumed Result:")
print(result)