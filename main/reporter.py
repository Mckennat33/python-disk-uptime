import psutil 
import datetime

print(psutil.cpu_times().idle // 3600)

print("CPU Statistics", psutil.cpu_stats().syscalls // 3600)

print("Booted at", psutil.boot_time())