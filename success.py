def check_result(success):
    state = {
        "done": False,
        "stops": False
    }

    if success:
        state["done"] = True
        state["stops"] = True

        return {
            "status": "success",
            "state": state
        }

    else:
        state["stops"] = True

        return {
            "status": "failure",
            "state": state
        }


print(check_result(True))
print(check_result(False))