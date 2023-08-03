# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
"""
Text editor created using Tkinter library
"""
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfilename


class TextEditor(tk.Tk):
    """
    With this class you can create the text editor objects
    """
    def __init__(self):
        """
        Constructor of the class
        """
        super().__init__()

        # Setting basic config for the window
        self.title('Text Editor')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)

        self.text_field_frame = None    # Frame where the text field is going to be inserted
        self.text_field = None          # Text field where we can edit the text
        self.file = None                # File to edit

        # Methods to create the menus and the elements of the window
        self._create_menu()
        self._create_elements()

    def _create_menu(self):
        """
        Method to create the menu of the window for the text editor
        :return:
        """
        # Adding the main menu to the window
        main_menu = tk.Menu(self)
        self.config(menu=main_menu)

        # Options submenu
        options_submenu = tk.Menu(main_menu, tearoff=False)
        options_submenu.add_command(label='About',
                                    command=lambda: messagebox.showinfo('About', 'App made by "/Ango1415" (on Github)'))
        options_submenu.add_command(label='Exit', command=self.quit)

        # Adding submenu
        main_menu.add_cascade(label='Options', menu=options_submenu)

    def _create_elements(self):
        """
        Method to create the elements of the window for the text editor
        :return:
        """
        # Defining the frames for the text editor app
        buttons_frame = tk.Frame(self, relief=tk.RAISED, bd=2)
        buttons_frame.grid(row=0, column=0, sticky='NS')

        self.text_field_frame = tk.LabelFrame(self, text='New file')
        self.text_field_frame.rowconfigure(0, weight=1)
        self.text_field_frame.columnconfigure(0, weight=1)
        self.text_field_frame.grid(row=0, column=1, padx=5, sticky='NSEW')

        # Adding elements to frame_buttons
        open_button = tk.Button(buttons_frame, text='Open', command=self._open_file)
        open_button.grid(row=0, column=0, sticky='EW', padx=5, pady=5)

        save_button = tk.Button(buttons_frame, text='Save', command=self._save_file)
        save_button.grid(row=1, column=0, sticky='EW', padx=5, pady=5)

        save_as_button = tk.Button(buttons_frame, text='Save as...', command=self._save_as_file)
        save_as_button.grid(row=2, column=0, sticky='EW', padx=5, pady=5)

        # Adding the text field to frame_text_field
        self.text_field = tk.Text(self.text_field_frame, wrap=tk.WORD)
        self.text_field.grid(row=0, column=0, padx=5, sticky='NSEW')

    def _open_file(self):
        """
        Method to define the functionality of the open button
        :return:
        """
        # Trying to open the text file to edit
        self.file = askopenfile(mode='r+', filetypes=[('Text Files', '*.txt')])
        if not self.file:
            messagebox.showerror('Error', 'It was not possible to find the text file.')
            return

        # If the text file was open correctly we erase the prior text field content
        self.text_field.delete(1.0, tk.END)

        # Process to insert the text of the file un the text field
        with open(self.file.name, 'r+') as opened_file:
            file_text = opened_file.read()
            self.text_field.insert(1.0, file_text)

            self.title(f'Text Editor - {self.file.name}')
            self.text_field_frame.config(text=f'{ self.file.name[self.file.name.rindex("/")+1:] }')

    def _save_file(self):
        """
        Method to define the functionality of the save button
        :return:
        """
        if self.file:
            # If the file is already open
            with open(self.file.name, 'w') as opened_file:
                text = self.text_field.get(1.0, tk.END)
                opened_file.write(text)

                messagebox.showinfo('Save process', 'The file was saved successfully')
        else:
            # If is a new file, it redirects to the save as functionality
            self._save_as_file()

    def _save_as_file(self):
        """
        Method to define the functionality of the save as button
        :return:
        """
        # Trying to save the text file
        self.file = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')]
        )
        if not self.file:
            messagebox.showerror('Error', 'It was not possible to save the text file in the defined location.')
            return

        # Process to save the content of text field in a file
        with open(self.file, 'w') as self.file:
            text = self.text_field.get(1.0, tk.END)
            self.file.write(text)

            self.title(f'Text Editor - {self.file.name}')
            self.text_field_frame.config(text=f'{self.file.name[self.file.name.rindex("/") + 1:]}')
            messagebox.showinfo('Save process', 'The file was saved successfully')


if __name__ == '__main__':
    text_editor = TextEditor()
    text_editor.mainloop()
