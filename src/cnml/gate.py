class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if not body.get("spot"): failed.append("need_spot")
    if not body.get("scale_to_zero"): failed.append("need_scale_to_zero")
    return {"passed": not failed, "failed": failed, "applied": False}
