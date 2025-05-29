import re

padrao = "Ka"
texto = "Kaue"
resultado = re.match(padrao, texto)
print(bool(resultado))

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,2}$'
    return bool(re.match(padrao, email))

emails = ['usuario-exemplo@dom.com.br', 'empresa@herval.com.br', '@domi.com']

for email in emails:
    print(f"{email}: {"Válido" if validar_email(email) else 'Inválido'}")

def validar_cpf(cpf):
    if len(cpf) != 11: 
        padrao = r'^[0-9]{3,}\.[0-9]{3,}\.'

