#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import logging
import sys

def main():
    
    logger = logging.getLogger('CLIENTE')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(name)s] | [%(levelname)s]\t| %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.info("Iniciando el Cliente TCP.")

    # Se crea el socket para protocolos IPv4 - TCP:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info("Socket TCP creado.")

    # Conexion al servidor loopback
    s.connect(("127.0.0.1", 4200))
    logger.info("Conexion TCP establecida con el servidor @ 127.0.0.1:4200.\n")


    while True:
        try:
            # Solicitud al usuario del string a ser transmitido
            print("Ingrese el string que desea transmitir al servidor:")
            print("(Presione Ctrl + C para interrumpir la conexion del cliente)")
            data_out = raw_input(">")

            # se revisa que la entrada no esta vacia
            while not data_out:
                data_out = raw_input(">")
    
            s.send(data_out)
            # Se recibe la respuesta del servidor:
            data_in = s.recv(1024)
            print("Respuesta del servidor: " + data_in + "\n")

        # En caso de interrupcion se cierra la conexion
        except (KeyboardInterrupt, SystemExit):
            logger.info("Terminando el cliente...")
            s.shutdown(socket.SHUT_RDWR) # Indica al servidor que se cierra la conexion
            s.close() # Se cierra el socket del lado del cliente
            logger.info("Cliente terminado")
            sys.exit(0)

if __name__ == "__main__":
    main()
