money_capital = 20000  # Подушка безопасности
salary = 5000          # Ежемесячная зарплата
spend = 6000           # Траты за первый месяц
increase = 0.05        # Ежемесячный рост цен

month = 0
capital = money_capital
current_spend = spend

while True:
    budget = capital + salary
    if budget < current_spend:
        break
    capital = budget - current_spend
    month += 1
    current_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", month)
