def run(data):
    urls = data.get("urls", [])
    domains = [u.split("//")[-1].split("/")[0] for u in urls]
    return {"domains": domains}
