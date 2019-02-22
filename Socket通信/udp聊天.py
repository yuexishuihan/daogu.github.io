import socket

def main():
    # 1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 获取对方的IP/PORT
    dest_ip = input("请输入对方IP：")
    dest_port = int(input("请输入对方端口号："))

# socket套接字可以同时进行收发数据
    # 2.使用套接字发送数据
    # 从键盘获取数据
    send_date = input("请输入要发送的内容：")
    udp_socket.sendto(send_date.encode("utf-8"),(dest_ip,dest_port))

    # 3.使用套接字接收数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)

    # 4.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()