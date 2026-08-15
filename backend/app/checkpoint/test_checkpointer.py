from app.checkpoint.checkpointer import checkpointer

thread_id = "checkpoint-demo-001"

config = {
    "configurable": {
        "thread_id": thread_id
    }
}

print("checkpointer:", checkpointer)
print("Thread Id:", thread_id)

checkpoint = checkpointer.get(config)

print("checkpoint:")
print(checkpoint)