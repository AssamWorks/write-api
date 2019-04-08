def btech(args):
    username = args('username')
    return {"msg": username }

def mtech():
    return {"success": True}

API_mappings = {"btech": btech, "mtech": mtech}
