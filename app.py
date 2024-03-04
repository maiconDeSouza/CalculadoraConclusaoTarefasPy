import os
print('Olá, digite quantas tarefas você agendou para está semana?')
tasks_of_the_week = input()

print('Agora digite quantas tarefas você já concluiu?')
completed = input()

try:
    number_asks_of_the_week = int(tasks_of_the_week)
    number_completed = int(completed)
    result = (number_completed / number_asks_of_the_week) * 100
    message_return = f'Você teve um total de {number_asks_of_the_week} tarefas essa semana e concluíu {
        number_completed} isso equivale há {result:.2f}%'
    os.system('clear')
    print(message_return)
    print()
except Exception as error:
    os.system('clear')
    print(error)
    print('Por favor, digite apenas números e que sejam interiros com 3, 2, 17, 23...')
    print('Tente novamente!')
    print()
