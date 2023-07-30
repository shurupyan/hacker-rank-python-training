# https://www.hackerrank.com/challenges/one-month-preparation-kit-simple-text-editor/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

# print(s)
line = ""
stack = [line]
for i in range(int(s)):
    s = input()

    # print(s)
    line = stack[-1]
    cmd = s.split()
    if cmd[0] == "1":
        line += cmd[1]
        stack.append(line)

    if cmd[0] == "2":
        line = line[:-int(cmd[1])]
        stack.append(line)

    if cmd[0] == "3":
        ind = int(cmd[1]) - 1
        # print(ind)
        print(line[ind])

    if cmd[0] == "4":
        stack.pop()

        #  print(stack)


