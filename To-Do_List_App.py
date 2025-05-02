import tkinter as tk
from tkinter import font

# Create the main window
window = tk.Tk()
window.title("To-Do List with Checkboxes")
window.geometry("500x500")

# Font for completed tasks
strike_font = font.Font(family='Arial', size=14, slant='italic', overstrike=1)
normal_font = font.Font(family='Arial', size=14)

# Container for tasks
task_frame = tk.Frame(window)
task_frame.pack(pady=20)

# Store task references
tasks = []

def add_task():
    task_text = entry.get()
    if task_text != "":
        var = tk.IntVar()
        # Create task frame
        frame = tk.Frame(task_frame)
        frame.pack(anchor='w')

        # Create checkbox and label
        cb = tk.Checkbutton(frame, variable=var)
        cb.pack(side='left')
        lbl = tk.Label(frame, text=task_text, font=normal_font)
        lbl.pack(side='left', padx=10)

        # Save task details
        tasks.append({'var': var, 'label': lbl})
        entry.delete(0, tk.END)

def mark_completed():
    for task in tasks:
        if task['var'].get():
            task['label'].config(font=strike_font)

def remove_completed():
    for task in tasks[:]:
        if task['var'].get():
            task['label'].master.destroy()  # Remove task frame from GUI
            tasks.remove(task)  # Remove from list

# Entry for input
entry = tk.Entry(window, width=30, font=('Arial', 14))
entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(window, text="Add Task", font=('Arial', 12), command=add_task)
add_button.pack(pady=5)

# Mark Completed Button
complete_button = tk.Button(window, text="Mark Completed", font=('Arial', 12), command=mark_completed)
complete_button.pack(pady=5)

# Optional: Remove Completed Tasks
remove_button = tk.Button(window, text="Remove Completed", font=('Arial', 12), command=remove_completed)
remove_button.pack(pady=5)

# Run the app
window.mainloop()
