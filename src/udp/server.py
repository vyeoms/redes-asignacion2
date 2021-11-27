#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Servidor UDP"""

import logging
import socket

logging.basicConfig(
    format='[SERVIDOR] | %(levelname)-6s | %(message)s', level=logging.DEBUG)


def main():
    # Host y puerto utilizado para comunicarse con los clientes
    host = '127.0.0.1'
    port = 15000

    # Bytes a leer del socket
    bytes_to_read = 1024

    # Contador de transacciones
    cnt = 0

    logging.info("Iniciando el servidor UDP...")

    # Se crea un socket IPv4 y UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    logging.info("Se creó el socket UDP.")

    # Se asocia un host y puerto al socket
    s.bind((host, port))
    logging.info("Escuchando en {}:{}".format(host, port))
    logging.info("Servidor UDP inició correctamente.")

    while True:
        try:
            # Se recibe la información que envían los clientes, así como su dirección
            data_in, addr = s.recvfrom(bytes_to_read)

            # Incrementa el contador de transacciones
            cnt += 1
            logging.debug("Número de transacciones = {}".format(cnt))

            # Cambia a mayúscula el string proveniente del cliente
            data_out = data_in.upper()

            # Se envía la información de vuelta al cliente
            s.sendto(data_out, addr)

        except KeyboardInterrupt:
            logging.info("Deteniendo el servidor UDP...")
            # Cierra el socket del lado del servidor cuando detecta keyboard interrupt
            s.close()
            logging.info("Se cerró el socket correctamente.")
            break

    logging.info("El servidor UDP finalizó correctamente.")


if __name__ == "__main__":
    main()
