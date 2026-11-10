import tkinter as tk

NUM_READINGS = 5          # how many readings we collect
CRITICAL_MARGIN = 10      # a reading this far above the limit is CRITICAL


def calculate_average(readings):
    """Return the average of a list, safely handling an empty list."""
    if len(readings) == 0:                        # avoid dividing by zero
        return 0
    return sum(readings) / len(readings)


def classify(reading, limit):
    """Return the status of one reading: OK, WARNING or CRITICAL."""
    if reading > limit + CRITICAL_MARGIN:
        return "CRITICAL"
    elif reading > limit:
        return "WARNING"
    else:
        return "OK"


def check_trend(readings):
    """TWIST: compare first and last readings to see where things are heading."""
    if len(readings) < 2:
        return "not enough data"
    change = readings[-1] - readings[0]
    if change > 0:
        return f"RISING (+{change:.1f} degrees)"
    elif change < 0:
        return f"FALLING ({change:.1f} degrees)"
    else:
        return "STEADY (no change)"


def read_number(entry, name):
    """Convert the text in an entry box to a float, or raise a clear error."""
    text = entry.get().strip()
    if text == "":
        raise ValueError(f"{name} is empty. Please type a number.")
    try:
        return float(text)                        # convert text to a decimal number
    except ValueError:
        raise ValueError(f"{name} must be a number, you typed '{text}'.")


def run_check():
    """Called when the Check button is clicked: read, calculate and display."""
    output.config(state="normal")
    output.delete("1.0", tk.END)                  # clear old results
    message_label.config(text="")

    try:
        # Read and validate the limit
        safe_limit = read_number(limit_entry, "Safe limit")
        if safe_limit <= 0:
            raise ValueError("Safe limit must be greater than 0.")

        # Read the 5 readings into a list
        readings = []
        for i in range(NUM_READINGS):             # loop runs 5 times
            readings.append(read_number(reading_entries[i], f"Reading {i + 1}"))
    except ValueError as error:
        # Show a friendly message instead of crashing
        message_label.config(text=error, fg="red")
        output.config(state="disabled")
        return

    # Show the statistics
    output.insert(tk.END, f"Highest : {max(readings)}\n")
    output.insert(tk.END, f"Lowest  : {min(readings)}\n")
    output.insert(tk.END, f"Average : {calculate_average(readings):.2f}\n")
    output.insert(tk.END, f"Trend   : {check_trend(readings)}\n\n")

    # Check each reading against the limit and count the alarms
    alarm_count = 0
    for number, reading in enumerate(readings, start=1):
        status = classify(reading, safe_limit)
        output.insert(tk.END, f"Reading {number}: {reading:>7.1f}  ->  {status}\n", status)
        if status != "OK":
            alarm_count += 1

    # Final summary message in the coloured label
    if alarm_count == 0:
        message_label.config(text="All readings are safe. Machine is OK.", fg="green")
    else:
        message_label.config(
            text=f"ALARM: {alarm_count} of {NUM_READINGS} readings above the limit!",
            fg="red")
    output.config(state="disabled")               # stop the user typing in results


def clear_all():
    """Empty every box so the user can start again."""
    limit_entry.delete(0, tk.END)
    for entry in reading_entries:
        entry.delete(0, tk.END)
    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.config(state="disabled")
    message_label.config(text="")


# ---------- Build the window ----------
window = tk.Tk()
window.title("Temperature Monitor and Alarm Checker")
window.resizable(False, False)

# Input area
input_frame = tk.Frame(window, padx=15, pady=10)
input_frame.pack()

tk.Label(input_frame, text="Safe limit (°C):").grid(row=0, column=0, sticky="e", pady=3)
limit_entry = tk.Entry(input_frame, width=12)
limit_entry.grid(row=0, column=1, pady=3)

reading_entries = []                              # list that stores the 5 entry boxes
for i in range(NUM_READINGS):
    tk.Label(input_frame, text=f"Reading {i + 1}:").grid(row=i + 1, column=0, sticky="e", pady=3)
    entry = tk.Entry(input_frame, width=12)
    entry.grid(row=i + 1, column=1, pady=3)
    reading_entries.append(entry)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack()
tk.Button(button_frame, text="Check", width=10, command=run_check).pack(side="left", padx=5)
tk.Button(button_frame, text="Clear", width=10, command=clear_all).pack(side="left", padx=5)

# Message line (errors and alarm summary)
message_label = tk.Label(window, text="", font=("Arial", 10, "bold"))
message_label.pack(pady=5)

# Results area with colours for each status
output = tk.Text(window, width=42, height=11, state="disabled", font=("Courier", 10))
output.pack(padx=15, pady=(0, 15))
output.tag_config("OK", foreground="green")
output.tag_config("WARNING", foreground="orange")
output.tag_config("CRITICAL", foreground="red")

window.mainloop()                                 # keep the window open
