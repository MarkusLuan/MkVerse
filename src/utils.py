import datetime
import re

def checar_campos_obrigatorios(j: dict, campos_obrigatorios: list):
    pattern_email = re.compile(r"(\w+)\@(\w{3,}[\w\.]{0,})")

    for campo in campos_obrigatorios:
        # Valida se o campo foi informado
        if campo not in j:
            raise ValueError(f"O campo '{campo}' não foi informado!")

        # Valida campo de e-mail
        if campo == "email" and not pattern_email.match(j[campo]):
            raise ValueError("O endereço de e-mail é invalido!")
        
        # Valida os campos de data
        if campo.startswith("dt_"):
            data = None
            formatos_data = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]
            
            formatos_data_str = ' ou '.join(formatos_data)\
                .replace("%Y", "ANO")\
                .replace("%m", "MÊS")\
                .replace("%d", "DIA")\
                .replace("%H", "HORA")\
                .replace("%M", "MINUTO")\
                .replace("%S", "SEGUNDO")
            
            for formato in formatos_data:
                try:
                    data = datetime.datetime.strptime(j[campo], formato)
                except:
                    ...
            
            if data:
                j[campo] = data
            else:
                raise ValueError(f"O campo '{campo}' não foi preenchido corretamente!\nData deverá ser informada nos seguintes formatos {formatos_data_str}")