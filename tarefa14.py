#Baseando-se nos Scripts "Matplotlib_Gráfico_Circular", "Matplotlib_Gráfico_de_Barras",
#e "Introdução_ao_Matplotlib_Gráfico_de_linhas", bem como nos vídeos da gravação da sessão,
#crie um ou vários scripts em que crie algumas funções e um menu de interação com o utilizador,
#criando uma situação em que seja útil tratar os dados com análise gráfica através da biblioteca MatPlotLib!

import matplotlib.pyplot as plt

def GraficoLinhas():
    
    x = []
    y = []
    
    print("Insira 5 valores para o Eixo X")
    for i in range(3):
        dadosX = float(input("Eixo X: {} valor:".format(i + 1)))
        x.append(dadosX)
        
    print("Insira 5 valores para o Y")
    for i in range(3):
        dadosY = float(input("Eixo Y: {} valor:".format(i + 1)))
        y.append(dadosY)
        
    plt.plot(x, y)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Gráfico de Linha")
    plt.show()

def GraficoBarras():
    
    produtos = []
    quantidade = []
    
    print("Insira 5 tipos de produtos e suas quantidades")
    for i in range(3):
        prod = input("Produto {}:".format(i + 1))
        produtos.append(prod)
        quant = int(input("Quantidade {}:".format(i + 1)))
        quantidade.append(quant)
    
    plt.bar(produtos, quantidade)  
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade')
    plt.title('Gráfico de Barras')
    plt.show()
    
def GraficoCircular():
    
    frutas = []
    vendas = []
    
    print("Frutas e quantidades vendidas")
    for i in range(3):
        fruta = input("Fruta {}:".format(i + 1))
        frutas.append(fruta)
        quant = int(input("Quantidade {}:".format(i + 1)))
        vendas.append(quant)
        
    plt.pie(vendas, labels = frutas, autopct = '%1.1f%%')
    plt.title('Gráfico Circular')
    plt.show()

while True: 
    print("Gráficos:")
    print("1 - Linhas")
    print("2 - Barras")
    print("3 - Circular")
    print("4 - Sair")           
        
    try:
        opcao = int(input("Escolha um tipo de gráfico: "))
        
        if opcao == 1:
            GraficoLinhas()
        elif opcao == 2:
            GraficoBarras()
        elif opcao == 3:
            GraficoCircular()
        elif opcao == 4:
            print("Saindo....")
            break
        else:
            print("Erro, opção inválida!")
    except ValueError:
        print("Escolha opções disponíveis no menu!")
