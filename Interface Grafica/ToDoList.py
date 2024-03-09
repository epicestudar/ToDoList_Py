import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To do List com GUI")
        self.geometry("400x400") # definindo tamanho
        style = Style(theme="flatly") # tema
        style.configure("Custon.TEntry", foreground="gray")

        # criação dos inputs para adicionar tarefa
        self.task_input = ttk.Entry(self, font=(
            "TkDefaultFont", 16), width=30, style="Custon.TEntry")
        self.task_input.pack(pady=10)

        # placeholder do input
        self.task_input.insert(0, "Adicione a tarefa aqui...")

        # quando o usuário clicar em adicionar a tarefa, o campo do input será limpado
        self.task_input.bind("<FocusIn>", self.limpar_placeholder)

        # restaura o espaço reservado quando o campo de entrada perde o foco
        self.task_input.bind("<FocusOut>", self.retornar_placeholder)

        # botão de adicionar tarefa
        ttk.Button(self, text="Adicione sua Tarefa", command=self.adicionar_tarefa).pack(pady=5)

        # criando uma listbox que mostrará as tarefas que o usuário adicionou
        self.task_list = tk.Listbox(self, font=(
            "TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # botão de marcar como concluída e de apagar tarefa
        ttk.Button(self, text="Tarefa Concluída", style="success.TButton",
                   command=self.tarefa_concluida).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Apagar Tarefa", style="danger.TButton",
                   command=self.deletar_tarefa).pack(side=tk.RIGHT, padx=10, pady=10)
        
        # botão dos dados da tarefa
        ttk.Button(self, text="Ver Dados", style="info.TButton",
                   command=self.visualizar_dados).pack(side=tk.BOTTOM, pady=10)
        
        self.carregar_tarefas()
    
    # função para visualizar os dados da tarefa
    def visualizar_dados(self):
        contador_concluidas = 0
        contador_total = self.task_list.size()
        for i in range(contador_total):
            if self.task_list.itemcget(i, "fg") == "green":
                contador_concluidas += 1
        messagebox.showinfo("Dados da Tarefa", f"Total de Tarefas: {contador_total}\nTarefas Completas: {contador_concluidas}")

    # criando as funções
    def adicionar_tarefa(self):
     task = self.task_input.get().strip()  # remove os espaços em branco em excesso
     if task and task != "Adicione a tarefa aqui...":
        self.task_list.insert(tk.END, task)
        self.task_list.itemconfig(tk.END, fg="orange")
        self.ordenar_tarefas()
        self.task_input.delete(0, tk.END)
        self.retornar_placeholder()
        self.salvar_tarefas()
     else:
        messagebox.showerror("Erro", "Por favor, insira uma tarefa válida.")

    def tarefa_concluida(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.ordenar_tarefas()
            self.salvar_tarefas()
        else:
           messagebox.showerror("Erro", "Por favor, selecione a tarefa que deseja concluir.")
    
    def deletar_tarefa(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.ordenar_tarefas()
            self.salvar_tarefas()
        else:
           messagebox.showerror("Erro", "Por favor, selecione a tarefa que deseja apagar.")
    
    def limpar_placeholder(self, event=None):
     if self.task_input.get() == "Adicione a tarefa aqui...":
        self.task_input.delete(0, tk.END)
        self.task_input.configure(style="TEntry")

    def retornar_placeholder(self, event=None):
     if not self.task_input.get():
        self.task_input.insert(0, "Adicione a tarefa aqui...")
        self.task_input.configure(style="Custom.TEntry")

    def carregar_tarefas(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])
                    self.ordenar_tarefas()
        except FileNotFoundError:
            pass
    
    def salvar_tarefas(self):
        data = [] # criando um vetor para armazenar as tarefas 
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

    def ordenar_tarefas(self):
        # obtém todas as tarefas na lista
        tasks = [self.task_list.get(idx) for idx in range(self.task_list.size())]
        # ordena as tarefas em ordem alfabética
        tasks.sort()
        # limpa a lista e reinsere as tarefas ordenadas
        self.task_list.delete(0, tk.END)
        for task in tasks:
            self.task_list.insert(tk.END, task)

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()