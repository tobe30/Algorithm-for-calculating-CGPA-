#pseudocode
#step 1:start
#step-2: input grade
#step-3: grade*points
#step-4: add grade
#step-5: total/24
#step-6: result
#step-7: stop

grade_values = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}


math101 = input('input grade in math101: ').upper()
gst104 = input('input grade in gst104: ').upper()
gst102 = input('input grade in gst102: ').upper()
stat131 = input('input grade in stat131: ').upper()
chem101 = input('input grade in chem101: ').upper()
phy107 = input('input grade in phy107: ').upper()
phy101 = input('input grade in phy101: ').upper()
csc101 = input('input grade in csc101: ').upper()
bio101 = input('input grade in bio101: ').upper()
csc107 = input('input grade in csc107: ').upper()


if math101 in grade_values:
    mresult = grade_values[math101] *3
    print('You got ' + str(mresult) + 'points in math101')
    if gst104 in grade_values:
        g4result = grade_values[gst104] *2
        print('You got ' + str(g4result) + 'points in gst104')
    if gst102 in grade_values:
        gresult = grade_values[gst102] *2
        print('You got ' + str(gresult) + 'points in gst102')
    if stat131 in grade_values:
        sresult = grade_values[stat131] *2
        print('You got ' + str(sresult) + 'points in stat131')
    if chem101 in grade_values:
        cresult = grade_values[chem101] *3
        print('You got ' + str(cresult) + 'points in chem101')
    if phy107 in grade_values:
        p7result = grade_values[phy107] *1
        print('You got ' + str(p7result) + 'points in phy107')
    if phy101 in grade_values:
        presult = grade_values[phy101] *3 
        print('You got ' + str(presult) + 'points in phy101')
    if csc101 in grade_values:
        cresult = grade_values[csc101] *3
        print('You got ' + str(cresult) + 'points in csc101')
    if csc107 in grade_values:
        c7result = grade_values[csc107] *2
        print('You got ' + str(c7result) + 'points in csc107')
    if bio101 in grade_values:
        bresult = grade_values[bio101] *3
        print('You got ' + str(bresult) + 'points in bio101')
    print('')

    result = (mresult + g4result + gresult + sresult + cresult + p7result + presult + cresult + c7result + bresult)/24
    print('Your 1 semester CGPA  is ' + str(result))
    
else:
    print('Enter grade e.g A,B,C,D,E,F')
