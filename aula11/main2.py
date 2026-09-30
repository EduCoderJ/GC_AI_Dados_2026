import random

cardapio = {
    "chocolate": 5.00,
    "baumilha": 4.50,
    "morango": 3.00,
    "flocos": 9.00
}

brindes = ["Canudo", "Copo Personalizado", "Gelo", "Badge"]

def mostrar_cardapio():
    print("Cardápio:")
    for sabor, preco in cardapio.items():
        print(f"{sabor}, R${preco:.2f}")

def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor = input("\nEscolha um sabor (ou digite 'fechar' para finalizar): ")
        if sabor == "fechar":
            break
        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"{sabor} adicionado ao pedido.")
        else:
            print("Sabor não disponível. Tente novamente.")
    return pedido, total

mostrar_cardapio()
pedido, total = fazer_pedido()

print(f"Pedido finalizado!\nItens do pedido: {pedido}")
print(f"Total a pagar: R${total:.2f}")

if total > 15:
    print(f"Parabéns! Você ganhou um brinde: {random.choice(brindes)}")
