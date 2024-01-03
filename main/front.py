from back import *
import tkinter as tk


class Main:  # Головне вікно

    main = tk.Tk()
    main.title("ToDoList")  # Заголовок
    main.geometry("1000x700")  # Розмір вікна
    main.config(bg='#999999')  # Фон
    main.resizable(False, False)  # Заборона на зміну розміру вікна

    # Верхнє меню, яке відповідає за керування файлами
    top_menu = tk.Menu()

    file_menu = tk.Menu(tearoff=0)
    file_menu.add_command(label="Створити файл", command=create_new_file)
    file_menu.add_command(label="Зберегти файл", command=save_file)
    file_menu.add_command(label="Відкрити файл", command=open_file)
    file_menu.add_command(label="Закрити файл", command=close_file)

    top_menu.add_cascade(label="Файл", menu=file_menu)

    main.config(menu=top_menu)

    # Головний фрейм
    main_buttons = tk.Frame(relief="groove", borderwidth=2)

    # Кнопки для роботи з задачами (доступна тільки остання)
    btn1 = tk.Button(main_buttons, text="Додати задачу", state="disabled")
    btn1.pack(fill="x", anchor="n", expand=1)

    btn2 = tk.Button(main_buttons, text="Видалити задачу", state="disabled")
    btn2.pack(fill="x", anchor="n", expand=1)

    btn3 = tk.Button(main_buttons, text="Додати підзадачу", state="disabled")
    btn3.pack(fill="x", anchor="n", expand=1)

    btn4 = tk.Button(main_buttons, text="Додати дедлайн", state="disabled")
    btn4.pack(fill="x", anchor="n", expand=1)

    btn5 = tk.Button(main_buttons, text="Допомога", command=help_with_program)
    btn5.pack(fill="x", anchor="s", expand=1)

    if status_file == 1:  # Розблокування кнопок для роботи з задачами
        btn1 = tk.Button(main_buttons, text="Додати задачу", state="normal", command=add_list)
        btn1.pack(fill="x", anchor="n", expand=1)

        btn2 = tk.Button(main_buttons, text="Видалити задачу", state="normal", command=delete_list)
        btn2.pack(fill="x", anchor="n", expand=1)

        btn3 = tk.Button(main_buttons, text="Призначити підзадачу", state="normal", command=add_sublist)
        btn3.pack(fill="x", anchor="n", expand=1)

        btn4 = tk.Button(main_buttons, text="Призначити дедлайн", state="normal", command=add_deadline)
        btn4.pack(fill="x", anchor="n", expand=1)

    main_buttons.config(bg='#999999')  # Фон фрейму
    main_buttons.pack(side="left", fill="y")  # Розташування головного фрейму

    # Частина для роботи з задачами
    list_frame = tk.Frame(relief="groove", borderwidth=2)

    greeting_label = tk.Label(list_frame, text="Вітаю в програмі ToDoList")
    greeting_label.config(bg='#999999')  # Фон фремй для роботи з задачами
    greeting_label.pack(anchor="center", expand=1)

    list_frame.config(bg="#999999")
    list_frame.pack(side="right", fill="both", expand=True)  # Розташування фрейму для роботи з задачами
    list_frame.destroy()

    main.mainloop()

if __name__ == '__main__':
    Main()
