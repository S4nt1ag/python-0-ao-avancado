# if / elif       / else
# se / se nao se / se nao

entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Seja bem vindo')
elif entrada == 'sair':
    print('Então vai embora')
elif entrada == '':
    print('Digita algo pelo menos')
else :
    print(f'{entrada} não é algo válido')
