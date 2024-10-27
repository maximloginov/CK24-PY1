salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
for month in range(months):
    if month > 0:  # нет повышения цен в первый (0) месяц
        spend *= 1 + increase
    money_capital += salary - spend

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", abs(int(money_capital)))
