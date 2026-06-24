# ==========================================
# Task 1: To-Do List GUI Application
# Developed for CodSoft Internship Program
# ==========================================

import tkinter as tk
from tkinter import messagebox

# Core Application Logic
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        
        # Color Palette matching image_3.png
        self.bg_color = "#6baed6"       # Light blue background
        self.btn_color = "#fca311"      # Yellow/Orange button color
        self.btn_text_color = "black"
        
        self.root.config(bg=self.bg_color)
        
        # Internal list to track tasks
        self.tasks = []
        
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(
            self.root, text="TO-DO LIST", 
            font=("Arial", 16, "bold"), bg=self.bg_color, fg="#d95d00"
        )
        title_label.pack(pady=(15, 2))

        # Subtitle Label
        sub_label = tk.Label(
            self.root, text="Enter the Task Title:", 
            font=("Arial", 11, "bold"), bg=self.bg_color, fg="#b85c00"
        )
        sub_label.pack(pady=(0, 5))

        # Task Entry Field
        self.task_field = tk.Entry(
            self.root, font=("Arial", 12), width=38, bd=1, relief="solid"
        )
        self.task_field.pack(pady=5)
        self.task_field.focus()

        # Button Frame (For Add, Remove, Delete All layout)
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(pady=10)

        # 1. Add Button
        add_btn = tk.Button(
            btn_frame, text="Add", font=("Arial", 10, "bold"), 
            bg=self.btn_color, fg=self.btn_text_color, width=11, 
            command=self.add_task, relief="groove", bd=2
        )
        add_btn.grid(row=0, column=0, padx=5)

        # 2. Remove Button
        remove_btn = tk.Button(
            btn_frame, text="Remove", font=("Arial", 10, "bold"), 
            bg=self.btn_color, fg=self.btn_text_color, width=11, 
            command=self.remove_task, relief="groove", bd=2
        )
        remove_btn.grid(row=0, column=1, padx=5)

        # 3. Delete All Button
        delete_all_btn = tk.Button(
            btn_frame, text="Delete All", font=("Arial", 10, "bold"), 
            bg=self.btn_color, fg=self.btn_text_color, width=11, 
            command=self.clear_all, relief="groove", bd=2
        )
        delete_all_btn.grid(row=0, column=2, padx=5)

        # Tasks Listbox Box
        self.task_listbox = tk.Listbox(
            self.root, font=("Arial", 11), width=38, height=10, 
            selectbackground="#a8dadc", selectforeground="black",
            bd=1, relief="solid"
        )
        self.task_listbox.pack(pady=10)

        # 4. Exit / Close Button (At the bottom)
        exit_btn = tk.Button(
            self.root, text="Exit / Close", font=("Arial", 11, "bold"), 
            bg=self.btn_color, fg=self.btn_text_color, width=34, 
            command=self.root.destroy, relief="groove", bd=2
        )
        exit_btn.pack(pady=(5, 15))

    # --- Button Functionalities ---
    
    def add_task(self):
        task_string = self.task_field.get().strip()
        if len(task_string) == 0:
            messagebox.showinfo("Error", "Field is Empty.")
        else:
            self.tasks.append(task_string)
            self.update_listbox()
            self.task_field.delete(0, tk.END)

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_all(self):
        if self.tasks:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete all tasks?")
            if confirm:
                self.tasks.clear()
                self.update_listbox()
        else:
            messagebox.showinfo("Notification", "The list is already empty.")

    def update_listbox(self):
        # Clear current view
        self.task_listbox.delete(0, tk.END)
        # Re-populate from internal storage
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f" {task}")

# Driver Code
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()