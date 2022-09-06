
salary = int(input('Зарплата за месяц > '))
credit = int(input('Месячный платеж по кредиту > '))
utilities = int(input('Коммунальные услуги > '))


#print(name, surname,",", 2022 - year)
print(f"Остаток: {salary - credit - utilities}\n")