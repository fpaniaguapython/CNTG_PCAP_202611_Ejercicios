opcion = 3

# Con if - elif
if opcion==1:
    print('Ha introducido 1')
elif opcion==2:
    print('Ha introducido 2')
elif opcion==3:
    print('Ha introducido 3')
else:
    print('Ha introducido otra cosa')

# Con match
match opcion:
    case 1:
        print('Ha introducido 1')
    case 2:
        print('Ha introducido 2')
    case 3:
        print('Ha introducido 3')
    case _: # Opción por defecto (es opcional)
        print('Ha introducido otra cosa')