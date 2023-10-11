from multiprocessing import Value
from optparse import Option, Values
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import font 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import ttfonts
from reportlab.platypus  import SimpleDocTemplate, Image
import webbrowser 
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+ "\\cliente.db"

root = Tk()

class Relatorios():
    def printClientes(self):
        webbrowser.open("Cliente.pdf")
        
    def geraRelatCliente(self):
        self.c = canvas.Canvas("Cliente.pdf")
        
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        
        self.c.setFont("Helvetica-Bold", 20)
        self.c.drawString(200, 790, "Ficha do Registro")
        
        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 735, "Codigo: ")
        self.c.drawString(50, 710, "Produto: ")
        self.c.drawString(50, 685, "Contato: ")
        self.c.drawString(50, 660, "Email: ")
        
        self.c.setFont("Helvetica", 14)
        self.c.drawString(135, 735, self.codigoRel)
        self.c.drawString(135, 710, self.nomeRel)
        self.c.drawString(135, 685, self.telefoneRel)
        self.c.drawString(135, 660, self.cidadeRel)
        
        ## self.c.rect(20, 550, 550, 1, fill=True, stroke=False)
        ## self.c.rect(35, 590, 520, 230, fill=False, stroke=True)
        self.c.rect(35, 650, 520, 170, fill=False, stroke=True)
     
        self.c.showPage()
        self.c.save()
        self.printClientes()

class Funcs():
       
    def limpa_cliente(self): ##
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        
    def conecta_bd(self):
        self.conn = sqlite3.connect(nomeBanco)
        self.cursor = self.conn.cursor()
               
    def desconecta_bd(self):
        self.conn.close(); print('Desconectando ao Banco de dados...')
        
    def montarTabelas(self): ### Criar Tabela
        self.conecta_bd()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS cotacao (
                            cod INTEGER PRIMARY KEY,
                            produto CHAR(40) NOT NULL,
                            contato INTEGER(20),
                            email CHAR(40));
                        """)
        self.conn.commit(); print("Banco de dados criado...")
        self.desconecta_bd()

    def variaveis(self): ### Variaveis
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self): ### Adicionar Cliente
        self.variaveis()
        
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO cotacao (produto, contato, email) VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
        self.conn.commit()   
        self.desconecta_bd()
        
        self.select_lista()
        self.limpa_cliente()
        
    def select_lista(self): ### Selecionar Lista
        self.listaCli.delete(*self.listaCli.get_children())
        
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, produto, contato, email FROM cotacao ORDER BY produto ASC; """)
        
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        self.nome_entry.insert(END, "%")
        
        nome = self.nome_entry.get()
        self.cursor.execute(""" SELECT * FROM cotacao WHERE produto LIKE '%s' ORDER BY produto ASC """ % nome)
    
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
    
        self.limpa_cliente()
        self.desconecta_bd()
 
    def OnDoubleClick(self, event):
        
        self.limpa_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self): ### Deletar Cliente
        self.variaveis()
        
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM cotacao WHERE cod = ? """, ([self.codigo]))
        
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def altera_cliente(self): ### Alterar Cliente
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE cotacao SET produto = ?, contato = ?, email = ? WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.codigo))
        
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
        
class Application(Funcs, Relatorios):
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montarTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()
        
    def tela(self):
        self.root.title("Registro de Pedidos de cotação")
        self.root.configure(background='#1e3743')
        self.root.maxsize(width=850, height=700)  
        self.root.minsize(width=750, height=600)
        
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg="#dfe3e3",highlightbackground="#759fe6",highlightthickness=3)
        self.frame_1.place(relx=0.01 , rely=0.01, relwidth=0.98, relheight=0.35 )
        
        self.frame_2 = Frame(self.root, bd=4, bg="#dfe3e3",highlightbackground="#759fe6",highlightthickness=3)
        self.frame_2.place(relx=0.01 , rely=0.37, relwidth=0.98, relheight=0.61 )
        
    def widgets_frame1(self):
        
        ############### LABEL FRAME INSERIR ######################
    
        lf_inserir = LabelFrame(self.frame_1, text=" Novo Registros ", font=('verdana', 11, 'bold'), bg="#dfe3e3")
        lf_inserir.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.70)
        
        # Criação da label e entrada do codigo
        self.lb_codigo = Label(lf_inserir, font="Arial, 10 bold", text="Código", bg="#dfe3ee", fg="#107db2")
        self.lb_codigo.place(relx=0.01, rely=0.1)
        
        self.codigo_entry = Entry(lf_inserir)
        self.codigo_entry.place(relx=0.09, rely=0.1, relwidth=0.09, relheight=0.2)
        
        # Criação da label e entrada do nome
        self.lb_nome = Label(lf_inserir, font="Arial, 10 bold", text="Produto", bg="#dfe3ee", fg="#107db2")
        self.lb_nome.place(relx=0.20, rely=0.1, )
        
        self.nome_entry = Entry(lf_inserir)
        self.nome_entry.place(relx=0.29, rely=0.1, relwidth=0.69, relheight=0.2)
         
        # Criação da label e entrada do Telefone
        self.lb_telefone = Label(lf_inserir, font="Arial, 10 bold", text="Contato", bg="#dfe3ee", fg="#107db2")
        self.lb_telefone.place(relx=0.01, rely=0.5)
        
        self.telefone_entry = Entry(lf_inserir)
        self.telefone_entry.place(relx=0.09, rely=0.5, relwidth=0.35, relheight=0.2)
        
        # Criação da label e entrada do Cidade
        self.lb_cidade = Label(lf_inserir, font="Arial, 10 bold", text="Email", bg="#dfe3ee", fg="#107db2")
        self.lb_cidade.place(relx=0.46, rely=0.5)
        
        self.cidade_entry = Entry(lf_inserir)
        self.cidade_entry.place(relx=0.53, rely=0.5, relwidth=0.45, relheight=0.2)
        
        # Botões Limpar
        self.bt_limpar = Button(self.frame_1 ,text="Limpar Campos", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 10, 'bold'), command=self.limpa_cliente)
        self.bt_limpar.place(relx=0.53, rely=0.76, relwidth=0.2, relheight=0.2)   
             
        # Botões Novo
        self.bt_novo = Button(self.frame_1 ,text="Novo", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 10, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.74, rely=0.76, relwidth=0.1, relheight=0.2)
        
        # Botões Alterar
        self.bt_alterar = Button(self.frame_1,text="Alterar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 10, 'bold'), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.85, rely=0.76, relwidth=0.1, relheight=0.2)
        
    ################## LABEL FRAME PESQUISAR ###########################
        
    def lista_frame2(self): ### Treeview e Scrollbar
        
        lf_pesquisar = LabelFrame(self.frame_2, text=" Pesquisar ",font=('verdana', 11, 'bold') , bg="#dfe3e3")
        lf_pesquisar.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.25)
        
        self.pesquisar_entry = Entry(lf_pesquisar)
        self.pesquisar_entry.place(relx=0.01, rely=0.1, relwidth=0.60, relheight=0.5)  
             
        btn_pesquisar = Button(lf_pesquisar, text="Pesquisar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", 
        activeforeground="#FFF", font=('verdana', 10, 'bold'), command=self.busca_cliente)
        btn_pesquisar.place(relx=0.64, rely=0.1, relwidth=0.2, relheight=0.6)

        btn_todos = Button(lf_pesquisar, text="Todos", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 10, 'bold'), command=self.busca_cliente)
        btn_todos.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.6)
        
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4" ))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Produto")
        self.listaCli.heading("#3", text="Contato")
        self.listaCli.heading("#4", text="Email")
        
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=25)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=115)
        self.listaCli.column("#4", width=135)
        self.listaCli.place(relx=0.01, rely=0.28, relwidth=0.94, relheight=0.60)
        
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.28, relwidth=0.03, relheight=0.60)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
        
         # Botões Apagar
        self.bt_apagar = Button(self.frame_2,text="Apagar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.01, rely=0.90, relwidth=0.1, relheight=0.1)    

    def Menus(self): ### Menus
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)
        
        def Quit(): self.root.destroy()
        
        menubar.add_cascade(label="Opções", menu = filemenu)
        menubar.add_cascade(label="Relatorios", menu = filemenu2)
        menubar.add_cascade(label="Segmento", menu = filemenu3)
        
        filemenu.add_cascade(label="Sair", command=Quit)
        filemenu2.add_command(label="Limpar Campos", command=self.limpa_cliente)
        filemenu2.add_command(label="Ficha de Registro", command=self.geraRelatCliente)
        
        filemenu3.add_command(label="Material Hospitalar", command=lambda: self.conecta_bd('materialHospitaler.db'))
        filemenu3.add_command(label="Medicamento Hospitalar", command=lambda: self.conecta_bd('medicamentoHospitaler.db'))
        filemenu3.add_command(label="Material Odontológico", command=lambda: self.conecta_bd('materialOdontologico.db'))
        filemenu3.add_command(label="Medicamento Odontológico", command=lambda: self.conecta_bd('medicamentoOdontologico.db'))
        
Relatorios() 
Funcs()
Application()