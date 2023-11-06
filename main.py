import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Tile(ctk.CTkButton):
    def __init__(self, row, column, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.isMine = False
        self.x = row
        self.y = column

    def __str__(self):
        return f"x: {self.x} y: {self.y} isMine: {self.isMine}"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Minesweeper")
        # self.geometry(f"{1100}x{580}")

        self.title("Minesweeper")
        # ctk.CTkButton(master=self, text=f"{i}, {j}", command=(lambda i, j: self.button_function(i, j)))
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                t = Tile(j, i, master=self, text=f"{i}, {j}")
                # t.configure(command=(lambda i=t.x, j=t.y: self.button_function(i, j)))
                t.configure(command=(lambda _t=t: print(_t)))
                t.configure(height=50, width=50)
                row.append(t)
                t.grid(row=j, column=i, padx=5, pady=5)
            self.board.append(row)


if __name__ == '__main__':
    a = App()
    a.mainloop()
