from sys import stdin, stdout

def input_data():
    queries = int(stdin.readline().strip())
    stack = []
    s = ''
    for _ in range(queries):
        query = stdin.readline().strip().split()
        if query[0] == '1':
            s = append(query[1], s, stack)
        elif query[0] == '2':
            s = delete(int(query[1]), s, stack)
        elif query[0] == '3':
            print_char(int(query[1]), s)
        else:
            s = undo(s, stack)

def append(w, s, stack):
    stack.append(s)
    s += w
    return s

def delete(w, s, stack):
    stack.append(s)
    s = s[:-w]
    return s

def print_char(w, s):
    if not s:
        stdout.write('')
    else:
        stdout.write(s[w-1] + '\n')

def undo(s, stack):
    s = stack.pop()
    return s

if __name__ == '__main__':
    input_data()