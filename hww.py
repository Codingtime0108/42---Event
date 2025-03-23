#convert cm to metre
import tkinter as tk

def centimeter_to_meter():
    centimeter = ent_measurement.get()
    meter = (float(centimeter)/100)
    lbl_results["text"] = f"{round(meter, 2)}"

window = tk.Tk()
window.title("Measurement Converter")
window.geometry("400x400")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_measurement = tk.Entry(master=frm_entry, width=10)
lbl_measure = tk.Label(master=frm_entry, text=" ")

ent_measurement.grid(row=0, column=0, sticky="e") 
lbl_measure.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
    master=window,
    text="-->",
    command=centimeter_to_meter
)
lbl_results = tk.Label(master=window, text=" ")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_results.grid(row=0, column=2, padx=10)

window.mainloop()