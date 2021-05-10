#Sydney Rudny
#May 2021
#This program runs an AES encryption GUI


from graphics import*
from button import*
from aes import*
from time import sleep

win = GraphWin("Encryption Implementation",600,600)
win.setCoords(-100,-100,100,100)


welcomeTxt = Text(Point(0,50),"This is an implementation of AES click below to begin.")
welcomeTxt.setFace('courier')
welcomeTxt.draw(win)

AESButton = Button(win,Point(0,0),40,10,"AES" )
AESButton.activate()



keepGoing = True

while keepGoing:
    p = win.getMouse()
    if AESButton.clicked(p):
        AESButton.rect.undraw()
        AESButton.label.undraw()
        welcomeTxt.undraw()
        Instr = Text(Point(0,50),"Pick your 16-bit key and plain text.")
        keyT = Text(Point(-40,0),"Key:")
        plainT = Text(Point(-50,-25),"Plaintext:")
        Instr.setFace('courier'),keyT.setFace('courier'),plainT.setFace('courier')
        Instr.draw(win),keyT.draw(win),plainT.draw(win)
        key = Entry(Point(0,0),20)
        plain = Entry(Point(0,-25), 20)
        key.draw(win),plain.draw(win)
        Enter = Button(win,Point(0,-40),40,10,"Enter")
        Enter.activate()
        while True:
            k =win.getMouse()
            if Enter.clicked(k):
                keyx=key.getText()
                plainx=plain.getText()
                Enter.deactivate()
                if len(keyx) != 16:
                    key.setFill('Red')
                    Error = Text(Point(0,25),"ERROR: Key and Plaintext must be length 16. \n Click anywhere to try again.")
                    Error.setTextColor("Red"),Error.setFace('courier'), Error.draw(win)
                    win.getMouse()
                    Error.undraw()
                    Enter.activate()
                if len(plainx) != 16:
                    plain.setFill('Red')
                    Error = Text(Point(0,25),"ERROR: Key and Plaintext must be length 16. \n Click anywhere to try again.")
                    Error.setTextColor("Red"),Error.setFace('courier'), Error.draw(win)
                    win.getMouse()
                    Error.undraw()
                    Enter.activate()
                if len(plainx) == 16 and len(keyx) == 16:
                    break
        KEY = strToHex(keyx)
        PLAIN = strToHex(plainx)
        key.undraw(),plain.undraw(),keyT.undraw(),plainT.undraw(),Instr.undraw()
        
        def AESencryption(key,plainTxt):
            
            roundKey = generateRoundKey(key)
            current = AESoutput(plainTxt,roundKey[0])
            txt1 = Text(Point(0,5)," ")
            txt2 = Text(Point(0,0)," ")
            txt3 = Text(Point(0,-5)," ")
            txt4 = Text(Point(0,-10)," ")
            txt1.draw(win),txt2.draw(win),txt3.draw(win),txt4.draw(win)
            
            for i in range(9):
                txt1.undraw(),txt2.undraw(),txt3.undraw(),txt4.undraw()
                temp = shiftRows(current)
                temp2 = mixColumns(temp)
                current = xorList(temp2,roundKey[i+1])
                txt1 = Text(Point(0,5),(current[0],current[4],current[8],current[12]))
                txt2 = Text(Point(0,0),(current[1],current[5],current[9],current[13]))  
                txt3 = Text(Point(0,-5),(current[2],current[6],current[10],current[14]))
                txt4 = Text(Point(0,-10),(current[3],current[7],current[11],current[15]))
                txt1.draw(win),txt2.draw(win),txt3.draw(win),txt4.draw(win)
                time.sleep(.5)
            txt1.undraw(),txt2.undraw(),txt3.undraw(),txt4.undraw()    
            temp3 = shiftRows(current)
            final = xorList(temp3,roundKey[10])
            txt1 = Text(Point(0,0),("Encoded message: ",final))
            txt1.draw(win)
            
                
                
        AESencryption(KEY,PLAIN)
        Enter.rect.undraw()
        Enter.label.undraw()
        
        win.getMouse()
        win.close()
            
        
        
        














