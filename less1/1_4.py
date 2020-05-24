# Реализовать функцию bank, которая приннимает следующие
# аргументы: сумма депозита, кол-во лет, и процент. Результатом
# выполнения должна быть сумма по истечению депозита


def bank(p, l, t):
    s = p * (1 + l/12) * t / 100
    return s

vklad = 100000
stavka = 20
termin_monthes = 24

summ = bank(vklad, stavka, termin_monthes)

print(f"Сумма по депозиту: {summ}")
