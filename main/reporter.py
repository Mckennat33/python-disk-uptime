import psutil 
import datetime
import tkinter as tk

root = tk.Tk()
root.title("Disk / Uptime Monitor")
lb = tk.Listbox(root)
cpu_time = psutil.cpu_times().idle // 3600
memory = psutil.virtual_memory()

boot = datetime.datetime.fromtimestamp(psutil.boot_time())
uptime = datetime.datetime.now() - boot
cpu_percentage = psutil.cpu_percent(interval=1)
logical_core_count = psutil.cpu_count(logical=True)
physical_core_count = psutil.cpu_count(logical=False)
total_gb = memory.total / (1024 ** 3)
available_gb = memory.available / (1024 ** 3)



print(f"CPU Time (idle, hours): {cpu_time}")
print(f"Booted at: {boot:%Y-%m-%d %H:%M}")
print(f"Uptime: {uptime}")
print(f"CPU: {cpu_percentage}")
print(f"Logical Core Count: {logical_core_count}")
print(f"Physical Core Count: {physical_core_count}")
print(f" Total Memory Usage: {total_gb}")
print(f" Available Memory Usage: {available_gb}")

lb.insert(1, "CPU Time", cpu_time)
lb.insert(2, f"Booted at: {boot:%Y-%m-%d %H:%M}")
lb.insert(3, f"Uptime: {uptime}")
lb.insert(4, f"CPU Usage: {cpu_percentage}%")
lb.insert(5, f"Logical Core Count: {logical_core_count}")
lb.insert(6, f"Physical Core Count: {physical_core_count}")
#lb.insert(7, f"Memory Usage: {memory_usage}")
lb.insert(8, f"Total Memory: {total_gb}")
lb.insert(8, f"Available Memory: {available_gb}")
lb.pack()
root.mainloop()
