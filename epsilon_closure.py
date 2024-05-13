# epsilon_closure.py

def epsilon_closure(transitions, state):
    closure = set()
    stack = [state]

    while stack:
        current = stack.pop()
        if current not in closure:
            closure.add(current)
            # Check if current state has epsilon transitions
            for transition in transitions:
                if transition.startswith(f"{current}, EPS"):
                    target_state = transition.split('=')[1].strip()
                    if target_state not in closure:
                        stack.append(target_state)

    return closure
