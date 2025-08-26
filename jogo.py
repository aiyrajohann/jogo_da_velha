# Jogo da Velha minimalista (Python 3)
wins = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

def show(b):
    print(f"\n {b[0]}|{b[1]}|{b[2]}\n-+-+-\n {b[3]}|{b[4]}|{b[5]}\n-+-+-\n {b[6]}|{b[7]}|{b[8]}\n")

b = [str(i) for i in range(1,10)]
p = "X"
for _ in range(9):
    show(b)
    c = input(f"Jogador {p}, casa (1-9): ")
    if c not in "123456789" or b[int(c)-1] in "XO":
        print("Inválido. Tente de novo."); continue
    b[int(c)-1] = p
    if any(b[a]==b[b_] == b[c_] == p for a,b_,c_ in wins):
        show(b); print(f"Venceu: {p}"); break
    p = "O" if p == "X" else "X"
else:
    show(b); print("Empate!")
