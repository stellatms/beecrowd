c1, n1, vu1 = input().split()
c1 = int(c1)
n1 = int(n1)
vu1 = float(vu1)

c2, n2, vu2 = input().split()
c2 = int(c2)
n2 = int(n2)
vu2 = float(vu2)

valor = n1 * vu1 + n2 * vu2
print(f"VALOR A PAGAR: R$ {valor:.2f}")