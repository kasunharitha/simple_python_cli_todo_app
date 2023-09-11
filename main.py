today_todo = []
tomorrow_todo = []

state = True

while state:
    when = input("Enter when the activity is due: ")
    if when == "-1":
        break
    else:
        if when == 'today':
            activity = input("Enter activity: ")
            today_todo.append(activity)
            print(today_todo)
        elif when == 'tomorrow':
            activity = input("Enter activity: ")
            tomorrow_todo.append(activity)
            print(tomorrow_todo)


