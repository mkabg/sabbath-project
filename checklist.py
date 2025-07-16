missiolist = ["קניית חלה", "בישול חמין", "הדלקת נרות", "סידור שולחן", "כיבוי טלפון"]
def numbering(list):
    for index, mission in enumerate(list):
        print(f"{index} {mission}")

numbering(missiolist)