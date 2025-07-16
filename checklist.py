mission_list = ["קניית חלה", "בישול חמין", "הדלקת נרות", "סידור שולחן", "כיבוי טלפון"]

# part 1
def numbering(list):
    for index, mission in enumerate(list):
        print(f"{index} {mission}")

# part 2
def add_status(list):
    status = []
    for index, mission in enumerate(list):
        status.append([index, mission, "not done"])
    return status

def update_status(num, list):
    for status in list:
        if status[0] == num:
            status[2] = "done"
            print(status)
            return

# numbering(mission_list)
# print(add_status(mission_list))
update_status(2, add_status(mission_list))