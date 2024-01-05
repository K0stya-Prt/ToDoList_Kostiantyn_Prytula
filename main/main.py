from tkinter import filedialog
import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import *
import ast


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ToDoList")
        self.geometry("1000x700")
        self.config(bg='#999999')
        self.resizable(False, False)

        self.top_menu()
        self.right_frame()

    def create_new_file(self):
        try:
            win_new_f = tk.Toplevel()
            win_new_f.grab_set()
            win_new_f.title("Creating the new file")
            win_new_f.geometry("250x100")
            win_new_f.resizable(False, False)

            def get_name():
                name_file = new_name_f.get() + ".txt"
                if name_file == ".txt":
                    showerror(message="Please, enter the name! >:(")
                else:
                    showinfo(message=f"Your file is saved as {name_file} in txt-type. You can open it whenever you want!")

                    current_directory = os.getcwd() # Отримання поточної директорії
                    parent_directory = os.path.dirname(current_directory)  # Шлях до батьківської директорії
                    new_directory = os.path.join(parent_directory, "saves") # Шлях до нової директорії в якій зберігаються лісти
                    new_file_path = os.path.join(new_directory, f"{name_file}") # Шлях до нового файлу в новій директорії

                    with open(new_file_path, 'x') as new_file: # Створення нового файлу
                        new_file.write("[('Enter the task', 'Not done', 'Put the deadline')]")

                    win_new_f.destroy()

            enter_name = tk.Label(win_new_f, text="Please, enter the name of new file")
            enter_name.pack(anchor="center", expand=1)

            new_name_f = tk.Entry(win_new_f)
            new_name_f.pack(anchor="center", expand=1)

            button_for_new_name = tk.Button(win_new_f, text="Accept", command=get_name)
            button_for_new_name.pack(anchor="center", expand=1)

            win_new_f.mainloop()
        except Exception as error:
            showerror(title="Error", message=f"An {error} has occured :(")

    def save_file(self): #Фукція для зберігання файлу, формат зберігання ліст - тапл
        all_values = []
        for item_id in self.table.get_children():
            item_values = self.table.item(item_id, 'values')
            all_values.append(item_values)

        print(all_values)

        with open(to_open_file, 'w', encoding='utf-8') as file:
            file.write(str(all_values))

    def open_file(self): #функція, яка відкриває файл в прогармі

        current_directory = os.getcwd()
        parent_directory = os.path.dirname(current_directory)
        new_directory = os.path.join(parent_directory, "saves")

        global to_open_file #тут потрібна бібліотека ast щоб файл міг читатися пайтоном
        to_open_file = filedialog.askopenfilename(initialdir=f"{new_directory}")

        try:
            with open(to_open_file, 'r', encoding='utf-8') as file:
                datas = ast.literal_eval(file.read())

                columns = ("Task", "Status", "Deadline")

                self.table = ttk.Treeview(columns=columns, show="headings", selectmode="browse")
                self.table.pack(fill=BOTH, expand=1)

                self.table.heading("Task", text="Task")
                self.table.heading("Status", text="Status")
                self.table.heading("Deadline", text="Deadline")

                # добавляем данные
                for data in datas:
                    self.table.insert("", END, values=data)

        except Exception as error:
            showerror(title="Error", message=f"An {error} has occurred :(")
        else: #тут кнопки стають активними, щоб користувач міг мучатися з інтерфейсом
            self.btn1.config(state="normal")
            self.btn2.config(state="normal")
            self.btn3.config(state="normal")
            self.btn4.config(state="normal")
            self.btn5.config(state="normal")

    def close_file(self): #функція яка достовляє задоволення та заставляє камінь випасти з душі
        self.table.destroy()
        self.btn1.config(state="disabled")
        self.btn2.config(state="disabled")
        self.btn3.config(state="disabled")
        self.btn4.config(state="disabled")
        self.btn5.config(state="disabled")

    def add_task(self): # адська функція яка додає задачу
        try:
            # Створюємо топ-рівень вікна для введення даних
            win_add_task = tk.Toplevel()
            win_add_task.grab_set()
            win_add_task.title("Add Task")
            win_add_task.geometry("250x250")
            win_add_task.resizable(False, False)


            def add_task_to_table(): # Функція для додавання завдання до таблиці
                task_text = entry_task.get()
                status_text = entry_status.get()
                deadline_text = entry_deadline.get()

                # Перевірка, чи введено всі необхідні дані
                if not task_text or not status_text or not deadline_text:
                    showwarning(message="Please fill in all fields.")
                    return

                # Додавання рядка з даними в таблицю
                self.table.insert("", END, values=(task_text, status_text, deadline_text))

                # Закриваємо вікно після додавання завдання
                win_add_task.destroy()

            # Створюємо та розміщуємо елементи для введення даних
            label_task = tk.Label(win_add_task, text="Task:")
            label_task.pack(anchor="center", padx=10, pady=5)
            entry_task = tk.Entry(win_add_task)
            entry_task.pack(anchor="center", padx=10, pady=5)

            status_possibilities = ["Done", "Not Done"]
            label_status = tk.Label(win_add_task, text="Status:")
            label_status.pack(anchor="center", padx=10, pady=5)
            entry_status = ttk.Combobox(win_add_task, values=status_possibilities, state='readonly')
            entry_status.pack(anchor="center", padx=10, pady=5)

            label_deadline = tk.Label(win_add_task, text="Deadline:")
            label_deadline.pack(anchor="center", padx=10, pady=5)
            entry_deadline = tk.Entry(win_add_task)
            entry_deadline.pack(anchor="center", padx=10, pady=5)

            button_add_task = tk.Button(win_add_task, text="Add Task", command=add_task_to_table)
            button_add_task.pack(anchor="center", pady=10)

            # Зачекати, поки вікно буде закрито
            win_add_task.wait_window()

        except Exception as error:
            showerror(title="Error", message=f"An {error} has occurred :(")

    def delete_task(self): #функція яка відправляє в стратосферу задачу
        self.table.delete([selected_item for selected_item in self.table.selection()])
        self.table.bind("<<TreeviewSelect>>", self.delete_task)

    def add_or_edit_deadline(self): #зайва непотрібна ніким функція яка дає можливість змінити дедлайн
        selected_item = self.table.selection()
        print(selected_item)

        # Перевірка, чи вибрано рядок
        if not selected_item:
            showwarning(message="Please select a row.")
            return

        # Отримання інформації про вибраний рядок
        item_data = self.table.item(selected_item, 'values')

        dead_win = tk.Toplevel()
        dead_win.title("Deadline")
        dead_win.geometry("200x200")
        dead_win.grab_set()
        dead_win.title("Adding or changing deadline")

        # Вивід поточного дедлайну
        tk.Label(dead_win, text=f"Current deadline: {item_data[2]}").pack(anchor='center', expand=1)

        # Поле для введення нового дедлайну
        info = tk.Entry(dead_win)
        info.pack(anchor='center', expand=1)

        # Функція для збереження нового дедлайну
        def deadline():
            new_deadline = info.get()

            # Оновлюємо значення дедлайну в таблиці
            self.table.item(selected_item, values=(item_data[0], item_data[1], new_deadline))

            # Закриваємо вікно після додавання завдання
            dead_win.destroy()

        # Кнопка для підтвердження
        submit = tk.Button(dead_win, text="Submit", command=deadline)
        submit.pack(anchor='center', expand=1)

    def edit_task(self): # найкорисніша функція яка дає можливість змінити все і вся в задачі
        selected_items = self.table.selection()

        # Перевірка, чи вибрано рядок
        if not selected_items:
            showwarning(message="Please select a row.")
            return

        item_data = self.table.item(selected_items, 'values')

        win_for_edit = tk.Toplevel()
        win_for_edit.title("Editing the task")
        win_for_edit.geometry("350x250")
        win_for_edit.grab_set()

        label_task = tk.Label(win_for_edit, text="The task:")
        label_task.pack(anchor='center', expand=1)
        entry_task_var = tk.StringVar(value=item_data[0])
        entry_task = tk.Entry(win_for_edit, textvariable=entry_task_var)
        entry_task.pack(anchor='center', expand=1)

        label_status = tk.Label(win_for_edit, text="The status")
        label_status.pack(anchor='center', expand=1)
        combobox_status_var = tk.StringVar(value=item_data[1])
        combobox_status = ttk.Combobox(win_for_edit, textvariable=combobox_status_var, values=["Done", "Not Done"], state='readonly')
        combobox_status.pack(anchor='center', expand=1)

        label_deadline = tk.Label(win_for_edit, text="The deadline")
        label_deadline.pack(anchor='center', expand=1)
        entry_deadline_var = tk.StringVar(value=item_data[2])
        entry_deadline = tk.Entry(win_for_edit, textvariable=entry_deadline_var)
        entry_deadline.pack(anchor='center', expand=1)

        def confirm_edit():
            new_task = entry_task_var.get()
            new_status = combobox_status_var.get()
            new_deadline = entry_deadline_var.get()

            self.table.item(selected_items, values=(new_task, new_status, new_deadline))
            win_for_edit.destroy()

        submit_button = tk.Button(win_for_edit, text="Enter!")
        submit_button.pack(anchor='center', expand=1)

        submit_button.config(command=confirm_edit)

    def help_with_program(self):
        help_win = tk.Toplevel()
        help_win.title("Help center")
        help_win.geometry("410x150")
        help_win.grab_set()
        help_win.resizable(False, False)

        def close_the_win():
            help_win.destroy()

        explain1 = tk.Label(help_win, text="This is the ToDoList program, which was created by junior python developer!\n"
                                           "The main idea of this program is setting any task \n with opportunities to set status (done or not done) and deadlines. \n"
                                           "The interface is easy to understand, \n so it should not cause any problems during the using this programe.\n")
        explain1.pack(anchor="nw")
        close_button = ttk.Button(help_win, text="Understandable!", command=close_the_win)
        close_button.pack(anchor='s', expand=1)


    def top_menu(self): # верхнє меню, яке дає можливість діяти з файлами
        top_menu = tk.Menu()

        file_menu = tk.Menu(tearoff=0)
        file_menu.add_command(label="Create file", command=self.create_new_file)
        file_menu.add_command(label="Save file", command=self.save_file)
        file_menu.add_command(label="Open file", command=self.open_file)
        file_menu.add_command(label="Close file", command=self.close_file)

        top_menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=top_menu)

    def right_frame(self): # фрейм, який вміщує в собі кнопки для взаємодіями з задачами
        # Головний фрейм
        self.main_buttons = tk.Frame(relief="groove", borderwidth=2)

        # Кнопки для роботи з задачами (доступна тільки остання)
        self.btn1 = tk.Button(self.main_buttons, text="Add task", state="disabled", command=self.add_task)
        self.btn1.pack(fill="x", anchor="n", expand=1)

        self.btn2 = tk.Button(self.main_buttons, text="Select and delete task", state="disabled",
                              command=self.delete_task)
        self.btn2.pack(fill="x", anchor="n", expand=1)

        self.btn3 = tk.Button(self.main_buttons, text="Edit task", state="disabled", command=self.edit_task)
        self.btn3.pack(fill="x", anchor="n", expand=1)

        self.btn4 = tk.Button(self.main_buttons, text="Select list and edit deadline", state="disabled",
                              command=self.add_or_edit_deadline)
        self.btn4.pack(fill="x", anchor="n", expand=1)

        self.btn5 = tk.Button(self.main_buttons, text="Help | Допомога", command=self.help_with_program)
        self.btn5.pack(fill="x", anchor="s", expand=1)

        self.main_buttons.config(bg='#999999')  # Фон фрейму
        self.main_buttons.pack(side="left", fill="y")  # Розташування головного фрейму


if __name__ == "__main__":
    app = Main()
    app.mainloop()
