####################################################
#   PART 0 (Character Creation)
#   Primary Author: Nichole Wong
#   Secondary Author: Chris Goebel
####################################################
init python:

    class Vampy:
        def __init__(self):
            self.name = "Vampy"
            self.color = "#ad0c00"
            self.dir = "images/Vampy2.0/"

        def getPart(self, part, index):
            #return self.dir + part + str(index) + ".png"
            return self.dir + part + str(index) + "_80s.png"

    v = Vampy()

    hair, eyes, face, acc, arms, legs = 1, 1, 1, 1, 1, 1
    maxHair, maxEyes, maxFaces, maxAcc, maxArms, maxLegs = [2, 5, 4, 2, 3, 2]

    def changeHair(dir):
        global hair
        hair += dir
        if hair > maxHair: hair = 1
        if hair < 1: hair = maxHair

    def changeEyes(dir):
        global eyes
        eyes += dir
        if eyes > maxEyes: eyes = 1
        if eyes < 1: eyes = maxEyes

    def changeFace(dir):
        global face
        face += dir
        if face > maxFaces: face = 1
        if face < 1: face = maxFaces

    def changeArms(dir):
        global arms
        arms += dir
        if arms > maxArms: arms = 1
        if arms < 1: arms = maxArms

    def changeLegs(dir):
        global legs
        legs += dir
        if legs > maxLegs: legs = 1
        if legs < 1: legs = maxLegs

    def changeAcc(dir):
        global acc
        acc += dir
        if acc > maxAcc: acc = 1
        if acc < 1: acc = maxAcc

####################################################
#   Set up Vampy's sprite
####################################################

layeredimage VampySprite:
    always v.dir + "Base.png"

    if hair == 1:
        v.getPart("Hair", 1)
    elif hair == 2:
        v.getPart("Hair", 2)

    if eyes == 1:
        v.getPart("Eyes", 1)
    elif eyes == 2:
        v.getPart("Eyes", 2)
    elif eyes == 3:
        v.getPart("Eyes", 3)
    elif eyes == 4:
        v.getPart("Eyes", 4)
    elif eyes == 5:
        v.getPart("Eyes", 5)

    if face == 1:
        v.getPart("Face", 1)
    elif face == 2:
        v.getPart("Face", 2)
    elif face == 3:
        v.getPart("Face", 3)
    elif face == 4:
        v.getPart("Face", 4)

    if legs == 1:
        v.getPart("Legs", 1)
    elif legs == 2:
        v.getPart("Legs", 2)

    if arms == 1:
        v.getPart("Arms", 1)
    elif arms == 2:
        v.getPart("Arms", 2)
    elif arms == 3:
        v.getPart("Arms", 3)
    elif arms == 4:
        v.getPart("Arms", 4)

    if acc == 1:
        v.getPart("Face", 4)
    elif acc == 2:
        v.getPart("Accessory", 1)

####################################################
#   Part 0: Character Creation Screen
####################################################

screen customization():
    hbox:
        yalign 1.0
        xalign 1.0
        spacing 100

    vbox:
        text "{color=#d3d3d3}{size=24}{font=fonts/arial.ttf} Hair{/font}{/color}{/sizeS}"
        hbox:
            textbutton "{color=#d3d3d3}<{/color}" action Function(changeHair, -1)
            textbutton "{color=#d3d3d3}>{/color}" action Function(changeHair, 1)
        text "{color=#d3d3d3}{size=24}{font=fonts/arial.ttf} Eyes{/font}{/color}{/size}"
        hbox:
            textbutton "{color=#d3d3d3}<{/color}" action Function(changeEyes, -1)
            textbutton "{color=#d3d3d3}>{/color}" action Function(changeEyes, 1)
        text "{color=#d3d3d3}{size=24}{font=fonts/arial.ttf} Facial Hair{/font}{/color}{/size}"
        hbox:
            textbutton "{color=#d3d3d3}<{/color}" action Function(changeFace, -1)
            textbutton "{color=#d3d3d3}>{/color}" action Function(changeFace, 1)
        text "{color=#d3d3d3}{size=24}{font=fonts/arial.ttf} Shirt{/font}{/color}{/size}"
        hbox:
            textbutton "{color=#d3d3d3}<{/color}" action Function(changeArms, -1)
            textbutton "{color=#d3d3d3}>{/color}" action Function(changeArms, 1)
        text "{color=#d3d3d3}{size=24}{font=fonts/arial.ttf} Pants{/font}{/color}{/size}"
        hbox:
            textbutton "{color=#d3d3d3}<{/color}" action Function(changeLegs, -1)
            textbutton "{color=#d3d3d3}>{/color}" action Function(changeLegs, 1)
        text "{color=#d3d3d3}{size=24}{font=fonts/arial.ttf} Accessories{/font}{/color}{/size}"
        hbox:
            textbutton "{color=#d3d3d3}<{/color}" action Function(changeAcc, -1)
            textbutton "{color=#d3d3d3}>{/color}" action Function(changeAcc, 1)
        textbutton "{color=#d3d3d3}{size=24}{font=fonts/arial.ttf} Done{/font}{/color}{/size}" action Return()

    add "VampySprite" at center
