import tkinter as tk
from tkinter import messagebox

def add_task(task_list, task_entry):
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task(task_list):
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected.")
        
def update_task(task_list, task_entry):
    try:
        index = task_list.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_list.delete(index)
            task_list.insert(index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected.")       

def clear_tasks(task_list):
    task_list.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry("560x660")
    root.config(bg="snow")
    root.title("To-Do List")
    
    heading_label = tk.Label(root, text="TO-DO LIST", font=("Helvetica", 18, "bold"))
    heading_label.pack(pady=30)
    
    task_entry = tk.Entry(root, font=("Helvetica", 12), bg="bisque1" , width=50)
    task_entry.pack(pady=20)

    task_list = tk.Listbox(root, font=("Helvetica", 12), bg="light blue" , width=50, height=10)
    task_list.pack(pady=10)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    add_btn = tk.Button(buttons_frame, text="Add Task", bg="MistyRose2" , command=lambda: add_task(task_list, task_entry))
    add_btn.pack(side=tk.LEFT, padx=5)
    
    update_btn = tk.Button(buttons_frame, text="Update Task", bg="wheat" , command=lambda: update_task(task_list, task_entry))
    update_btn.pack(side=tk.LEFT, padx=5)

    delete_btn = tk.Button(buttons_frame, text="Delete Task", bg="light coral" , command=lambda: delete_task(task_list))
    delete_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = tk.Button(buttons_frame, text="Clear All", bg="gray56" , command=lambda: clear_tasks(task_list))
    clear_btn.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == '__main__':
    main()
