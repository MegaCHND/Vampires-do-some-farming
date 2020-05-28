####################################################
#   This is where all characters are defined
####################################################

#Characters
define mc = Character("[MCname]", color=v.color, who_font="fonts/Precious.ttf", what_font="fonts/Precious.ttf")
define jd = Character("[JDname]", who_font="fonts/ALGER.ttf", what_font="fonts/ALGER.ttf")
define jdw = Character("[JDWname]", who_font="fonts/ITCBLKAD.ttf", what_font="fonts/ITCBLKAD.ttf")
define janed = Character("[janedName]", who_font="fonts/PORKYS.ttf", what_font="fonts/PORKYS.ttf")
define jc = Character("[JCname]", who_font="fonts/comic.ttf", what_font="fonts/comic.ttf")

define unknow =  Character("[unknowName]", color=v.color, who_font="fonts/Precious.ttf", what_font="fonts/Precious.ttf")
define Anna = Character("[AnnaName]", who_font="fonts/ITCBLKAD.ttf", what_font="fonts/ITCBLKAD.ttf") #new npc in chapter3
define Franklin = Character("Franklin")
define newCharacter = Character("???")
define Steve = Character("Steve")

# The script of the game goes in this file.

label start:

    $ JDname = "???"
    $ JDWname = "Jannet Doe"
    $ janedName = "???"
    $ JCname = "???"
    $ AnnaName = "???"
    $ unknowName = "???"
    $ FN = "???"
    $ jd_dead = False
    $ janeD_dead = False
    $ jc_dead = False
    $ ana_dead = False
    $ CurrentChap = 1
    $ total_trust = 10
    $ trust_for_anna = 5
    $ crops_tended_chp4 = 0

    scene Ranch_Sunset

    "*Whoosh noise* Crash! Bang *oh my leg sfx"

    jd "What in tarnation?! That spooked my horses!"

    scene Woods_Sunset

    jd "Well...What do we have here? "

    $ MCname = renpy.input("Hey Mr, what’s your name?")
    $ MCname = MCname.strip()

    jd "Let me give ya a hand...and a jacket. All right buddy, up we go."

    $ JDname = "John Doe"

    show JD
    jd "I’ll take ya back to my place, we can wash that soot and dust off of ya there. Name’s John Doe if ur interested."

    scene Black_Wall

    jd "Come out to the front after ya freshen up some. Feel free to wear what I’ve got lying around."

    call screen customization()

    show VampySprite

    scene Farmhouse_Night

    show VampySprite at left
    pause
    show JD_With_Gun at right
    jd "*Cocks rifle* Alrighty, so what were ya doing in those woods?"

    menu:
        "Tell the truth":
            jump Tell_the_truth
        "Keep Silent":
            jump Tell_a_lie
        "Make something up":
            $ y = renpy.input("better be persuasive")
            jump Tell_a_lie

label Tell_the_truth:
    mc "I can't rememb'r"
    jd "hmph, if you're gonna lie, at least make it believable. I’ll give ya one more chance to get your story straight."
    menu:
        "Keep Silent":
            jump Tell_a_lie
        "Make something up":
            $ y = renpy.input("better be persuasive")
            jump Tell_a_lie

label Tell_a_lie:
    jd "hmph, guess a man’s gotta have his secrets huh? *Fires gun* "
    jd "I swear, ya harm me or my wife and the next one’s goin between the eyes. Now get off my property!"

    scene Night_Highway

    mc "fie. What shalt I do? the weath'r is bitter cold and th're is nay roof ov'r mine own headeth"
    menu:
        "Keep going down the road":
            $ choice1 = 1
        "Apologize to John":
            $ choice1 = 2

    scene Farmhouse_Bed

    show JDW at left

    jdw "Did you really have to shoot at that poor man Honey?"

    show JD_Sleepy at right

    jd "I don't like the color of his skin or the way he speaks. Everything about him is off."

    jdw "Honey! That’s racist!"

    jd "Yeah, well I definitely don’t like how he ended up in that crater in the woods! I swear that “man” is a wendigo darling"

    "*knock knock*"

    jd "He better not have come back…"

    hide JDW
    hide JD_Sleepy

    "*knock knock*"

    show JD

    jd "I’m coming!  I’m coming!"

    "Mr. Doe cocks his rifle and slams open the door"

    jd "God dammit"

    scene Farmhouse_Night

    show VampySprite at left
    show JD_With_Gun at right

    if choice1 == 1:
        mc " I'm s'rry mr.  Doe, I seemeth to hath gotten lost and madeth mine own way backeth here."
        mc "The weath'r is bitter cold tonight.  Shall thee alloweth me to stayeth in thine barn?"
        jump Back_To_Story1

    if choice1 == 2:
        mc "I apologizeth f'r falsing Mr.  Doe but thee wouldst not believeth me coequal if 't be true I toldeth the sooth."
        mc " The weath'r is bitter cold tonight.  Shall thee alloweth me to stayeth in thine barn?"
        jump Back_To_Story1

label Back_To_Story1:

    show JDW
    jdw "Honey just let the poor man stay for a while. He can help around the farm to earn his keep."

    jd "Fine but he doesn’t go anywhere near this house!"

    scene Farmhouse_Day

    "The rooster crows at the crack of dawn but it's cry is drowned out by Mr.Doe's unrelent banging"

    show JD

    jd "Rise and shine pale boy! We’re going to town for supplies today."

    show VampySprite at right

    mc "Hiss!"

    jd "Don’t hiss at me Wendigo! Ur gonna get in the truck and like it!"

    scene Sad_Farm_1

    menu:
        "...":
            $ choice1 = 1
        "grumble...":
            $ choice1 = 1

    scene Sad_Farm_2

    menu:
        "...":
            $ choice1 = 1
        "Fidget...":
            $ choice1 = 1

    scene Sad_Farm_3

    menu:
        "...":
            $ choice1 = 1
        "Ask about the farms":
            $ choice1 = 2

    if choice1 == 1:
        jd "Got something to say spit it out already"
        mc "Wherefore art th're so many exsufflicate farms?"
        jump Back_To_Story2

    if choice1 == 2:
        jump Back_To_Story2

label Back_To_Story2:
    jd "ah that...Farm crisis. A few years ago, land was really cheap and Russia really wanted wheat."
    jd "But now, there’s too much wheat, and  no one wants to buy. People can’t pay for their farms anymore so they had to give up their farms."
    jd "Frank's practically eaten em all up and spit em out to rot."
    jd "Sad thing really."

    mc "I offer mine own condolences"

    jd "Thanks…"

    scene Strip_Mall

    show JD
    jd "I’m gonna buy supplies. Feel free to tag along or wander off but if ya wander off, be back here by noon. I’ll need help loading the truck"

    $ Jane = 0
    $ Cash = 0
    $ Doe = 1

    menu:
        "Tag along":
            $ Jane += 1
            jump Tag_Along
        "Wander":
            $ Cash += 1
            jump Wander

label Tag_Along:
    jd "Alrighty then, just hang out around the mall. I’ll be done soon"

    scene Clothing_Store

    show VampySprite at left

    mc "So many styles of robes!"

    janed "Hiya QT! Anythin suit your fancy?"

    mc "Hiss! An apparition hast hath appeared!"

    $ janedName = "Jane Dough"
    show JaneD at right

    janed "I’m not a ghost silly. I’m Jane, Jane Dough!"

    mc "Doth thee has't any relation to John Doe?"

    janed "No no! My last name is D-O-U-G-H not D-O-E"

    mc "Well then, colours me"

    janed "mm, welp if there’s anything you need, just holler. K QT?"

    mc "Thanketh thee"

    hide JaneD

    "A clock in the clothing store chimes as [MCname] leaves"

    jump At_noon

label Wander:
    jd "Well then, feel free to explore the town. But remember, here at noon."

    scene Creek_Bridge

    show VampySprite at left

    mc "Mine own! What a lovely sight..."

    jc "*Cough cough* *Hack hack*"

    mc "ruin'd by such unsightly sounds…"

    jc "*WHEEZE*"

    "After following the sounds, [MCname] arives at it's source"

    mc "Sir, art thee tis fine?"

    $ JCname = "Johnny Cash"
    show JC at right

    jc "*Puffs* yeeeeeah maan. Name’s Johnny Cash. Call me JC if you want man. *cough*"

    jc "Heyyy man, you wanna try some?"

    mc "Nay  I'm fine. I has't a meeting with an aquantance"

    jc "Oh suure man, wellll come back sooon"

    hide JC

    "With a beautiful sight fouled by the company, [MCname] decides it's better to head back"

    jump At_noon

label At_noon:

    scene Strip_Mall
    show JD

    jd "Alrighty, ur back!"

    jd "Help me load this stuff in the truck and lets go home"

    scene Black_Wall

    "[MCname] returns to the Doe farm and spend the rest of the day helping Mr. Doe"

    scene Farmhouse_Bed
    show JD at right
    show JDW at left

    jdw "So Honey? How was he today?"

    jd "Ok I guess. Feels like he doesn't like the sun much. He kept running back to the shade every 10 minutes"

    jdw "But he worked really hard Honey. Even worked through dinner."

    jd "Darling, what are ya tryin to say?"

    jdw "Honey, I think we should keep him for a bit."

    jd "Wha-"

    jdw "He works hard and doen't ask for money. All he wants is a place to stay."

    jd "No, he leaves tomorrow. I still don't trust him."

    jdw "John think of the farm. We need all the help we can get."

    jd "..."

    jd "Fine, he can stick around."

label Next_Morning:

    if Doe == 3:
        jump Frenzy
    if Jane == 3:
        jump Frenzy
    if Cash == 3:
        jump Frenzy

    scene Farmhouse_Day

    "The rooster crows at the crack of dawn and its cry is actually heard for once followed by a gentle knock on the door"

    show JDW at right

    jdw "Hello? I brought you some breakfast"

    show VampySprite at left

    mc "Thanketh thee"

    jdw "Honey is still getting ready. He said you can join him or run some errands in town"

    menu:
        "Help tend the farm":
            $ Doe += 1
            jump Help_Farm
        "Run errands in town":
            jump Town_Options

label Help_Farm:
    scene Ranch_Sunset
    show JD at left
    show VampySprite at right

    if Doe == 2:
        "Digging holes is straining for someone like [MCname]"

        "However, once dug deep enough, the shade is quite pleasent"

        jd "Phew, hey thanks for helping out."

        mc "Nay, thanketh thee f'r giving me lodging"

        jd "Ya know what, no need to sleep in the barn tonight. I'll fluff the couch cushions and you can sleep there tonight."

        mc "Art thee sure? Well thanketh thee"

    if Doe == 3:
        
        "On the porch of the Doe farm, Mrs. Doe enjoys her Honey's singing...and [MCname]'s attempt."
        
        jd "Never gonna give you up"

        mc "Nev'r gonna alloweth thee down"

        jd "Never gonna run around"

        mc "and des'rt thee"

        show JDW

        jdw "Honey, it's time for dinner."

        jdw "[MCname], come in too."

        mc "I'm going to finish up Mrs. Doe.  W'rry not about me"

        jdw "Are you sure? You never seem to want to eat with us"

    jump Next_Morning

label Town_Options:
    menu:
        "Buy more supplies":
            $ Jane += 1
            jump Strip_Mall_Fun
        "Collect fish from the creek":
            $ Cash += 1
            jump Creek_Shenanigans

label Strip_Mall_Fun:
    scene Clothing_Store

    if Jane == 1:
        show VampySprite at left

        mc "So many styles of robes!"

        janed "Hiya QT! Anythin suit your fancy?"

        mc "Hiss! An apparition hast hath appeared!"

        $ janedName = "Jane Dough"
        show JaneD at right

        janed "I’m not a ghost silly. I’m Jane, Jane Dough!"

        mc "Doth thee has't any relation to John Doe?"

        janed "No no! My last name is D-O-U-G-H not D-O-E"

        mc "Well then, colours me"

        janed "mm, welp if there’s anything you need, just holler. K QT?"

        mc "Thanketh thee"

    if Jane == 2:
        show VampySprite at left

        "With such a huge assortment of clothes and knicknacks, it's easy to forget what one originally came for."

        mc "Nay. What didst Mrs. Doe asketh f'r again?"

        show JaneD at right

        janed "Hiya QT! Need help with anything?"

        mc "Nay prithee leaveth"

        janed "Fine... but before I go, my friends and I were gonna have a party tonight. Would you like to come?"

        mc "Sorry but i hath oth'r plans"

    if Jane == 3:
        show VampySprite at left

        "For instance, the cover of this black book is sinister but oddly charming"

        mc "Ah this one looks valorous"

        show JaneD at right

        janed "Oh you're back. Why would a QT like you visit a store like this so often?"

        mc "Prithee, ms dough, mine own nameth is [MCname], prithee useth it"

        janed "Oh sorry about that. Um...so I guess I've been alittle annoying...Would you mind having lunch with me?"

        mc "..."

        janed "I'll pay for it..."

        mc "I'll consid'r thee f'rgiven if't thee giveth me these supplies"

        janed "Really? Yay!"

        "Through some twist of fate, [MCname] and Jane have become acquaintances!"

    jump Next_Morning

label Creek_Shenanigans:
    scene Creek_Bridge

    if Cash == 1:
        show VampySprite at left

        mc "Mine own! What a lovely sight..."

        jc "*Cough cough* *Hack hack*"

        mc "ruin'd by such unsightly sounds…"

        jc "*WHEEZE*"

        "After following the sounds, [MCname] arives at it's source"

        mc "Sir, art thee tis fine?"

        $ JCname = "Johnny Cash"
        show JC at right

        jc "*Puffs* yeeeeeah maan. Name’s Johnny Cash. Call me JC if you want man. *cough*"

        jc "Heyyy man, you wanna try some?"

        mc "Nay I'm fine. I has't a meeting with an aquantance"

        jc "Oh suure man, wellll come back sooon"

    if Cash == 2:
        show VampySprite at left

        "Fishing alone in the woods has it's own charm to it don't you think?"

        mc "Haa...This is nice."

        "However that charm is broken as the bushes rustle around"

        mc "hm?"

        "*Cough Cough*"

        show JC at right

        jc "Oh! I diiidn't think you'll be back..."

        mc "I am not h're f'r thee but to fish."

        mc "Mine own nameth is [MCname]"

        mc "I pref'r thee useth"

        jc "Yeeeah, I'm not gonna remember that buddy"

        mc "Then i suggesteth thee leaveth"

    if Cash == 3:
        show VampySprite at left

        "Though, being lost in your thoughts is only useful when you have something to think about"

        mc "Tis boring..."

        "Oh look! Something to think about."

        mc "hm?"

        show JC_Fishing at right

        jc "Oh hey man! Mind if I join you?"

        mc "um..."

        jc "Ya know, I might have been rude the other day but I really can't remember names..."

        jc "Anyways, I have this map of all the best fishing spots. Here have a look."

        mc "Well...Thanketh thee"

        jc "Eyy no problem man. And I reeeally don't wanna by rube but you're really pale.\n I think you should see a doctor, man."

    jump Next_Morning

label Frenzy:
    scene Black_Wall

    $ CurrentChap = 2

    "In the Doe farm, everyone sleeps soundly...well almost everyone."
    "[MCname] tosses and turns on the couch, trapped in a nightmare."
    "A voice pluages him, binding him to it's command..."

    if Jane == 0:
        menu:
            "Kill John":
                jump John_Dies
            "Kill Johnny":
                jump Cash_Dies

    if Cash == 0:
        menu:
            "Kill John":
                jump John_Dies
            "Kill Jane":
                jump Jane_Dies

    menu:
        "Kill John":
            jump John_Dies
        "Kill Jane":
            jump Jane_Dies
        "Kill Johnny":
            jump Cash_Dies


label John_Dies:

    "The rooster crows, it's cry heard loud and clear over the Doe farm."
    "The only other sound that can be heard comes from a shovel placing dirt over the dried corpses of Mr. and Mrs Doe."
    
    $ jd_dead = True
    $ janeD_dead = False
    $ jc_dead = False
    $ chap_two_days = 0

    jump Chapter1_End_John_Dead

label Jane_Dies:
    
    $ jd_dead = False
    $ janeD_dead = True
    $ jc_dead = False
    $ chap_two_days = 0

    jump Chapter1_End_Jane_Dead

label Cash_Dies:
    
    $ jd_dead = False
    $ janeD_dead = False
    $ jc_dead = True
    $ chap_two_days = 0

    jump Chapter1_End_Cash_Dead
    return
