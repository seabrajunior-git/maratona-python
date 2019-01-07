# Estrutura Sequnecial Exercício 04
leitura = 1
qtd_notas_bimestrais = 4
soma = 0
while leitura <= qtd_notas_bimestrais:
  nota = float(input("Digite a {}ª nota:".format(leitura)))
  print("nota inserida com suceeso!")
  soma += nota
  leitura += 1
print("A média das notas foram : {:.2f}".format(soma/qtd_notas_bimestrais))
