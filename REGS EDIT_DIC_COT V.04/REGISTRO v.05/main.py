from tkinter import *
from tkinter import ttk
import sqlite3
import os
from unittest import result
import pyperclip as pc
from tkinter import messagebox


arquivo_db = os.path.dirname(__file__)
nome_arquivo = arquivo_db+ "\\registros.db"

colorfg = "#107db2"
fontLabelFrame = "Arial, 11 bold"
fontAll = "Arial, 10"

window = Tk()
window.iconphoto(False, PhotoImage(file='icon.png'))


class Funcs():
       
    def limpar(self): ##
        self.entry_cod.delete(0, END)
        self.entry_produto.delete(0, END)
        self.entry_marca.delete(0, END)
        self.entry_frete.delete(0, END)
        self.entry_suframa.delete(0, END)
        self.entry_icms.delete(0, END)
        self.entry_contato.delete(0, END)
        self.entry_email.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect(nome_arquivo)
        self.cursor = self.conn.cursor()
               
    def desconecta_bd(self):
        self.conn.close(); print('Desconectando ao Banco de dados...')
        
    def criar_tabela(self): ### Criar Tabela
        self.conecta_bd()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS registros (
                            cod INTEGER PRIMARY KEY,
                            produto CHAR(40) NOT NULL,
                            marca CHAR(40),
                            frete INTEGER(10),
                            suframa INTEGER(10),
                            icms INTEGER(10),
                            contato INTEGER(20),
                            email CHAR(40));
                        """)
        self.conn.commit(); print("Banco de dados criado...")
        self.desconecta_bd()

    def variaveis(self): ### Variaveis
        self.cod = self.entry_cod.get()
        self.produto = self.entry_produto.get()
        self.marca = self.entry_marca.get()
        self.frete = self.entry_frete.get()
        self.suframa = self.entry_suframa.get()
        self.icms = self.entry_icms.get()
        self.contato = self.entry_contato.get()
        self.email = self.entry_email.get()

    def cadastrar(self): ### Adicionar Cliente
        self.variaveis()

        if self.entry_produto.get()  == "":
            messagebox.showinfo(title="Erro de operação!" ,message="Digite o Nome do Produto para Cadastrar!")
            self.entry_produto.focus()
        else:
            self.conecta_bd()
            self.cursor.execute(""" INSERT INTO registros (produto, marca, frete, suframa, icms, contato, email) VALUES(?, ?, ?, ?, ?, ?, ?) """, (self.produto, self.marca, self.frete, self.suframa, self.icms, self.contato, self.email))
            self.conn.commit()   
            self.desconecta_bd()
            self.selecionar()
            self.limpar()
        
    def selecionar(self): ### Selecionar Lista
        self.registrados.delete(*self.registrados.get_children())
        
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, produto, marca, frete, suframa, icms, contato, email FROM registros ORDER BY produto ASC; """)
        
        for i in lista:
            self.registrados.insert("", END, values=i)
        self.desconecta_bd()

    def consultar_produto(self):
        self.conecta_bd()
                
        if self.pesquisar_entry.get()  == "":
            messagebox.showinfo(title="Erro de operação!" ,message="Digite algo no 'Campo de produto' para pesquisar!")
            self.pesquisar_entry.focus()
        else: 
            self.registrados.delete(*self.registrados.get_children())
            self.pesquisar_entry.insert(END, "%")
            
            nome = self.pesquisar_entry.get()
            self.cursor.execute(""" SELECT * FROM registros WHERE produto LIKE '%s' ORDER BY produto ASC """ % nome)
        
            buscanome = self.cursor.fetchall()
            for i in buscanome:
                self.registrados.insert("", END, values=i)
            self.limpar()
            self.desconecta_bd()
    
    def consulta_marca(self):
        self.conecta_bd()
                
        if self.pesquisar_marca_entry.get()  == "":
            messagebox.showinfo(title="Erro de operação!" ,message="Digite algo no 'Campo de Marca' para pesquisar!")
            self.pesquisar_marca_entry.focus()
        else: 
            self.registrados.delete(*self.registrados.get_children())
            self.pesquisar_marca_entry.insert(END, "%")
            
            nome = self.pesquisar_marca_entry.get()
            self.cursor.execute(""" SELECT * FROM registros WHERE marca LIKE '%s' ORDER BY marca ASC """ % nome)
        
            buscanome = self.cursor.fetchall()
            for i in buscanome:
                self.registrados.insert("", END, values=i)
            self.limpar()
            self.desconecta_bd()
                
    def consulta_contato(self):
        self.conecta_bd()
                
        if self.pesquisar_contato_entry.get()  == "":
            messagebox.showinfo(title="Erro de operação!" ,message="Digite algo no 'Campo de Contato' para pesquisar!")
            self.pesquisar_contato_entry.focus()
        else: 
            self.registrados.delete(*self.registrados.get_children())
            self.pesquisar_contato_entry.insert(END, "%")
            
            nome = self.pesquisar_contato_entry.get()
            self.cursor.execute(""" SELECT * FROM registros WHERE contato LIKE '%s' ORDER BY contato ASC """ % nome)
        
            buscanome = self.cursor.fetchall()
            for i in buscanome:
                self.registrados.insert("", END, values=i)
            self.limpar()
            self.desconecta_bd()
         
    def consultar_tudo(self):
        self.conecta_bd()
        
        self.pesquisar_entry.delete(0, END)
    
        self.registrados.delete(*self.registrados.get_children())
        self.pesquisar_entry.insert(END, "%")
        
        nome = self.pesquisar_entry.get()
        self.cursor.execute(""" SELECT * FROM registros WHERE produto LIKE '%s' ORDER BY produto ASC """ % nome)
        buscanome = self.cursor.fetchall()
        
        for i in buscanome:
            self.registrados.insert("", END, values=i)
            
        self.pesquisar_entry.delete(0, END)
        self.desconecta_bd() 
  
    def OnDoubleClick(self, event):
        self.limpar()  
        self.registrados.selection()
        for n in self.registrados.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.registrados.item(n, 'values')
            self.entry_cod.insert(END, col1)
            self.entry_produto.insert(END, col2)
            self.entry_marca.insert(END, col3)
            self.entry_frete.insert(END, col4)
            self.entry_suframa.insert(END, col5)
            self.entry_icms.insert(END, col6)
            self.entry_contato.insert(END, col7)
            self.entry_email.insert(END, col8)

    def deletar(self): ### Deletar Cliente
        self.variaveis()
        
        if self.entry_cod.get()  == "":
            messagebox.showinfo(title="Erro de operação!" ,message="Digite o número 'Cod' do Registro no campo 'Cod' ou dê um click duplo no Registro que deseja excluir e aperte no botão Excluir!")
            self.entry_cod.focus()
        else: 
            verify = messagebox.askyesno(title="Excluir Registro?", message="Deseja Excluir esse Registro?")
            if  verify == True:  
                self.conecta_bd()
                self.cursor.execute(""" DELETE FROM registros  WHERE cod = ? """, ([self.cod]))
                self.conn.commit()
                self.desconecta_bd()
                self.limpar()
                self.selecionar()
            else:
                messagebox.showinfo(message="Operação Cancelada!")
   
    def alterar(self): ### Alterar Cliente
        self.variaveis()
        
        if self.entry_produto.get()  == "":
            messagebox.showinfo(title="Erro de operação!" ,message="Escolha um registro já cadastrado para Alterar as Informações!")
        else:
            self.conecta_bd()
            self.cursor.execute(""" UPDATE registros SET produto = ?, marca = ?, frete = ?, suframa = ?, icms = ?, contato = ?, email = ? WHERE cod = ? """, (self.produto , self.marca , self.frete , self.suframa , self.icms , self.contato , self.email, self.cod))
            
            self.conn.commit()
            self.desconecta_bd()
            self.selecionar()
            self.limpar()
           
    def copy_contato(self):
        self.variaveis()    
        pc.copy(self.contato)
        
    def copy_email(self):
        self.variaveis()   
        pc.copy(self.email)        
        
class Aplication(Funcs):
    
    def __init__(self):
        self.window = window
        self.tela()
        self.FrameNovoRegistro()
        self.FrameConsultarRegistros()
        self.FrameCadastradosRegistros()
        self.criar_tabela()
        self.selecionar()
        self.Menus()
        window.mainloop()
        
    def tela(self):
        self.window.title(" Registros ")
        self.window.configure(background='#1e3743')
        self.window.geometry("900x480")
        self.window.maxsize(width=900, height=480)  
        self.window.minsize(width=800, height=450)
        
    def FrameNovoRegistro(self):
        self.frameNovo = Frame(self.window)
        self.frameNovo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.30 )
        self.labelFrame_Novo = LabelFrame(self.frameNovo, text=" Novo Registro ", font=fontLabelFrame, fg=colorfg)
        self.labelFrame_Novo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.95)
        
        ### cod
        self.lb_cod = Label(self.labelFrame_Novo, font=fontAll, text="Cod", fg=colorfg)
        self.lb_cod.place(relx=0.01, rely=0.02)
        self.entry_cod = Entry(self.labelFrame_Novo,)
        self.entry_cod.place(relx=0.05, rely=0.02, relwidth=0.10, relheight=0.2)
        
        ### produto
        self.lb_produto = Label(self.labelFrame_Novo, font=fontAll, text="Produto", fg=colorfg)
        self.lb_produto.place(relx=0.17, rely=0.02)
        self.entry_produto = Entry(self.labelFrame_Novo)
        self.entry_produto.place(relx=0.25, rely=0.02, relwidth=0.60, relheight=0.2)
        
        ### marca
        self.lb_marca = Label(self.labelFrame_Novo, font=fontAll, text="Marca", fg=colorfg)
        self.lb_marca.place(relx=0.01, rely=0.3)
        self.entry_marca = Entry(self.labelFrame_Novo)
        self.entry_marca.place(relx=0.08, rely=0.3, relwidth=0.33, relheight=0.2)
        
        ### frte
        self.lb_frete = Label(self.labelFrame_Novo, font=fontAll, text="% Frete", fg=colorfg)
        self.lb_frete.place(relx=0.42, rely=0.3)
        self.entry_frete = Spinbox(self.labelFrame_Novo, from_=10, to=50)
        self.entry_frete.place(relx=0.49, rely=0.3, relwidth=0.055, relheight=0.2)
        
        ### suframa
        self.lb_suframa = Label(self.labelFrame_Novo, font=fontAll, text="% Suframa", fg=colorfg)
        self.lb_suframa.place(relx=0.56, rely=0.3)
        self.entry_suframa = Spinbox(self.labelFrame_Novo, from_=0, to=50)
        self.entry_suframa.place(relx=0.66, rely=0.3, relwidth=0.05, relheight=0.2)
        
        ### icms
        self.lb_icms = Label(self.labelFrame_Novo, font=fontAll, text=" % Icms", fg=colorfg)
        self.lb_icms.place(relx=0.72, rely=0.3)
        self.entry_icms = Spinbox(self.labelFrame_Novo, from_=11, to=50)
        self.entry_icms.place(relx=0.80, rely=0.3, relwidth=0.05, relheight=0.2)
        
        ### contato 
        self.lb_contato = Label(self.labelFrame_Novo, font=fontAll, text="Contato", fg=colorfg)
        self.lb_contato.place(relx=0.01, rely=0.6)
        self.entry_contato = Entry(self.labelFrame_Novo)
        self.entry_contato.place(relx=0.09, rely=0.6, relwidth=0.20, relheight=0.2)
        self.bt_contato = Button(self.labelFrame_Novo, text="Copy", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 7, 'bold'), command=self.copy_contato)
        self.bt_contato.place(relx=0.30, rely=0.6)
        
        ### email
        self.lb_email = Label(self.labelFrame_Novo, font=fontAll, text="Email", fg=colorfg)
        self.lb_email.place(relx=0.37, rely=0.6)
        self.entry_email = Entry(self.labelFrame_Novo)
        self.entry_email.place(relx=0.43, rely=0.6, relwidth=0.35, relheight=0.2)
        self.bt_email = Button(self.labelFrame_Novo, text="Copy", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 7, 'bold'), command=self.copy_email)
        self.bt_email.place(relx=0.79, rely=0.6)
        
        ### BUTÕES
        
        # Botões Limpar
        self.bt_limpar = Button(self.labelFrame_Novo, text="Limpar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 9, 'bold'), command=self.limpar)
        self.bt_limpar.place(relx=0.86, rely=0.02, relwidth=0.12)   
             
        # Botões Cadastrar
        self.bt_novo = Button(self.labelFrame_Novo, text="Cadastrar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 9, 'bold'), command=self.cadastrar)
        self.bt_novo.place(relx=0.86, rely=0.3, relwidth=0.12)
        
        # Botões Alterar
        self.bt_alterar = Button(self.labelFrame_Novo, text="Alterar", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 9, 'bold'), command=self.alterar)
        self.bt_alterar.place(relx=0.86, rely=0.6, relwidth=0.12)
        
    def FrameConsultarRegistros(self):
        self.frameConsultar = Frame(window)
        self.frameConsultar.place(relx=0.01 , rely=0.32, relwidth=0.98, relheight=0.20)
        
        self.labelFrame_Novo = LabelFrame(self.frameConsultar, text=" Consultar Registros ", font=fontLabelFrame, fg=colorfg)
        self.labelFrame_Novo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.90)
        
        ## PESQUISAR PRODUTO
        self.pesquisar_entry = Entry(self.labelFrame_Novo)
        self.pesquisar_entry.place(relx=0.01, rely=0.02, relwidth=0.27, relheight=0.3)  
        
        btn_pesquisar = Button(self.labelFrame_Novo, text="Pesquisar por produto", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 8, 'bold'), command=self.consultar_produto)
        btn_pesquisar.place(relx=0.01, rely=0.42, relwidth=0.27)
        
        ## PESQUISAR MARCA
        self.pesquisar_marca_entry = Entry(self.labelFrame_Novo)
        self.pesquisar_marca_entry.place(relx=0.29, rely=0.02, relwidth=0.28, relheight=0.3)  
        
        btn_pesquisar_marca = Button(self.labelFrame_Novo, text="Pesquisar por marca", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 8, 'bold'), command=self.consulta_marca)
        btn_pesquisar_marca.place(relx=0.29, rely=0.42, relwidth=0.28)
        
        ## PESQUISAR CONTATO
        self.pesquisar_contato_entry = Entry(self.labelFrame_Novo)
        self.pesquisar_contato_entry.place(relx=0.58, rely=0.02, relwidth=0.27, relheight=0.3)  
        
        btn_pesquisar_contato = Button(self.labelFrame_Novo, text="Pesquisar por contato", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 8, 'bold'), command=self.consulta_contato)
        btn_pesquisar_contato.place(relx=0.58, rely=0.42, relwidth=0.27)       
        

        ## PESQUISAR TODOS
        
        btn_todos = Button(self.labelFrame_Novo, text="Mostrar\ntodos", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 10, 'bold'), command=self.consultar_tudo)
        btn_todos.place(relx=0.86, rely=0.02, relwidth=0.12, relheight=0.76)
        
    def FrameCadastradosRegistros(self):
    
        self.frameCadastrados = Frame(window)
        self.frameCadastrados.place(relx=0.01 , rely=0.53, relwidth=0.98, relheight=0.45)
        
        self.labelFrame_Cadastrados = LabelFrame(self.frameCadastrados, text=" Registros Cadastrados ", font=fontLabelFrame, fg=colorfg)
        self.labelFrame_Cadastrados.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.95)
        
        self.registrados = ttk.Treeview(self.labelFrame_Cadastrados, height=3, columns=( "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8" ))
        
        self.registrados.heading("#0", text="")
        self.registrados.heading("#1", text="Cod")
        self.registrados.heading("#2", text="Produto")
        self.registrados.heading("#3", text="Marca")
        self.registrados.heading("#4", text="% Frete")
        self.registrados.heading("#5", text="% Suframa")
        self.registrados.heading("#6", text="% ICMS")
        self.registrados.heading("#7", text="Contato")
        self.registrados.heading("#8", text="Email")
        
        self.registrados.column("#0", width=1)
        self.registrados.column("#1", width=1)
        self.registrados.column("#2", width=150)
        self.registrados.column("#3", width=50)
        self.registrados.column("#4", width=1)
        self.registrados.column("#5", width=20)
        self.registrados.column("#6", width=1)
        self.registrados.column("#7", width=50)
        self.registrados.column("#8", width=100)
        
        self.registrados.place(relx=0.01, rely=0.02, relwidth=0.95, relheight=0.75)
        
        self.scroolLista = Scrollbar(self.labelFrame_Cadastrados, orient='vertical')
        self.registrados.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.02, relwidth=0.02, relheight=0.75)
        self.registrados.bind("<Double-1>", self.OnDoubleClick)
        
         # Botões Apagar
        self.bt_apagar = Button(self.frameCadastrados, text="Excluir", bd=3, bg="#107db2", fg="#FFF", activebackground="#108ecb", activeforeground="#FFF", font=('verdana', 8, 'bold'), command=self.deletar)
        self.bt_apagar.place(relx=0.02, rely=0.80, relwidth=0.1, relheight=0.12)   
        
        self.infor_lb = Label(self.frameCadastrados, text="OBS: Para selecionar um registro dê um click duplo.", font="Arial, 10 bold", fg="#108ecb")
        self.infor_lb.place(relx=0.14, rely=0.80)

    def Menus(self): ### Menus
        
        menu_barra = Menu(self.window)
        self.window.config(menu = menu_barra)
        
        filemenu = Menu(menu_barra)
        filemenu2 = Menu(menu_barra)
        
        def Quit(): self.window.destroy()
        
        menu_barra.add_cascade(label="Opções", menu = filemenu)
        filemenu.add_command(label="Limpar Campos", command=self.limpar)
        filemenu.add_separator()
        filemenu.add_cascade(label="Sair", command=Quit)
       
        menu_barra.add_cascade(label="Categoria", menu = filemenu2)
        filemenu2.add_command(label="Material Hospitalar")
        filemenu2.add_separator()
        filemenu2.add_command(label="Medicamento Hospitalar")
        filemenu2.add_separator()
        filemenu2.add_command(label="Material Odontológico")
        filemenu2.add_separator()
        filemenu2.add_command(label="Medicamento Odontológico")
        
Funcs()   
Aplication()

