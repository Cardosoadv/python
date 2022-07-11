from tkinter import *
inicial = Tk()
inicial.title("Sistema de Advocacia")

largura = 500
altura = 300

#resolução da tela
largura_tela = inicial.winfo_screenwidth()
altura_tela = inicial.winfo_screenheight()

#posição da janela
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2

print(posx, posy)

# geometry
inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


inicial.mainloop()
