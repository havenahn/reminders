import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
import time
from tktimepicker import SpinTimePickerModern, SpinTimePickerOld
from tktimepicker import constants
def show_reminder_dialog():
    reminder_input = simpledialog.askstring("Add Reminder", "Enter your reminder:")
    if reminder_input:
        top = tk.Toplevel(root)

        time_picker = SpinTimePickerModern(top)
        time_picker.addAll(constants.HOURS12)  # Show time in 12-hour format (with AM/PM)
        time_picker.configureAll(bg="#404040", height=1, fg="#ffffff", font=("Times", 16),
                             hoverbg="#404040", hovercolor="#d73333", clickedbg="#2e2d2d", clickedcolor="#d73333")
        time_picker.configure_separator(bg="#404040", fg="#ffffff")

        time_picker.pack(expand=True, fill="both")

        ok_btn = tk.Button(top, text="OK", command=lambda: updateTime(time_picker.time()))
        ok_btn.pack()

        if time_selection:
            reminder_listbox.insert(tk.END, f"{time_selection}: {reminder_input}")
            messagebox.showinfo("Reminder Added", "Reminder added successfully!")

def remove_reminder():
    selected_index = reminder_listbox.curselection()
    if selected_index:
        reminder_listbox.delete(selected_index)
        messagebox.showinfo("Reminder Removed", "Reminder removed successfully!")
    else:
        messagebox.showwarning("No Selection", "Please select a reminder to remove.")

def clear_reminders():
    reminder_listbox.delete(0, tk.END)
    messagebox.showinfo("Reminders Cleared", "All reminders cleared successfully!")

def check_reminders():
    current_time = time.strftime("%I:%M %p")
    for item in reminder_listbox.get(0, tk.END):
        time_str, reminder = item.split(": ", 1)
        if current_time == time_str:
            messagebox.showinfo("Reminder", reminder)
            break
    app.after(60000, check_reminders)  # Check every 1 minute (60000 milliseconds)

# Create the main application window
app = tk.Tk()
app.title("Reminders App")
app.geometry("400x300")

# Create the UI elements
reminder_listbox = tk.Listbox(app, width=40, height=10)
reminder_listbox.pack(pady=5)

add_button = tk.Button(app, text="Add Reminder", command=show_reminder_dialog)
add_button.pack(pady=5)

remove_button = tk.Button(app, text="Remove Reminder", command=remove_reminder)
remove_button.pack(pady=5)

clear_button = tk.Button(app, text="Clear Reminders", command=clear_reminders)
clear_button.pack(pady=5)

# Start checking for reminders
app.after(0, check_reminders)

app.mainloop()
