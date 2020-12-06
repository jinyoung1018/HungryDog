from bangtal import*

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene1 = Scene('게임설명','Images/게임설명.png')
scene2 = Scene('scene2','Images/배경2.png')
scene3 = Scene('scene3','Images/집안.png')

startButton = Object('Images/start.png')
startButton.locate(scene1,90,570)
startButton.setScale(1.7)
startButton.show( )

restartButton = Object('Images/restart.png')
restartButton.locate(scene2,560,500)
restartButton.setScale(1.7)

restartButton2 = Object('Images/restart.png')
restartButton2.locate(scene3,560,500)
restartButton2.setScale(1.7)

endButton = Object('Images/end.png')
endButton.locate(scene2,560,400)
endButton.setScale(1.7)

endButton2 = Object('Images/end.png')
endButton2.locate(scene3,560,400)
endButton2.setScale(1.7)



playButton = Object('Images/play.png')
playButton.locate(scene2,610,20 )
playButton.show( )

house = Object('Images/house.png')
house.locate(scene2,950,90)
house.setScale(0.6)
house.show( )

dog = Object('Images/dog.png')
dog.setScale(0.2)
dog.x = 0
dog.y = 90
dog.locate(scene2,dog.x, dog.y)
dog.show( )

dog2 = Object('Images/pet.png')
dog2.setScale(0.2)
dog2.x = 0
dog2.y = 90
dog2.locate(scene2,dog2.x, dog2.y)
dog2.show( )

bone1 = Object('Images/bone.png')
bone1.setScale(0.1)
bone1.x = 100
bone1.y = 720
bone1.locate(scene2,bone1.x, bone1.y)
bone1.show( )

bone2 = Object('Images/bone.png')
bone2.setScale(0.1)
bone2.x = 130
bone2.y = 720
bone2.locate(scene2,bone2.x, bone2.y)
bone2.show( )

bone3 = Object('Images/bone.png')
bone3.setScale(0.1)
bone3.x = 1000
bone3.y = 720
bone3.locate(scene2,bone2.x, bone2.y)
bone3.show( )

bone4 = Object('Images/bone.png')
bone4.setScale(0.1)
bone4.x = 500
bone4.y = 720
bone4.locate(scene2,bone4.x, bone4.y)
bone4.show( )

bone5 = Object('Images/bone.png')
bone5.setScale(0.1)
bone5.x = 320
bone5.y = 720
bone5.locate(scene2,bone5.x, bone5.y)
bone5.show( )

bone6 = Object('Images/bone.png')
bone6.setScale(0.1)
bone6.x = 850
bone6.y = 720
bone6.locate(scene2,bone6.x, bone6.y)
bone6.show( )

bone7 = Object('Images/bone.png')
bone7.setScale(0.1)
bone7.x = 400
bone7.y = 720
bone7.locate(scene2,bone7.x, bone7.y)
bone7.show( )

bone8 = Object('Images/bone.png')
bone8.setScale(0.1)
bone8.x = 470
bone8.y = 720
bone8.locate(scene2,bone8.x, bone8.y)
bone8.show( )

bone9 = Object('Images/bone.png')
bone9.setScale(0.1)
bone9.x = 600
bone9.y = 720
bone9.locate(scene2,bone9.x, bone9.y)
bone9.show( )

bone10 = Object('Images/bone.png')
bone10.setScale(0.1)
bone10.x = 700
bone10.y = 720
bone10.locate(scene2,bone10.x, bone10.y)
bone10.show( )

bone11 = Object('Images/bone.png')
bone11.setScale(0.1)
bone11.x = 610
bone11.y = 720
bone11.locate(scene2,bone11.x, bone11.y)
bone11.show( )

box1 = Object('Images/box.png')
box1.setScale(0.24)
box1.locate(scene3,357,243)
box1.show( )

box2 = Object('Images/box.png')
box2.setScale(0.24)
box2.locate(scene3,479,120)
box2.show( )

box3 = Object('Images/box.png')
box3.setScale(0.24)
box3.locate(scene3,870,80)
box3.show( )

box4 = Object('Images/box.png')
box4.setScale(0.24)
box4.locate(scene3,1150,180)
box4.show( )

bowl = Object('Images/bowl.png')
bowl.setScale(0.24)
bowl.locate(scene3,357,243)


food = Object('Images/food.png')
food.setScale(0.24)
food.locate(scene3,870,80)

plus1 = Object('Images/plus.png')
plus1.setScale(0.05)
plus1.locate(scene2,700,690)


three1 = Object('Images/three.png')
three1.setScale(0.05)
three1.locate(scene2,720,690)


s1 = Object('Images/s.png')
s1.setScale(0.05)
s1.locate(scene2,740,690)

plus2 = Object('Images/plus.png')
plus2.setScale(0.05)
plus2.locate(scene2,700,690)


three2 = Object('Images/three.png')
three2.setScale(0.05)
three2.locate(scene2,720,690)


s2 = Object('Images/s.png')
s2.setScale(0.05)
s2.locate(scene2,740,690)

plus3 = Object('Images/plus.png')
plus3.setScale(0.05)
plus3.locate(scene2,700,690)


three3 = Object('Images/three.png')
three3.setScale(0.05)
three3.locate(scene2,720,690)


s3 = Object('Images/s.png')
s3.setScale(0.05)
s3.locate(scene2,740,690)

plus4 = Object('Images/plus.png')
plus4.setScale(0.05)
plus4.locate(scene2,700,690)


three4 = Object('Images/three.png')
three4.setScale(0.05)
three4.locate(scene2,720,690)


s4 = Object('Images/s.png')
s4.setScale(0.05)
s4.locate(scene2,740,690)

plus5 = Object('Images/plus.png')
plus5.setScale(0.05)
plus5.locate(scene2,700,690)


three5 = Object('Images/three.png')
three5.setScale(0.05)
three5.locate(scene2,720,690)


s5 = Object('Images/s.png')
s5.setScale(0.05)
s5.locate(scene2,740,690)

plus6 = Object('Images/plus.png')
plus6.setScale(0.05)
plus6.locate(scene2,700,690)


three6 = Object('Images/three.png')
three6.setScale(0.05)
three6.locate(scene2,720,690)


s6 = Object('Images/s.png')
s6.setScale(0.05)
s6.locate(scene2,740,690)

plus7 = Object('Images/plus.png')
plus7.setScale(0.05)
plus7.locate(scene2,700,690)


three7 = Object('Images/three.png')
three7.setScale(0.05)
three7.locate(scene2,720,690)


s7 = Object('Images/s.png')
s7.setScale(0.05)
s7.locate(scene2,740,690)

plus8 = Object('Images/plus.png')
plus8.setScale(0.05)
plus8.locate(scene2,700,690)


three8 = Object('Images/three.png')
three8.setScale(0.05)
three8.locate(scene2,720,690)


s8 = Object('Images/s.png')
s8.setScale(0.05)
s8.locate(scene2,740,690)

plus9 = Object('Images/plus.png')
plus9.setScale(0.05)
plus9.locate(scene2,700,690)


three9 = Object('Images/three.png')
three9.setScale(0.05)
three9.locate(scene2,720,690)


s9 = Object('Images/s.png')
s9.setScale(0.05)
s9.locate(scene2,740,690)

plus10 = Object('Images/plus.png')
plus10.setScale(0.05)
plus10.locate(scene2,700,690)


three10 = Object('Images/three.png')
three10.setScale(0.05)
three10.locate(scene2,720,690)


s10 = Object('Images/s.png')
s10.setScale(0.05)
s10.locate(scene2,740,690)

plus11 = Object('Images/plus.png')
plus11.setScale(0.05)
plus11.locate(scene2,700,690)


three11 = Object('Images/three.png')
three11.setScale(0.05)
three11.locate(scene2,720,690)


s11 = Object('Images/s.png')
s11.setScale(0.05)
s11.locate(scene2,740,690)




count = 0

timer1 = Timer(4)
timerStart = Timer(10)
timer2 = Timer(3)
timer3 = Timer(1)
timer4 = Timer(2)
timer5 = Timer(5)
timer6 = Timer(6)
timer7 = Timer(7)
timer8 = Timer(8)
timer9 = Timer(9)
timer10 = Timer(5)
timer11 = Timer(6)
timerDog2 = Timer(3)
timerHide1 = Timer(0.5)
timerHide2 = Timer(0.5)
timerHide3 = Timer(0.5)
timerHide4 = Timer(0.5)
timerHide5 = Timer(0.5)
timerHide6 = Timer(0.5)
timerHide7 = Timer(0.5)
timerHide8 = Timer(0.5)
timerHide9 = Timer(0.5)
timerHide10 = Timer(0.5)
timerHide11 = Timer(0.5)




def time_onTimeout():
    dog2.x = dog2.x + 10
    dog2.locate(scene2, dog2.x,dog2.y)

    global count
    count = count + 1
    if count < 9000:
        timerDog2.set(0.1)
        timerDog2.start()

timerDog2.onTimeout = time_onTimeout
   
def time_onTimeout():
    bone1.y = bone1.y - 10
    bone1.locate(scene2, bone1.x,bone1.y)

    global count
    count = count + 1
    if count < 20000:
        timer1.set(0.01)
        timer1.start()

timer1.onTimeout = time_onTimeout


def time_onTimeout():
    bone2.y = bone2.y - 10
    bone2.locate(scene2, bone2.x,bone2.y)

    global count
    count = count + 1
    if count < 20000:
        timer2.set(0.07)
        timer2.start()

timer2.onTimeout = time_onTimeout


def time_onTimeout():
    bone3.y = bone3.y - 10
    bone3.locate(scene2, bone3.x,bone3.y)

    global count
    count = count + 1
    if count < 20000:
        timer3.set(0.1)
        timer3.start()

timer3.onTimeout = time_onTimeout

def time_onTimeout():
    bone4.y = bone4.y - 10
    bone4.locate(scene2, bone4.x,bone4.y)

    global count
    count = count + 1
    if count < 20000:
        timer4.set(0.01)
        timer4.start()

timer4.onTimeout = time_onTimeout

def time_onTimeout():
    bone5.y = bone5.y - 10
    bone5.locate(scene2, bone5.x,bone5.y)

    global count
    count = count + 1
    if count < 20000:
        timer5.set(0.05)
        timer5.start()

timer5.onTimeout = time_onTimeout

def time_onTimeout():
    bone6.y = bone6.y - 10
    bone6.locate(scene2, bone6.x,bone6.y)

    global count
    count = count + 1
    if count < 20000:
        timer6.set(0.02)
        timer6.start()

timer6.onTimeout = time_onTimeout

def time_onTimeout():
    bone7.y = bone7.y - 10
    bone7.locate(scene2, bone7.x,bone7.y)

    global count
    count = count + 1
    if count < 20000:
        timer7.set(0.05)
        timer7.start()

timer7.onTimeout = time_onTimeout

def time_onTimeout():
    bone8.y = bone8.y - 10
    bone8.locate(scene2, bone8.x,bone8.y)

    global count
    count = count + 1
    if count < 20000:
        timer8.set(0.01)
        timer8.start()

timer8.onTimeout = time_onTimeout

def time_onTimeout():
    bone9.y = bone9.y - 10
    bone9.locate(scene2, bone9.x,bone9.y)

    global count
    count = count + 1
    if count < 20000:
        timer9.set(0.05)
        timer9.start()

timer9.onTimeout = time_onTimeout

def time_onTimeout():
    bone10.y = bone10.y - 10
    bone10.locate(scene2, bone10.x,bone10.y)

    global count
    count = count + 1
    if count < 20000:
        timer10.set(0.08)
        timer10.start()

timer10.onTimeout = time_onTimeout

def time_onTimeout():
    bone11.y = bone11.y - 10
    bone11.locate(scene2, bone11.x,bone11.y)

    global count
    count = count + 1
    if count < 20000:
        timer11.set(0.1)
        timer11.start()

timer11.onTimeout = time_onTimeout

def time_onTimeout():

    plus1.hide( )
    three1.hide( )
    s1.hide( )


timerHide1.onTimeout = time_onTimeout

def time_onTimeout():

    plus2.hide( )
    three2.hide( )
    s2.hide( )


timerHide2.onTimeout = time_onTimeout

def time_onTimeout():

    plus3.hide( )
    three3.hide( )
    s3.hide( )


timerHide3.onTimeout = time_onTimeout
 
def time_onTimeout():

    plus4.hide( )
    three4.hide( )
    s4.hide( )


timerHide4.onTimeout = time_onTimeout

def time_onTimeout():

    plus5.hide( )
    three5.hide( )
    s5.hide( )


timerHide5.onTimeout = time_onTimeout

def time_onTimeout():

    plus6.hide( )
    three6.hide( )
    s6.hide( )


timerHide6.onTimeout = time_onTimeout

def time_onTimeout():

    plus7.hide( )
    three7.hide( )
    s7.hide( )


timerHide7.onTimeout = time_onTimeout

def time_onTimeout():

    plus8.hide( )
    three8.hide( )
    s8.hide( )


timerHide8.onTimeout = time_onTimeout

def time_onTimeout():

    plus9.hide( )
    three9.hide( )
    s9.hide( )


timerHide9.onTimeout = time_onTimeout

def time_onTimeout():

    plus10.hide( )
    three10.hide( )
    s10.hide( )


timerHide10.onTimeout = time_onTimeout

def time_onTimeout():

    plus11.hide( )
    three11.hide( )
    s11.hide( )


timerHide11.onTimeout = time_onTimeout

def startButton_onMouseAction(x,y,action):
   scene2.enter( )

   timer1.set(4) 
   timerStart.set(10)
   timer2.set(3)
   timer3.set(1)
   timer4.set(2)
   timer5.set(5)
   timer6.set(6)
   timer7.set(7)
   timer8.set(8)
   timer9.set(9)
   timer10.set(5)
   timer11.set(6)
   timerDog2.set(3)

   showTimer(timerStart)
   timerStart.start( )
   timer1.start()
   timer2.start()
   timer3.start()
   timer4.start()
   timer5.start()
   timer6.start()
   timer7.start()
   timer8.start()
   timer9.start()
   timer10.start()
   timer11.start()
   timerDog2.start()

   restartButton.hide( )
   endButton.hide( )
   playButton.show( )

   

   dog.x = 0
   dog2.x = 0
   bone1.y = 720
   bone2.y = 720
   bone3.y = 720
   bone4.y = 720
   bone5.y = 720
   bone6.y = 720
   bone7.y = 720
   bone8.y = 720
   bone9.y = 720
   bone10.y = 720
   bone11.y = 720


   dog.locate(scene2,dog.x, dog.y)
   dog2.locate(scene2,dog2.x, dog2.y)
   bone1.locate(scene2,bone1.x, bone1.y)
   bone2.locate(scene2,bone2.x, bone2.y)
   bone3.locate(scene2,bone3.x, bone3.y)
   bone4.locate(scene2,bone4.x, bone4.y)
   bone5.locate(scene2,bone5.x, bone5.y)
   bone6.locate(scene2,bone6.x, bone6.y)
   bone7.locate(scene2,bone7.x, bone7.y)
   bone8.locate(scene2,bone8.x, bone8.y)
   bone9.locate(scene2,bone9.x, bone9.y)
   bone10.locate(scene2,bone10.x, bone10.y)
   bone11.locate(scene2,bone11.x, bone11.y)
   
   box1.setImage('Images/box.png')
   box2.setImage('Images/box.png')
   box3.setImage('Images/box.png')
   box4.setImage('Images/box.png')

   food.hide( )
   box3.show( )
   restartButton2.hide( )
   endButton2.hide( )

   

startButton.onMouseAction = startButton_onMouseAction

def restartButton_onMouseAction(x,y,action):
   startGame(scene1)
   timerDog2.start()
  
restartButton.onMouseAction = restartButton_onMouseAction

def restartButton2_onMouseAction(x,y,action):
   startGame(scene1)
   timerDog2.start()
  
restartButton2.onMouseAction = restartButton2_onMouseAction


def playButton_onMouseAction(x,y,action):
    dog.x = dog.x + 30
    dog.locate(scene2,dog.x,dog.y)

    if dog.x > 950 and dog2.x < dog.x:
        showMessage('집 도착!!')
        scene3.enter( )
    elif dog.x < 950 and dog2.x > 950:
        showMessage('게임실패! 먼저 도착 해야돼요ㅜㅜ')
        restartButton.show( )
        endButton.show( )
        timerStart.stop( )
        

       
playButton.onMouseAction = playButton_onMouseAction

def endButton_onMouseAction(x,y,action):
    endGame( )
endButton.onMouseAction = endButton_onMouseAction

def endButton2_onMouseAction(x,y,action):
    endGame( )
endButton2.onMouseAction = endButton2_onMouseAction



def bone1_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone1.hide( )
    plus1.show( )
    three1.show( )
    s1.show( )
    timerHide1.start()

    
bone1.onMouseAction = bone1_onMouseAction

def bone2_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone2.hide( )
    plus2.show( )
    three2.show( )
    s2.show( )
    timerHide2.start()

    
bone2.onMouseAction = bone2_onMouseAction

def bone3_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone3.hide( )
    plus3.show( )
    three3.show( )
    s3.show( )
    timerHide3.start()

    
bone3.onMouseAction = bone3_onMouseAction

def bone4_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone4.hide( )
    plus4.show( )
    three4.show( )
    s4.show( )
    timerHide4.start()

    
bone4.onMouseAction = bone4_onMouseAction

def bone5_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone5.hide( )
    plus5.show( )
    three5.show( )
    s5.show( )
    timerHide5.start()

    
bone5.onMouseAction = bone5_onMouseAction

def bone6_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone6.hide( )
    plus6.show( )
    three6.show( )
    s6.show( )
    timerHide6.start()

    
bone6.onMouseAction = bone6_onMouseAction

def bone7_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone7.hide( )
    plus7.show( )
    three7.show( )
    s7.show( )
    timerHide7.start()


bone7.onMouseAction = bone7_onMouseAction

def bone8_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone8.hide( )
    plus8.show( )
    three8.show( )
    s8.show( )
    timerHide8.start()

    
bone8.onMouseAction = bone8_onMouseAction

def bone9_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone9.hide( )
    plus9.show( )
    three9.show( )
    s9.show( )
    timerHide9.start()

    
bone9.onMouseAction = bone9_onMouseAction

def bone10_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone10.hide( )
    plus10.show( )
    three10.show( )
    s10.show( )
    timerHide10.start()

    
bone10.onMouseAction = bone10_onMouseAction

def bone11_onMouseAction(x,y,action):
    
    timerStart.increase(3)
    bone11.hide()
    plus11.show( )
    three11.show( )
    s11.show( )
    timerHide11.start()
    
bone11.onMouseAction = bone11_onMouseAction



def box1_onMouseAction(x,y,action):
    
    box1.setImage('Images/package.png')
   
box1.onMouseAction = box1_onMouseAction

def box2_onMouseAction(x,y,action):
    
    box2.setImage('Images/package.png')

    
box2.onMouseAction = box2_onMouseAction

def box3_onMouseAction(x,y,action):
    
    box3.hide( )
    food.show( )

    showMessage('게임성공!!!')
    restartButton2.show( )
    endButton2.show( )
    timerStart.stop( )
    
    
box3.onMouseAction = box3_onMouseAction



def box4_onMouseAction(x,y,action):
    
    box4.setImage('Images/package.png')

    
box4.onMouseAction = box4_onMouseAction

def timer_onTimeout( ):
    showMessage('게임실패!! 시간이 다 됐어요ㅜㅜ')
    timerStart.stop
    playButton.hide( )
    restartButton2.show( )
    endButton2.show( )
    restartButton.show( )
    endButton.show( )
    
timerStart.onTimeout = timer_onTimeout




startGame(scene1)
