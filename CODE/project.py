subjects = int(input("How many subjects do you have? "))

data = []

for i in range(subjects):
    print("\nSubject", i+1)
    
    n = input("Enter subject name: ")
    t = int(input("Enter total classes: "))
    a = int(input("Enter attended classes: "))
    
    data.append([n, t, a])

print("\nAttendance Report")

for item in data:
    n = item[0]
    t = item[1]
    a= item[2]
    
    percent = (a/ t) * 100
    
    print("\nSubject:", n)
    print("Attendance:", round(percent, 2), "%")
    
    if percent >= 75:
        bunk = 0
        t = t
        a = a
        while True:
            if (a / (t + 1)) * 100 >= 75:
                t = t + 1
                bunk = bunk + 1
            else:
                break
        
        print("Status: Safe")
        print("You can miss", bunk, "classes")
    
    else:
        need = 0
        t = t
        a = a
        
        while True:
            if (a / t) * 100 < 75:
                t = t + 1
                a = a + 1
                need = need + 1
            else:
                break
        
        print("Status: Low attendance")
        print("Attend next", need, "classes to reach 75%")