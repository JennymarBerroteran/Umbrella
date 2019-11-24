#lista original de invitados

guest_dinner = ['mama', 'papa', 'abuela', 'abuelo', 'amigos']
print(guest_dinner)
message = 'te quiero invitar cordialmente a mi cena'
print(f'\n {guest_dinner[0].title()} ' + message)
print(f'\n {guest_dinner[1].title()} ' + message)
print(f'\n {guest_dinner[2].title()} ' + message)
print(f'\n {guest_dinner[3].title()} ' + message)
print(f'\n {guest_dinner[4].title()} ' + message)

#invitados que no pueden asistir

guest_n_dinner = ['abuela', 'abuelo']
print(f'\n\t Invitados que no podran asistir a la cena {guest_n_dinner}')

#nuevos invitados

guest_dinner[2] = 'tia'
guest_dinner[3] = 'tio'
print(f'\t{guest_dinner}')

print(f'\n {guest_dinner[0].title()} ' + message)
print(f'\n {guest_dinner[1].title()} ' + message)
print(f'\n {guest_dinner[2].title()} ' + message)
print(f'\n {guest_dinner[3].title()} ' + message)
print(f'\n {guest_dinner[4].title()} ' + message)

#invitando amas personas
print('Queridos ivitados he encontrado una mesa para cenar mas grande, se nos uniran mas invitados')
guest_dinner.insert(0, 'kevin')
guest_dinner.insert(3, 'ana')
guest_dinner.append('alejandro')
print(f'\n {guest_dinner[0].title()} ' + message)
print(f'\n {guest_dinner[1].title()} ' + message)
print(f'\n {guest_dinner[2].title()} ' + message)
print(f'\n {guest_dinner[3].title()} ' + message)
print(f'\n {guest_dinner[4].title()} ' + message)
print(f'\n {guest_dinner[5].title()} ' + message)
print(f'\n {guest_dinner[6].title()} ' + message)
print(f'\n {guest_dinner[7].title()} ' + message)

#eliminando invitados de la lista
print('\n\tSolo puedo invitar a 2 personas')
invitado_eliminado =guest_dinner.pop()
message_2 = 'lo siento mucho pero no te puedo invitar :p'
print(f'{invitado_eliminado.title()} ' + message_2)

invitado_eliminado =guest_dinner.pop()
print(f'{invitado_eliminado.title()} ' + message_2)

invitado_eliminado =guest_dinner.pop()
print(f'{invitado_eliminado.title()} ' + message_2)

invitado_eliminado =guest_dinner.pop()
print(f'{invitado_eliminado.title()} ' + message_2)

invitado_eliminado =guest_dinner.pop()
print(f'{invitado_eliminado.title()} ' + message_2)

invitado_eliminado =guest_dinner.pop()
print(f'{invitado_eliminado.title()} ' + message_2)

print(f'Invitados  restantes {guest_dinner}')

#lista vacia
del guest_dinner[0]
del guest_dinner[0]

print(guest_dinner)
