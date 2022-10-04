def read_cnab(file):
    type = file[0:1]
    date = file[1:9]
    value = file[9:19]
    cpf = file[19:30]
    card = file[30:42]
    hour = file[42:48]
    story_property = file[48:62]
    store_name = file[62:81]
    return {
        "type": type,
        "date": date,
        "value": value,
        "cpf": cpf,
        "card": card,
        "hour": hour,
        "story_property": story_property,
        "store_name": store_name,
    }
