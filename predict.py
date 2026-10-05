def agent_loop():
    log = []
    step = 0

    while step < 2:
        action = "move"
        log.append(f"Step {step + 1}: {action}")
        step += 1

    return log


print(agent_loop())