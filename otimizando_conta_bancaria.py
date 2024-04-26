def menu():
    menu = """\n
    Escolha a opção desejada: 
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Criar conta
    [5]Contas existentes
    [6]Criar usuário
    [7]Sair 
    """
    return input(menu)

def depositar (saldo, valor, extrato, /):
#Passando parametro por posição
#Deve-se colocar ', /', tudo o que estiver antes dele será passado por posição
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print(f"{extrato}Saldo: R$ {saldo: .2f}")
    else:
        print("#ERRO! O valor digitado não é valido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_de_saques, valor_limite_por_saque,quant_limite_por_saque):
#passando parametros apenas por palavras-chaves/forma nomeada.
#Deve-se colocar  '*,' antes do primeiro parâmetro

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > valor_limite_por_saque

    execedeu_n_saques = numero_de_saques >= quant_limite_por_saque

    if excedeu_saldo:
        print(f"Saldo insuficiente.\nSeu saldo é: R${saldo: .2f}")

    elif excedeu_limite:
        print(f"Não é possivel fazer saques a cima de R$500,00")

    elif execedeu_n_saques:
         print(f"Você excedeu o número máximo de saques!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor: .2f}\n"
        print(f"{extrato}Saldo: R${saldo: .2f}")
        numero_de_saques += 1

    else:
        print("Falha na operação. Informe um valor válido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(30, "*"))
    print("Seu extrato ainda está vazio." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("*".center(30, "*"))

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF:  ")
    usuarios = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("Usuario já existe")
        return
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Inform a data de nascimento: ")
    endereco = input("informe o endereço(Rua, numero, bairro,cidade, estado(sigla)): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print(linha)

def main():
    QUANT_LIMITE_POR_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    valor_limite_por_saque = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=valor_limite_por_saque,
                numero_saques=numero_de_saques,
                limite_saques=QUANT_LIMITE_POR_SAQUE,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, escolha novamente!")
main()