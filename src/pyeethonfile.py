import os
import ctypes
import tkinter as tk
from tkinter import ttk
from time import sleep
class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Selector")
        root.geometry("720x405")

        self.selected_file_path = tk.StringVar()

        self.dark_mode_var = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        files = self.get_files_with_extensions(".3dst", ".argb", ".rgba")
        files.insert(0, "Select File")
        file_var = tk.StringVar()
        file_var.set(files[0])

        style = ttk.Style()
        style.configure('Outline.TMenubutton', borderwidth=2, relief="solid")

        dropdown = ttk.OptionMenu(self.root, file_var, *files, command=self.update_selected_file, style='Outline.TMenubutton')
        dropdown.place(x=10, y=10)

        action_button = ttk.Button(self.root, text="Extract Colors", command=self.color_extract)
        action_button.place(x=10, y=50)

        settings_button = ttk.Button(self.root, text="\u2699", command=self.open_settings)
        settings_button.place(relx=1.0, rely=0.8725, anchor='ne', x=-10, y=-10)

    def get_files_with_extensions(self, *extensions):

        if os.path.exists("mc3dsflip.config"):
            with open('mc3dsflip.config', 'r') as f:
                lines = f.readlines()
                fourth_line = lines[4].strip()

            if fourth_line == "True":
                files = []
                for foldername, subfolders, filenames in os.walk('.'):
                    for filename in filenames:
                        if any(filename.endswith(extension) for extension in extensions):
                            files.append(os.path.join(foldername, filename))
                return files
            
            elif fourth_line == "False":
                files = []
                for extension in extensions:
                    files.extend([file for file in os.listdir() if file.endswith(extension)])
                return files

            else:
                files = []
                for extension in extensions:
                    files.extend([file for file in os.listdir() if file.endswith(extension)])
                return files                

    def update_selected_file(self, selected_file):
        if selected_file != "Select File":
            self.selected_file_path.set(os.path.abspath(selected_file))
        else:
            self.selected_file_path.set("")

    def color_extract(self):
        image_path = self.selected_file_path.get()
        filename = os.path.basename(image_path)
        print(f"Extracting Colors From: '{filename}'.")
        print(f"Image Path: '{image_path}'.\n")
        tmp0 = filename.replace('.3dst','')
        output_path = f"{tmp0}_colors.txt"

        existing_colors = set()
    
        try:
            with open(output_path, "r") as existing_file:
                existing_colors = {line.strip() for line in existing_file}
        except FileNotFoundError and OSError:
            pass
    
        with open(image_path, "rb") as image_file:
            image_file.seek(0x20)
            argb_data = image_file.read()
        
            rgb_hex_values = []
            for i in range(0, len(argb_data), 4):
                b, g, r, _ = argb_data[i:i+4]
                rgb_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
            
                if rgb_hex not in existing_colors:
                    existing_colors.add(rgb_hex)
                    rgb_hex_values.append(rgb_hex)
        
            with open(output_path, "a") as output_file:
                for hex_value in rgb_hex_values:
                    output_file.write(hex_value + "\n")

            sleep(0.25)

            if os.path.exists("mc3dsflip.config"):
                with open('mc3dsflip.config', 'r') as f:
                    lines = f.readlines()
                    second_line = lines[7].strip()

                    if second_line == "Enabled":
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        result = MessageBox(None, 'Would you like to open the generated Text-File in Notepad?', 'MC-3DS-Flip (GUI) - NOTICE', 0x04 | 0x40)

                        if result == 6:
                            os.system(f"notepad.exe {output_path}")
                        else:
                            pass

                    else:
                        pass

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x150")

        toggle_button_text = "Toggle Theme" if not self.dark_mode_var.get() else "Toggle Theme"
        toggle_button = ttk.Button(settings_window, text=toggle_button_text, command=self.toggle_dark_mode)
        toggle_button.pack(pady=10)

        toggle_subdir_text = "Toggle Subdirectories" if not self.dark_mode_var.get() else "Toggle Subdirectories"
        toggle_subdir_button = ttk.Button(settings_window, text=toggle_subdir_text, command=self.MessageBoxW)
        toggle_subdir_button.pack(pady=10)

        toggle_messagebox = "Toggle MessageBox Notifications" if not self.dark_mode_var.get() else "Toggle MessageBox Notifications"
        toggle_msgbox_button = ttk.Button(settings_window, text=toggle_messagebox, command=self.toggle_message_box)
        toggle_msgbox_button.pack(pady=10)

    def toggle_dark_mode(self):
        self.dark_mode_var.set(not self.dark_mode_var.get())
        self.apply_dark_mode()


    def toggle_message_box(self):
        if os.path.exists("mc3dsflip.config"):
            with open('mc3dsflip.config', 'r') as f:
                lines = f.read()
                if "Enabled" in lines:
                    num0 = 1
                else:
                    num0 = 0

                if num0 == 1:
                    data = lines.replace("Enabled","Disabled")
                    print("Changed Value: 'Enabled' ---> 'Disabled'. | Settings\n")
                elif num0 == 0:
                    data = lines.replace("Disabled","Enabled")
                    print("Changed Value: 'Disabled' ---> 'Enabled'. | Settings\n")
            
            with open('mc3dsflip.config', 'w') as file:
                file.write(data)


    def toggle_subdirs(self):
        if os.path.exists("mc3dsflip.config"):
            with open('mc3dsflip.config', 'r') as f:
                lines = f.read()
                if "True" in lines:
                    num0 = 1
                elif "False" in lines:
                    num0 = 0

                if num0 == 1:
                    data = lines.replace("True","False")
                    print("Changed Value: 'True' ---> 'False'. | Settings\n")
                elif num0 == 0:
                    data = lines.replace("False","True")
                    print("Changed Value: 'False' --> 'True'.  | Settings\n")
                
            with open('mc3dsflip.config', 'w') as file:
                file.write(data)

    def MessageBoxW(self):
        if os.path.exists("mc3dsflip.config"):
            with open('mc3dsflip.config', 'r') as f:
                lines = f.readlines()
                second_line = lines[7].strip()

                if second_line == "Enabled":
                    MessageBox = ctypes.windll.user32.MessageBoxW
                    MessageBox(None, 'For the Changes to take place. Please restart the Application.', 'MC-3DS-Flip (GUI) - NOTICE', 0x00)
                else:
                    pass

        self.toggle_subdirs()


    def apply_dark_mode(self):
        theme = "alt" if self.dark_mode_var.get() else "clam"
    
        if self.dark_mode_var.get():
            # Dark mode
            print("Changed Value: 'Light' --> 'Dark'.  | Settings\n")
            self.root.tk_setPalette(
                background="#2E2E2E",
                foreground="#FFFFFF",
                activeBackground="#2E2E2E",
                activeForeground="#FFFFFF",
            )
            var0 = "Dark"

            with open('mc3dsflip.config','r') as f:
                read = f.read()
                data = read.replace("Light",var0)

            with open('mc3dsflip.config','w') as file:
                file.write(data)

        else:
            # Light mode
            print("Changed Value: 'Dark' ---> 'Light'. | Settings\n")
            self.root.tk_setPalette(
                background="#e3e3e3",
                foreground="#000000",
                activeBackground="#555555",
                activeForeground="#FFFFFF",
            )
            var0 = "Light"

            with open('mc3dsflip.config','r') as f:
                read = f.read()
                data = read.replace("Dark",var0)
            
            with open('mc3dsflip.config','w') as file:
                file.write(data)

        ttk.Style().theme_use(theme)


if __name__ == "__main__":
    root = tk.Tk()

    if os.path.exists("mc3dsflip.config"):
        with open('mc3dsflip.config', 'r') as f:
            lines = f.readlines()
            second_line = lines[1].strip()

            if second_line == "Dark":
                root.tk_setPalette(
                    background="#2E2E2E",
                    foreground="#FFFFFF",
                    activeBackground="#555555",
                    activeForeground="#FFFFFF",
                )
            elif second_line == "Light":
                root.tk_setPalette(
                    background="#e3e3e3",
                    foreground="#000000",
                    activeBackground="#555555",
                    activeForeground="#FFFFFF",
                )

            else:
                s = 0

    else:
        with open('mc3dsflip.config','w') as f:
            f.write("[THEME]\n")
            f.write("Light\n")
            f.write("\n")
            f.write("[SUBDIRECTORIES]\n")
            f.write("True\n")
            f.write("\n")
            f.write("[MESSAGEBOX]\n")
            f.write("Enabled")


    app = FileSelectorApp(root)
    root.mainloop()
