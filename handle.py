def handle_action(action):
    valid_actions = ["move", "stop"]

    if action not in valid_actions:
        return {
            "error": "Invalid action",
            "action": action
        }

    return {
        "success": True,
        "action": action
    }


print(handle_action("jump"))