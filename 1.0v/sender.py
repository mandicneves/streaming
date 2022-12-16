from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('192.168.0.136', 9999) #specify the public ip adrres

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != "STOP":
    continue
sender.stop_stream()