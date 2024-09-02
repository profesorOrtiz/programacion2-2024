invitados = {'juan', 'pedro', 'daniela', 'daiana', 'gimena', 'david'}

asistentes = {'juan', 'daiana', 'gimena', 'david', 'alan'}

faltaron = invitados - asistentes

print(faltaron)

todos = invitados | asistentes

print(todos)

invitados_asistentes = invitados & asistentes

print(invitados_asistentes)

faltaron_extras = invitados ^ asistentes

print(faltaron_extras)
