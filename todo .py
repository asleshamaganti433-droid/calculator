import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        save_tasks()
        print(f"Task '{removed}' deleted successfully!")
    except:
        print("Invalid task number!")

def mark_completed():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark completed: "))
        tasks[task_no - 1] += " ✔"
        save_tasks()
        print("Task marked as completed!")
    except:
        print("Invalid task number!")

def main():
    load_tasks()
    
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def mark_completed():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(selected, task + " ✔")
    except:
        messagebox.showwarning("Warning", "Please select a task!")

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

complete_btn = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_btn.pack()

root.mainloop()
