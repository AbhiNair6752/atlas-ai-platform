from app.graph.planner import planner

state ={
    "session_id": "test_session",
    "question": "Please summarize the uploaded HR policy document",
    "intent": "",
    "answer": "",
    "sources": [],
    "evaluation": {}
}
result = planner.classify(state)

print("Planner Result:")
print(result)

print("\nDetected Intent:")
print(result["intent"])