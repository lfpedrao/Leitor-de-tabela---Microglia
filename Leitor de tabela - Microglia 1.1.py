#!/usr/bin/env python
# coding: utf-8

# In[20]:


from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox

class main():
    def __init__(self, run):
        import tkinter 
        top = Frame(run).pack()
        bottom = Frame(run).pack(side='bottom')
        
        self.title = Label(text="Leitor de Tabelas - Microglia", fg='red', font="Times 18")
        self.title.pack(side='top')
        
        self.cell = tkinter.IntVar()
        self.entrada = Entry(master=run)
        self.entrada.pack()
        self.entrada['textvariable'] = self.cell
        
        self.gerenciar = Button(master=run)
        self.gerenciar['text'] = 'Selecione a tabela'
        self.gerenciar['command'] = self.Table
        self.gerenciar.pack(side='bottom')
        
        self.message = Label(text="Por favor, selecione os arquivos que saem do ImageJ", font='Times 10')
        self.message.pack(side ='top')
        
    def Table(self):
        
        self.con = []
        self.branch = []
        self.endpoint = []
        self.arch = filedialog.askopenfilename()
        self.list = open(self.arch, 'r')
        self.list = self.list.read()
        self.list = self.list.split('\n')
        self.list.pop(0)
        
        
        for i in range (len(self.list) - 1):
            
            self.con.append(self.list[i].split(','))
            self.branch.append(int(self.con[i].pop(1)))
            self.endpoint.append(int(self.con[i].pop(1)))
            
        self.branch.sort()
        self.endpoint.sort()    
        
        self.branch = [k for k in self.branch if k > 9]
        self.endpoint = [o for o in self.endpoint if o > 2]        
        self.somabranch = sum(self.branch)
        self.somaendpoint = sum(self.endpoint)
        
        
        self.celulas = self.cell.get()
        
        self.finalbranch = (self.somabranch/self.celulas)/1000
        self.finalendpoint = self.somaendpoint/self.celulas
        
        
        L1 = Label(text="Branches: " + str(self.finalbranch) + "\nEndpoints: " + str(self.finalendpoint)).pack()
        
run = Tk()
run.title("Leitor de Tabela - Microglia")
run.geometry("480x164")
prog = main(run)
run.mainloop()


# In[ ]:





# In[ ]:




