import re



txt = """Hamas y la "promoción de la democracia" Noam Chomsky Hamas gano combinando una fuerte resistencia contra la ocupación militar con la creación de organizaciones sociales de base y de servicio a los pobres, una plataforma y una práctica que probablemente haría ganar votos en cualquier lugar. La victoria electoral de Hamas es ominosa pero comprensible, a la luz de los acontecimientos. Es enteramente justo describir a Hamas como fundamentalista, extremista y violentista, y como una seria amenaza a la paz y a un acuerdo políticamente justo. Sin embargo, es útil recordar que, en aspectos importantes, Hamas no es tan extremista como otros. Por ejemplo, declara que estaría de acuerdo con una tregua con Israel sobre la base de la frontera reconocida a nivel internacional antes de la guerra arabe-israeli de junio de l967.
La dirección IP es un conjunto de números que identifica, de manera lógica y jerárquica, a una Interfaz en la red de un dispositivo que utilice el protocolo o, que corresponde al nivel de red del modelo TCP/IP como, por ejemplo; 192.168.0.2, 192.168.6.5, 192.168.1.9, 192.168.6.2, 192.168.0.4 entre otros.
Un número de teléfono es una secuencia de dígitos utilizada para identificar una línea telefónica dentro de una red telefónica conmutada. El número contiene la información necesaria para identificar el punto final de la llamada algunos ejemplos son; 983 112 3453, 987 154 7372, 986 145 5657, 987 165 4342, 987 154 3435, 876 345 5657 solo por mencionar algunos
La hora es una unidad de tiempo que se corresponde con la vigésima cuarta parte de un día solar medio. Se utiliza para el tiempo civil y comprende 60 minutos o 3600 segundos, aunque pequeñas irregularidades en la rotación de la Tierra hacen que sean necesarios ajustes están 04:30 pm, 05:30 pm, 12:00 pm, 06:30 pm entre otros
Correos electrónicos como; maria@gmail.com, alexispeshoso@gmail.com, russelrenion@gmail.com, eduardo173@gmail.com
Ejemplos de URLs: www.google.com, www.red.com, www.futbolmundial.com, www.stormy.com, www.blackwidow.com, entre otros 
Códigos postales 77121, 98765, 56465, 97543, 67423, 87632"""

x = r"[A-Za-záéíóú]{7,}"

resulta = re.findall(x,txt)
print("---------------------------------------------")
print("PALABRAS CON LONGITUD 7 O MÁS")

for resultados in resulta:
    print(resultados)

print("---------------------------------------------")
print("2.Expresiones que NO finalicen con una vocal.")

y = r"[A-Za-záéíóú]{1,}[^aeiou\s/W]\b"
resulta1 = re.findall(y,txt)

for resultados1 in resulta1:
    print(resultados1)

print("---------------------------------------------")
print("3.Las palabras que inicien con “M” donde la segunda letra no sea vocal.")

x1 = r"[M][^aeiouáéíóú]\w{1,}"
resulta2 = re.findall(x1,txt)

for resultados2 in resulta2:
    print(resultados2)

print("---------------------------------------------")
print("4.Expresiones encerradas entre comillas")

y1 = r"(\"[\w\s]+\")"
resulta3 = re.findall(y1,txt)

for resultados3 in resulta3:
    print(resultados3)

print("---------------------------------------------")
print("5. Encuentra Direcciones Ip’s")

x2 = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
resulta4 = re.findall(x2,txt)

for resultados4 in resulta4:
    print(resultados4)

print("---------------------------------------------")
print("6. Encuentra Horas")

y2 = r"[0-9]{1,2}\:[0-9]{1,2}\s[a|p][m]"
resulta5 = re.findall(y2,txt)

for resultados5 in resulta5:
    print(resultados5)

print("---------------------------------------------")
print("7. Encuentra Telefonos")

x3 = r"[0-9]{1,3}\s[0-9]{1,3}\s[0-9]{1,4}"
resulta6 = re.findall(x3,txt)

for resultados6 in resulta6:
    print(resultados6)

print("---------------------------------------------")
print("8. Encuentra Correos Electronicos")

y3 = r"\w+[\@]+\w+[.]+\w+"
resulta7 = re.findall(y3,txt)

for resultados7 in resulta7:
    print(resultados7)

print("---------------------------------------------")
print("9. Encuentra de Url’s")

x4 = r"[Ww]+\w[.]\w+[.]\w+"
resulta8 = re.findall(x4,txt)

for resultados8 in resulta8:
    print(resultados8)

print("---------------------------------------------")
print("10. Encuentra de Código postal")

y4 = r"[0-9]{5}"
resulta9 = re.findall(y4,txt)

for resultados9 in resulta9:
    print(resultados9)