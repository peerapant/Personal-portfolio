student_names = []
menu = 0
for i in range (3):
    name = input(f"Enter Student Name #{i+1} : ")
    student_names.append(name)
#Loop จนกว่าจะ exit
while menu != 5:

    print("\nEnter operator you want to do")
    print("1.Search student name Enter")
    print("2.Remove student name Enter")
    print("3.Sort student name Enter")
    print("4.Count number of student Enter")
    print("5.Exit")
    menu = int(input("Please Enter number you want to do :"))
    print("")

    match menu:
        case 1:
#ค้นหาชื่อนักเรียน
            search_name = input("Enter student name's you want to find :")
            if search_name in student_names:
                print(f"Found {search_name} at position {student_names.index(search_name)+1}") 
            else:
                print(f"Student {search_name} not found in system.")

        case 2:
#ลบชื่อนักเรียนออก 
            remove_student = input("Who you want to delete from list : ")
            if remove_student in student_names:
                student_names.remove(remove_student)
                print(f"Removed {remove_student}")
            else:
                print(f"Not found {remove_student} in system.")
        case 3:
#เรียงลำดับนักเรียน
            student_names.sort
            print(f"Sorted list : {student_names}")

        case 4:
            print(f"Total number of student is {len(student_names)}")
