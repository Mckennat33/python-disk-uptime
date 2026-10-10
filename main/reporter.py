import psutil 
import datetime
import tkinter as tk

root = tk.Tk()
root.title("Disk / Uptime Monitor")
lb = tk.Listbox(root)
cpu_time = psutil.cpu_times().idle // 3600

boot = datetime.datetime.fromtimestamp(psutil.boot_time())
uptime = datetime.datetime.now() - boot

lb.insert(1, "CPU Time", cpu_time)
lb.insert(2, f"Booted at: {boot:%Y-%m-%d %H:%M}")
lb.insert(3, f"Uptime: {uptime}")
lb.pack()
root.mainloop()

    