import platform
import socket
import tkinter as tk
from tkinter import ttk

def get_system_info():
    """Collect basic system identification info."""
    return {
        "Hostname": socket.gethostname(),
        "OS": f"{platform.system()} {platform.release()}",
        "Version": platform.version(),
    }

def build_window():
    root = tk.Tk()
    root.title("System Info")
    root.geometry("420x260")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    # Header
    header = tk.Label(
        root,
        text="System Information",
        font=("Segoe UI", 16, "bold"),
        bg="#1e1e2e",
        fg="#f5f5f5",
        pady=15,
    )
    header.pack(fill="x")

    # Card frame to hold the info rows
    card = tk.Frame(root, bg="#2a2a3d", padx=20, pady=20)
    card.pack(padx=20, pady=10, fill="both", expand=True)

    info = get_system_info()

    for label_text, value_text in info.items():
        row = tk.Frame(card, bg="#2a2a3d")
        row.pack(fill="x", pady=8)

        label = tk.Label(
            row,
            text=f"{label_text}:",
            font=("Segoe UI", 11, "bold"),
            bg="#2a2a3d",
            fg="#9aa5ce",
            anchor="w",
            width=10,
        )
        label.pack(side="left")

        value = tk.Label(
            row,
            text=value_text,
            font=("Segoe UI", 11),
            bg="#2a2a3d",
            fg="#f5f5f5",
            anchor="w",
            wraplength=250,
            justify="left",
        )
        value.pack(side="left", fill="x", expand=True)

    root.mainloop()


if __name__ == "__main__":
    build_window()





