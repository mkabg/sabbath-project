mission_list = ["קניית חלה", "בישול חמין", "הדלקת נרות", "סידור שולחן", "כיבוי טלפון"]

# part 1
def numbering(lst):
    for index, mission in enumerate(lst):
        print(f"{index} {mission}")

# part 2
def add_status(lst):
    status = []
    for index, mission in enumerate(lst):
        status.append([index, mission, "not done"])
    return status

def update_status(num, lst):
    for status in lst:
        if status[0] == num:
            status[2] = "done"
            print(status)
            return
    print("mission not found")

# part 3
def add_mission(mission, lst):
    lst.append(mission)
    return lst

def del_mission(num, lst):
    for mission in lst:
        if mission[0] == num:
            lst.remove(mission)
            return lst
    print("mission not found")
    return None

status = add_status(mission_list)
# numbering(mission_list)
# print(status)
# update_status(2, status)
# print(mission_list)
# print(add_mission("k", mission_list))
# print(del_mission(2, status))

