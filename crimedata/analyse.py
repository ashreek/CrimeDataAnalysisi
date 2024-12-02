import pandas as pd
from tkinter import Tk, filedialog, Label, Button, Listbox, Scrollbar, END

# Function to load the CSV file
def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not filepath:
        return
    global data
    data = pd.read_csv(filepath)
    label_status.config(text=f"Loaded {len(data)} responses")
    display_data()

# Function to display the data in the listbox
def display_data():
    listbox_data.delete(0, END)
    for index, row in data.iterrows():
        listbox_data.insert(END, f"{row['Name']} ({row['Age']} {row['Gender']}) - Q1: {row['Q1']}, Q2: {row['Q2']}, Q3: {row['Q3']}")

# Function to analyze survey responses
def analyze_data():
    if data is None:
        label_status.config(text="No data loaded")
        return
    
    summary = data.describe(include="all")
    listbox_data.delete(0, END)
    listbox_data.insert(END, "Survey Analysis Summary:")
    listbox_data.insert(END, "-" * 40)
    for column in data.columns[3:]:
        listbox_data.insert(END, f"{column}:")
        listbox_data.insert(END, str(data[column].value_counts()))
        listbox_data.insert(END, "")

# Initialize the Tkinter application
root = Tk()
root.title("Mental Health Survey Analysis")

data = None

# Create GUI Elements
label_title = Label(root, text="Mental Health Survey Analyzer", font=("Arial", 16))
label_title.pack(pady=10)

btn_load = Button(root, text="Load Survey Data", command=load_file)
btn_load.pack(pady=5)

btn_analyze = Button(root, text="Analyze Data", command=analyze_data)
btn_analyze.pack(pady=5)

label_status = Label(root, text="No data loaded", fg="red")
label_status.pack(pady=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

listbox_data = Listbox(root, yscrollcommand=scrollbar.set, width=80, height=20)
listbox_data.pack(pady=10)

scrollbar.config(command=listbox_data.yview)

# Run the Tkinter event loop
root.mainloop()
