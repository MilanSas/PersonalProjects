#groot hoofd met meer detail als extra
def big_smiley(i):
    output = "" 
    #sets optimal scale, optimal scale starts at big_smiley(1)
    if i < 1:
        print("scale to low")
    i = 24 + i *12 
    radius = i/2 
    middenooglinks = i/3
    middenoogrechts= middenooglinks + i/3   
    radiusoog = middenooglinks/4
    radiusneus = (i/32)
    mondhoekas = (i/3)*2
    mondhoeklinks = radius/2
    mondhoekrechts = mondhoeklinks + radius 
    radiusmond = i/6
    for y in range(0, i+1):
        for x in range(0, i+1):
            if int(afstand(x, radius, y, radius)) == int(radius):
                output += "#"
            #hat
            elif y == int(i/6):
                output += "#"
            elif int(afstand(x, radius, y, radius)) < (radius) and y < i/6:
                output += "#"
            #left eye
            elif x == int(middenooglinks) and y == int(middenooglinks):
                output += "$"
            #right eye
            elif x == int(middenoogrechts) and y == int(middenooglinks):
                output += "$"    
            #scaleble eyebrows
            elif y == int(middenooglinks-(radiusoog)-1) and x > (middenooglinks-radiusoog) and x < (middenooglinks+radiusoog):
                output += "="
            elif y == int(middenooglinks-radiusoog-1) and x > (middenoogrechts-radiusoog) and x < (middenoogrechts+radiusoog):
                output += "="
            #scaleble eyes
            elif int(afstand(x, middenooglinks, y, middenooglinks)) == int(radiusoog):
                output += "0"
            elif int(afstand(x, middenoogrechts, y, middenooglinks)) == int(radiusoog):
                output += "0"
            #scaleble nose
            elif int(afstand(x, radius, y, radius)) == int(radiusneus):
                output += ">"
            elif x == int (mondhoeklinks) and y == int(mondhoekas):
                output += "\\" 
            elif x == int(mondhoekrechts) and y == int(mondhoekas):
                output += "/"     
            #mouth
            elif x > (mondhoeklinks) and x < (mondhoekrechts) and y == int(mondhoekas):
                output += "_"
            #scaleble mouth
            elif int(afstand(x, radius, y, mondhoekas+1)) < int(radiusmond):
                if int(y) >= int(mondhoekas+1) and int(x) == int(radius):
                    output += "|"
                else: output += " "
            #tong
            elif int(afstand(x, radius, y, mondhoekas+1)) == int(radiusmond):
                if int(y) >= int(mondhoekas+1):
                    output += "#"
                else:
                    output += " "
            else:
                output += " "        

        output += "\n"
    print(output)
def afstand(x, x2, y, y2):
    import math    
    return math.sqrt(((x-x2)**2)+(y-y2)**2)  

big_smiley(int(input("Put in size of smiley starting at '1':\n")))