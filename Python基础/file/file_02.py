# some_sentences = '''\
#     I love learning python
#     beacuse python is fun
#     and also easy to use
#     '''

# f = open('sentence.txt','w')
# f.write(some_sentences)
# f.close()

f = open('sentence.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close
