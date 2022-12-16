from vidstream import StreamingServer
import threading

# host (IP addres), port, slot(how many can connect)
receiver = StreamingServer('192.168.0.136', 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != "STOP":
    continue

receiver.stop_server()
