import multiprocessing

def download_from_web(q):
    '''下载数据'''
    data = [11,22,33,44]
    for temp in data:
        q.put(temp)
    print("---下载器已经下载完了数据并存入到队列中---")

def analysis_data(q):
    '''数据处理'''
    waiting_analysis_data = []
    while True:
        data = q.get
        waiting_analysis_data.append(data)
        if q.empty():
            break
    print(waiting_analysis_data)
    print("shem")

def main():
    # 1.创建一个队列
    q = multiprocessing.Queue()
    # 2.创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target = download_from_web,args = (q,))
    p2 = multiprocessing.Process(target = analysis_data,args = (q,))
    p1.start()
    p2.start()
    

if __name__ == "__main__":
    main()