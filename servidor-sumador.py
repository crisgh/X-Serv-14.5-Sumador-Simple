#! /usr/bin/python
# -*-  coding: utf-8 -*-

#María Cristina Gallego Herrero

import socket

mysocket= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR,1 )
mysocket.bind(("localhost",2312))

mysocket.listen(4)

primer_num = True

try:
    while True:
        print "Waiting for connections"
        (recvSocket , address) = mysocket.accept()
        dato = recvSocket.recv(1024)
        try:
            numero = int(dato.split()[1][1:])
        except ValueError:
            print "Tienes que introducir un número"
            recvSocket.send("HTTP/1.1 200 OK \r\n\r\n" + "<html><body><h1> ERROR : Tienes que introducir un numero </h1></body></html>" + "\r\n")
            recvSocket.close()
            continue

        if primer_num : # Evito el if primer_num == "None"
            primer_numero = numero
            primer_num = False
            print "Necesito otro numero"
            recvSocket.send("HTTP/1.1 200 OK \r\n\r\n" + "<html><body><h1>Introduce otro numero</h1></body></html>" + "\r\n")

        else:
            suma = primer_numero + numero
            print "La suma es...." + str(suma)
            recvSocket.send("HTTP/1.1 200 OK \r\n\r\n" + "<html><body><h1> El primer numero era : " + str(primer_numero) + " el segundo numero : " + str(numero) + ", la suma es : " + str(suma) + "</h1></body></html>" + "\r\n")
            primer_num = True

        recvSocket.close()

except KeyboardInterrupt:
    print "Servidor cerrado"
    mysocket.close()
