import os

def shutdown_now(os_name):
    """
    Shuts down the computer immediately using os.system().
    """
    if os_name == 'nt': # Windows
        os.system("shutdown /s /t 0")
    elif os_name == 'posix': # Linux or macOS
        # May require root privileges
        os.system("sudo shutdown now")
    else:
        print(f"Unsupported operating system: {os_name}")

# To use:
shutdown_now(os.name)
