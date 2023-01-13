from dataclasses import dataclass
import socket


@dataclass 
class packet_ids:
    HANDSHAKE_BEGIN: int = 0b0001
    HANDSHAKE_CONTINUE: int = 0b0010
    ENC_START_RQ: int = 0b0011
    ENC_ACK: int = 0b0100
    AUTH_DATA: int = 0b0101
    AUTH_REPLY: int = 0b0110
    FETCH: int = 0b0111
    SEND_MSG: int = 0b1000
    RCV_MSG: int = 0b1001

@dataclass
class Packet:
    packet_id: int
    data: dict


# PACKET DEFINITIONS:

# HANDSHAKE BEGIN
# starts the handshake process to hopefully get an encrypted communication between the server and client

# ENCRYPTION START RQ
# client is requesting the server to send its public key to start an encrypted communication stream

# ENCRYPTION ACK
# server acknowledged the packet and is sending its public key

# AUTH DATA
# client is sending the user auth data through the encrypted stream

# AUTH REPLY
# server reply to auth data

# FETCH
# client is fetching data from server

# SEND MSG
# client is sending a message

# RECIEVE MSG
# server is notifying a new message has been send


class client(self):
    def connect(ip: str):
        # TODO
    def sendPacket(packet: Packet):
        # TODO
        packet = Packet(packet_id, data)
        pass
    def sendMessage(message: str)
        # TODO
        data = {"message":message}
        packet = Packet(packet_ids.SEND_MSG, data)
        sendPacket(packet)
