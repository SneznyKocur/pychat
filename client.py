from dataclasses import dataclass
import socket
import json


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
    FETCH_REPLY: int = 0b1001
    
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

# ENCRYPTED:
    # AUTH DATA
    # client is sending the user auth data

    # AUTH REPLY
    # server reply to auth data

    # FETCH
    # client is fetching data from server

    # SEND MSG
    # client is sending a message

    # RECIEVE MSG
    # server is notifying a new message has been send

    # FETCH REPLY
    # server is replying with data to a previous fetch

# Packet:
# { 
#   type:<PACKET_ID>
#   data: {
#       <data> 
#   }
# }
class Client:
    def connect(self, ip: str, port: int):
        self.s = socket.socket(socket.AddressFamily.AF_INET,socket.SocketKind.SOCK_STREAM)
        host = socket.gethostname()
        print(host)
        try:
            self.s.connect((host,port))
        except Exception as e:
            print(e)
        else:
            return 0
    
    
    def _sendPacket(self, packet: Packet):
        data = {"type":packet.packet_id, "data":packet.data}
        return self.s.send(str(data).encode())
        
    
    def _sendMessage(self, message: str):
        data = {"message":message}
        packet = Packet(packet_ids.SEND_MSG, data)
        return self._sendPacket(packet)
        
        
    def _recvPacket(self) -> Packet:
        data = json.loads(str(self.s.recv(1024).decode()))
        packet = Packet(data["type"], data["data"])
        return packet
    
    
client = Client()
client.connect("127.0.0.1",5000)
while True:
    packet_id = input("PACKET_ID:")
    
    data1 = f"{input('data:')}"
    
    data = {"data":data1}
    client._sendPacket(packet=Packet(packet_id,data))
    print(client._recvPacket())