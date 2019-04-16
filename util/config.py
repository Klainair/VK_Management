def get_config(path="config.json"):
    data = None
    with open(path, 'r') as f:
        data = json.loads(f.read())
    return data
