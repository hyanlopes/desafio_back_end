def read_cnab(file):
    type = file[0:1]
    date = file[1:9]
    value = file[9:19]
    cpf = file[19:30]
    card = file[30:42]
    hour = file[42:48]
    story_property = file[48:62].strip().replace("/", "")
    store_name = file[62:81].strip().replace("/", "")

    if type == "1":
        type = "Débito"
    if type == "2":
        type = "Boleto"
    if type == "3":
        type = "Financiamento"
    if type == "4":
        type = "Crédito"
    if type == "5":
        type = "Recebimento Empréstimo"
    if type == "6":
        type = "Vendas"
    if type == "7":
        type = "Recebimento TED"
    if type == "8":
        type = "Recebimento DOC"
    if type == "9":
        type = "Aluguel"

    date = f"{date[0:4]}/{date[4:6]}/{date[6:]}"

    hour = f"{hour[0:2]}:{hour[2:4]}:{hour[4:]}"

    return {
        "type": type,
        "date": date,
        "value": int(value),
        "cpf": int(cpf),
        "card": str(card),
        "hour": hour,
        "store_property": str(story_property),
        "store_name": str(store_name),
    }
