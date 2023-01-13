from dataclasses import dataclass
import socket
import json
import threading

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
    FETCH_REPLY: int = 0b1010

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
    # client is sending the user auth data through the encrypted stream

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
class Server:
    # TODO: FIX THIS   
    def _recvLoop(self):
        while(True):
            packet = self._recvPacket()
            print(f"C -> S: {packet.packet_id}")
            
    def listen(self, port: int = 5000):
        host = socket.gethostname()
        self.s = socket.socket(socket.AddressFamily.AF_INET,socket.SocketKind.SOCK_STREAM)
        self.s.bind((host,port))
        self.s.listen(20)
        self.conn, self.address = self.s.accept()
        t = threading.Thread(target=self._recvLoop)
        t.start()
    def _sendPacket(self, packet: Packet):
        data = {"type":packet.packet_id, "data":packet.data}
        self.s.sendall(str(data).encode())
        print(f"C <- S: {packet.packet_id}")
        pass
    
    
        
        
    def _recvPacket(self) -> Packet:
        data = json.loads(str(self.s.recv(1024).decode()))
        packet = Packet(data["type"], data["data"])
    
server = Server()
server.listen()