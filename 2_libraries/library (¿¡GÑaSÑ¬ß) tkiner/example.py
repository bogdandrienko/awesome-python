from tkinter import *

value = 0


def calc():
    global value

    print(f'chk_value: {chk_value.get()}')
    print(f'entr_value: {entr_value.get()}')

    if chk_value.get():
        str1 = entr_value.get()
        if str(str1).isdigit():
            value += int(str1)
            lbl.config(text=value)
        else:
            lbl.config(text="Вы ввели некорректное значение!")
    print('press')


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=calc)  # тут нужна ссылка на функцию (имя функции)
btn.grid(column=0, row=1)

entr_value = StringVar(value='1')
entr = Entry(textvariable=entr_value, )
entr.grid(column=1, row=0)

chk_value = IntVar()
chk = Checkbutton(text="Добавлять/не добавлять", variable=chk_value)
chk.grid(column=1, row=1)

window.mainloop()


##############################################################################


class TkinterClass:
    @staticmethod
    def example():
        def play_func(data: str):
            global play
            play = False
            sleep(0.5)
            play = True

            def whiles():
                print(data)

            thread_render = Thread(target=whiles)
            thread_render.start()
            app.set_title("Завершено")

        class Application(tkinter.Frame):
            def __init__(self, root, **kw):
                super().__init__(**kw)
                self.id = 0
                self.iid = 0
                self.root = root
                self.root.title("ожидание")
                self.root.grid_rowconfigure(0, weight=1)
                self.root.grid_columnconfigure(0, weight=1)
                self.root.config(background="black")
                self.root.geometry('1280x720')
                self.master.minsize(1280, 720)
                self.master.maxsize(1280, 720)

                self.play_btn = tkinter.Button(self.root, text="Запустить", font="100", command=self.play_button)
                self.play_btn.grid(row=0, column=0, sticky=tkinter.W)
                self.stop_btn = tkinter.Button(self.root, text="Остановить", font="100", command=self.stop_button)
                self.stop_btn.grid(row=0, column=1, sticky=tkinter.W)
                self.quit_btn = tkinter.Button(self.root, text="Выход", font="100", command=self.quit_button)
                self.quit_btn.grid(row=0, column=2, sticky=tkinter.W)

                self.export_label = tkinter.Label(self.root, text="Видеофайл для анализа/ip для анализа", font="100")
                self.export_label.grid(row=1, column=0, sticky=tkinter.W)
                self.export_entry = tkinter.Entry(self.root, font="100")
                self.export_entry.grid(row=1, column=1, sticky=tkinter.W)
                self.export_entry.insert(0, 'video.mp4')

                chk_state = tk.BooleanVar()
                chk_state.set(False)
                chk = ttk.Checkbutton(self.root, text='Выбрать', var=chk_state)
                chk_state.set(False)
                chk.grid(row=2, column=1)

                self.combo = ttk.Combobox(self.root)
                self.combo['values'] = (1, 2, 3, 4, 5, "Text")
                self.combo.current(1)
                self.combo.grid(row=3, column=1, sticky=tkinter.W)

                self.text = tkinter.Text(self.root, font="100")
                self.text.grid(row=4, column=0, sticky=tkinter.W)

            def play_button(self):
                self.set_title("в процессе")
                play_func(data="старт")

            def stop_button(self):
                self.set_title("пауза")
                global play
                play = False

            def quit_button(self):
                self.set_title("выход")
                global play
                play = False
                self.quit()

            def set_title(self, title: str):
                self.root.title(title)

        if __name__ == "__main__":
            play = False
            app = Application(tk.Tk())
            thread_main = Thread(target=app.root.mainloop())
            thread_main.start()

    @staticmethod
    def example_generate_list():
        class Application(tk.Frame):
            def __init__(self, root, **kw):
                super().__init__(**kw)
                self.root = root
                self.initialize_user_interface()

            def initialize_user_interface(self):
                self.root.title("Попытка в приложение")
                self.root.grid_rowconfigure(0, weight=1)
                self.root.grid_columnconfigure(0, weight=1)
                self.root.config(background="black")
                self.root.geometry('1280x720')

                # Define the different GUI widgets
                self.SurnameNumber_label = tk.Label(self.root, text="Фамилия:", font="100")
                self.SurnameNumber_entry = tk.Entry(self.root, font="100")
                self.SurnameNumber_label.grid(row=0, column=0, sticky=tk.W)
                self.SurnameNumber_entry.grid(row=0, column=0)

                self.NameName_label = tk.Label(self.root, text="Имя:", font="100")
                self.NameName_entry = tk.Entry(self.root, font="100")
                self.NameName_label.grid(row=1, column=0, sticky=tk.W)
                self.NameName_entry.grid(row=1, column=0)

                self.PatronymicName_label = tk.Label(self.root, text="Отчество:", font="100")
                self.PatronymicName_entry = tk.Entry(self.root, font="100")
                self.PatronymicName_label.grid(row=2, column=0, sticky=tk.W)
                self.PatronymicName_entry.grid(row=2, column=0)

                self.Extra_label = tk.Label(self.root, text="Дополнительно:", font="100")
                self.Extra_entry = tk.Entry(self.root, font="100")
                self.Extra_label.grid(row=3, column=0, sticky=tk.W)
                self.Extra_entry.grid(row=3, column=0)

                self.submit_button = tk.Button(self.root, text="Добавить", font="100", command=self.insert_data)
                self.submit_button.grid(row=2, column=1, sticky=tk.W)

                self.exit_button = tk.Button(self.root, text="Выход", font="100", command=self.quit)
                self.exit_button.grid(row=0, column=1, sticky=tk.W)

                # Set the treeview
                self.tree = ttk.Treeview(self.root, columns=('№', 'Фамилия:', 'Имя:', 'Отчество:', 'Дополнительно:'))

                # Set the heading (Attribute Names)
                self.tree.heading('#0', text='№')
                self.tree.heading('#1', text='Фамилия')
                self.tree.heading('#2', text='Имя')
                self.tree.heading('#3', text='Отчество')
                self.tree.heading('#4', text='Дополнительно')

                # Specify attributes of the columns (We want to stretch it!)
                self.tree.column('#0', stretch=tk.YES)
                self.tree.column('#1', stretch=tk.YES)
                self.tree.column('#2', stretch=tk.YES)
                self.tree.column('#3', stretch=tk.YES)
                self.tree.column('#4', stretch=tk.YES)

                self.tree.grid(row=3, columnspan=4, sticky='nsew')
                self.treeview = self.tree

                self.id = 0
                self.iid = 0

            def insert_data(self):
                self.treeview.insert('', 'end', iid=self.iid, text=str(self.id + 1),
                                     values=(self.SurnameNumber_entry.get(), self.NameName_entry.get(),
                                             self.PatronymicName_entry.get(),
                                             str(self.SurnameNumber_entry.get() + self.NameName_entry.get() +
                                                 self.PatronymicName_entry.get())))
                self.iid = self.iid + 1
                self.id = self.id + 1

        app = Application(tk.Tk())
        thread_main = Thread(target=app.root.mainloop())
        thread_main.start()


#########################################################################################

