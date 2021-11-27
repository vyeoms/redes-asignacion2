#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cliente UDP"""

import logging
import socket

logging.basicConfig(
    format='[CLIENTE] | %(levelname)-6s | %(message)s', level=logging.DEBUG)


def main():
    # Host y puerto utilizado para comunicarse con el server
    host = '127.0.0.1'
    port = 15000

    # Bytes a leer del socket
    bytes_to_read = 1024

    logging.info("Iniciando el cliente UDP...")

    # Se crea un socket IPv4 y UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    logging.info("Se creó el socket UDP.")
    logging.info("Cliente UDP inició correctamente.")

    while True:
        try:
            # Se toma la entrada del usuario
            print("Ingrese lo que quiera enviar al servidor:")
            print("(Presione CTRL-C para terminar)")
            data_out = raw_input(' > ')

            # Se debe revisar que la entrada no esté vacía
            while not data_out:
                data_out = raw_input(' > ')

            # Se envía el string al server
            s.sendto(data_out, (host, port))
            logging.debug("Se envió {} al host {} y al puerto {}.".format(
                data_out, host, port))

            # Se recibe la respuesta del server
            data_in, _ = s.recvfrom(bytes_to_read)
            print("El servidor dice: " + data_in + "\n")

        except KeyboardInterrupt:
            logging.info("Deteniendo el cliente UDP...")
            # Cierra el socket del lado del cliente cuando detecta keyboard interrupt
            s.close()
            logging.info("Se cerró el socket correctamente.")
            break

    logging.info("El cliente UDP finalizó correctamente.")


if __name__ == "__main__":
    main()
