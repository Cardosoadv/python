import tkinter as tk

def login():
    print("First Name: %s\nLast Name: %s" % (nome_txt.get(), senha_txt.get()))

master = tk.Tk()
tk.Label(master, 
         text="Nome").grid(row=0)
tk.Label(master, 
         text="Senha").grid(row=1)

nome_txt = tk.Entry(master)
senha_txt = tk.Entry(master)

nome_txt.grid(row=0, column=1)
senha_txt.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=login).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()