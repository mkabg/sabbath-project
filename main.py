# main.py

from checklist import *
from storage import save_to_file, load_from_file

default_missions = ["קניית חלה", "בישול חמין", "הדלקת נרות", "סידור שולחן", "כיבוי טלפון"]

missions = load_from_file()
if missions is None:
    missions = add_status(default_missions)

while True:
    print("\n===== Shabbat Checklist =====")
    print_missions(missions)
    print("\nבחר פעולה:")
    print("1. סמן משימה כבוצעה")
    print("2. הוסף משימה")
    print("3. מחק משימה")
    print("4. שמור ויצא")

    choice = input(">> ")

    if choice == "1":
        num = int(input("מספר המשימה לסימון: "))
        update_status(num, missions)
    elif choice == "2":
        desc = input("תיאור משימה חדשה: ")
        add_mission(desc, missions)
    elif choice == "3":
        num = int(input("מספר משימה למחיקה: "))
        del_mission(num, missions)
    elif choice == "4":
        save_to_file(missions)
        print("הרשימה נשמרה. שבת שלום!")
        break
    else:
        print("בחירה לא חוקית.")
