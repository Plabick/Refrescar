from tkinter import *
from PIL import ImageTk, Image

# from winreg import *

if __name__ == '__main__':
    REGISTRY_LOCATION = r'SYSTEM\Setup\MoSetup'
    REGISTRY_KEY = r'AllowUpgradesWithUnsupportedTPMOrCPU'
    window = Tk()
    window.title("Refrescar")
    window.geometry('500x300')
    window.configure(bg="white")

    # Determine Current Status of Registry Key
    try:
        fullKey = OpenKey(HKEY_LOCAL_MACHINE, REGISTRY_LOCATION, 0, KEY_ALL_ACCESS)
        current = QueryValueEx(fullKey, REGISTRY_KEY)
        ok = True  # TODO Set ok to be the result of this lookup
    except:
        ok = False;
    print(ok)

    # Display logo
    logo = Image.open("Refrescar.ppm").resize((318, 105))
    logoImage = ImageTk.PhotoImage(logo)
    logoLabel = Label(image=logoImage)
    logoLabel.image = logoImage
    logoLabel.pack()

    # Display Current Status
    if ok:
        status = Label(text="Current Status: Patched", anchor=CENTER, fg="green")
    else:
        status = Label(text="Current Status: Unpatched", anchor=CENTER, fg="red")
    status.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Display tagline
    tagLine = Label(text="Enable Windows 11 installation on computers with unsupported CPUs", anchor=CENTER)
    tagLine.place(relx=0.5, rely=0.9, anchor=CENTER)


    def on_click():
        overwrite_window()
        update_registry()


    def update_registry():
        if not ok:
            print("Update Registry")
            # Create a Label in New window
            # Create key
            # key = CreateKey(HKEY_CURRENT_USER, REGISTRY_LOCATION)
            # SetValueEx(key, REGISTRY_KEY, 0, REG_DWORD, 1)
            # CloseKey(key)


    def overwrite_window():
        success = Image.open("directions.ppm").resize((500, 300))
        success_image = ImageTk.PhotoImage(success)
        success_label = Label(image=success_image)
        success_label.image = success_image
        success_label.place(relx=0.5, rely=0.5, anchor=CENTER)


    # Make Start button
    button = Image.open("button.pbm").resize((275, 42))
    button_image = ImageTk.PhotoImage(button)
    btn = Button(window, image=button_image, bg='white', fg='white', command=on_click)
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    window.mainloop()
