import socket


def send_msg(udp_socket):
    '''发送消息'''
    # 获取对方的IP/PORT
    dest_ip = input("请输入对方IP：")
    dest_port = int(input("请输入对方端口号："))
    # socket套接字可以同时进行收发数据
    # 2.使用套接字发送数据
    # 从键盘获取数据
    send_date = input("请输入要发送的内容：")
    udp_socket.sendto(send_date.encode("utf-8"),(dest_ip,dest_port))


def recv_msg(udp_socket):
    '''接收消息'''
    # 3.使用套接字接收数据
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]),recv_data[0].decode("utf-8")))


def main():
    # 1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    # 绑定信息
    udp_socket.bind("",8080)

    # 循环处理
    while True:
        print("-----xx聊天室------")
        print("1.发送消息")
        print("2.接收消息")
        print("0.退出聊天室")
        op = input("请输入功能序号：")

        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2"
            # 接收并显示
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误请重新输入。。。")



    # 4.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()