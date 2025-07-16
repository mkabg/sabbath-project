def add_status(lst):
    status = []
    for index, mission in enumerate(lst):
        status.append([index, mission, "not done"])
    return status

def update_status(num, lst):
    for status in lst:
        if status[0] == num:
            status[2] = "done"
            print(f"Updated: {status}")
            return
    print("mission not found")

def add_mission(mission, lst):
    new_id = max([m[0] for m in lst]) + 1 if lst else 0
    lst.append([new_id, mission, "not done"])
    return lst

def del_mission(num, lst):
    for mission in lst:
        if mission[0] == num:
            lst.remove(mission)
            return lst
    print("mission not found")
    return lst

def print_missions(lst):
    for mission in lst:
        status_symbol = "✔" if mission[2] == "done" else "✘"
        print(f"{mission[0]}. {mission[1]} [{status_symbol}]")
