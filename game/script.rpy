####################################################
#   PART 1
#   Primary Author: Chris Dang
#   Secondary Authors: Chris Goebel, Nam-Giao Nguyen, Nichole Wong
####################################################
####################################################
#   This is where all characters are defined
####################################################

#Characters
define mc = Character("[MCname]", color=v.color, who_font="fonts/arial.ttf", what_font="fonts/arial.ttf")
define jd = Character("[JDname]", who_font="fonts/arial.ttf", what_font="fonts/arial.ttf")
define jdw = Character("[JDWname]", who_font="fonts/arial.ttf", what_font="fonts/arial.ttf")
define janed = Character("[janedName]", who_font="fonts/arial.ttf", what_font="fonts/arial.ttf")
define jc = Character("[JCname]", who_font="fonts/arial.ttf", what_font="fonts/arial.ttf")

define unknow =  Character("[unknowName]", color=v.color, who_font="fonts/arial.ttf", what_font="fonts/arial.ttf")
define Anna = Character("[AnnaName]", who_font="fonts/arial.ttf", what_font="fonts/arial.ttf") #new npc in chapter3
define Franklin = Character("Franklin")
define newCharacter = Character("???")
define Steve = Character("[SteveName]")
define shadow = Character("???", who_font = "fonts/arial.ttf", what_font="fonts/arial.ttf")

# The script of the game goes in this file.

label start:
    $ JDname = "???"
    $ JDWname = "Jannet Doe"
    $ janedName = "???"
    $ JCname = "???"
    $ AnnaName = "???"
    $ SteveName = "???"
    $ unknowName = "???"
    $ FN = "???"
    $ jd_dead = False
    $ janeD_dead = False
    $ jc_dead = False
    $ ana_dead = False
    $ frank_dead = False
    $ CurrentChap = 1
    $ total_trust = 10
    $ trust_for_anna = 5
    $ crops_tended_chp4 = 0
    $ money = 0
    $ day = 1
    $ wentWithJohnToMall = False
    $ MeetingAnna = False
    $ JannetBroughtBreakfast = False
    $ JohnGreetCh5 = False
    $ c51, c52 = False, False
    $ jinfo = False

    screen Money_Counter():
        text "{color=#FFF}{b}Money: $[money]{/b}{/color}" xpos 0.05 ypos 0.05
    screen Day_Counter():
        text "{color=#FFF}{b}Day: [day]{/b}{/color}" xpos 0.05 ypos 0.10
    show screen Day_Counter


    scene Woods_Sunset
    with fade

    "WHOOSH! CRASH! BANG!"
    shadow "Ow. What happened?"
    shadow "One moment I was sipping wine in a London pub. Now I'm...somewhere with a bunch of trees. In this hole."
    shadow "Where am I? Am I still in England? Where is everyone?"

    "You listen for the sound of footsteps, but all you hear is the sound of chirping crickets."
    "Time for a more direct approach."
    shadow "HELLO? CAN ANYONE HEAR ME?"
    shadow "HELLO?"

    "You yell into the pitch black woods, waiting for a reply."

    scene Ranch_Sunset
    show JD
    with dissolve

    jd "Easy, boys. Easy!"
    jd "What in tarnation was that?! Sounds like those noises came from the woods..."
    jd "Bet some poor drunken sop got lost. Typical."
    jd "Jannet, dear, I'm goin' off to see what's that sound! Watch the horses for me!"
    jdw "Okay! Be careful, Honey!"

    scene Woods_Sunset
    with fade

    show JD at center
    with dissolve

    jd "Well, what do we have here?"
    shadow "Finally, a face! Sir, could you offer me some assistance? I'm afraid this hole is rather deep."
    jd "Just hold on a minute, buddy. Give me yer name first."

    $ MCname = renpy.input("")
    $ MCname = MCname.strip()

label Confirm_Name:
    $ renpy.say(jd, MCname + ", huh?")
    menu:
        "Yes.":
            jump Customization
        "No.":
            jd "That ain't it? What's yer name then?"
            jump Confirm_Name_2

label Confirm_Name_2:
    $ MCname = renpy.input("")
    $ MCname = MCname.strip()
    jump Confirm_Name

label Customization:
    scene Black_Wall
    with fade

    hide screen Day_Counter
    call screen customization()
    show screen Day_Counter

    show Woods_Sunset
    show JD at center
    with dissolve

    jd "[MCname]. Can't say I recognize that name or yer face."
    jd "But I ain't one to let a man die in a rut either."

    jd "Give me yer hand."

    "You grab his hand."

    jd "Alright, buddy. Up we go."

    show VampySprite at left
    with dissolve

    show JD at right
    with dissolve

    mc "Thank you, sir. I am forever in your debt. May I have the name of my savior?"
    $ JDname = "John Doe"
    jd "It's John. John Doe. The guy who'll slug ya if ya make any funny moves."
    jd "Now, what am I gonna do with ya? Jannet would throw a fit if she found out I left someone out here like this."
    jd "Hmm, ya don't seem to be hidin' a weapon. And ya don't smell like beer..."

    jd "Alright. Come with me. We're goin' to my place."

    scene Black_Wall
    with fade

    scene Farmhouse_Night
    with fade

    show VampySprite at left
    with dissolve

    show JD at right
    with dissolve

    mc "This is a beautiful property, Mr. Doe--"
    jd "'Mr.Doe'? Spare the manners and call me John."
    jd "And quit the praise. Butterin' won't help ya. Just stay here."

    hide JD with dissolve

    "*CHUCHAK*"

    show JD_With_Gun at right
    with dissolve

    mc "A gun? Please, Mr. Doe! I hardly believe that I pose a threat to you."
    jd "Ya don't seem surprised. First ya ask for my name. Then my farm. Next thing I know, ya takin' my property!"
    mc "Sir, that's quite the leap in logic. Perhaps we could come to a compromise?"
    jd "I'm the one askin' the questions! What were ya doin' out there in those woods?"

    $ told_truth = False

label What_Do_You_Tell_John:
    menu:
        "Tell the truth" if told_truth == False:
            $ told_truth = True
            jump Tell_the_truth
        "Tell a lie":
            mc "I thought it'd be a lovely day to stroll through the woods."
            jd "A walk? In this weather? I don't believe ya."
            jump Tell_a_lie
        "Keep silent":
            mc "..."
            jd "Not sayin' a word, are we?"
            jump Tell_a_lie

label Tell_the_truth:
    mc "I'm afraid I cannot recall anything."
    jd "Hmph, if yer gonna lie, at least make it believable. I'll give ya one more chance to set yer story straight."
    jump What_Do_You_Tell_John


label Tell_a_lie:
    jd "Hmph, guess a man's gotta have his secrets."
    "John points his gun up to the sky."
    "*BANG*"
    jd "I swear, if ya harm me or my wife, I won't hesitate to shoot. Now git off my farm!"
    "While you could easily take down a man in a fight, you would rather not fight this late at night."
    "Reluctantly, you head towards the safety of the road marking the edge of John's property."

    scene Night_Highway
    with fade

    "You head down the path until you reach the highway and keep walking."
    "The winds howl and swipe at you with icy talons, trying to hold you back."
    "You have no idea how you got here, but you're leaving, even if the damn weather objects."
    "About an hour later (you suppose), you feel a wrenching sensation in your stomach."

    scene Black_Wall with fade

    "Black spots start to fill your vision. The street distorts."

    scene Farmhouse_Night

    "Somehow, you're back on Mr.Doe's property."
    # "What the hell is going on?"

label Highway_Choice:
    menu:
        "Keep walking":
            "You decide to brave the winds and head down the road."
            scene Black_Wall with fade
            "The same thing happens again. Your stomach twists. The world briefly goes black."
            "Then you end up in front of the Does' door."
            mc "Again?"
            $ choice = 1
            jump Highway_Choice
        "Return to the Does' Farm":
            "You must have taken a wrong turn somewhere."
            "Your bones ache. Your head pounds. Maybe a rest would help."
            "Perhaps if you make an apology to Mr. Doe and appeal to his good nature, he'd let you stay in his barn."
            mc "It's a plan at least."
            "You turn around and head back."
            $ choice = 2

    scene Farmhouse_Bed
    with fade

    show JDW at left
    with dissolve

    jdw "Did you really have to shoot at that poor man, Honey?"

    show JD_Sleepy at right
    with dissolve

    jd "Have ya seen his skin? Pale as a ghost! And he speaks all high and might like Frank. Bet they're in cahoots, schemin' to chase us off our farm."

    jdw "Honey! Aren't you making a few assumptions?"

    jd "Yeah, well, I don't see how he ended up in that crater in the woods! It ain't normal for someone to wander in that deep."

    "KNOCK. KNOCK."

    jdw "Who is it?"
    jd "I don't know. Don't move, darling. I'm gonna grab my gun."

    hide JDW
    with dissolve

    hide JD_Sleepy
    with dissolve

    "KNOCK! KNOCK!"

    show JD_With_Gun
    with dissolve

    jd "Quit knockin'! I'm coming already!"

    "*SLAM*"
    "John thrusts open the door and points his gun towards the opening."
    jd "Goddammit! Didn't ya hear me the first time?"

    scene Farmhouse_Night
    with fade

    show VampySprite at left
    with dissolve

    show JD_With_Gun at right
    with dissolve

    # if choice == 1:
    #     mc "Apologies, Mr. Doe. I'm not well acquainted with the area and wandered back here."
    #
    # if choice == 2:
    #     mc "Apologies for deceiving you earlier, Mr. Doe. I was afraid you'd scoff at the truth."

    menu:
        "Provide an excuse":
            mc "Apologies, Mr. Doe. I'm not well acquainted with the area and wandered back here."
        "Apologize for lying":
            mc "Apologies for deceiving you earlier, Mr. Doe. I was afraid you'd scoff at the truth."

    mc "I beg you. It's cold out here. Would you let me spend a night in your barn?"

    show JDW
    with dissolve

    jdw "Honey, just let the poor man stay a while. Look at how tired he is!"
    jdw "And didn't you say you wanted to hire someone to help you around the fields the other day? I'm sure he wouldn't mind?"

    mc "I'm happy to offer my assistance should it be needed."

    jd "Fine, but he doesn’t go anywhere near this house!"

    hide JDW with dissolve
    hide JD_With_Gun with dissolve

    scene Black_Wall with fade
    "You take a short nap in the Does' barn to recover some of your strength."
    # "In the early hours before dawn, you sneak away to the road."
    "Deep in the middle of the night you awaken from your nap and sneak away to the road."
    "This time, you head the other way."
    "You feel your limbs twist in all sorts of directions. Your vision fades."

    show Farmhouse_Night with fade
    mc "This is rather perplexing. I can't seem to get away from the farm."

    show VampySprite at center

    "You consider your options."
    mc "{i}I cannot seem to travel beyond a certain distance.{/i}"
    mc "{i}This is rather troublesome. I cannot subsist on two people. And such a remote location promises few meals.{/i}"
    mc "{i}I must find out where I am and why I'm here.{/i}"
    mc "{i}Clearly, I'm somewhere out in the countryside. By the Doe's accent, most likely the States. But where exactly?{/i}"
    mc "{i}Are we in Calfornia? Texas? Montana?{/i}"
    mc "{i}I doubt the Does conveniently keep any atlases...{/i}"

    "You consider your next actions carefully."

    mc "{i}I suppose I could ask around and see if I gather any information about where I am.{/i}"
    mc "{i}Then, if I'm fortunate, someone might be able to give hints about why I'm here.{/i}"
   
    mc "{i}It's a plan at least, albeit a rather poorly-thought-out one.{/i}"
    mc "{i}Better than idling in Mr. Doe's barn forever, I suppose.{/i}"
    mc "{i}Tonight, I rest. Tomorrow, I'll start asking questions.{/i}"


    "You collapse into a pile of hay and sleep."


    scene Farmhouse_Day
    with fade

    $ day += 1
    show screen Money_Counter

    "COCK-A-DOODLE-DOO."
    "BANG! BANG! BANG!"

    jd "Ya awake yet? Come on, wake up!"
    show JD at right with dissolve

    jd "Rise and shine! We’re going to town for supplies today."

    show VampySprite at left
    with dissolve

    mc "What?"

    jd "Ya heard me! Truck. Town. Supplies. Come on!"

    hide VampySprite with fade

    "You climb into John's truck. John guns the engine and you two head off to town."
    "You brace yourself for the strange barrier you've been experiencing. You wonder what John will say when you disappear from the truck."
    "John glances at you."

    jd "Ya alright?"
    mc "Pardon? Oh, yes. I shall be fine, Mr. Doe."

    show Black_Wall with fade
    "You keep expecting the world to go black or your stomach to twist, but nothing happens."
    "Eventually, you start to relax."

    scene Sad_Farm_1
    with fade

    "You spend time gazing at the local scenery."
    "The beauty of the rolling hills is marred by the sight of dilapidated buildings and barren fields."

    # mc "Mr. Doe?"
    # jd "John. None of that mister business."
    # mc "Mr. Doe -- I mean, John. Where are we?"
    # jd "Where are we? Did that fall damage yer head? These here are the hills of the North Dakotan countryside!"
    #
    # mc "{i}North Dakota? That's quite far from England.{/i}"
    # mc "{i}Well, at least I know where I am now.{/i}"
    #
    # mc "Those are indeed lovely hills, Mr -- John."
    # jd "Mighty beautiful, aren't they? Used to be prettier though."
    # jd "We always get a few bright-eyed farmers in the spring thinkin' they know how the business works."
    # jd "Then harvest comes and they realize they didn't plant enough to profit. They miss their bills. Then they give up the land."
    # jd "Frank's practically eaten 'em all up and spit 'em out to rot. Sad, really."
    #
    # mc "Ah, that's rather unfortunate. Apologies, Mr. Doe. I hope your farm never suffers such a dreadful fate."
    # jd "Thanks. I hope so too..."

    menu:
        "Ask where you are.":
            mc "Mr. Doe?"
            jd "John. None of that mister business."
            mc "Mr. Doe -- I mean, John. Where are we?"
            jd "Where are we? Did that fall damage yer head? These here are the hills of the North Dakotan countryside!"
            mc "{i}North Dakota? That's quite far from England.{/i}"
            mc "{i}Well, at least I know where I am now.{/i}"
            mc "Those are indeed lovely hills, Mr -- John."
            jd "Mighty beautiful, aren't they? Used to be prettier though."
            jd "We always get a few bright-eyed farmers in the spring thinkin' they know how the business works."
            jd "Then harvest comes and they realize they didn't plant enough to profit. They miss their bills. Then they give up the land."
            jd "Frank's practically eaten 'em all up and spit 'em out to rot. Sad, really."
            mc "Ah, that's rather unfortunate. Apologies, Mr. Doe. I hope your farm never suffers such a dreadful fate."
            jd "Thanks. I hope so too..."
        "Ask about the buildings":
            mc "Mr. Doe?"
            jd "John. None of that mister business."
            mc "Mr. Doe -- I mean, John. Are those buildings abandoned?"
            "There's a long pause."
            jd "...Yeah. These used to be the greatest hills in all of North Dakota. But now, they just house those wrecks."
            # jd "Unfortunately yes. Quite the eye sore on our beautiful North Dakotan hills aren't they?"
            mc "{i}North Dakota? That's quite far from England.{/i}"
            mc "{i}Well, at least I know where I am now.{/i}"
            mc "How did the farms end up that way, Mr. Doe?"
            jd "Well, we always get a few bright-eyed farmers in the spring thinkin' they know how the business works."
            jd "Then harvest comes and they realize they didn't plant enough to profit. They miss their bills. Then they give up the land."
            jd "Frank's practically eaten 'em all up and spit 'em out to rot. Sad, really."
            mc "Ah, that's rather unfortunate. Apologies, Mr. Doe. I hope your farm never suffers such a dreadful fate."
            jd "Thanks. I hope so too..."


    scene Strip_Mall
    with fade

    show JD
    with dissolve

    jd "Alright, buddy. We're here."
    jd "I’m gonna buy supplies. Feel free to tag along or wander off."
    jd "But if ya wander off, be back here by noon. I’ll need help loading the truck."

    $ Jane = 0
    $ Cash = 0
    $ Doe = 1
    $ TagAlongTrack = False
    $ WanderTrack = False

    menu:
        "Tag along":
            $ TagAlongTrack = True
            $ Jane += 1
            jump Tag_Along
        "Wander":
            $ WanderTrack = True
            $ Cash += 1
            jump Wander

label Tag_Along:
    "You follow John around the strip mall, past colorful window displays."
    "One display catches your eye: A eccentric combination of brightly-colored shirts, metallic studs, and animal prints."
    "John catches your wandering eye and grunts."
    jd "That store belongs to Jane. Sometimes I stop by to grab a few supplies."
    mc "Jane?"
    jd "Yeah, Jane. Shopkeeper. Say hi if ya want, but be careful. She'll yap until yer ears fall off."
    jd "I have some business to do at the supermarket. Just hang around until I get back."

    hide JD with fade
    show VampySprite at center with dissolve

    mc "I doubt this Jane character is as irritating as Mr. Doe implies."
    "You head inside the store."


label Clothing_Store_Meeting:
    scene Clothing_Store
    with fade

    show VampySprite at left
    with dissolve

    mc "Ah, what a wonderful assortment of clothes!"

    janed "Ooh? Did someone come to visit me?"

    show JaneD at right
    with dissolve

    janed "Hiya cutie! You look like you're new in town."

    $janedName = "Jane Dough"

    janed "My name is Jane Dough, but you can call me Jane."

    mc "Dough? Are you related to Mr. Doe, by any means?"

    janed "That old geezer? No, no. My last name is 'Dough' like cookie dough."

    mc "My sincerest apologies, Ms. Dough."

    janed "It's okay, sweetie. Everyone here has made that mistake once in a while."

    janed "So, looking for anything? Clothes? Accessories?"

    "Jane smiles and bats her eyelashes."

    janed "Or maybe you're looking for something a little more...exotic?"

    menu:
        "Mention waiting for someone":
            mc "No need, madam. I'm merely waiting for someone."
        "State that you're browsing":
            mc "No need, madam, I'm not looking for anything specific."

    "She shakes her head slowly and turns her attention to a pile of clothes on the counter."

    janed "Mmm, well, if there's anything you need, just holler, okay?"

    hide JaneD
    with dissolve

    if TagAlongTrack and wentWithJohnToMall == False:
        "A clock in the clothing store chimes. Time to meet up with John."
        jump At_noon
    if CurrentChap == 1:
        jump Next_Morning
    elif CurrentChap == 2:
        jump Chapter_Two_Morning
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5

label Wander:
    jd "Yer choice, buddy. Just remember we're surrounded by woods. Don't ya go too far in and get lost. I ain't goin' back to find ya."

label Creek_Stuff:
    scene Creek_Bridge with fade
    show VampySprite at left with dissolve

    "You decide to explore the surrounding area."
    "You carefully tread through a few bushes."
    "You're prepared to suddenly black out and end up at the Does' farm."
    "Eventually, you stumble upon a creek."
    "A man sits nearby the bridge, fishing."
    show JC at right with dissolve
    "He must have heard you coming. He turns and looks at you."
    jc "Woah? A ghost! Rad! I don't think I meet a ghost before."
    mc "Excuse me? I'm certainly not a ghost!"
    jc "Hey, relax! No harm in being a ghost. I won't tell. What's your name?"
    $ JCname = "Johnny Cash"
    mc "My name is [MCname]. And I am still not a ghost."
    jc "[MCname]? Sounds like a ghost name."
    jc "Name's Johnny. Johnny Cash. Like the singer. Everyone calls me J.C. Good to meet you ghost!"
    jc "Man, I've seen a lot of things in this town, but not ghosts. Wild..."

    mc "May I presume that you've lived in this town for a while then?"
    jc "Yeah. About two years. Maybe less. I came from Cali. Wanted to see the Badlands."
    jc "Hiked the Maah Dahh Hey trail. Pretty place. Well, when it's not frozen."
    jc "And now I'm stuck up here in Bottineau! Haha!"
    "He laughs for a bit."
    mc "{i}Bottineau? So that is the name of my prison. Good to know...{/i}"
    mc "{i}I wonder if outsiders suffer the same curse?{/i}"

    if WanderTrack and wentWithJohnToMall == False:
        $ wentWithJohnToMall = True
        "You open your mouth to ask, only to hear someone yelling in the distance."
        "You wonder if the voice belongs to John."
        mc "{i}Better to be safe than sorry, I suppose. I should not keep Mr. Doe waiting...{/i}"
        "Reluctantly, you leave Johnny at the creek."
        jump At_noon
    if CurrentChap == 1:
        jump Next_Morning
    elif CurrentChap == 2:
        jump Chapter_Two_Morning
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5


label At_noon:

    scene Strip_Mall
    with fade

    show JD
    with dissolve

    jd "Ah, ya came back! Thought ya got yerself lost again."

    jd "Take these sacks and load them into the truck. Then we go home."

    "You help John load a few sacks. You then join him on a trip back to the farm."

    scene Black_Wall
    with fade

    "You and John spend the rest of the day dragging the sacks from the truck to the barn and performing tasks around the farm."
    "You toil and sweat until the moon rises."
    jd "Well you did work the whole day, I guess you've earned this."
    $ money = money + 5
    "John pays you $5 for your work, then you retire to the barn."

    scene Farmhouse_Bed
    with fade

    show JD at right
    with dissolve

    show JDW at left
    with dissolve

    jdw "So, Honey? How was he today?"

    jd "Fine. Doesn't seem used to workin' on a farm. Kept runnin' back to the shade every ten minutes."

    jdw "But he worked really hard Honey. Even through dinner!"

    jd "Darling, what are ya tryin' to say?"

    jdw "Honey, I think we should keep him for a bit."

    jd "Wha-"

    jdw "He works hard, and we don't have to pay him much. All he wants is a place to stay."

    jd "No, he leaves tomorrow. I don't trust him."

    jdw "John, think of the farm. Have you seen this month's bill? We need all the help we can get."

    jd "..."

    jd "Fine, he can stick around."


label Next_Morning:
    if (Doe == 3 or Jane == 3 or Cash == 3) and (janeD_dead == False and jd_dead == False and jc_dead == False):
        jump Frenzy

    $ day += 1
    scene Farmhouse_Day
    with fade

    "COCK-A-DOODLE-DOO!"
    if JannetBroughtBreakfast == False:
        $ JannetBroughtBreakfast = True
        "KNOCK. KNOCK."
        "You wake up."

        show JDW at right
        with dissolve

        "Jannet stands at the door with a bowl of porridge."

        jdw "Good morning [MCname]? I brought you some breakfast."

        show VampySprite at left
        with dissolve

        mc "Thank you, Mrs. Doe."

        jdw "Honey is still getting ready. He said you can join him or run some errands in town."

    else:
        "You wake up."
        "It seems that Mrs. Doe has made you breakfast."
        mc "What shall I do today?"

    menu:
        "Help tend the farm":
            "You head off to the fields."
            $ Doe += 1
            jump Help_Farm
        "Run errands in town":
            jump Town_Options

label Help_Farm:
    scene Ranch_Sunset
    with fade

    show JD at left
    with dissolve

    show VampySprite at right
    with dissolve

    if Doe == 2:
        "Pulling up cornstalks is rather hard work."
        "You pull. You tug. You try to not snap the stems in two."
        "It takes hours, but you eventually manage to clear out a patch of land."
        "John nods approvingly."
        jd "Good work, [MCname]. I'll throw in a bit of change for yer work today."
        $ money += 5
        mc "The pleasure was all mine. Anything to repay your generosity."
        jd "Ya know what? You've been doin' good work around the farm recently."
        jd "Don't sleep in the barn tonight. I'll fluff up the couch cushions. Ya can sleep there instead."
        mc "Are you certain, Mr. John?"
        jd "Yeah, why not? It'll be much more comfy than a pile of hay."
        mc "Thank you."

    if Doe == 3:

        "As John and you rake away at the ground, John suddenly breaks out into a song."

        jd "Never gonna give ya up."

        mc "Never gonna let you down."

        jd "Never gonna run around--"

        menu:
            "and desert you!":
                jd "Heh. So yer familiar with the song, then?"
                mc "Anyone can appreciate music, Mr. John. That song is quite catchy, isn't it?"
                jd "Ha! Well, would ya look at that! I thought ya only listened to borin' classical music."
                "He laughs."
                jd "I love this song, ya know? Makes me remember my dancin' days..."

            "Pardon?":
                jd "Heh? Yer telling me you don't know that song?"
                mc "I'm afraid not. My preferences lean towards classical music."
                jd "Classical? Ha! I guess that does suit ya."
                "He laughs."
                jd "It's by some kid named Astley I think. One of my favorite songs. Makes me remember my dancin' days..."

        "He turns his head gazes off into the sunset."


        show JDW
        with dissolve

        jdw "Honey! [MCname]! Why don't you boys come in and enjoy a nice supper?"

        mc "Ah, I'm sure your meal is splendid, but I still have a few more plots to rake."

        mc "Worry not. I'll be able to find some food later. I wish you and John the most wonderful dinnertime."

        jdw "Oh, are you sure? You never seem to want to eat with us. At least take your day's pay."

        $ money += 5

    if CurrentChap == 1:
        jump Next_Morning
    elif CurrentChap == 2:
        jump John_Response
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5


label Town_Options:
    menu:
        "Buy more supplies":
            $ Jane += 1
            jump Strip_Mall_Fun
        "Collect fish from the creek":
            $ Cash += 1
            jump Creek_Shenanigans


label Strip_Mall_Fun:
    if Jane == 1:
        $ Jane = 1
        jump Clothing_Store_Meeting

    scene Clothing_Store
    with fade


    if Jane == 2:
        show VampySprite at left
        with dissolve

        "On that shelf, you spot a glint from a row of soup cans. On another shelf, you see a bedazzling sequinned dress."

        "With such a huge assortment of clothes and knicknacks, it's easy to forget what one originally came for."

        mc "Ah. What did Mrs. Doe request again?"

        "At the sound of your voice, Jane puts down a magazine and waves towards you."

        show JaneD at right
        with dissolve

        janed "Welcome back, cutie! You came back to see little old me?"

        menu:
            "Excuse yourself":
                mc "Sorry, Ms. Dough, but I'm preoccupied with an errand for Mr. Doe. Perhaps we can chat another time?"

                "She sighs."

            "Flirt":
                mc "Well perhaps I did..."
                
                "You give her a little wink. She smiles."
                
                mc "Unfortunately, I'm rather preoccupied running errands at the moment. May we chat another time?"
                
                "She sighs."

        janed "Oh, of course, hun. But before I go, I want to ask you something."

        janed "My friends and I are gonna attend a party tonight? You wanna come? You could be my plus-one..."

        mc "I appreciate the offer, Ms. Dough, but I don't have time. Please enjoy the party in my stead."

        "You search around and grab the items John wanted. You throw the cash on the counter before sprinting back to the farm."

    if Jane == 3:
        show VampySprite at left with dissolve

        "You walk into the store, expecting to hear Jane's voice."

        show JaneD at right with dissolve

        "Instead you see her hunched over a rather large black book, scribbing down notes with a red pen."

        mc "Excuse me. Ms. Dough?"

        "She slams the book shut and dashes in front of the counter."

        janed "Oh, you're back! Can't get enough of me, huh?"
        "She flashes a smile. She keeps her hands behind her back."

        mc "Indeed. May I ask what you are reading? You seemed rather engrossed in your book."

        janed "Ah. Um. That. That is...is....{i}Dracula{/i}! Yes, {i}Dracula{/i}! I borrowed it from Anna."

        mc "{i}Dracula{/i}? A classic! It holds a special place in my heart."

        "She freezes. She probably was not expecting that."

        mc "What do you think of it so far, Ms. Dough?"

        "Her face turns a bright red. She shuffles her feet."

        janed "I just started a few days ago so I don't really have any thoughts..."

        mc "I see. Well, I hope you will enjoy it. To observe the rise and fall of a great villain like Dracula is a unique opportunity. We could all learn from a few mistakes."

        janed "Yeah. Of course! Say, uh, [MCname], would you like to have lunch with me?"

        mc "Lunch? Jane, it's nearly four o'clock."

        janed "It doesn't have to be lunch. Maybe coffee or something. I'll pay for it."

        "She shuffles her feet."

        mc "I unfortunately must pass. I have business at the farm in about twenty minutes."
        mc "However, I would be greatful if you could give me these supplies."

        "You hand her a shopping list."

        janed "Of course, I'll help, [MCname]. Just give me a couple of minutes."

        "She hands you a box full of cans. You give her the money."

        "You quickly thank Jane and dash off with the box of supplies."
        hide VampySprite

    if CurrentChap == 1:
        jump Next_Morning
    elif CurrentChap == 2:
        jump Jane_Response
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5

label Creek_Shenanigans:
    if Cash == 1:
       jump Creek_Stuff

    scene Creek_Bridge
    with fade


    if Cash == 2:
        show VampySprite at left
        with dissolve

        "You decide today would be as good as any to fish."
        "You borrow a few fishing supplies from the Does' barn and head towards the creek."
        "When you arrive, you see Johnny."

        show VampySprite at left with dissolve
        show JC at right with dissolve

        "He grins."
        jc "Hey ghost! Welcome back! You here to fish too?"
        mc "Yes. Should I assume the same of you, Mr.Cash?"
        jc "Yeah. It's peaceful out here."
        "Johnny coughs."
        jc "Can't say I'm a fan of the winters though. Gets pretty cold."
        mc "Then why not leave?"
        "He shrugs."
        jc "Why not stay?"
        "You can't tell whether to take his remark seriously."
        mc "{i}Can he not leave the town too? Or is it that he chooses not to?{/i}"
        "You decide it's time to be more direct."
        mc "Mr. Cash, do you ever visit the nearby towns?"
        jc "Sometimes. Pop into Manitoba time to time, north of the border. Got some majestic views, man."
        "He nods and turns his attention back to his rod."
        mc "{i}Ah. It appears that Mr. Cash can leave whenever he wants then.{/i}"
        mc "{i}Whatever it is that keeps dragging me back is only affecting me...{/i}"
        "You spend the rest of the day fishing with Johnny."
        "When evening comes, you return to the farm."


    if Cash == 3:
        show VampySprite at left with dissolve

        "You cast your line into the water. When nothing bites, you throw it again. And again. And again."
        mc "No fish yet...perhaps I should visit another spot."
        "As you ponder the possible options (your limited mobility rather hinders things), Johnny emerges from the bushes."
        show JC at right with dissolve

        "When he spots your face, he grins."
        jc "Oh, oh! The ghost came back! Mind if I join you?"
        "Before you can respond, he plops beside you."
        "He seems to be in a particularly jolly mood today."
        jc "Fishing great, isn't it? I use to fish while sailin. Beat doing nothing on the deck."
        mc "Sailing?"
        "He nods."
        jc "Yeah! Sailing! From the coast. Got to see and learn all sorts of things."
        mc "That's a rather exciting history, Mr. Cash. Why are you still here then?"
        "Johnny shrugs."
        jc "Eh, Bottineau isn't that terrible, man. Sometimes I just want a quiet place to enjoy my books and fish."
        jc "Plus, sometimes you get to see and hear some funny things out here."
        jc "Like, there was someone out here near the creek a couple of days ago doing some kind of thing."
        jc "Candles, chanting -- that kind of stuff, you know?"
        jc "Anyway, soon that person was joined by this shorter figure carrying a big-looking book. Then they started flipping through it and dancing around in circles."
        jc "It was pretty weird, man, but it didn't look like they were harming anyone."
        mc "That is rather interesting, Mr. Cash? Who do you think they were?"
        jc "You asking me? I don't really know. I bet it was probably some teens playing a prank."
        jc "It was pretty dark. Didn't get a good look at their faces."
        mc "I see. Well, that is a rather interesting story, Mr. Cash."
        "Johnny nods. You continue to fish in silence."
        "Then you pack up your fishing gear and head back to the farm."

    if CurrentChap == 1:
        jump Next_Morning
    elif CurrentChap == 2:
        jump Cash_Response
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5

label Frenzy:
    scene Black_Wall
    with fade

    $ CurrentChap = 2

    "Night creeps over the farm."
    "Your stomach growls. You haven't eaten anything for a while."
    "You toss and turn, trying to supress your hunger, but eventually, it becomes too much."
    "Blood, blood, blood. You need blood. Now."

    menu:
        "Kill the Does":
            jump John_Dies
        "Kill Jane" if Jane > 0:
            jump Jane_Dies
        "Kill Johnny" if Cash > 0:
            jump Cash_Dies

label John_Dies:

    "They never hear your creep up the stairs. They barely notice you enter their room."
    "John goes down first. You knock him out with a well-aimed punch the face."
    "Jannet screams. You silence her with a quick bite to the neck."
    "Slowly, you drain the couple's bodies. Their blood tastes mellow and earthy."
    $ jd_dead = True

    jump Chapter1_End_John_Dead

label Jane_Dies:

    show Clothing_Store with fade

    "She does not hear you open the door. She does not notice you creep up behind her."
    "You let your fangs sink into her neck. She slumps over the counter."
    "Her blood is almost sickeningly sweet."
    "When you finish, you look around the store."
    "You stuff as many heavy-looking items as you can into her pockets. You tie the cash register to her chest."
    "Then you dipose the body in the creek."

    $ janeD_dead = True

    jump Chapter1_End_Jane_Dead

label Cash_Dies:

    show Creek_Bridge with fade
    "You find him in his usual spot, slumped over by the bridge."
    "You strike. Johnny doesn't have any time to react."
    "You savor the taste of salt, citrus, and thyme."
    "Fortunately, his coat is rather spacious. You stuff his pockets with rocks and twigs before kicking him into the creek."
    "You wonder if anyone will miss him."

    $ jc_dead = True

    jump Chapter1_End_Cash_Dead
    return
