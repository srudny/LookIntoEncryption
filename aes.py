
#Function that converts string charcters to hex
def strToHex(string):
    key = []
    ct = 0
    for n in string:
        key.append(hex(ord(n)))
        key[ct] = key[ct][2:]
        ct += 1    
    return key





#standard input matrix used in MixColumns
stdMatrix = [['02','03','01','01'],['01','02','03','01'],['01','01','02','03'],['03','01','01','02']]


# hex xor table
hexXOR=[['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'],
        ['1','0','3','2','5','4','7','6','9','8','b','a','d','c','f','e'],
        ['2','3','0','1','6','7','4','5','a','b','8','9','e','f','c','d'],
        ['3','2','1','0','7','6','5','4','b','a','9','8','f','e','d','c'],
        ['4','5','6','7','0','1','2','3','c','d','e','f','8','9','a','b'],
        ['5','4','7','6','1','0','3','2','d','c','f','e','9','8','b','a'],
        ['6','7','4','5','2','3','0','1','e','f','c','d','a','b','8','9'],
        ['7','6','5','4','3','2','1','0','f','e','d','c','b','a','9','8'],
        ['8','9','a','b','c','d','e','f','0','1','2','3','4','5','6','7'],
        ['9','8','b','a','d','c','f','e','1','0','3','2','5','4','7','6'],
        ['a','b','8','9','e','f','c','d','2','3','0','1','6','7','4','5'],
        ['b','a','9','8','f','e','d','c','3','2','1','0','7','6','5','4'],
        ['c','d','e','f','8','9','a','b','4','5','6','7','0','1','2','3'],
        ['d','c','f','e','9','8','b','a','5','4','7','6','1','0','3','2'],
        ['e','f','c','d','a','b','8','9','6','7','4','5','2','3','0','1'],
        ['f','e','d','c','b','a','9','8','7','6','5','4','3','2','1','0']]

#s-box conversion table
sbox =  [['63','7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67','2b', 'fe', 'd7', 'ab', '76'],
        ['ca','82', 'c9', '7d', 'fa', '59','47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'], 
        ['b7','fd', '93', '26', '36','3f','f7', 'cc', '34', 'a5', 'e5', 'f1','71', 'd8', '31', '15'], 
        ['04', 'c7', '23', 'c3', '18', '96', '05','9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'], 
        ['09', '83', '2c', '1a', '1b', '6e', '5a','a0', '52', '3b', 'd6', 'b3', '29','e3', '2f', '84'], 
        ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b','6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
        ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45','f9', '02', '7f', '50', '3c','9f', 'a8'],
        ['51', 'a3', '40', '8f', '92', '9d', '38','f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'], 
        ['cd', '0c', '13', 'ec','5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19','73'],
        ['60','81','4f','dc','22','2a','90','88','46','ee','b8', '14', 'de', '5e', '0b', 'db'], 
        ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
        ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4','ea', '65', '7a', 'ae', '08'], 
        ['ba', '78', '25', '2e', '1c', 'a6','b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'], 
        ['70','3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9','86', 'c1', '1d', '9e'],
        ['e1', 'f8', '98', '11', '69', 'd9', '8e','94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'], 
        ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99','2d', '0f', 'b0', '54', 'bb', '16']]

#RCON used to generate round keys
rcon = [['01','00','00','00'],['02','00','00','00'],['04','00','00','00'],['08','00','00','00'],
        ['10','00','00','00'],['20','00','00','00'],['40','00','00','00'],['80','00','00','00'],
        ['1b','00','00','00'],['36','00','00','00']]

#subByte step using S-box substitution
def sbox_convert(value):
    hexConvert = {'a':['10'],'b':['11'],'c':['12'],'d':['13'],'e':['14'],'f':['15']}
    x,y = 0,0
    if value[0] in '0123456789':
        x = int(value[0])
    else:
        x = int(hexConvert[value[0]][0])
    if value[1] in '0123456789':
        y = int(value[1])
    else:
        y = int(hexConvert[value[1]][0])
    return sbox[x][y]

#Inputs two decimal numbers and xor them in hexadecimal        
def xorHex(n1,n2):
    hexConvert = {'a':['10'],'b':['11'],'c':['12'],'d':['13'],'e':['14'],'f':['15']}
    if n1 not in '0123456789':
        n1 = hexConvert[n1][0]
    if n2 not in '0123456789':
        n2 = hexConvert[n2][0]
        
    return hexXOR[int(n1)][int(n2)]

#xor a list of hex values
def xorList(l1,l2):
    result = []
    for n in range(len(l1)):
        new = ''
        for digit in range(2):
            new = new + xorHex(l1[n][digit],l2[n][digit])
        result.append(new)
        
    return result

#xor binary numbers         
def xorBin(b1,b2):
    result = ''
    for n in range(len(b1)):
        if b1[n] == b2[n]:
            result = result + '0'
        else:
            result = result + '1'
    return result
            
#Test key and plaintext
key = ['54','68','61','74','73','20','6d','79','20','4b','75','6e','67','20','46','75']
plainText = ['54','77','6f','20','4f','6e','65','20','4e','69','6e','65','20','54','77','6f']

#generates Round Keys for all 10 rounds
def generateRoundKey(key):
    roundKeys = {}
    
    roundKeys[0] = key
    
    for keys in range(10):
        currentKey = key
        w4 = []
        w5= []
        w6 = []
        w7 = []
        w0 = currentKey[0:4]
        w1 = currentKey[4:8]
        w2 = currentKey[8:12]
        ogw3 = currentKey[12:16]
        w3 = [ogw3[1],ogw3[2],ogw3[3],ogw3[0]]
       
        gw3 = []
        for n in w3:
           
            gw3.append(sbox_convert(n))
#add round constant
        gw3 = xorList(gw3,rcon[keys])
        w4 = xorList(gw3,w0)
        w5 = xorList(w4,w1)
        w6 = xorList(w5,w2)
        w7 = xorList(w6,ogw3)
        
        roundKeys[keys+1] = w4 + w5 + w6 + w7
        key = roundKeys[keys + 1]
    return roundKeys

#Add RoundKey Step   
def AESoutput(current,key):
    output = xorList(current, key)      
    return output

#ShiftRow step
def shiftRows(start):
    temp = []
    for bit in start:
        temp.append(sbox_convert(bit))
            
    r0 = [temp[0],temp[4],temp[8],temp[12]]
    r1 = [temp[5],temp[9],temp[13],temp[1]]
    r2 = [temp[10],temp[14],temp[2],temp[6]]
    r3 = [temp[15],temp[3],temp[7],temp[11]]
    
    shifted = [r0[0],r1[0],r2[0],r3[0],r0[1],r1[1],r2[1],r3[1],r0[2],r1[2],r2[2],r3[2],r0[3],r1[3],r2[3],r3[3]]
    return shifted
hexBin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}

#Converts hexadecimal value to binary
def hexToBin(hexNum):
    num = ''
    for n in hexNum:
        num = num + hexBin[n]
    return num

#GF(2^8) polynomial multiplication used in MixedColumns step
def multPoly(s1,s2):
#inputs case and hex
    poly= ''
    s2= hexToBin(s2)
    case2 = '00011011'
    if s1 == '01':
        poly = s2
    elif s1 == '02':
        shift = s2[1:] + '0'
        if s2[0] == '0':
            poly = shift
        
        else:
            for n in range(len(shift)):
                if shift[n] == case2[n]:
                    poly = poly + '0'
                else:
                    poly = poly + '1'
    else:
        c2 = ''
        shift = s2[1:] + '0'
        if s2[0] == '0':
            c2 = shift
        
        else:
            for n in range(len(shift)):
                if shift[n] == case2[n]:
                    c2 = c2 + '0'
                else:
                    c2 = c2 + '1'
        for k in range(len(c2)):
            if c2[k] == s2[k]:
                poly = poly + '0'
            else:
                poly = poly + '1'   
    return poly
                
    
#MixColumns step
def mixColumns(start):
    c1 = start[0:4]
    c2 = start[4:8]
    c3 = start[8:12]
    c4 = start[12:16]
    matrixAES = [c1,c2,c3,c4]
    result = []
    final = []
    for i in range(4):
        for j in range(4):
            product = '00000000'
            for p in range(4):
                product = xorBin(product,multPoly(stdMatrix[j][p],matrixAES[i][p]))
                
            result.append(product) 
            
    for n in result:
        temp1 = ''
        temp2 = ''
        p1 = n[0:4]
        p2 = n[4:8]
        for n in hexBin:
            if p1 == hexBin[n]:
                temp1 = str(n)
            if p2 == hexBin[n]:
                temp2 = str(n)
        final.append(temp1+temp2)
            
    return final
    
    
#Runs AES algorithm for 128 bit key encryption   
def AESencryption(key,plainTxt):
    roundKey = generateRoundKey(key)
    current = AESoutput(plainTxt,roundKey[0])
    
    for i in range(9):
        
        temp = shiftRows(current)
        temp2 = mixColumns(temp)
        current = xorList(temp2,roundKey[i+1])
        print(current)
        
    temp3 = shiftRows(current)
    final = xorList(temp3,roundKey[10])
    return final
    
        
        
      
['54','68','69','73','20','69','73','20','61','20','53','79','64','6e','65','79']        
    
