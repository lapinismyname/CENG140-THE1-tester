import os

openOutp = open("pyramid_outp.txt")
openInp = open("pyramid_inp.txt")
outputs = openOutp.read().split("-*********************************************************\n")[1:]
inputs = openInp.read().splitlines()
openOutp.close()
openInp.close()

for i in range(len(inputs)):
    open('user_inp.txt', 'w').close()

    open('user_inp.txt', 'w').write(inputs[i])
    os.system("./the1_pyramid < user_inp.txt > user_outp.txt")
    
    test = open('user_outp.txt').read()
    if test == outputs[i][:-3]:
        print(f"Case {i+1}: PASS")
    else:
        print(f"\nCase {i+1}: FAILED")
        test = test.splitlines()
        compare = outputs[i][:-3]
        for j in test:
            if j + "\n" != compare[:len(j)+1]:
                print("Expected: " + compare[:len(j)+1][:-1])
                print("Your Result: " + j)
            compare = compare[len(j)+1:]
        print()