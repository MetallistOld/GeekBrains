from sys import argv

if len(argv) == 1:
    for linenum, line in enumerate(open('bakery.csv', 'r')):
        print(line.strip())

elif len(argv) == 2:
    for linenum, line in enumerate(open('bakery.csv', 'r')):
        if linenum >= int(argv[1])-1:
            print(line.strip())

elif len(argv) == 3:
    for linenum, line in enumerate(open('bakery.csv', 'r')):
        if int(argv[1])-1 <= linenum <= int(argv[2])-1:
            print(line.strip())
else:
    print('Передано слишком много параметров')
