from tkinter import *
from math import sin,cos,tan,factorial,log
#import math

d={'bg':'#395B64','font':('arial',11,'bold')}
d2={'width':130,'height':70}
d3={'width':95,'height':60,'cursor':'hand2'}
d4={'width':129,'height':70,'cursor':'hand2'}
d5={'width':95,'height':70,'cursor':'hand2'}
#dict komaki(c) baraye malom kardan vaziat alamat haye mohasebati
c={'prntz':'off','alamat':'off','x':'off','math':'off','memory':'off'}
mood=0
natije=0
parantezNtj=0

#btns func
def funcBtn(adad):
    global mood
    if lbl2['text']=='0' or mood==0:
        lbl2['text']=str(adad)
        mood=1
    elif mood==1:
        lbl2['text']=str(lbl2['text'])+str(adad)

def funcDot(event=None):
    global mood
    if lbl2['text']=='0' or mood==0:
        lbl2['text']='0.'
        mood=1
    elif mood==1 and '.' not in lbl2['text']:
        lbl2['text']=str(lbl2['text'])+'.'
        
def funcPlus(event=None):
    global mood, natije
    c['mns']='off'
    c['zrb']='off'
    c['tghsm']='off'
    if c['prntz']=='baz':
        lbl2['text']=lbl2['text']+' + '
    elif c['prntz']=='baste':
        lbl2['text']=int(lbl2['text'][1:-2])
    elif c['alamat']=='off':
        lbl1['text']=str(lbl2['text'])+' + '
        natije=float(lbl2['text'])
        lbl2['text']=0
        c['alamat']='pls'
        mood=0
    elif mood==0:
        lbl1['text']=lbl1['text'][:-3]+' + '
        lbl2['text']='0'
        c['alamat']='pls'
        mood=0
    elif c['alamat']=='msv':
        lbl1['text']=lbl1['text'][:-3]+ ' + '
        c['alamat']='pls'
        mood=0
    elif c['alamat']!='off' :
        mood=0
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' + '
        if c['alamat']=='mns':
            natije=float(natije)-float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='pls'
        elif c['alamat']=='zrb':
            natije=float(natije)*float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='pls'
        elif c['alamat']=='tghsm':
            natije=float(natije)/float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='pls'
        elif c['alamat']=='pls':
            natije=float(natije)+float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='pls'
        elif c['alamat']=='tvn':
            natije=float(natije)**float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='pls'
            
def funcMinus(event=None):
    global mood, natije
    c['pls']='off'
    c['zrb']='off'
    c['tghsm']='off'
    if c['prntz']=='baz':
        lbl2['text']=lbl2['text']+' - '
    elif c['alamat']=='off':
        lbl1['text']=str(lbl2['text'])+' - '
        natije=float(lbl2['text'])
        lbl2['text']=0
        c['alamat']='mns'
        mood=0
    elif mood==0:
        lbl1['text']=lbl1['text'][:-3]+' - '
        lbl2['text']='0'
        c['alamat']='mns'
        mood=0
    elif c['alamat']=='msv':
        lbl1['text']=lbl1['text'][:-3]+ ' - '
        c['alamat']='mns'
        mood=0
    elif c['alamat']!='off':
        mood=0
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' - '
        if c['alamat']=='pls':
            natije=float(natije)+float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='mns'
        elif c['alamat']=='zrb':
            natije=float(natije)*float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='mns'
        elif c['alamat']=='tghsm':
            natije=float(natije)/float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='mns'
        elif c['alamat']=='mns':
            natije=float(natije)-float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='mns'
        elif c['alamat']=='tvn':
            natije=float(natije)**float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='mns'

def funcZarb(event=None):
    global mood, natije
    c['mns']='off'
    c['pls']='off'
    c['tghsm']='off'
    if c['prntz']=='baz':
        lbl2['text']=lbl2['text']+' × '
    
    elif c['alamat']=='off':
        lbl1['text']=str(lbl2['text'])+' × '
        natije=float(lbl2['text'])
        lbl2['text']=0
        c['alamat']='zrb'
        mood=0
    elif mood==0:
        lbl1['text']=lbl1['text'][:-3]+' × '
        lbl2['text']='0'
        c['alamat']='zrb'
        mood=0
    elif c['alamat']=='msv':
        lbl1['text']=lbl1['text'][:-3]+ ' × '
        c['alamat']='zrb'
        mood=0
    elif c['alamat']!='off':
        mood=0
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' × '
        if c['alamat']=='pls':
            natije=float(natije)+float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='zrb'
        elif c['alamat']=='mns':
            natije=float(natije)-float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='zrb'
        elif c['alamat']=='tghsm':
            natije=float(natije)/float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='zrb'
        elif c['alamat']=='zrb':
            natije=float(natije)*float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='zrb'
        elif c['alamat']=='tvn':
            natije=float(natije)**float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='zrb'
        
def funcTaghsim(event=None):
    global mood , natije
    c['mns']='off'
    c['zrb']='off'
    c['pls']='off'
    if c['prntz']=='baz':
        lbl2['text']=lbl2['text']+' ÷ '
    elif c['alamat']=='off':
        lbl1['text']=str(lbl2['text'])+' ÷ '
        natije=float(lbl2['text'])
        lbl2['text']=0
        c['alamat']='tghsm'
        mood=0
    elif mood==0:
        lbl1['text']=lbl1['text'][:-3]+' ÷ '
        lbl2['text']='0'
        c['alamat']='tghsm'
        mood=0
    elif c['alamat']=='msv':
        lbl1['text']=lbl1['text'][:-3]+ ' ÷ '
        c['alamat']='tghsm'
        mood=0
    elif c['alamat']!='off':
        mood=0
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' ÷ '
        if c['alamat']=='pls':
            natije=float(natije)+float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tghsm'
        elif c['alamat']=='mns':
            natije=float(natije)-float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tghsm'
        elif c['alamat']=='zrb':
            natije=float(natije)*float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tghsm'
        elif c['alamat']=='tghsm':
            natije=float(natije)/float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tghsm'
        elif c['alamat']=='tvn':
            natije=float(natije)**float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tghsm'        

def funcTavan(event=None):
    global mood , natije
    c['mns']='off'
    c['zrb']='off'
    c['pls']='off'
    c['tghsm']='off'
    if c['prntz']=='baz':
        lbl2['text']=lbl2['text']+' ^ '
    elif c['alamat']=='off':
        lbl1['text']=str(lbl2['text'])+' ^ '
        natije=float(lbl2['text'])
        lbl2['text']=0
        c['alamat']='tvn'
        mood=0
    elif mood==0:
        lbl1['text']=lbl1['text'][:-3]+' ^ '
        lbl2['text']='0'
        c['alamat']='tvn'
        mood=0
    elif c['alamat']=='msv':
        lbl1['text']=lbl1['text'][:-3]+ ' ^ '
        c['alamat']='tvn'
        mood=0
    elif c['alamat']!='off':
        mood=0
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' ^ '
        if c['alamat']=='pls':
            natije=float(natije)+float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tvn'
        elif c['alamat']=='mns':
            natije=float(natije)-float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tvn'
        elif c['alamat']=='zrb':
            natije=float(natije)*float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tvn'
        elif c['alamat']=='tghsm':
            natije=float(natije)/float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tvn'
        elif c['alamat']=='tvn':
            natije=float(natije)**float(lbl2['text'])
            lbl2['text']=natije
            c['alamat']='tvn'
        
def funcMosavi(event=None):
    global natije
    mood=0
    #PLUS
    if c['alamat']=='pls':
        c['lstNum']=lbl2['text']
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' = '
        natije=float(natije)+float(lbl2['text'])
        lbl2['text']=natije
        c['pls']='msvOn'
        c['alamat']='msv'
    elif c['pls']=='msvOn':
        lbl1['text']=str(lbl1['text'][:-3]) + ' + ' + str(c['lstNum']) + ' = '
        natije=float(natije)+float(c['lstNum'])
        lbl2['text']=natije
    #MINUS
    elif c['alamat']=='mns':
        c['lstNum']=lbl2['text']
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' = '
        natije=float(natije)-float(lbl2['text'])
        lbl2['text']=natije
        c['mns']='msvOn'
        c['alamat']='msv'
    elif c['mns']=='msvOn':
        lbl1['text']=str(lbl1['text'][:-3]) + ' - ' + str(c['lstNum']) + ' = '
        natije=float(natije) - float(c['lstNum'])
        lbl2['text']=natije
    #Zarb
    elif c['alamat']=='zrb':
        c['lstNum']=lbl2['text']
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' = '
        natije=float(natije)*float(lbl2['text'])
        lbl2['text']=natije
        c['zrb']='msvOn'
        c['alamat']='msv'
    elif c['zrb']=='msvOn':
        lbl1['text']=str(lbl1['text'][:-3]) + ' × ' + str(c['lstNum']) + ' = '
        natije=float(natije) * float(c['lstNum'])
        lbl2['text']=natije
    #Taghsim
    elif c['alamat']=='tghsm':
        c['lstNum']=lbl2['text']
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' = '
        natije=float(natije)/float(lbl2['text'])
        lbl2['text']=natije
        c['tghsm']='msvOn'
        c['alamat']='msv'
    elif c['tghsm']=='msvOn':
        lbl1['text']=str(lbl1['text'][:-3]) + ' ÷ ' + str(c['lstNum']) + ' = '
        natije=float(natije) / float(c['lstNum'])
        lbl2['text']=natije
    #Tavan
    elif c['alamat']=='tvn':
        c['lstNum']=lbl2['text']
        lbl1['text']=str(lbl1['text']) + str(lbl2['text']) + ' = '
        natije=float(natije)**float(lbl2['text'])
        lbl2['text']=natije
        c['tavan']='msvOn'
        c['alamat']='msv'
    elif c['tavan']=='msvOn':
        lbl1['text']=str(lbl1['text'][:-3]) + ' ^ ' + str(c['lstNum']) + ' = '
        natije=float(natije) ** float(c['lstNum'])
        lbl2['text']=natije

def funcClear(event=None):
    global mood
    if lbl2['text']!='0' and len(lbl2['text'])>1:
        lbl2['text']=lbl2['text'][0:len(lbl2['text'])-1]
    elif lbl2['text']!='0' and len(lbl2['text'])==1:
        lbl2['text']='0'
        mood=0

def funcClearA(event=None):
    global mood,natije,c ,parantez
    lbl1['text']='0'
    lbl2['text']='0'
    c['alamat']='off'
    parantez=0
    mood=0

def funcPrntzB(event=None):
    global mood
    if mood==0:
        lbl2['text']='( '
        c['prntz']='baz'
        mood=1

def funcPrntzC(event=None):
    global mood , parantezNtj , natije
    if c['prntz']=='baz':
        parantezLst = list(lbl2['text'].split(' '))
        del parantezLst[0]
        parantezNtj=int(parantezLst[0])
        for i in range(len(parantezLst)-1):
            if parantezLst[i] == '×':
                parantezNtj=int(parantezNtj)*int(parantezLst[i+1])
            elif parantezLst[i] == '÷':
                parantezNtj=int(parantezNtj)/int(parantezLst[i+1])
            elif parantezLst[i] == '+':
                parantezNtj=int(parantezNtj)+int(parantezLst[i+1])
            elif parantezLst[i] == '-':
                parantezNtj=int(parantezNtj)-int(parantezLst[i+1])
            elif parantezLst[i] == '^':
                parantezNtj=int(parantezNtj)**int(parantezLst[i+1])
        if c['math']=='off':
            lbl2['text']=float(parantezNtj)
            parantezNtj=0
        elif c['math']=='sin':
            lbl2['text']=float(sin(parantezNtj))
        elif c['math']=='cos':
            lbl2['text']=float(cos(parantezNtj))
        elif c['math']=='tan':
            lbl2['text']=float(tan(parantezNtj))
        elif c['math']=='e':
            lbl2['text']=2.718281828459045**float(parantezNtj)
        elif c['math']=='fact':
            lbl2['text']=float(factorial(parantezNtj))
        elif c['math']=='log':
            lbl2['text']=float(log(parantezNtj))
        elif c['math']=='ln':
            lbl2['text']=float(ln(parantezNtj))
        c['prntz']='off'
        c['math']='off'
        mood=1
    

def funcKasr(event=None):
    h=0
    if c['prntz']=='off' and mood==1:
        if lbl1['text']=='0':
            lbl2['text']=1/float(lbl2['text'])
            c['x']='on'
        elif c['x']=='on':
            lbl2['text']=1/float(lbl2['text'])
        else:
            lbl2['text']=1/float(lbl2['text'])
            c['x']='on'

def funcXtvn2(event=None):
    j=0
    if lbl1['text']=='0':
        lbl2['text']=float(lbl2['text'])**2
        c['x']='on'
    elif c['x']=='on':
        lbl2['text']=float(lbl2['text'])**2
    else:
        lbl2['text']=float(lbl2['text'])**2
        c['x']='on'

def funcRadikal(event=None):
    j=0
    if lbl1['text']=='0':
        lbl2['text']=float(lbl2['text'])**0.5
        c['x']='on'
    elif c['x']=='on':
        lbl2['text']=float(lbl2['text'])**0.5
    else:
        lbl2['text']=float(lbl2['text'])**0.5
        c['x']='on'

def funcPi(event=None):
    global mood
    lbl2['text']='3.141592653589793'
    mood=0

def funcE(event=None):
    global mood
    lbl2['text']='2.718281828459045'
    mood=0
def funcGhadr(event=None):
    if str(lbl2['text'])[0]=='-':
            lbl2['text']=lbl2['text'][1:]

def funcMath(SCT):
    global mood
    lbl2['text']=str(SCT)+'( '
    c['math']=str(SCT)
    c['prntz']='baz'
    mood=1

def funcETavan(event=None):
    global mood
    lbl2['text']='e^( '
    c['prntz']='baz'
    c['math']='e'
    mood=1

def funcPlsMns(event=None):
    if str(lbl2['text'])[0]!='-':
        lbl2['text']='-'+str(lbl2['text'])
    elif str(lbl2['text'])[0]=='-':
        lbl2['text']=lbl2['text'][1:]

def funcMemory(val):
    global mood
    if val=='MS':
        c['memory']=float(lbl2['text'])
        MClbl['fg']='white'
        MRlbl['fg']='white'
        Mtavan['fg']='white'
    elif val=='MP' and c['memory']!='off':
        c['memory']=c['memory']+c['memory']
    elif val=='MN' and c['memory']!='off':
        c['memory']=c['memory']-c['memory']
    elif val=='MT' and c['memory']!='off':
        c['memory']=c['memory']*c['memory']
    elif val=='MC' and c['memory']!='off':
        c['memory']='off'
        MClbl['fg']='#8BBCCC'
        MRlbl['fg']='#8BBCCC'
        Mtavan['fg']='#8BBCCC'
    elif val=='MR' and c['memory']!='off':
        lbl2['text']=float(c['memory'])
    mood=0
        
def funcDarsad (event=None):
    lbl2['text']=float(lbl2['text'])*float(0.01)
    
def funcBtnHover(img,url):
    img['file']=url

win=Tk()

win.geometry('520x758+700+140')
win.configure(bg='#2C3333')
win.resizable(False,False)
win.title('calculator')
# win.iconbitmap('calculator-icon.ico')
#natije 
ntjfrm=LabelFrame(win,width=520,height=105,bg='#395B64',bd=0)
lbl1=Label(ntjfrm,bg='#395B64',width=30,bd=0,text='0',font=('arial',20,'bold'),fg='#FFFFFF',anchor='e')
lbl2=Label(ntjfrm,bg='#395B64',width=16,bd=0,text='0',font=('arial',35,'bold'),fg='white',anchor='e')

#buttons image
img1=PhotoImage(file='images/btn1.png')
imgFaktoriel=PhotoImage(file='images/btnfaktoriel.png')
imgpi=PhotoImage(file='images/btnpi.png')
imglog=PhotoImage(file='images/btnlog.png')
imgin=PhotoImage(file='images/btnin.png')
imge=PhotoImage(file='images/btne.png')
imgsin=PhotoImage(file='images/btnsin.png')
imgcos=PhotoImage(file='images/btncos.png')
imgtan=PhotoImage(file='images/btntan.png')
imgetn=PhotoImage(file='images/btnetn.png')
imgxtn=PhotoImage(file='images/btnxtn.png')
imgrdkl=PhotoImage(file='images/btnrdkl.png')
imgxt2=PhotoImage(file='images/btnxt2.png')
imgdrsd=PhotoImage(file='images/btndrsd.png')
imgghadr=PhotoImage(file='images/btnbrkt.png')
imgksr=PhotoImage(file='images/btnksr.png')
imgprntzb=PhotoImage(file='images/btn(.png')
imgprntzc=PhotoImage(file='images/btn).png')
imgzrb=PhotoImage(file='images/btnzrb.png')
imgtghsm=PhotoImage(file='images/btntghsm.png')
imgminus=PhotoImage(file='images/btnminus.png')
img7=PhotoImage(file='images/btn7.png')
img8=PhotoImage(file='images/btn8.png')
img9=PhotoImage(file='images/btn9.png')
imgpls=PhotoImage(file='images/btnpls.png')
img4=PhotoImage(file='images/btn4.png')
img5=PhotoImage(file='images/btn5.png')
img6=PhotoImage(file='images/btn6.png')
imgclear=PhotoImage(file='images/btnclear.png')
img1=PhotoImage(file='images/btn1.png')
img2=PhotoImage(file='images/btn2.png')
img3=PhotoImage(file='images/btn3.png')
imgc=PhotoImage(file='images/btnc.png')
imgplsmins=PhotoImage(file='images/btnplsmins.png')
img0=PhotoImage(file='images/btn0.png')
imgdot=PhotoImage(file='images/btndat.png')
imgmsvi=PhotoImage(file='images/btnmsvi.png')

#buttons
memoryfrm=LabelFrame(win,width=520,height=40,bg='#395B64',bd=0)
MClbl=Label(memoryfrm,fg='#8BBCCC',text='MC',**d)
MRlbl=Label(memoryfrm,fg='#8BBCCC',text='MR',**d)
Mplus=Label(memoryfrm,fg='white',text='M+',**d)
Mmiuns=Label(memoryfrm,fg='white',text='M-',**d)
MSlbl=Label(memoryfrm,fg='white',text='MS',**d)
Mtavan=Label(memoryfrm,fg='#8BBCCC',text='M*',**d)

btnsfrm=LabelFrame(win,width=520,height=258,bd=0,bg='#395B64')
btnFaktoriel=Label(btnsfrm,image=imgFaktoriel,**d3)
btnpi=Label(btnsfrm,image=imgpi,**d3)
btnlog=Label(btnsfrm,image=imglog,**d3)
btnin=Label(btnsfrm,image=imgin,**d3)
btne=Label(btnsfrm,image=imge,**d3)
btnsin=Label(btnsfrm,image=imgsin,**d3)
btncos=Label(btnsfrm,image=imgcos,**d3)
btntan=Label(btnsfrm,image=imgtan,**d3)
btnetn=Label(btnsfrm,image=imgetn,**d3)
btnxtn=Label(btnsfrm,image=imgxtn,**d3)
btnrdkl=Label(btnsfrm,image=imgrdkl,**d3)
btnxt2=Label(btnsfrm,image=imgxt2,**d3)
btndrsd=Label(btnsfrm,image=imgdrsd,**d3)
btnghadr=Label(btnsfrm,image=imgghadr,**d3)
btnksr=Label(btnsfrm,image=imgksr,**d3)
btnprntzb=Label(btnsfrm,image=imgprntzb,**d3)
btnprntzc=Label(btnsfrm,image=imgprntzc,**d3)
btnzrb=Label(btnsfrm,image=imgzrb,**d3)
btntghsm=Label(btnsfrm,image=imgtghsm,**d3)
btnminus=Label(btnsfrm,image=imgminus,**d3)
btnsfrm2=LabelFrame(win,width=520,height=296,bd=0,bg='#395B64')
btn7=Label(btnsfrm2,image=img7,**d4)
btn8=Label(btnsfrm2,image=img8,**d4)
btn9=Label(btnsfrm2,image=img9,**d4)
btnpls=Label(btnsfrm2,image=imgpls,**d5)
btn4=Label(btnsfrm2,image=img4,**d4)
btn5=Label(btnsfrm2,image=img5,**d4)
btn6=Label(btnsfrm2,image=img6,**d4)
btnclear=Label(btnsfrm2,image=imgclear,**d5)
btn1=Label(btnsfrm2,image=img1,**d4)
btn2=Label(btnsfrm2,image=img2,**d4)
btn3=Label(btnsfrm2,image=img3,**d4)
btnc=Label(btnsfrm2,image=imgc,**d5)
btnplsmins=Label(btnsfrm2,image=imgplsmins,**d4)
btn0=Label(btnsfrm2,image=img0,**d4)
btndot=Label(btnsfrm2,image=imgdot,**d4)
btnmsvi=Label(btnsfrm2,image=imgmsvi,**d5)

#click btns
btn1.bind('<Button-1>',lambda event :funcBtn(1))
btn2.bind('<Button-1>',lambda event :funcBtn(2))
btn3.bind('<Button-1>',lambda event :funcBtn(3))
btn4.bind('<Button-1>',lambda event :funcBtn(4))
btn5.bind('<Button-1>',lambda event :funcBtn(5))
btn6.bind('<Button-1>',lambda event :funcBtn(6))
btn7.bind('<Button-1>',lambda event :funcBtn(7))
btn8.bind('<Button-1>',lambda event :funcBtn(8))
btn9.bind('<Button-1>',lambda event :funcBtn(9))
btn0.bind('<Button-1>',lambda event :funcBtn(0))
btnpls.bind('<Button-1>',funcPlus)
btnminus.bind('<Button-1>',funcMinus)
btntghsm.bind('<Button-1>',funcTaghsim)
btnzrb.bind('<Button-1>',funcZarb)
btnmsvi.bind('<Button-1>',funcMosavi)
btnc.bind('<Button-1>',funcClear)
btnclear.bind('<Button-1>',funcClearA)
btndot.bind('<Button-1>',funcDot)
btnplsmins.bind('<Button-1>',funcPlsMns)
btnprntzb.bind('<Button-1>',funcPrntzB)
btnprntzc.bind('<Button-1>',funcPrntzC)
btnksr.bind('<Button-1>',funcKasr)
btnxt2.bind('<Button-1>',funcXtvn2)
btnrdkl.bind('<Button-1>',funcRadikal)
btnpi.bind('<Button-1>',funcPi)
btne.bind('<Button-1>',funcE)
btnghadr.bind('<Button-1>',funcGhadr)
btnsin.bind('<Button-1>',lambda event :funcMath('sin'))
btncos.bind('<Button-1>',lambda event :funcMath('cos'))
btntan.bind('<Button-1>',lambda event :funcMath('tan'))
btnxtn.bind('<Button-1>',funcTavan)
btnetn.bind('<Button-1>',funcETavan)
btnplsmins.bind('<Button-1>',funcPlsMns)
btnFaktoriel.bind('<Button-1>',lambda event :funcMath('fact'))
btnlog.bind('<Button-1>',lambda event :funcMath('log'))
btnin.bind('<Button-1>',lambda event :funcMath('ln'))
MClbl.bind('<Button-1>',lambda event :funcMemory('MC'))
MRlbl.bind('<Button-1>',lambda event :funcMemory('MR'))
Mplus.bind('<Button-1>',lambda event :funcMemory('MP'))
Mmiuns.bind('<Button-1>',lambda event :funcMemory('MM'))
MSlbl.bind('<Button-1>',lambda event :funcMemory('MS'))
Mtavan.bind('<Button-1>',lambda event :funcMemory('MT'))
btndrsd.bind('<Button-1>',funcDarsad)
#hover buttons
btn1.bind('<Enter>',lambda event :funcBtnHover(img1,'images/btn1H.png'))
btn1.bind('<Leave>',lambda event :funcBtnHover(img1,'images/btn1.png'))
btn2.bind('<Enter>',lambda event :funcBtnHover(img2,'images/btn2H.png'))
btn2.bind('<Leave>',lambda event :funcBtnHover(img2,'images/btn2.png'))
btn3.bind('<Enter>',lambda event :funcBtnHover(img3,'images/btn3H.png'))
btn3.bind('<Leave>',lambda event :funcBtnHover(img3,'images/btn3.png'))
btn4.bind('<Enter>',lambda event :funcBtnHover(img4,'images/btn4H.png'))
btn4.bind('<Leave>',lambda event :funcBtnHover(img4,'images/btn4.png'))
btn5.bind('<Enter>',lambda event :funcBtnHover(img5,'images/btn5H.png'))
btn5.bind('<Leave>',lambda event :funcBtnHover(img5,'images/btn5.png'))
btn6.bind('<Enter>',lambda event :funcBtnHover(img6,'images/btn6H.png'))
btn6.bind('<Leave>',lambda event :funcBtnHover(img6,'images/btn6.png'))
btn7.bind('<Enter>',lambda event :funcBtnHover(img7,'images/btn7H.png'))
btn7.bind('<Leave>',lambda event :funcBtnHover(img7,'images/btn7.png'))
btn8.bind('<Enter>',lambda event :funcBtnHover(img8,'images/btn8H.png'))
btn8.bind('<Leave>',lambda event :funcBtnHover(img8,'images/btn8.png'))
btn9.bind('<Enter>',lambda event :funcBtnHover(img9,'images/btn9H.png'))
btn9.bind('<Leave>',lambda event :funcBtnHover(img9,'images/btn9.png'))
btn0.bind('<Enter>',lambda event :funcBtnHover(img0,'images/btn0H.png'))
btn0.bind('<Leave>',lambda event :funcBtnHover(img0,'images/btn0.png'))
btndot.bind('<Enter>',lambda event :funcBtnHover(imgdot,'images/btndatH.png'))
btndot.bind('<Leave>',lambda event :funcBtnHover(imgdot,'images/btndat.png'))
btnplsmins.bind('<Enter>',lambda event :funcBtnHover(imgplsmins,'images/btnplsminsH.png'))
btnplsmins.bind('<Leave>',lambda event :funcBtnHover(imgplsmins,'images/btnplsmins.png'))
btnmsvi.bind('<Enter>',lambda event :funcBtnHover(imgmsvi,'images/btnmsviH.png'))
btnmsvi.bind('<Leave>',lambda event :funcBtnHover(imgmsvi,'images/btnmsvi.png'))
btnc.bind('<Enter>',lambda event :funcBtnHover(imgc,'images/btncH.png'))
btnc.bind('<Leave>',lambda event :funcBtnHover(imgc,'images/btnc.png'))
btnclear.bind('<Enter>',lambda event :funcBtnHover(imgclear,'images/btnclearH.png'))
btnclear.bind('<Leave>',lambda event :funcBtnHover(imgclear,'images/btnclear.png'))
btnpls.bind('<Enter>',lambda event :funcBtnHover(imgpls,'images/btnplsH.png'))
btnpls.bind('<Leave>',lambda event :funcBtnHover(imgpls,'images/btnpls.png'))
btnminus.bind('<Enter>',lambda event :funcBtnHover(imgminus,'images/btnminusH.png'))
btnminus.bind('<Leave>',lambda event :funcBtnHover(imgminus,'images/btnminus.png'))
btntghsm.bind('<Enter>',lambda event :funcBtnHover(imgtghsm,'images/btntghsmH.png'))
btntghsm.bind('<Leave>',lambda event :funcBtnHover(imgtghsm,'images/btntghsm.png'))
btnzrb.bind('<Enter>',lambda event :funcBtnHover(imgzrb,'images/btnzrbH.png'))
btnzrb.bind('<Leave>',lambda event :funcBtnHover(imgzrb,'images/btnzrb.png'))
btnprntzb.bind('<Enter>',lambda event :funcBtnHover(imgprntzb,'images/btn(H.png'))
btnprntzb.bind('<Leave>',lambda event :funcBtnHover(imgprntzb,'images/btn(.png'))
btnprntzc.bind('<Enter>',lambda event :funcBtnHover(imgprntzc,'images/btn)H.png'))
btnprntzc.bind('<Leave>',lambda event :funcBtnHover(imgprntzc,'images/btn).png'))
btnksr.bind('<Enter>',lambda event :funcBtnHover(imgksr,'images/btnksrH.png'))
btnksr.bind('<Leave>',lambda event :funcBtnHover(imgksr,'images/btnksr.png'))
btnFaktoriel.bind('<Enter>',lambda event :funcBtnHover(imgFaktoriel,'images/btnFaktorielH.png'))
btnFaktoriel.bind('<Leave>',lambda event :funcBtnHover(imgFaktoriel,'images/btnFaktoriel.png'))
btnlog.bind('<Enter>',lambda event :funcBtnHover(imglog,'images/btnlogH.png'))
btnlog.bind('<Leave>',lambda event :funcBtnHover(imglog,'images/btnlog.png'))
btnpi.bind('<Enter>',lambda event :funcBtnHover(imgpi,'images/btnpiH.png'))
btnpi.bind('<Leave>',lambda event :funcBtnHover(imgpi,'images/btnpi.png'))
btnin.bind('<Enter>',lambda event :funcBtnHover(imgin,'images/btninH.png'))
btnin.bind('<Leave>',lambda event :funcBtnHover(imgin,'images/btnin.png'))
btne.bind('<Enter>',lambda event :funcBtnHover(imge,'images/btneH.png'))
btne.bind('<Leave>',lambda event :funcBtnHover(imge,'images/btne.png'))
btnsin.bind('<Enter>',lambda event :funcBtnHover(imgsin,'images/btnsinH.png'))
btnsin.bind('<Leave>',lambda event :funcBtnHover(imgsin,'images/btnsin.png'))
btncos.bind('<Enter>',lambda event :funcBtnHover(imgcos,'images/btncosH.png'))
btncos.bind('<Leave>',lambda event :funcBtnHover(imgcos,'images/btncos.png'))
btntan.bind('<Enter>',lambda event :funcBtnHover(imgtan,'images/btntanH.png'))
btntan.bind('<Leave>',lambda event :funcBtnHover(imgtan,'images/btntan.png'))
btnetn.bind('<Enter>',lambda event :funcBtnHover(imgetn,'images/btnetnH.png'))
btnetn.bind('<Leave>',lambda event :funcBtnHover(imgetn,'images/btnetn.png'))
btnxtn.bind('<Enter>',lambda event :funcBtnHover(imgxtn,'images/btnxtnH.png'))
btnxtn.bind('<Leave>',lambda event :funcBtnHover(imgxtn,'images/btnxtn.png'))
btnrdkl.bind('<Enter>',lambda event :funcBtnHover(imgrdkl,'images/btnrdklH.png'))
btnrdkl.bind('<Leave>',lambda event :funcBtnHover(imgrdkl,'images/btnrdkl.png'))
btnxt2.bind('<Enter>',lambda event :funcBtnHover(imgxt2,'images/btnxt2H.png'))
btnxt2.bind('<Leave>',lambda event :funcBtnHover(imgxt2,'images/btnxt2.png'))
btndrsd.bind('<Enter>',lambda event :funcBtnHover(imgdrsd,'images/btndrsdH.png'))
btndrsd.bind('<Leave>',lambda event :funcBtnHover(imgdrsd,'images/btndrsd.png'))
btnghadr.bind('<Enter>',lambda event :funcBtnHover(imgghadr,'images/btnbrktH.png'))
btnghadr.bind('<Leave>',lambda event :funcBtnHover(imgghadr,'images/btnbrkt.png'))

lbl1.grid(row=1,column=1,padx=(0,5),pady=(10,0))
lbl2.grid(row=2,column=1,padx=(0,5),pady=5)
ntjfrm.grid(row=1,column=1)
memoryfrm.grid(row=2,column=1,pady=10)
MClbl.place(x=40,y=10)
MRlbl.place(x=120,y=10)
Mplus.place(x=200,y=10)
Mmiuns.place(x=280,y=10)
MSlbl.place(x=360,y=10)
Mtavan.place(x=440,y=10)
btnsfrm.grid(row=3,column=1)
btnFaktoriel.grid(row=1,column=1,padx=2,pady=2)
btnpi.grid(row=1,column=2,padx=2,pady=2)
btnlog.grid(row=1,column=3,padx=2,pady=2)
btnin.grid(row=1,column=4,padx=2,pady=2)
btne.grid(row=1,column=5,padx=2,pady=2)
btnsin.grid(row=2,column=1,padx=2,pady=2)
btncos.grid(row=2,column=2,padx=2,pady=2)
btntan.grid(row=2,column=3,padx=2,pady=2)
btnetn.grid(row=2,column=4,padx=2,pady=2)
btnxtn.grid(row=2,column=5,padx=2,pady=2)
btnrdkl.grid(row=3,column=1,padx=2,pady=2)
btndrsd.grid(row=3,column=2,padx=2,pady=2)
btnxt2.grid(row=3,column=3,padx=2,pady=2)
btnghadr.grid(row=3,column=4,padx=2,pady=2)
btnksr.grid(row=3,column=5,padx=2,pady=2)
btnprntzb.grid(row=4,column=1,padx=2,pady=2)
btnprntzc.grid(row=4,column=2,padx=2,pady=2)
btnzrb.grid(row=4,column=3,padx=2,pady=2)
btntghsm.grid(row=4,column=4,padx=2,pady=2)
btnminus.grid(row=4,column=5,padx=2,pady=2)
btnsfrm2.grid(row=4,column=1)
btn7.grid(row=1,column=1,padx=(3,2),pady=2)
btn8.grid(row=1,column=2,padx=2,pady=2)
btn9.grid(row=1,column=3,padx=2,pady=2)
btnpls.grid(row=1,column=4,padx=2,pady=2)
btn4.grid(row=2,column=1,padx=(3,2),pady=2)
btn5.grid(row=2,column=2,padx=2,pady=2)
btn6.grid(row=2,column=3,padx=2,pady=2)
btnclear.grid(row=2,column=4,padx=2,pady=2)
btn1.grid(row=3,column=1,padx=(3,2),pady=2)
btn2.grid(row=3,column=2,padx=2,pady=2)
btn3.grid(row=3,column=3,padx=2,pady=2)
btnc.grid(row=3,column=4,padx=2,pady=2)
btnplsmins.grid(row=4,column=1,padx=(3,2),pady=2)
btn0.grid(row=4,column=2,padx=2,pady=2)
btndot.grid(row=4,column=3,padx=2,pady=2)
btnmsvi.grid(row=4,column=4,padx=2,pady=2)

win.mainloop()
