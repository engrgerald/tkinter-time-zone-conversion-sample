
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Function to convert time based on the time difference
def convert_time():
    try:
        # Get user inputs
        input_time_str = entry_time.get()
        input_city = entry_city.get()

        # Parse the input time
        input_time = datetime.strptime(input_time_str, "%H:%M")

        # Calculate the time difference
        time_difference = time_difference_dict[input_city]

        # Convert the time
        converted_time = input_time + timedelta(hours=time_difference)

        # Display the result
        result_var.set(f"Time in {input_city}: {converted_time.strftime('%H:%M')}")
    except ValueError:
        result_var.set("Invalid time format. Please use HH:MM")

# Create the main Tkinter window
window = tk.Tk()
window.title("Time Zone Converter")

# Time difference dictionary (adjust these values based on the actual time differences)
time_difference_dict = {"New York": -5, "London": 0, "Tokyo": 9}

# Label and Entry for input time
label_time = ttk.Label(window, text="Enter Time (HH:MM):")
label_time.grid(row=0, column=0, padx=10, pady=10)
entry_time = ttk.Entry(window)
entry_time.grid(row=0, column=1, padx=10, pady=10)

# Label and Entry for input city
label_city = ttk.Label(window, text="Select City:")
label_city.grid(row=1, column=0, padx=10, pady=10)
entry_city = tk.StringVar()
city_options = list(time_difference_dict.keys())
entry_city.set(city_options[0])  # Default value
dropdown_city = ttk.Combobox(window, textvariable=entry_city, values=city_options)
dropdown_city.grid(row=1, column=1, padx=10, pady=10)

# Button to trigger time conversion
convert_button = ttk.Button(window, text="Convert Time", command=convert_time)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the result
result_var = tk.StringVar()
result_label = ttk.Label(window, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
```

