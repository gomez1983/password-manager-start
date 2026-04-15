from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Gera uma senha aleatória segura e a copia para a área de transferência."""
    # LIMPEZA: Remove qualquer senha anterior antes de inserir a nova
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Cria listas de caracteres aleatórios usando list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))] # Para cada número sorteado entre 8 e 10, escolhe uma letra aleatória da lista
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]  # Para cada número sorteado entre 2 e 4, escolhe um algarismo aleatório da lista
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]  # Para cada número sorteado entre 2 e 4, escolhe um símbolo aleatório da lista

    # Une as listas e embaralha a ordem dos caracteres
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list) # Converte a lista em uma string única
    password_entry.insert(0, password) # Insere a senha gerada no campo de entrada
    pyperclip.copy(password) # Copia automaticamente para o CTRL+C do usuário

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Captura os dados inseridos, valida campos vazios e salva em arquivo TXT."""
    website = website_entry.get() # Obtém o texto do campo Website
    email = email_entry.get() # Obtém o texto do campo Email
    password = password_entry.get() # Obtém o texto do campo Password

    # Validação simples para impedir campos em branco
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Informe os campos de entrada.") # Exibe alerta de erro

    else:
        # Caixa de diálogo para confirmação do usuário
        is_ok = messagebox.askokcancel(title=website, message=f"Esses são os detalhes inseridos: \nEmail: {email} "
                                                    f"\nSenha: {password} \nOs dados estão corretos para salvá-los?")
        if is_ok:
            # Abre o arquivo no modo 'a' (append) para adicionar conteúdo sem apagar o anterior
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n") # Escreve os dados formatados
                website_entry.delete(0, END) # Limpa o campo de Website após salvar
                password_entry.delete(0, END) # Limpa o campo de Senha após salvar
                website_entry.focus()  # Retorna o foco para o campo Website para facilitar a próxima entrada

# ---------------------------- UI SETUP ------------------------------- #

window = Tk() # Cria o objeto da janela raiz
window.title("My password manager") # Define o título da barra superior
window.config(padx=50, pady=50) # Define margens internas de 50 pixels

# Configuração do Canvas para o logotipo
canvas = Canvas(height=200, width=200) # Define área de 200x200 para a imagem
logo_img = PhotoImage(file="logo.png") # Carrega o arquivo de imagem
canvas.create_image(100, 100, image=logo_img) # Posiciona a imagem no centro do canvas
canvas.grid(row=0, column=1) # Posiciona o canvas na grade: linha 0, coluna 1

# Labels (Rótulos)
website_label = Label(text="Website:") # Rótulo para o site
website_label.grid(row=1, column=0) # Alinhamento na linha 1, coluna 0
email_label = Label(text="Email/Username:") # Rótulo para o email
email_label.grid(row=2, column=0) # Alinhamento na linha 2, coluna 0
pass_label = Label(text="Password:") # Rótulo para a senha
pass_label.grid(row=3, column=0) # Alinhamento na linha 3, coluna 0

# Entries (Campos de Entrada)
website_entry = Entry(width=35) # Campo de entrada para o site
website_entry.grid(row=1, column=1, columnspan=2) # Ocupa duas colunas (1 e 2)
website_entry.focus() # Define o foco do teclado neste campo ao iniciar

email_entry = Entry(width=35) # Campo de entrada para o email
email_entry.grid(row=2, column=1, columnspan=2) # Ocupa duas colunas (1 e 2)
email_entry.insert(0, "andregc1983@gmail.com") # Insere um email padrão no início

password_entry = Entry(width=21) # Campo de entrada menor para a senha
password_entry.grid(row=3, column=1) # Alinhamento na linha 3, coluna 1

# Buttons (Botões)
generate_password_button = Button(text="Generate Password", command=generate_password) # Botão para gerar senha
generate_password_button.grid(row=3, column=2) # Alinhamento na linha 3, coluna 2

add_button = Button(text="Add", width=36, command=save) # Botão para salvar os dados
add_button.grid(row=4, column=1, columnspan=2) # Centralizado abaixo dos outros campos

window.mainloop() # Inicia o loop para manter a janela aberta