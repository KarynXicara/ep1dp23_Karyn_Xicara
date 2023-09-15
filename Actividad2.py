class CentroEducativo:
    #Creamos los códigos
    codigo1="1"
    codigo2="2"
    codigo3="3"
    codigo4="4"
    codigo5="5"
    # Asignamos nombres de colegios
    colegio1 = "Colegio A"
    colegio2 = "Colegio B"
    colegio3 = "Colegio C"
    colegio4 = "Colegio D"
    colegio5 = "Colegio E"

    # Asignamos direcciones
    direccion1 = "Calle 1"
    direccion2 = "Avenida Principal"
    direccion3 = "Carrera 10"
    direccion4 = "Callejón del Sol"
    direccion5 = "Pasaje Flores"
    # Asignar números de teléfono ficticios
    telefono1 = "1234567890"
    telefono2 = "9876543210"
    telefono3 = "5555555555"
    telefono4 = "9999999999"
    telefono5 = "1111111111"

    # Asignar nombres de directores
    director1 = "Steven"
    director2 = "Christopher"
    director3 = "Juan"
    director4 = "Martin"
    director5 = "Alfonso"

    # Asignamos  direcciones web
    url1 = "https://www.ejemplo1.com"
    url2 = "https://www.ejemplo2.com"
    url3 = "https://www.ejemplo3.com"
    url4 = "https://www.ejemplo4.com"
    url5 = "https://www.ejemplo5.com"

    # Mi función permite concatenar los datos de los atributos
    def concatenar_datos(colegio, direccion, telefono, director, url):
        return colegio + " - " + direccion + " - " + telefono + " - " + director + " - " + url

    #Estos metodos almacenan los datos correspondientes a cada colegio

    resultado1 = concatenar_datos(colegio1, direccion1, telefono1, director1, url1)    

    resultado2 = concatenar_datos(colegio2, direccion2, telefono2, director2, url2)    

    resultado3 = concatenar_datos(colegio3, direccion3, telefono3, director3, url3)    

    resultado4 = concatenar_datos(colegio4, direccion4, telefono4, director4, url4)    

    resultado5 = concatenar_datos(colegio5, direccion5, telefono5, director5, url5)
    

