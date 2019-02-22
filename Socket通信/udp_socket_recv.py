 import socket
def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    localaddr = ("",8080)
    udp_socket.bind(localaddr)
    # 3.接收信息
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # recv_data这个变量中存储的是一个元组(接收到的数据,(发送方的ip,port))
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        # 4.打印接收到的信息
        print("%s:%s"%(send_addr,recv_msg.decode("gbk")))
    # 5.关闭套接字
    udp_socket.close()

 if __name__ == __main__:
     main()