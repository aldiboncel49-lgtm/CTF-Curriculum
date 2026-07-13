import os
def handler(event,_):
    # VULN: event data eval'd
    return eval(event["code"])
