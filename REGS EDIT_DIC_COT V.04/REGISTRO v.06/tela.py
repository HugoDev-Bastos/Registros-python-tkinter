from tkinter import *
from tkinter import ttk

window = Tk()

class Aplication():
    
    def __init__(self):
        self.window = window
        self.tela()
        self.FrameNovoRegistro()
        self.FrameConsultarRegistros()
        self.FrameCadastradosRegistros()
        
    def tela(self):
        self.window.title(" Registro de Pedidos de cotação ")
        self.window.configure(background='#1e3743')
        self.window.geometry("900x415")
        self.window.maxsize(width=825, height=435)  
        self.window.minsize(width=800, height=415)
        
    def FrameNovoRegistro(self):
        self.frameNovo = Frame(self.window)
        self.frameNovo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.30 )
        
        self.labelFrame_Novo = LabelFrame(self.frameNovo, text=" Novo Registro ")
        self.labelFrame_Novo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.95)
        
        ### cod
        self.lb_cod = Label(self.labelFrame_Novo, font="Arial, 10 ", text="Cod")
        self.lb_cod.place(relx=0.01, rely=0.02)
        self.entry_cod = Entry(self.labelFrame_Novo)
        self.entry_cod.place(relx=0.05, rely=0.02, relwidth=0.10, relheight=0.2)
        
        ### produto
        self.lb_produto = Label(self.labelFrame_Novo, font="Arial, 10 ", text="Produto")
        self.lb_produto.place(relx=0.17, rely=0.02)
        self.entry_produto = Entry(self.labelFrame_Novo)
        self.entry_produto.place(relx=0.25, rely=0.02, relwidth=0.60, relheight=0.2)
        
        ### marca
        self.lb_marca = Label(self.labelFrame_Novo, font="Arial, 10 ", text="Marca")
        self.lb_marca.place(relx=0.01, rely=0.3)
        self.entry_marca = Entry(self.labelFrame_Novo)
        self.entry_marca.place(relx=0.08, rely=0.3, relwidth=0.33, relheight=0.2)
        
        ### frte
        self.lb_frete = Label(self.labelFrame_Novo, font="Arial, 10 ", text="% Frete")
        self.lb_frete.place(relx=0.42, rely=0.3)
        self.entry_frete = Entry(self.labelFrame_Novo)
        self.entry_frete.place(relx=0.50, rely=0.3, relwidth=0.05, relheight=0.2)
        
        ### suframa
        self.lb_suframa = Label(self.labelFrame_Novo, font="Arial, 10 ", text="% Suframa")
        self.lb_suframa.place(relx=0.56, rely=0.3)
        self.entry_suframa = Entry(self.labelFrame_Novo)
        self.entry_suframa.place(relx=0.66, rely=0.3, relwidth=0.05, relheight=0.2)
        
        ### icms
        self.lb_icms = Label(self.labelFrame_Novo, font="Arial, 10 ", text="ICMS")
        self.lb_icms.place(relx=0.74, rely=0.3)
        self.entry_icms = Entry(self.labelFrame_Novo)
        self.entry_icms.place(relx=0.80, rely=0.3, relwidth=0.05, relheight=0.2)
        
        ### contato 
        self.lb_contato = Label(self.labelFrame_Novo, font="Arial, 10 ", text="Contato")
        self.lb_contato.place(relx=0.01, rely=0.6)
        self.entry_contato = Entry(self.labelFrame_Novo)
        self.entry_contato.place(relx=0.09, rely=0.6, relwidth=0.20, relheight=0.2)
        self.bt_contato = Button(self.labelFrame_Novo, text="Copy", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 7, 'bold'))
        self.bt_contato.place(relx=0.30, rely=0.6)
        
        ### email
        self.lb_email = Label(self.labelFrame_Novo, font="Arial, 10 ", text="Email")
        self.lb_email.place(relx=0.37, rely=0.6)
        self.entry_email = Entry(self.labelFrame_Novo)
        self.entry_email.place(relx=0.43, rely=0.6, relwidth=0.35, relheight=0.2)
        self.bt_email = Button(self.labelFrame_Novo, text="Copy", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 7, 'bold'))
        self.bt_email.place(relx=0.79, rely=0.6)
        
        ### BUTÕES
        
        # Botões Limpar
        self.bt_limpar = Button(self.labelFrame_Novo, text="Limpar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 9, 'bold'))
        self.bt_limpar.place(relx=0.86, rely=0.02, relwidth=0.12)   
             
        # Botões Novo
        self.bt_novo = Button(self.labelFrame_Novo, text="Novo", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 9, 'bold'))
        self.bt_novo.place(relx=0.86, rely=0.3, relwidth=0.12)
        
        # Botões Alterar
        self.bt_alterar = Button(self.labelFrame_Novo, text="Alterar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 9, 'bold'))
        self.bt_alterar.place(relx=0.86, rely=0.6, relwidth=0.12)
        
    def FrameConsultarRegistros(self):
        self.frameConsultar = Frame(window)
        self.frameConsultar.place(relx=0.01 , rely=0.32, relwidth=0.98, relheight=0.15)
        
        self.labelFrame_Novo = LabelFrame(self.frameConsultar, text=" Consultar Registros ")
        self.labelFrame_Novo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.95)
        
        self.pesquisar_entry = Entry(self.labelFrame_Novo)
        self.pesquisar_entry.place(relx=0.01, rely=0.02, relwidth=0.70, relheight=0.6)  
        btn_pesquisar = Button(self.labelFrame_Novo, text="Pesquisar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 10, 'bold'))
        btn_pesquisar.place(relx=0.72, rely=0.02, relwidth=0.12)
        btn_todos = Button(self.labelFrame_Novo, text="Todos", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 10, 'bold'))
        btn_todos.place(relx=0.86, rely=0.02, relwidth=0.12)
        
    def FrameCadastradosRegistros(self):
        self.frameCadastrados = Frame(window)
        self.frameCadastrados.place(relx=0.01 , rely=0.48, relwidth=0.98, relheight=0.50)
        
        self.labelFrame_Cadastrados = LabelFrame(self.frameCadastrados, text=" Registros Cadastrados ")
        self.labelFrame_Cadastrados.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.95)
        
        self.registrados = ttk.Treeview(self.labelFrame_Cadastrados, height=3, columns=( "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8" ))
        self.registrados.heading("#0", text="Cod")
        self.registrados.heading("#1", text="Produto")
        self.registrados.heading("#2", text="Marca")
        self.registrados.heading("#3", text="% Frete")
        self.registrados.heading("#4", text="% Suframa")
        self.registrados.heading("#5", text="% ICMS")
        self.registrados.heading("#6", text="Contato")
        self.registrados.heading("#7", text="Email")
        self.registrados.heading("#8", text="")

        
        self.registrados.column("#0", width=2)
        self.registrados.column("#1", width=100)
        self.registrados.column("#2", width=25)
        self.registrados.column("#3", width=15)
        self.registrados.column("#4", width=20)
        self.registrados.column("#5", width=15)
        self.registrados.column("#6", width=35)
        self.registrados.column("#7", width=100)
        self.registrados.column("#8", width=1)
        
        self.registrados.place(relx=0.01, rely=0.02, relwidth=0.95, relheight=0.75)
        
        self.scroolLista = Scrollbar(self.labelFrame_Cadastrados, orient='vertical')
        self.registrados.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.02, relwidth=0.02, relheight=0.50)
        
         # Botões Apagar
        self.bt_apagar = Button(self.frameCadastrados, text="Apagar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 9, 'bold'))
        self.bt_apagar.place(relx=0.02, rely=0.80, relwidth=0.1, relheight=0.12)    
        
Aplication()
window.mainloop()
