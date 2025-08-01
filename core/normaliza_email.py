import re

#Verificacao basica se o email segue uma estrutura adequada
def verificar_email(email):
    padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if(re.fullmatch(padrao_email, email)):
        return f'=HYPERLINK("mailto:{email}", "{email}")'
    return "Email invalido"

#caso o email nao seja valido poderiamos tratar de acordo com as regras de negocio