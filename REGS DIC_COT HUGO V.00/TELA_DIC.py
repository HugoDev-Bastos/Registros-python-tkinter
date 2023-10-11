from tkinter import *

form = Tk()

consultar = LabelFrame(form, text=" Consultar ")
consultar.pack(padx=10, pady=10, ipadx=8, ipady=8)

digiteTexto = Entry(consultar, font="Arial 15")
digiteTexto.pack(padx=8, pady=8, ipadx=8, ipady=8)

buttaoConsultar = Button(consultar, text="Buscar", font="Arial 13" )
buttaoConsultar.pack()


resultado = LabelFrame(consultar, text=" Resultado da Busca ")
resultado.pack(padx=10, pady=10, ipadx=8, ipady=8)

listConsultar = Listbox(resultado,)
listConsultar.pack()

###############

cadastrar = LabelFrame(form, text=" Cadastrar ")
cadastrar.pack(padx=10, pady=10, ipadx=8, ipady=8)

segmento = Listbox(cadastrar)
segmento.insert(1, "Material Hospitalar")
segmento.insert(2, "Medicamentos")
segmento.insert(3, "Expediente")
segmento.insert(4, "Outros")
segmento.pack()

digiteTexto = Entry(cadastrar, font="Arial 15")
digiteTexto.pack(padx=8, pady=8, ipadx=8, ipady=8)

buttaoConsultar = Button(cadastrar, text="Buscar", font="Arial 13" )
buttaoConsultar.pack()

form.mainloop()