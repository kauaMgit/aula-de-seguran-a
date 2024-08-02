cargo=input('digite seu cargo')
dia_semana=input('digite o dia da semanan: ')
dias_da_semana_aceito = "segunda ,terça,quarta,quinta,sexta"
dias_da_semana_nao_aceito='sabado,domingo'

if cargo == 'estagiario' and dias_da_semana_aceito:
    print('acesso permitido')
elif cargo == 'gerente' :
    print ('acesso permitido')
else:
    cargo == 'estagiario' and dias_da_semana_nao_aceito
    print ('acesso negado')

# else
#     print ('erro)

#and (e) or (ou)