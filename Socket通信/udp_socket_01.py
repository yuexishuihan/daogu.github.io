import socket
def main():
    # 创建一个UDP套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 使用套接字收发数据
    # udp_socket.sendto("ahsdu",对方的IP以及Port)
    udp_socket.sendto(b"ahsdu",("192.168.1.2",8080))
    # 关闭套接字
    udp_socket.close()
if __name__ =="__main__":
    main()