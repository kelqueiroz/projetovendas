# Métricas do relatório de vendas de março
import csv

with open("vendas.csv", encoding="utf-8") as arquivo:
    linhas = list(csv.DictReader(arquivo))

receita = sum(float(linha["valor"]) for linha in linhas)
pedidos = sum(int(linha["pedidos"]) for linha in linhas)

print("Receita total:", receita)
print("Pedidos:", pedidos)

print("Ticket medio: ", receita / pedidos) 
