import os

openOutp = open("pyramid_outp.txt")
openInp = open("pyramid_inp.txt")
outputs = openOutp.read().split("-*********************************************************\n")[1:]
inputs = openInp.read().splitlines()
openOutp.close()
openInp.close()

for i in range(len(inputs)):
    open('user_inp.txt', 'w').write(inputs[i])
    os.system("./the1_pyramid < user_inp.txt > user_outp.txt")
    
    test = open('user_outp.txt').read()
    if test == outputs[i][:-3]:
        print(f"Case {i+1}: PASS")
    else:
        false_list = []
        test = test.splitlines()
        compare = (outputs[i][:-3]).splitlines()
        for j in range(len(test)):
            try:
                if test[j] != compare[j]:
                    if test[j][:-1] == compare[j][:-1] and abs(test[j][-1] - compare[j][-1]) == 1:
                        continue
                    else:
                        false_list.append(j)          
            except: 
                break
        if false_list:
            print(f"\nCase {i+1}: FAILED")
            for k in false_list:
                print(f"Expected: {compare[k]}")
                print(f"Your Result: {test[k]}")
            print()
        else:
            print(f"Case {i+1}: PASS")