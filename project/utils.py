def read_cnab(file):
    type = file[0:1]
    date = file[1:9]
    value = file[9:19]
    cpf = file[19:30]
    card = file[30:42]
    hour = file[42:48]
    story_property = file[48:62].strip()
    store_name = file[62:81].strip()
    return {
        "type": int(type),
        "date": int(date),
        "value": int(value),
        "cpf": int(cpf),
        "card": str(card),
        "hour": int(hour),
        "store_property": str(story_property),
        "store_name": str(store_name),
    }
