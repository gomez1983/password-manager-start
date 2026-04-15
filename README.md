# Password Manager

Um gerenciador de senhas desenvolvido em Python utilizando a biblioteca **Tkinter**. O aplicativo permite armazenar websites, e-mails e senhas em um arquivo local, além de contar com um gerador de senhas seguras integrado.

## 🛠️ Funcionalidades

* **Interface Gráfica:** Desenvolvida com Tkinter para facilitar a interação.
* **Gerador de Senhas:** Cria senhas fortes aleatórias misturando letras, números e símbolos.
* **Área de Transferência:** A senha gerada é copiada automaticamente para o seu CTRL+C (via pyperclip).
* **Persistência de Dados:** Salva as informações formatadas em um arquivo `data.txt`.
* **Validação:** Impede o salvamento de campos vazios e solicita confirmação antes de gravar.

## 🚀 Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Instale a dependência necessária para a área de transferência:
    ```bash
    pip install pyperclip
    ```
3.  Execute o script:
    ```bash
    python main.py
    ```

## 📂 Estrutura do Projeto

* `main.py`: Código principal com a lógica da UI e funções.
* `logo.png`: Imagem utilizada no cabeçalho do app.
* `data.txt`: Arquivo gerado automaticamente onde as senhas são armazenadas.

## 📝 Notas de Estudo
Este projeto faz parte do curso "100 Days of Code: The Complete Python Pro Bootcamp", focado em manipulação de arquivos, tratamento de erros e interfaces gráficas.