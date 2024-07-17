'''
Crie um programa onde tem um formulário feito em GUI com tkinter, onde tenha campo de entrada ex:
nome, sobrenome, idade, senha, cpf. Valide esse formulário, se o campo de entrada estiver vazio mostre um
pop-up, falando que o formulario precisa ser prenchido, se a idade for menor de 18 fale que o usuario precisa
ter no minino 18 anos, se o cpf estiver errado mostre um pop-up de erro. Esse formulário sera para uma entrada
de uma balada.

'''
import tkinter as tk
import tkinter.messagebox as mb
from datetime import date


janela = tk.Tk()

janela.title('CADASTRO BALADA')
janela.geometry('400x500')
janela.config(bg='#1E90FF')

# Texto principal
texto = tk.Label(janela, text='CADASTRO BALADA', bg='#1E90FF', font=('Arial', 20))
texto.pack()
# Nome usuario
texto_nome = tk.Label(janela, text='Digite seu Nome:', bg='#1E90FF', font=('Arial', 18))
texto_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()
# Sobrenome usuario
texto_sobrenome = tk.Label(janela, text='Digite seu Sobrenome:', bg='#1E90FF', font=('Arial', 18))
texto_sobrenome.pack()

entrada_sobrenome = tk.Entry(janela)
entrada_sobrenome.pack()
# ano nascimento usuario
texto_ano_nascimento= tk.Label(janela, text='Digite o Ano que você nasceu:', bg='#1E90FF', font=('Arial', 18))
texto_ano_nascimento.pack()

# Validando entrada ano nascimento com biblioteca datetime

entrada_ano_nascimento = tk.Entry(janela)
entrada_ano_nascimento.pack()
# CPF usuario
texto_cpf= tk.Label(janela, text='Digite seu CPF:', bg='#1E90FF', font=('Arial', 18))
texto_cpf.pack()

entrada_cpf = tk.Entry(janela)
entrada_cpf.pack()
# senha usuario

texto_senha= tk.Label(janela, text='Crie uma senha:', bg='#1E90FF', font=('Arial', 18))
texto_senha.pack()

entrada_senha = tk.Entry(janela)
entrada_senha.pack()

# Botão e validação
def validar():
    if entrada_nome.get() == '' or entrada_sobrenome.get() == '' or entrada_ano_nascimento.get() == '' or entrada_cpf.get() == '' or entrada_senha.get() == '':
        mb.showerror("Erro", "Preencha todos os campos")
        return
    
    try:
        ano_nascimento = int(entrada_ano_nascimento.get())
    except ValueError:
        mb.showerror("Erro", "Ano de nascimento inválido. Digite apenas números.")
        return
    # Pegando ano atual e fazendo a soma
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    
    if idade < 18:
        mb.showerror("Erro", "Você não pode se cadastrar, pois você não tem 18 anos ")
        return
    # Valida CPF de usuario
    cpf_digitado = entrada_cpf.get()
    
    if len(cpf_digitado) != 11:
        mb.showerror("Erro", "CPF inválido. O CPF deve ter 11 dígitos.")
        return
    
    else:
        mb.showinfo("Finalizado", "Cadastro realizado com exido!")
        entrada_nome.delete(0, tk.END)
        entrada_sobrenome.delete(0, tk.END)
        entrada_ano_nascimento.delete(0, tk.END)
        entrada_cpf.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)


    
    

    
    
botao = tk.Button(janela, text='Enviar', command=validar)
botao.pack()





janela.mainloop()