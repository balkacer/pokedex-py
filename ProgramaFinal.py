import requests, marshal, os, sys, goslate, collections
print("Programa de Pokemones. (Trabajo Final)")
urlApi = "https://pokeapi.co/api/v2/pokemon/"
pokeDt = []

#Clase Pokemon
class pokemon():
    nombre = ""
    dia = ""
    mes = ""
    an = ""
    latitud = ""
    longitud = ""
    comida = ""
    sangre = ""
    tipo = ""
    zodiaco = ""
    id_ = ""

#Cargar el archivo con los datos guardado anteriormente.
try:
    arch = open("datPk.dat", "br")
    pokeLoad = marshal.load(arch)
    for z in pokeLoad:
        pk = pokemon()
        pk.nombre = z[0]
        pk.dia = z[1]
        pk.mes = z[2]
        pk.an = z[3]
        pk.latitud = z[4]
        pk.longitud = z[5]
        pk.comida = z[6]
        pk.sangre = z[7]
        pk.tipo = z[8]
        pk.zodiaco = z[9]
        pk.id_ = z[10]
        pokeDt.append(pk)
    arch.close()
except:
    print("No se encontraron datos para mostrar.")

#Menu principal
def menu():
    print("""
Menú de opciones:

1-Agregar Pokemon
2-Ver Pokemones
3-Reportes
4-Exportar Pokemon
5-Exportar Mapa
6-Salir
""")
    select = input("Ingrese el número correspondiente a la opción: ")

    if select == "1":
        agPk()
    elif select == "2":
        verPk()
    elif select == "3":
        repPk()
    elif select == "4":
        expPk()
    elif select == "5":
        expMp()
    elif select == "6":
        salir()
    else:
        print("Por favor verifique la opcion ingresada.")
        menu()
        
#Gestionando Signo Zodiacal
def zodiaco():
    sig = ["Capricornio", "Acuario", "Piscis", "Aries",
        "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",
        "Libra", "Escorpio", "Sagitario"]
    fech = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
    
    dia = int(fechN[0:2])
    mes = int(fechN[3:5])
    mes = mes - 1
    an = int(fechN[6:10])
    edad = 2018 - an
    if dia > fech[mes]:
        mes = mes + 1
        if mes == 12:
            mes = 0
    global pkZod
    pkZod = sig[mes]

#Guardar los datos de los pokemones
def salvarPk():
    print("Ahora procede a ingresar los datos de",nomPk.capitalize(),"\n")
    global fechN
    fechN = input("Fecha de Nacimiento(dd-mm-aaaa): ")
    lat = float(input("Latidud(donde fue caputaro): "))
    long = float(input("Longitud(donde fue caputaro): "))
    cmFav = input("Comida Favorita: ")
    sangre = input("Tipo de Sangre: ")

    if sangre.upper() == "A+" or sangre.upper() == "A-":
        pass
    elif sangre.upper() == "B+" or sangre.upper() == "B-":
        pass
    elif sangre.upper() == "AB+" or sangre.upper() == "AB-":
        pass
    elif sangre.upper() == "O+" or sangre.upper() == "O-":
        pass
    else:
        print("No podemos comprobar este tipo de sangre, por favor ingrese uno valido.")
        sangre = input("Tipo de Sangre: ")

    tipo = [tipo['type']['name'] for tipo in datos['types']]
    tpPk = ", ".join(tipo)
    
    #tipES = goslate.Goslate()
    #trueType = tipES.translate(tpPk, 'es')
    
    idPk = datos['id']

    zodiaco()
    
    pk = pokemon()
    pk.nombre = nomPk.capitalize()
    pk.dia = int(fechN[0:2])
    pk.mes = int(fechN[3:5])
    pk.an = int(fechN[6:10])
    pk.latitud = lat
    pk.longitud = long
    pk.comida = cmFav
    pk.sangre = sangre
    pk.tipo = tpPk.title()
    pk.zodiaco = pkZod
    pk.id_ = idPk

    pokeDt.append(pk)

    input("Terminamos de agregar el pokemon exitosamente. Presione enter para volever al menu principal")
    menu()
    
#Agregar pokemones
def agPk():
    print ("Vamos a agregar Pokemones.\n")
    global nomPk
    nomPk = input("Digite el nombre del pokemon: ")
    print("""Espere, estamos validado el pokemon...
""")
    trueURL = urlApi + nomPk.lower()
    
    infDT = requests.get(trueURL)
    global datos
    datos = infDT.json()

    if infDT and nomPk.lower() == datos["name"]:
        print("Bien,",nomPk.capitalize(),"es un pokemon valido.")
        salvarPk()
    else:
        print("Lo siento, no creo que",nomPk.capitalize(),"sea un pokemon.")
        input("""
Puse cualquier tecla para continuar: """)
        menu()
        
#Ver Pokemones registrados    
def verPk():
    print ("Visualización de Pokemones guardados")
    
    if len(pokeDt) == 1:
        print("Hay solo un Pokemon registrado.")
    else:
        print("Hay",len(pokeDt),"Pokemones actuelmente en el registro.")

    for pkm in pokeDt:
        print("""
-Nombre: {}
-Fecha de Nacimiento: {}/{}/{}
-Tipo de Sangre: {}
-Signo Zodiacal: {}
-Tipo: {}
""".format(pkm.nombre, pkm.dia, pkm.mes, pkm.an, pkm.sangre, pkm.zodiaco, pkm.tipo))

    input("presione Enter para continuar.")
    menu()
    
#Reporte Cumpleaños por Mes
def repCxM():
    print("Reporte de Cumpleaños por Mes.\n")
    
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    fechaMes = int(input("Digite el mes de cumplaños: "))

    if fechaMes > 0 and fechaMes < 13:
        print("""
Bien veamos cuales pokemones estan de cumpleaños en""",meses[fechaMes-1]+"""...
""")
        count = 0
        for p in pokeDt:
            if fechaMes == p.mes:
                count = count + 1
                print(p.nombre,"cumple años el día",p.dia,"de",meses[fechaMes-1])
        if count == 0:
            print("""
No hay pokemones nacidos en este mes.
""")
        elif count == 1:
            print("""
Hay solo""",count,"""pokemon que está de cumpleaños en ese mes.
""")
        else:
            print("""
Hay""",count,"""pokemones que estan de cumpleaños en ese mes.
""")
        input("precione cualquier tecla para continuar... ")
        menu()
        
    else:
        input("El dato ingresado no es correcto. Por favor intentelo de nuevo... ")
        repCxM()
        
#Reportes Pokemon por Tipo
def repPxT():
    print("Reporte de Pokemones por Tipo.\n")
    
    frec = []
    for i in pokeDt:
        frec.append(i.tipo)
        cuenta = collections.Counter(frec)
    for h in cuenta:
        print("-"+h,"-("+str(cuenta[h])+")")
    input("Precione cualquier tecla para volver al menu... ")
    menu()
    
#Reporte Comida por Tipo
def repCxT():
    print("Reporte de Comidas por Tipo.\n")
    
    frec = []
    cuenta = ""
    for i in pokeDt:
        frec.append(i.tipo)
        cuenta = collections.Counter(frec)
    for h in cuenta:
        print(h+":")
        for g in pokeDt:
            if h == g.tipo:
                print(" -"+g.comida)
    input("Precione cualquier tecla para volver al menu... ")
    menu()

#Menu de opciones de reportes
def repPk():
    print("""
Reportes de Poquemons. Seleccione una opcion.

1-Reportes de ~Cumpleaños por mes~
2-Reportes de ~Pokemones por tipo~
3-Reportes de ~Comida por tipo~
""")
    rep = input("¿Que reporte desea ver?: ")

    if rep == "1":
        repCxM()
    elif rep == "2":
        repPxT()
    elif rep == "3":
        repCxT()
    else:
        print("Solo puede selecionar una de las opciones dadas")
        repPk()

#Cargar los datos de la plantilla a dataGet.
def getFile(file):
    if os.path.exists(file):
        arch = open(file, "r")
        dataGet = arch.read()
        arch.close()
        return dataGet

#Exportar a html con codigo directo
def expPk():
    imgPk = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
    print("Seleccione el pokemon que va a exportar.")
    
    for l in pokeDt:
        print(l.nombre)
    i = input("Digite el pokemon que desea exportar: ")
    for g in pokeDt:
        if i.capitalize() == g.nombre:
            edad = 2018 - g.an
            hola = imgPk+"{}.png".format(g.id_)
            
            htmlA = open(("Datos/PkExpotadosHtml/"+g.nombre+".html"),"a")
            htmlA.writelines(["""<html>
    <head>
        <link rel="shortcut icon" type="image/x-icon" href="poke.ico" />
	<link rel="stylesheet" type="text/css" href="style/style.css"/>
    <head/>
    <body>
	<h1>Estos son los datos del Pokemon<h1/>
	<table>
            <tr>
                <th><img src="{}"></th>
		<td></td>
	    </tr>
	    <tr>
		<th>Nombre</th>
		<td>{}</td>
	    </tr>
	    <tr>
		<th>Tipo</th>
		<td>{}</td>
	    </tr>
	    <tr>
		<th>Signo Zodiacal</th>
		<td>{}</td>
	    </tr>
	    <tr>
		<th>Edad</th>
		<td>{}</td>
	    </tr>
	    <tr>
		<th>Fecha de macimiento</th>
		<td>{}/{}/{}</td>
	    </tr>
	    <tr>
		<th>Comida Favorita</th>
		<td>{}</td>
	    </tr>
	    <tr>
		<th>Lat. de ubicaión</th>
		<td>{}</td>
	    </tr>
	    <tr>
		<th>Long. de ubicaión</th>
		<td>{}</td>
	    </tr>
	</table>
    <body/>
<html/>""".format(hola,g.nombre,g.tipo,g.zodiaco,str(edad),str(g.dia),str(g.mes),str(g.an),g.comida,g.latitud,g.longitud)])
            htmlA.close()
            
    input("Listo. Pulse cualquier tecla para ir al menu... ")
    menu()

#Exportar mapa html desde plantilla.
def expMp():
    print("Estamos generando el Mapa Pokemon")
    
    plat = getFile("MapaPlantilla.html")
    fnl = []
    for t in pokeDt:
        edad = 2018 - t.an
        deita = """L.marker(["""+str(t.latitud)+""","""+str(t.longitud)+"""])
    .addTo(map)
    .bindPopup('Hola soy """+t.nombre.title()+""" y tengo """+str(edad)+""" años.');"""
        fnl.append(deita)
    
    deita = " ".join(fnl)
    plat = plat.replace("{marcacdores}", deita)
    
    e = open("Datos/Mapa.html","w")
    e.write(plat)
    e.close()
    
    input("Listo. Pulse cualquier tecla para ir al menu... ")
    menu()

#Guardando datos en un archivo .dat
def cDt():
    nwDatos = []
    for poke in pokeDt:
        nw = []
        nw.append(poke.nombre)
        nw.append(poke.dia)
        nw.append(poke.mes)
        nw.append(poke.an)
        nw.append(poke.latitud)
        nw.append(poke.longitud)
        nw.append(poke.comida)
        nw.append(poke.sangre)
        nw.append(poke.tipo)
        nw.append(poke.zodiaco)
        nw.append(poke.id_)
        nwDatos.append(nw)
    
    dt = open("datPk.dat","bw")
    marshal.dump(nwDatos, dt)
    dt.close()

#Terminar el programa y guargar los datos.
def salir():
    salir = input("¿Seguro que desea salir? S/N: ")
    
    if salir.lower() == "s":
        cDt()
        sys.exit()
    elif salir.lower() == "n":
        print("Volviendo al menú principal...")
        menu()
    else:
        print("Digite S/N!")
        salir = input("¿Seguro que desea salir? S/N: ")

menu()
