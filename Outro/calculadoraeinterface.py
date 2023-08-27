import tkinter as tk

class CalculadoraApp:
    def __init__ (self, root):
        self.root = root
        self.root.title("Calculadora")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_ui()
        
    def create_ui(self):
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial",20))
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [ 
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
            ]
        
        row_val = 1
        col_val = 0
        for button_text in buttons:
            button = tk.Button(self.root, text=button_text, padx=20, pady=20,
                                font=("Arial", 20), command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Erro")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk ()
    app = CalculadoraApp(root)
    root.mainloop()

        