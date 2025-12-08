import customtkinter as ctk
from datetime import datetime
from tkinter import simpledialog, messagebox, Toplevel, Text, Scrollbar, RIGHT, Y, BOTH, END

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ARQUIVO_DADOS = "dados_transportadora.txt"


# ==========================================================
# FUNÇÃO --- SALVAR REGISTRO
# ==========================================================
def salvar_dados():
    dados = {
        "remetente": entry_remetente.get(),
        "destinatario": entry_destinatario.get(),
        "endereco": entry_endereco.get(),
        "produto": entry_produto.get(),
        "peso": entry_peso.get(),
        "codigo": entry_codigo.get(),
        "caminhao": entry_caminhao.get(),
        "funcionario": entry_funcionario.get(),
        "entrada": entry_entrada.get(),
        "saida": entry_saida.get(),
        "km_inicial": entry_km_inicial.get(),
        "km_final": entry_km_final.get()
    }

    if any(valor == "" for valor in dados.values()):
        avisos.configure(text="⚠ Preencha todos os campos!", text_color="red")
        return

    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    conteudo = (
        f"=== REGISTRO ===\n"
        f"Data: {data_atual}\n"
        f"Remetente: {dados['remetente']}\n"
        f"Destinatário: {dados['destinatario']}\n"
        f"Endereço: {dados['endereco']}\n"
        f"Produto: {dados['produto']}\n"
        f"Peso: {dados['peso']}\n"
        f"Código de Rastreio: {dados['codigo']}\n"
        f"Caminhão: {dados['caminhao']}\n"
        f"Funcionário: {dados['funcionario']}\n"
        f"Entrada: {dados['entrada']}\n"
        f"Saída: {dados['saida']}\n"
        f"KM Inicial: {dados['km_inicial']}\n"
        f"KM Final: {dados['km_final']}\n"
        f"-----------------------------\n"
    )

    with open(ARQUIVO_DADOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    avisos.configure(text="✔ Registro salvo com sucesso!", text_color="green")

    for entry in entradas:
        entry.delete(0, ctk.END)


# ==========================================================
# LER ARQUIVO COMPLETO
# ==========================================================
def carregar_registros():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return ""


# ==========================================================
# TELA PARA VISUALIZAR REGISTROS
# ==========================================================
def ver_registros():
    janela = Toplevel(app)
    janela.title("Registros Salvos")
    janela.geometry("700x600")

    texto = Text(janela, wrap="word", font=("Arial", 12))
    texto.pack(expand=True, fill=BOTH)

    barra = Scrollbar(texto)
    barra.pack(side=RIGHT, fill=Y)

    texto.config(yscrollcommand=barra.set)
    barra.config(command=texto.yview)

    conteudo = carregar_registros()
    texto.insert(END, conteudo if conteudo else "Nenhum registro encontrado.")


# ==========================================================
# FUNÇÃO --- ATUALIZAR REGISTRO (agora por DESTINATÁRIO)
# ==========================================================
def atualizar_registro():
    destinatario = simpledialog.askstring("Atualizar", "Digite o nome do Destinatário:")

    if not destinatario:
        return

    registros = carregar_registros().split("=== REGISTRO ===")
    novo_conteudo = ""
    encontrado = False

    for bloco in registros:
        if bloco.strip() == "":
            continue

        if f"Destinatário: {destinatario}" in bloco:
            encontrado = True

            ok = messagebox.askyesno("Confirmar", f"Atualizar registro do destinatário '{destinatario}'?")
            if not ok:
                return

            novo = {
                "remetente": simpledialog.askstring("Atualizar", "Novo remetente:"),
                "destinatario": simpledialog.askstring("Atualizar", "Novo destinatário:"),
                "endereco": simpledialog.askstring("Atualizar", "Novo endereço:"),
                "produto": simpledialog.askstring("Atualizar", "Novo produto:"),
                "peso": simpledialog.askstring("Atualizar", "Novo peso:"),
                "codigo": simpledialog.askstring("Atualizar", "Novo código de rastreio:"),
                "caminhao": simpledialog.askstring("Atualizar", "Novo caminhão:"),
                "funcionario": simpledialog.askstring("Atualizar", "Novo funcionário:"),
                "entrada": simpledialog.askstring("Atualizar", "Novo horário de entrada:"),
                "saida": simpledialog.askstring("Atualizar", "Novo horário de saída:"),
                "km_inicial": simpledialog.askstring("Atualizar", "Nova KM inicial:"),
                "km_final": simpledialog.askstring("Atualizar", "Nova KM final:")
            }

            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            bloco = (
                f"\nData: {data_atual}\n"
                f"Remetente: {novo['remetente']}\n"
                f"Destinatário: {novo['destinatario']}\n"
                f"Endereço: {novo['endereco']}\n"
                f"Produto: {novo['produto']}\n"
                f"Peso: {novo['peso']}\n"
                f"Código de Rastreio: {novo['codigo']}\n"
                f"Caminhão: {novo['caminhao']}\n"
                f"Funcionário: {novo['funcionario']}\n"
                f"Entrada: {novo['entrada']}\n"
                f"Saída: {novo['saida']}\n"
                f"KM Inicial: {novo['km_inicial']}\n"
                f"KM Final: {novo['km_final']}\n"
                f"-----------------------------\n"
            )

        novo_conteudo += "=== REGISTRO ===" + bloco

    if not encontrado:
        messagebox.showerror("Erro", "Destinatário não encontrado!")
        return

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        arquivo.write(novo_conteudo)

    messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")


# ==========================================================
# FUNÇÃO --- REMOVER REGISTRO
# ==========================================================
def remover_registro():
    codigo = simpledialog.askstring("Remover", "Digite o Código de Rastreio do registro:")

    if not codigo:
        return

    registros = carregar_registros().split("=== REGISTRO ===")
    novo_conteudo = ""
    encontrado = False

    for bloco in registros:
        if bloco.strip() == "":
            continue

        if f"Código de Rastreio: {codigo}" in bloco:
            encontrado = True
            ok = messagebox.askyesno("Confirmar", f"Deseja excluir o registro {codigo}?")
            if not ok:
                return
            continue

        novo_conteudo += "=== REGISTRO ===" + bloco

    if not encontrado:
        messagebox.showerror("Erro", "Código inexistente!")
        return

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        arquivo.write(novo_conteudo)

    messagebox.showinfo("Sucesso", "Registro removido!")


# ==========================================================
# INTERFACE
# ==========================================================
app = ctk.CTk()
app.title("Sistema da Transportadora")
app.geometry("760x820")

titulo = ctk.CTkLabel(app, text="Cadastro de Envio", font=("Arial", 24))
titulo.pack(pady=10)

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=20, fill="both", expand=True)

labels = [
    "Remetente:", "Destinatário:", "Endereço:", "Produto:", "Peso:",
    "Código de Rastreio:", "Caminhão:", "Funcionário:",
    "Horário de Entrada:", "Horário de Saída:",
    "KM Inicial:", "KM Final:"
]

entries = []

for i, texto in enumerate(labels):
    label = ctk.CTkLabel(frame, text=texto)
    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

    entry = ctk.CTkEntry(frame, width=400)
    entry.grid(row=i, column=1, padx=10, pady=10)

    entries.append(entry)

(entry_remetente, entry_destinatario, entry_endereco, entry_produto,
 entry_peso, entry_codigo, entry_caminhao, entry_funcionario,
 entry_entrada, entry_saida, entry_km_inicial, entry_km_final) = entries

entradas = entries

avisos = ctk.CTkLabel(app, text="")
avisos.pack(pady=5)

# ------- BOTÕES -------
ctk.CTkButton(app, text="Salvar Registro", command=salvar_dados).pack(pady=5)
ctk.CTkButton(app, text="Ver Registros", command=ver_registros).pack(pady=5)
ctk.CTkButton(app, text="Atualizar Registro", command=atualizar_registro).pack(pady=5)
ctk.CTkButton(app, text="Remover Registro", command=remover_registro).pack(pady=5)

app.mainloop()
