print("En el siguiente formato tendras que poner tu nombre, salon, grupo y calificacion")
#Seccion de escribir nombre:
nombre_completo=input("\nEscribe tu nombre completo:")
#Impresion de tu nombre completo.
print(f"Muchisimas Gracias, {nombre_completo}.")
#Seccion de escribir salon y grupo
salon_grupo=input("\nEscribe tu salon y grupo:")
#Seccion de escribir calificacion dada por el maestro:
calificacion=float(input("\nEscribe la calificacion que te haya dado tu profesor en el salon:"))

#Ingreso de numero para saber que resultado tuviste en la materia 

if calificacion==10:
    print("Estuvo perfecto, eres sobresaliente")
elif calificacion>=8.5:
    print("Muy bien hecho")
elif calificacion>=7.5:
    print("Estuvo bien, pero puedes hacer algo mejor")
elif calificacion>=6:
    print("No estuvo bien esta vez, pero sera para la proxima")
elif calificacion>=5.5:
    print("Tienes derecho a darle un 500 al maestro")
elif calificacion<=5:
    print("Tendras que recursar la clase")
else:
    print("Valiste Pilin, vuelves a repetir")

print("Esos son tus resultados, ponerse en contacto con el profesor si tienes alguna duda")





