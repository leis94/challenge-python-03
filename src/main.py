import re

def run():
    message = ''
    pattern = re.compile(r'([a-z\s?])')
    f = open('encoded.txt', 'r', encoding='utf-8')
    for line in f:
        match = re.findall(pattern, line)
        if match != "":
             print(message.join(match))
        else:
            print('No encontro nada')
    f.close()

if __name__ == '__main__':
    run()



