# Sistema de Venta de Entradas (Servidor en Python)

## Descripción
Este proyecto es un servidor de venta de entradas implementado en Python, que utiliza sockets y threading para manejar conexiones simultáneas de varios clientes. El sistema permite a los usuarios comprar entradas para un evento o consultar información del mismo a través de comandos enviados por clientes.

## Características
- **Manejo de múltiples clientes**: Usa `threading` para atender varias solicitudes al mismo tiempo.
- **Validaciones robustas**: Se limita la cantidad de entradas por solicitud y se asegura que no se vendan más asientos de los disponibles.
- **Comandos simples**: Los clientes pueden interactuar con el servidor usando comandos como:
  - `BUY <num_asientos>`: Para comprar entradas.
  - `INFO`: Para obtener información del evento.

## Requisitos
- Python 3.7 o superior.

## Instalación
1. Clona este repositorio en tu equipo local:
   ```bash
   git clone https://github.com/jorgerebolledoa/Comunicacion-de-computadore
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Comunicacion-de-computadore
   ```

## Uso

### Ejecución del servidor
1. Asegúrate de que los puertos especificados en el código no estén siendo utilizados.
2. Inicia el servidor ejecutando el archivo principal:
   ```bash
   python server.py
   ```
   El servidor estará escuchando en `127.0.0.1:65432` por defecto.

### Interacción con el cliente
Los clientes pueden enviar comandos al servidor mediante sockets. Algunos ejemplos son:

#### Comprar entradas:
   ```
   BUY <num_asientos>
   ```
   Donde `<num_asientos>` es el número de entradas deseadas (máximo 5 por solicitud).

#### Consultar información del evento:
   ```
   INFO
   ```

#### Respuestas del servidor:
- **Compra exitosa**:
  ```
  COMPRADO: Total=<total>, Asientos=[<lista_de_asientos>]
  ```
- **Error por límites de compra**:
  ```
  ERROR: No puede comprar más de 5 entradas por petición.
  ```
- **Error por asientos insuficientes**:
  ```
  ERROR: No hay suficientes asientos disponibles.
  ```
- **Error por comando desconocido**:
  ```
  ERROR: Comando desconocido.
  ```

# Servidor de Juego por Turnos (Protocolo UDP)

## Descripción
Este proyecto es un servidor de juego por turnos implementado en Python, que utiliza sockets UDP para la comunicación con clientes. Los jugadores pueden unirse al juego y participar en rondas donde uno de ellos será eliminado aleatoriamente. El servidor permite un máximo de 3 jugadores activos por partida.

## Características
- **Comunicación basada en UDP**: Se utiliza `socket` para manejar mensajes entre el servidor y los clientes.
- **Manejo de concurrencia**: Usa `threading` para gestionar el juego de manera independiente mientras procesa las solicitudes de los jugadores.
- **Asignación de nombres automática**: Los jugadores reciben un nombre asignado al unirse al juego.
- **Eliminación aleatoria**: Un jugador es eliminado aleatoriamente al final de cada ronda.


## Uso

### Ejecución del servidor
1. Asegúrate de que los puertos especificados en el código no estén siendo utilizados.
2. Inicia el servidor ejecutando el archivo principal:
   ```bash
   python server.py
   ```
   El servidor estará escuchando en `127.0.0.1:65433` por defecto.

### Interacción con el cliente
Los clientes deben enviar comandos al servidor para participar en el juego. Los comandos disponibles son:

#### Unirse al juego:
   ```
   JOIN
   ```
   Este comando permite que un cliente se una al juego.

#### Respuestas del servidor:
- **Unirse exitosamente**:
  ```
  UNIDO COMO JUGADOR <nombre>
  ```
- **Juego completo**:
  ```
  LA PARTIDA ESTA COMPLETA, ESPERE A QUE TERMINE
  ```
- **Jugador ya en el juego**:
  ```
  YA ESTAS EN EL JUEGO
  ```
- **Comando no reconocido**:
  ```
  COMANDO NO RECONOCIDO
  ```



