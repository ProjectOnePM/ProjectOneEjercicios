print "---------------EJERCICIO 8------------------"
print ""
print "---------------MATEMATICA------------------"
print ""
#matematica 90% nota 10% tareas
nota_matematica = input("ingrese nota del examen de matematica: ")
tarea_matematica1 = input("ingrese nota de tarea de matematica 1: ")
tarea_matematica2 = input("ingrese nota de tarea de matematica 2: ")
tarea_matematica3 = input("ingrese nota de tarea de matematica 3: ")
promedio_matematica=0.9*nota_matematica+0.1*((tarea_matematica1+tarea_matematica2+tarea_matematica3)/3)
print "Promedio matematica: ",promedio_matematica
print ""
print "---------------FISICA------------------"
print ""
#fisica 80% nota 20% tareas
nota_fisica = input("ingrese nota del examen de fisica: ")
tarea_fisica1 = input("ingrese nota de tarea de fisica 1: ")
tarea_fisica2 = input("ingrese nota de tarea de fisica 2: ")
promedio_fisica=0.8*nota_fisica+0.2*((tarea_fisica1+tarea_fisica2)/2)
print "promedio fisica: ",promedio_fisica
print ""
print "---------------QUIMICA------------------"
print ""
#quimica 85% nota 15%
nota_quimica = input("ingrese nota del examen de quimica: ")
tarea_quimica1 = input("ingrese nota de tarea de quimica 1: ")
tarea_quimica2 = input("ingrese nota de tarea de quimica 2: ")
tarea_quimica3 = input("ingrese nota de tarea de quimica 3: ")
promedio_quimica=0.85*nota_quimica+0.15*((tarea_quimica1+tarea_quimica2+tarea_quimica3)/3)
print "promedio quimica: ",promedio_quimica
#promedio total
print ""
print "---------------PROMEDIO TOTAL------------------"

promedio_total=(promedio_matematica+promedio_quimica+promedio_fisica)/3
print "promedio total: ",promedio_total
