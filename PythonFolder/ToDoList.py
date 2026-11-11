print("loaded")




List = []


while True:
    print("    TO DO LIST   ")
    print("--------------------")
    print("1: Add a task")
    print("2: Show all tasks")
    print("3: Remove a task")
    print("4: Exit")
    ans = int(input("Choose an option"))
    if ans == 1:
        task = str(input("Add the name of a task."))
        List.append(task)
    elif ans == 2:
        '''Num = 1
        for i in List:
            print(f"{Num}:{i}")
            Num += 1'''
        for i in range(len(List)):
            print(i+1," ",List[i])

    elif ans == 3:
        numRemove = int(input("Enter the serial number of task you want to remove. (Starts from 0)"))
        List.pop(numRemove-1)
    else:
        break




        
