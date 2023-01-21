class Reset:
    def __init__(self,hostel_name):
        self.hostel_name = hostel_name

    def hostel_reset_func(self):
        for num_floor in range(1,11):
            for num_room in range(21):
                if num_room//10 == 0:
                    num_room = "0"+str(num_room)
                with open(f"C:\\Users\\Utsav Garg\\Desktop\\Personal Project IP\\{self.hostel_name}\\Floor{num_floor}\\Room{num_floor}{num_room}.txt","w") as file_room:
                    pass

class Hostel:
    def __init__(self,stu_name,stu_batch,stu_building):
        self.stu_name = stu_name
        self.stu_batch = stu_batch
        self.stu_building = stu_building
    
    def hostel_allot(self):
        print(f"You have chosen {self.stu_building}")
        floor_num = input("Enter your choice of floor number(1-10): ")
        full_room_list = full_room_check(self.stu_building,floor_num)
        if len(full_room_list) == 0:
            print("All rooms have vacancy")
        else:
            print("The following rooms are not vacant:")
            print(*full_room_list)
        room_num = input("Enter Room Number(00-20): ")
        if full_room_list.count(("Room"+floor_num+room_num)) ==1:
            print("Wrong Entry Chosen")
            print("Try Again:")
            self.hostel_allot()
        else:
            room_mate_list = []
            with open(f"C:\\Users\\Utsav Garg\\Desktop\\Personal Project IP\\{self.stu_building}\\Floor{floor_num}\\Room{floor_num}{room_num}.txt","r") as file_room:
                for i in file_room:
                    room_mate_list.append(i)
            if len(room_mate_list) == 0:
                print("No one has been alloted this room")
            else:
                print(f"{room_mate_list[0]} has already booked this room, do you wish to be his roommate?")
            choice_input = input("Do you want to add in this room type in Yes/No: ")
            if choice_input == "Yes":
                with open(f"C:\\Users\\Utsav Garg\\Desktop\\Personal Project IP\\{self.stu_building}\\Floor{floor_num}\\Room{floor_num}{room_num}.txt","a") as file_room:
                    file_room.write(f"{self.stu_name}\n")
                print("You have been added to the records, the system is exiting")
                exit()
            else:
                print("Again choose the floor number for fresh start")
                self.hostel_allot()

def full_room_check(building_name,floor_num):
    full_room_list = []
    for num_room in range(21):
        if num_room//10 == 0:
            num_room = "0"+str(num_room)        
        with open(f"C:\\Users\\Utsav Garg\\Desktop\\Personal Project IP\\{building_name}\\Floor{floor_num}\\Room{floor_num}{num_room}.txt","r") as file_room:
            temp = file_room.readlines()
            if len(temp) == 2:
                full_room_list.append(f"Room{floor_num}{num_room}")
    return full_room_list

def hostel_reset():
    print("ALL, Old_Boys, Old_Boys_Extension, H1, H2")
    hostel_nam = input("Type Hostel Name: ")
    check_list_hostel = ["ALL","Old_Boys","H1","H2","Old_Boys_Extension"]
    if check_list_hostel.count(hostel_nam) == 1:
        if hostel_nam == "ALL":
            reset_hostel_var = Reset("Old_Boys")
            reset_hostel_var.hostel_reset_func()
            reset_hostel_var = Reset("H1")
            reset_hostel_var.hostel_reset_func()
            reset_hostel_var = Reset("H2")
            reset_hostel_var.hostel_reset_func()
            reset_hostel_var = Reset("Old_Boys_Extension")
            reset_hostel_var.hostel_reset_func()
        else:
            reset_hostel_var = Reset(hostel_nam)
            reset_hostel_var.hostel_reset_func()
    else:
        print("Wrong Input, Try Again")
        hostel_reset()

def batch_wrong_reset():
    student_batch = input("Enter Student Batch Year(Joining): ")
    check_stubatch_list = ["2018","2019","2020","2021"]
    if check_stubatch_list.count(student_batch) == 1:      
        if student_batch == "2018":
            print("You are in 4th year - college has alloted the Old-Boys Hostel ")
            stu_class = Hostel(student_name,student_batch,"Old_Boys")
            stu_class.hostel_allot()
        elif student_batch == "2019":
            print("You are in 3th year - college has alloted the Old-Boys Hostel and H1")
            preference_hostel_type = input("Enter Preference - Old/H1: ")
            if preference_hostel_type == "Old":
                stu_class = Hostel(student_name,student_batch,preference_hostel_type)
                stu_class.hostel_allot()
            elif preference_hostel_type == "H1":
                stu_class = Hostel(student_name,student_batch,preference_hostel_type)  
                stu_class.hostel_allot()
            else:
                print("Wrong Input, Try Again from start")
                batch_wrong_reset()
        elif student_batch == "2020":
            print("You are in 2nd year - college has alloted the H1 Boys Hostel and H2 Boys Hostel")
            preference_hostel_type = input("Enter Preference - H1/H2: ")
            if preference_hostel_type == "H2":
                stu_class = Hostel(student_name,student_batch,preference_hostel_type)
                stu_class.hostel_allot()
            elif preference_hostel_type == "H1":
                stu_class = Hostel(student_name,student_batch,preference_hostel_type)
                stu_class.hostel_allot()  
            else:
                print("Wrong Input, Try Again from start")                
                batch_wrong_reset()
        elif student_batch == "2021":
            print("You are in 1st year - college has alloted the H2 Boys Hostel")
            stu_class = Hostel(student_name,student_batch,"H2")
            stu_class.hostel_allot()
    else:
        print("Wrong Input, Try Again")
        batch_wrong_reset()

print("Welcome To IIIT-D Hostel Booking Software")
new_old_start = input("Do the software needs to be reset(Yes/No): ")
if new_old_start == "Yes":
    print("Are You Sure?")
    hostel_reset()
else:
    student_name = input("Enter Student Name: ")
    batch_wrong_reset()



"""
list_room = ["0"+str(room_num) for room_num in range(10)]
list_room.extend([room_num for room_num in range(10,21)])
print(list_room)
list_floor_room = [f"Floor{i}" for i in range(11)]
"""


