import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from winreg import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    REGISTRY_LOCATION = r'SYSTEM\Setup\MoSetup'
    REGISTRY_KEY = r'AllowUpgradesWithUnsupportedTPMOrCPU'


    def on_click():
        overwrite_window()
        update_registry()


    def update_registry():
        if not bypass_enabled:
            # Create key
            key = CreateKey(HKEY_LOCAL_MACHINE, REGISTRY_LOCATION)
            SetValueEx(key, REGISTRY_KEY, 0, REG_DWORD, 1)
            CloseKey(key)


    def overwrite_window():
        for widget in window.winfo_children():
            widget.destroy()
        success = Label(text="Success", anchor=CENTER, bg="white", font=('Arial bold', '20'))
        enabled = Label(text="The Windows 11 update has been enabled", anchor=CENTER, bg="white",
                        font=('Arial ', '15'))
        next = Label(text="Use the Windows 11 Upgrade Assistant to install the update", anchor=CENTER, bg="white", font=('Arial ', '12'))

        success.pack()
        enabled.pack()
        next.pack()


    try:
        # Check for access to Windows Registry
        fullKey = OpenKey(HKEY_LOCAL_MACHINE, REGISTRY_LOCATION, 0, KEY_ALL_ACCESS)
    except PermissionError:
        messagebox.showinfo('Error', 'Please run Refrescar as an Administrator')
        exit(1)

    try:
        # Check if key exists and is set to the correct value
        current = QueryValueEx(fullKey, REGISTRY_KEY)
        bypass_enabled = current[0] == 1
    except FileNotFoundError:
        bypass_enabled = False;

    # Create Window
    window = Tk()
    window.title("Refrescar")
    window.geometry('500x300')
    window.configure(bg="white")

    # Add logo to window
    logo = Image.open(resource_path("images/logo.ppm")).resize((318, 105))

    logoImage = ImageTk.PhotoImage(logo)
    logoLabel = Label(image=logoImage, bg="white")
    logoLabel.image = logoImage
    logoLabel.pack()

    # Display Current Patch Status
    if bypass_enabled:
        status_message = "Patched"
        status_color = "green"
    else:
        status_message = "Unpatched"
        status_color = "red"
    status = Label(text=f"Current Status: {status_message}", anchor=CENTER, fg=status_color, bg="white")
    status.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Display tag line
    tagLine = Label(text="Enable Windows 11 installation on computers with unsupported CPUs", anchor=CENTER, bg="white")
    tagLine.place(relx=0.5, rely=0.9, anchor=CENTER)

    # Display Run button
    button = Image.open(resource_path("images/button.pbm")).resize((275, 42))

    button_image = ImageTk.PhotoImage(button)
    btn = Button(window, image=button_image, bg='white', fg='white', highlightthickness=0, bd=0, command=on_click)
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    window.mainloop()
