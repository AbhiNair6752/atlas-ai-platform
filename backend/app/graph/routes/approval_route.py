def approval_route(state):

    if state["approved"]:
        return "approved"
    
    return "rejected"