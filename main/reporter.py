import psutil 
import datetime
import tkinter as tk

import tkinter as tk

root = tk.Tk()
root.title("Disk / Uptime Monitor")
lb = tk.Listbox(root)
cpu_time = psutil.cpu_times().idle // 3600

lb.insert(1, "CPU Time", cpu_time)
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any other")
lb.pack()
root.mainloop()


print("CPU Statistics", psutil.cpu_stats().syscalls // 3600)

boot = datetime.datetime.fromtimestamp(psutil.boot_time())
uptime = datetime.datetime.now() - boot

print(f"Booted at: {boot:%Y-%m-%d %H:%M}")
print(f"Uptime: {uptime}")

