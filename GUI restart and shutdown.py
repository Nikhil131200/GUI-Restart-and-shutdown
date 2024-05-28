import tkinter as tk
import os

def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def logout():
    os.system("shutdown -l")

root = tk.Tk()
root.title("PC Control Panel")

shutdown_btn = tk.Button(root, text="Shutdown", command=shutdown)
shutdown_btn.pack()

restart_btn = tk.Button(root, text="Restart", command=restart)
restart_btn.pack()

logout_btn = tk.Button(root, text="Logout", command=logout)
logout_btn.pack()

root.mainloop()
