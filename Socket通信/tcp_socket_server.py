import socket


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定本地信息
    tcp_server_socket.bind(("",7890))
    # 3.让默认的套接字由主动变为被动
    tcp_server_socket.listen(128)

    while True:
        # 4.等待客户端链接
        print("等待客户端链接")
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("有客户端接入：")
        print(client_addr)

        while True:
            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode("utf-8"))

            # 如果recv解阻塞，那么有两种方式
                # 1.客户端发送过来数据
                # 2.客户端调用close导致recv解阻塞
            if recv_data:
                # 发送数据给客户端
                new_client_socket.send("Im ok--.".encode("utf-8"))
            else:
                break
                
        # 关闭套接字
        new_client_socket.close()
        print("已经关闭当前链接！")
    tcp_server_socket.close()



if __name__ == "__main__":
    main()