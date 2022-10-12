import code
import regex as re
import math
#declaring arm length
a1=3000
a2=2550

with open(r"gcode2.txt",'r') as f:
    print(f)
    lines=f.readlines()
    for line in lines:

        #test case 1:
        print('---------',line)
        #match=re.findall(r'G[0-9]+ X[0-9]+\.[0-9]+ Y[0-9]+\.[0-9]+',line)
        #print("passing match",match)

        #matching x and y val using regex
        x_val=re.findall(r'(X[0-9]+|X[0-9]+\.[0-9]\d+ )',line)
        print(x_val)
        y_val=re.findall(r'Y[0-9]+|Y[0-9]+\.[0-9]\d+',line)
        X_val=re.findall(r'[0-9]+|[0-9]+\.[0-9]\d+',x_val[0])
        Y_val=re.findall(r'[0-9]+|[0-9]+\.[0-9]\d+',y_val[0])
        print("x_val",X_val)
        print("y_val",Y_val)

        #formula for cos inverse
        U_of_q2=(float(X_val[0])**2 + float(Y_val[0])**2 -a1**2 -a2**2)/(2*a1*a2)

        
        #value of U_of_q2
        print('U_of_q2-->',U_of_q2)

        if U_of_q2<=-1:
            max_cos_inverse=-1
            print(max_cos_inverse)
            cos_inverse=math.degrees(math.acos(max_cos_inverse))
            print('if---passing',cos_inverse)

        else:
            cos_inverse=math.degrees(math.acos((U_of_q2)))
            print('else------passing',cos_inverse)

        #formula for V_of_q1
        #v_of_q1=math.degrees(math.atan(float(Y_val[0])/float(X_val[0]))) # - math.degrees(math.atan((a2*math.sin(cos_inverse))))#/(a1+(a2*math.cos(cos_inverse)))))  
        v_of_q1= (math.degrees(math.sin(180)))#/(a1+(a2*math.cos(cos_inverse)))))  
        print(v_of_q1) 