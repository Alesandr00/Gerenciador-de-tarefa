from tkinter import messagebox
import ttkbootstrap as tb

class TarefaApp:
    def __init__(self, root):
        self.style = tb.Style(theme='flatly')
        self.root = root
        self.root.title("Gerenciador de Tarefas - Alesandro")
        self.root.state('zoomed')

    # ... (outros métodos e funcionalidades aqui)

if __name__ == "__main__":
    root = tb.Window()
    app = TarefaApp(root)
    root.mainloop()
