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
used_ram = total_gb - available_gb
used_perc = (used_ram / total_gb) * 100


print(f"CPU Time (idle, hours): {cpu_time}")
print(f"Booted at: {boot:%Y-%m-%d %H:%M}")
print(f"Uptime: {uptime}")
print(f"CPU: {cpu_percentage}")
print(f"Logical Core Count: {logical_core_count}")
print(f"Physical Core Count: {physical_core_count}")
print("RAM")
print(f" Total: {total_gb:.1f}")
print(f" Used: {used_ram:.1f}")
print(f" Available: {available_gb:.1f}")

lb.insert(1, "CPU Time", cpu_time)
lb.insert(2, f"Booted at: {boot:%Y-%m-%d %H:%M}")
lb.insert(3, f"Uptime: {uptime}")
lb.insert(4, f"CPU Usage: {cpu_percentage}%")
lb.insert(5, f"Logical Core Count: {logical_core_count}")
lb.insert(6, f"Physical Core Count: {physical_core_count}")

def ram_usage(): 
    if f"{used_perc:1f}" >= 80
lb.insert(7, "RAM")
print(f"{used_perc:.1f}")
lb.insert(8, f"Total: {total_gb:.1f}")
lb.insert(9, f"Used: {used_ram:.1f}")
lb.insert(10, f"Available Memory: {available_gb:.1f}")
lb.pack()
root.mainloop()
