print(f''' 
============= PAINEL DE LOGIN =============
sistema para calcular o notas das escolas.
criado por mim: ZkDragonZk , Estudante De TI
===========================================
''')

primeira = int(input('Primeiro Bimestre: '))
segundo = int(input('Segundo Bimestre: '))
calcular = (primeira + segundo) - 180
print('Você Precisa Tirar No Total: {} Para Pode Passar!'.format(calcular))