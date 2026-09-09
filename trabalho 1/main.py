from math import comb
import matplotlib.pyplot as plt


def disponibilidade(n, k, p):
    if not (1 <= k <= n and 0 <= p <= 1):
        raise ValueError("Use 1 <= k <= n e 0 <= p <= 1.")

    return sum(
        comb(n, i) * p**i * (1 - p)**(n - i)
        for i in range(k, n + 1)
    )


cenarios = {
    "k = 1": lambda n: 1,
    "k = n/2": lambda n: n // 2,
    "k = n": lambda n: n,
}

print(f"{'n':>3} {'p':>6} {'k=1':>12} {'k=n/2':>12} {'k=n':>12}")

for n in [2, 4, 6, 10]:
    for p in [0.5, 0.9, 0.99]:
        resultados = [
            disponibilidade(n, regra(n), p)
            for regra in cenarios.values()
        ]
        print(
            f"{n:>3} {p:>6.2f}"
            + "".join(f"{a:>12.4%}" for a in resultados)
        )

fig, eixos = plt.subplots(1, 2, figsize=(12, 4))

n = 10
valores_p = [i / 100 for i in range(101)]

for nome, regra in cenarios.items():
    valores_a = [
        disponibilidade(n, regra(n), p)
        for p in valores_p
    ]
    eixos[0].plot(valores_p, valores_a, label=nome)

eixos[0].set_title("Efeito de p — n = 10")
eixos[0].set_xlabel("Disponibilidade de cada servidor (p)")

p = 0.9
valores_n = list(range(2, 22, 2))

for nome, regra in cenarios.items():
    valores_a = [
        disponibilidade(n, regra(n), p)
        for n in valores_n
    ]
    eixos[1].plot(valores_n, valores_a, marker="o", label=nome)

eixos[1].set_title("Efeito de n — p = 0,9")
eixos[1].set_xlabel("Número de servidores (n)")

for eixo in eixos:
    eixo.set_ylabel("Disponibilidade do serviço")
    eixo.set_ylim(0, 1.05)
    eixo.grid(alpha=0.3)
    eixo.legend()

plt.tight_layout()
plt.show()
