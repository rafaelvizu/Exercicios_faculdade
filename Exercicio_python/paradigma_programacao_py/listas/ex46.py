a = list()

for i in range(0, 10):
    print('=' * 40)
    a.append(int(input(f'Número {i + 1}: ')))

print('--' * 40)

soma_dos_quadrados = len(a) * (a[0] ** 2 + a[-1] ** 2) / 2
print(f'A soma dos quadrados dos números é: {soma_dos_quadrados}')
