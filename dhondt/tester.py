import os

openOutp = open("dhondt_outp.txt")
openInp = open("dhondt_inp.txt")
outputs = openOutp.read().split("-**********\n")[1:]
inputs = openInp.read().splitlines()
openOutp.close()
openInp.close()

for i in range(len(inputs)):
    open('user_inp.txt', 'w').close()

    open('user_inp.txt', 'w').write(inputs[i])
    os.system("./the1_dhondt < user_inp.txt > user_outp.txt")

    if open('user_outp.txt').read() in outputs[i]:
        print(f"Case {i+1}: PASS")
    else:
        print(f"Case {i+1}: FAILED")