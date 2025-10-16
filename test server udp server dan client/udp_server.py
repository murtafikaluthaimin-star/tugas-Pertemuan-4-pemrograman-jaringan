import socket
import datetime

HOST = "127.0.0.1"   # alamat lokal
PORT = 5005          # port bebas

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Server UDP berjalan di {HOST}:{PORT}")
print("Menunggu pesan dari client...\n")

while True:
    data, addr = server_socket.recvfrom(1024)
    pesan = data.decode("utf-8")
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{waktu}] Pesan dari {addr}: {pesan}")

    # Simpan log ke file
    with open("server_log.txt", "a") as f:
        f.write(f"[{waktu}] {addr} : {pesan}\n")

    balasan = f"Pesan '{pesan}' diterima pada {waktu}"
    server_socket.sendto(balasan.encode("utf-8"), addr)
