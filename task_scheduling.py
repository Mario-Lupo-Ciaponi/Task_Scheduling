def is_queue_empty(tasks_queue):
    if tasks_queue:
        return False

    return True


def add_tasks(tasks_queue, task):
    tasks_queue.append(task)

    print(f"'{task}' added successfully!")

    return tasks_queue


def remove_task(tasks_queue):
    removed_task = tasks_queue.pop(0)

    print(f"'{removed_task}' removed successfully!")

    return tasks_queue


def most_important_task_in_schedule(task_queue):
    return task_queue[0]


def least_important_task_in_schedule(task_queue):
    return task_queue[-1]


def show_task_schedule(task_queue):
    print("\nTasks:")

    for number in range(1, len(task_queue) + 1):
        if number == 1:
            print(f"{number} - {task_queue[number - 1]} (most important task)")
        elif number == len(task_queue):
            print(f"{number} - {task_queue[number - 1]} (least important task)")
        else:
            print(f"{number} - {task_queue[number - 1]}")


def show_operations():
    print("\n/---Task Operations---\\")
    print("\t1) Add task\n\t2) Mark Task as completed\n\t3) Show the most important task"
          "\n\t4) Show the least important task\n\t5) Show Task Schedule\n\t6) Quit\n")


def task_manipulation(task_queue):
    print("Welcome to the Task Scheduling!")

    while True:
        show_operations()
        option = int(input("Chose the number of the operation that you would like to do: "))

        if option == 1:
            task_to_add = input("Task: ")

            task_queue = add_tasks(task_queue, task_to_add)
        elif option == 2:
            if not is_queue_empty(task_queue):
                task_queue = remove_task(task_queue)
            else:
                print("Task schedule is empty!")
        elif option == 3:
            if len(task_queue) == 1:
                print(f"\nYou have only one task. Task: {task_queue[0]}")
            elif len(task_queue) == 0:
                print("\nNo tasks!")
            else:
                most_important_task = most_important_task_in_schedule(task_queue)

                print(f"Most important task: {most_important_task}")
        elif option == 4:
            if len(task_queue) == 1:
                print(f"You have only one task. Task: {task_queue[0]}")
            elif len(task_queue) == 0:
                print("\nNo tasks!")
            else:
                least_important_task = least_important_task_in_schedule(task_queue)

                print(f"Least important task: {least_important_task}")
        elif option == 5:
            if not is_queue_empty(task_queue):
                show_task_schedule(task_queue)
            else:
                print("\nNo tasks!")
        elif option == 6:
            print("\nGoodbye! Have a wonderful day!")
            break
        else:
            print("Invalid operation!")


def main():
    task_queue = []

    task_manipulation(task_queue)


if __name__ == "__main__":
    main()
