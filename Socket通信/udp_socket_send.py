import socket
def main():
    # 1.创建一个UDP套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind("",8080)

    while True:
        #从键盘获取数据
        send_date = input("请输入要发送的数据：")
        if send_date == "exit":
            break
        # 2.使用套接字收发数据
        # udp_socket.sendto("ahsdu",对方的IP以及Port)
        # udp_socket.sendto(b"ahsdu",("192.168.1.2",8080))
        udp_socket.sendto(send_date.encode("utf-8"),("192.168.1.2",8080))
    # 3.关闭套接字
    udp_socket.close()
if __name__ =="__main__":
    main()