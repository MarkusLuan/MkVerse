def checar_campos_obrigatorios(j: dict, campos_obrigatorios: list):
    for campo in campos_obrigatorios:
        if campo not in j:
            raise ValueError(f"O campo '{campo}' não foi preenchido corretamente!")