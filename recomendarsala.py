def recomendar_sala (participantes, tipo_de_reiniao):
    if tipo_de_reiniao == 'executiva':
        return('sala grande')
    elif participantes <= 5:
        return 'sala pequena'
    elif participantes <=15:
        return 'sala media'
    else:
        return 'sala grande'
participantes = int(input('digite o numero de participantes'))
tipo_de_reiniao = input('digite o tipo de reuniao')
    
if participantes <0:
        print('valor nao pode ser negativo ,erro!!!!')
elif tipo_de_reiniaonot not in ['normal', 'executiva']:
        print ('tipo de  reuniao invaliada')
else:
        recomendar_sala = recomendar_sala(participantes,tipo_de_reiniao)
        print (f'a sala ideal e:{recomendar_sala}')