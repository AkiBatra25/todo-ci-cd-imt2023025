# app.py
# Simple To-Do CLI

tasks = []  # list of task strings


def add_task(title: str) -> str:
    title = title.strip()
    if title == "":
        return "Task cannot be empty."
    tasks.append(title)
    return f"Task added: {title}"


def list_tasks() -> str:
    if not tasks:
        return "No tasks available."
    lines = []
    for i, t in enumerate(tasks, start=1):
        lines.append(f"{i}. {t}")
    return "\n".join(lines)


def remove_task(index: int) -> str:
    if index < 1 or index > len(tasks):
        return "Invalid task number."
    removed = tasks.pop(index - 1)
    return f"Task removed: {removed}"


def main():
    print("=== To-Do CLI (IMT2023025) ===")
    while True:
        print("\nChoose option:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter task: ")
            print(add_task(title))
        elif choice == "2":
            print(list_tasks())
        elif choice == "3":
            try:
                idx = int(input("Enter task number to remove: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            print(remove_task(idx))
        elif choice == "4":
            print("Bye from IMT2023025!")
            break
        else:
            print("Invalid choice.")
            

if __name__ == "__main__":
    main()
