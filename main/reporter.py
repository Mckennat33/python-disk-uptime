import psutil 
import datetime
import tkinter as tk

root = tk.Tk()
root.title("Disk / Uptime Monitor")
root.geometry("500x400")
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
print(f" Used %: {used_perc:.1f}%")

lb.insert(1, "CPU Time", cpu_time)
lb.insert(2, f"Booted at: {boot:%Y-%m-%d %H:%M}")
lb.insert(3, f"Uptime: {uptime}")
lb.insert(4, f"CPU Usage: {cpu_percentage}%")
lb.insert(5, f"Logical Core Count: {logical_core_count}")
lb.insert(6, f"Physical Core Count: {physical_core_count}")

def ram_usage():
    if used_perc >= 90:
        return 'Critical above 90% usage'
    elif used_perc >= 80:
        return 'Warning above 80% usage'
    else:
        return "Good to go"

print(ram_usage())

lb.insert(7, "RAM")
lb.insert(8, f"Total: {total_gb:.1f}")
lb.insert(9, f"Used: {used_ram:.1f}")
lb.insert(10, f"Available Memory: {available_gb:.1f}")
lb.insert(11, f"Used %: {used_perc:.1f}%")
lb.insert(12, ram_usage())
lb.pack(fill=tk.BOTH, expand=True)
root.mainloop()
