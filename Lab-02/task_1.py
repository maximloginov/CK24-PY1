money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

money_remains = money_capital  # начальный бюджет
month_counter = 0              #
while money_remains > 0:       # пока не вышли из бюджета
    month_counter += 1
    if month_counter > 1:      # рост расходов со второго месяца
        spend *= 1 + increase
    money_remains += salary - spend
month_counter -= 1             # коррекция, в последний месяц вышли из бюджета

print("Количество месяцев, которое можно протянуть без долгов:", month_counter)
