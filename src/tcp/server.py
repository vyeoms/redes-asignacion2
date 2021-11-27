import socket
import logging
import sys

def main():
    
    logger = logging.getLogger('SERVIDOR')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(name)s] | [%(levelname)s]\t| %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    # Contador de transacciones
    contador = 0

    logger.info("Iniciando el servidor TCP.")
    # Se crea el socket para protocolos IPv4 - TCP:
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info("Socket TCP creado.")

    # Asignacion de una direccion IP y Puerto al socket TCP:
    socket_servidor.bind(("127.0.0.1", 4200))
    logger.info("Socket TCP asignado a la direccion 127.0.0.1:4200.")

    # Establecer el socket en modo escucha
    socket_servidor.listen(1)
    logger.info("Socket TCP en modo escucha...")

    # Al establecer una conexion se genera el socket socket_cliente:
    socket_cliente, dir_cliente = socket_servidor.accept()
    logger.info("Conexion establecida con el cliente desde " + str(dir_cliente))

    while True:
        try:
            # Se recibe la informacion:
            data_in = socket_cliente.recv(1024)
            # Se valida el dato:
            if data_in:
                # Se aumenta el contador de transacciones:
                contador = contador + 1
                logger.debug("Numero de transacciones = " + str(contador))
                # Se modifica el string recibido (Para verificar la transaccion):
                data_out = data_in.upper()
                # Se envia el dato modificado de vuelta al cliente:
                socket_cliente.send(data_out)
                
        # En caso de interrupcion se cierran los sockets
        except KeyboardInterrupt:
            logger.info("Terminando el servicio del servidor...")
            socket_cliente.close()
            logger.info("Conexion terminada con el cliente " + str(dir_cliente))
            socket_servidor.close()
            logger.info("Socket del servidor cerrado")
            sys.exit(0)

if __name__ == "__main__":
    main()