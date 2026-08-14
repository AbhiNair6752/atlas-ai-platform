from app.memory.conversation_memory import conversation_memory

session_id = "test-session-001"

conversation_memory.clear_history(session_id)

conversation_memory.add_messages(
    session_id=session_id,
    role="user",
    content="What is the leave policy?"
)

conversation_memory.add_messages(
    session_id=session_id,
    role="assistant",
    content="The leave policy provides annual and sick leave.",
)

conversation_memory.add_messages(
    session_id=session_id,
    role="user",
    content="How many days of annual leave?",
)

history = conversation_memory.get_history(session_id)

print("Conversation History:")

for message in history:
    print(message)