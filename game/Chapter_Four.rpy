####################################################
#   PART 4
#   Primary Author: Jared Clark
#   Secondary Authors: Chris Goebel, Nichole Wong
####################################################
label Start_chp4:
    $ jc_info = 0
    $ gone_to_bank = False
    $ gone_to_psychic = False
    $ gone_to_supplies = False
    $ gone_to_creek = False
    $ CurrentChap = 4
    $ bonfire_invite = False
    $ keepMoney = False
    $ frank_dead = False
    $ ask1, ask2, ask3 = False, False, False
    $ FranklinCounter = 0

    scene Farmhouse_Day
    with fade

    "COCK-A-DOODLE-DOO!"

    if jd_dead == True:
        jump Meeting_the_Banker
    else:
        jump Meeting_the_Banker2

label Meeting_the_Banker:
    "When you wake up, you find a letter in the mailbox."
    "It seems that the Does needed to pay off a loan at the bank."
    "It wouldn't do good to lose the farm to debt collectors just yet -- not when you have no means to escape Bottineau."
    "You search around the house. There! The money!"
    "You check the address on the letter, snatch the wad of cash, and dash off to the bank."
    jump Going_to_the_Bank

label Meeting_the_Banker2:

    "You walk towards the fields and find John scratching his head."
    "He notices you and turns around."
    show VampySprite at left with dissolve 
    show JD at right with dissolve

    jd "Hey, [MCname]. Got any idea how to fix a pivot?"
    mc "What kind of pivot?"
    
    "John points to what looks like a very long sprinkler on wheels."
    jd "That kind of pivot."
    mc "I'm afraid repairing pivots is outside of my knowledge."
    jd "Didn't think so."
    "He sighs."
    jd "Looks like I'll be spendin' my day fixin' this then."
    jd "Well if ya can't fix anythin' how about this?"
    jd "I need ya to take a letter to the bank for me. Ya can do that, right?"
    mc "Of course."
    hide VampySprite with fade
    hide JD with fade
    "John hands you an envelope and gives you directions to the bank branch at the mall."
    "You could have guessed it would be the mall. There aren't many other options in this town."
    
    jump Going_to_the_Bank

label Going_to_the_Bank:
    scene Bank_Lobby
    with fade

    show Franklin at right
    with dissolve
    
    "You walk into the bank. A well-dressed man taps his fingers on the counter."
    "The sounds of your footsteps prompts him to straighten his posture and smile."
    Franklin "Good afternoon, sir, what can I help you with?"
    mc "Good afternoon. I am here to deliver this letter on behalf of the Does."
    "You hand over the envelope."
    Franklin "Ah, thank you. One moment--"
    "He jots down something in a ledger and slides your envelope into a drawer."
    Franklin "There. All done Mister....?"
    mc "[MCname]. I recently arrived here."
    Franklin "Nice to meet you, Mr. [MCname]. Call me Franklin. Hope you've been enjoying our town."
    mc "It's a bit remote, but that doesn't make this town unpleasant."
    Franklin "Yeah, it's nice town. Terribly small though. I've met everyone here at least once."
    mc "{i}Everyone? He must be familiar with the townspeople then.{/i}"
    mc "{i}I wonder if he knows anyone interested in the occult. That would explain why I never seem able to leave town.{/i}"
    mc "{i}Or if not, perhaps he can point me to the more unscrupulous folk.{/i}"
    mc "Everyone? You must chat with a lot of people then!"
    Franklin "Eh, not really. But I hear interesting snippets from time to time."
    Franklin "Stop by anytime! I'll have to get back to work."
    "You wave goodbye to Franklin and leave the bank."
    jump CHP4_morning
    
label Lets_eat:
    scene Ranch_Sunset
    with fade
    $ day += 1

    "The sun sets on another hard day's work."

    scene Black_Wall
    with fade

    menu:
        "Kill John and Jannet" if jd_dead == False:
            $ jd_dead = True

        "Kill Jane Dough" if janeD_dead == False:
            $ janeD_dead = True

        "Kill Johnny Cash" if jc_dead == False:
            $ jc_dead = True

        "Kill Anna" if ana_dead == False:
            $ ana_dead = True
    jump CHP4_morning

label CHP4_morning:
#    $ crops_tended_chp4 = 0
    scene Farmhouse_Day
    with fade
    $ day += 1

    show VampySprite
    with dissolve
    hide VampySprite
    with dissolve

    if FranklinCounter >= 7:
        jump CHP4_end

    menu:
        "Tend to the crops" if crops_tended_chp4 == 0:
            $ FranklinCounter += 1
            $ Doe += 1
            jump CHP4_crops
        "Go get supplies" if janeD_dead == False and gone_to_supplies == False:
            $ FranklinCounter += 1
            $ Jane += 1
            jump CHP4_Supplies
        "Go to the creek" if jc_dead == False and gone_to_creek == False:
            $ FranklinCounter += 1
            $ Cash += 1
            jump CHP4_Creek
        "Visit the fortune teller" if ana_dead == False and gone_to_psychic == False and money >= 5:
            $ FranklinCounter += 1
            jump CHP4_Psychic
        "Visit the Bank" if gone_to_bank == False and frank_dead == False:
            $ FranklinCounter += 1
            jump Time_with_frank
    jump CHP4_end

label CHP4_crops:
    if jd_dead:
        mc "It isn't much, but it's honest work."
        $ money = money + 5
        jump CHP4_morning
    else:
        jump John_info

label CHP4_Supplies:
#meet jane say im ready to meet your friends go to bonfire later tonight
    
    scene Clothing_Store
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    if Jane < 3:
        jump Strip_Mall_Fun
    else:
        janed "Welcome back! What do you need today, hun?"
        mc "I'm here to see you, Ms. Dough."
        "You spend the rest of the day chatting with Jane."
        "You discuss the weather, the news, rumors -- smalltalk."
        if bonfire_invite == False:
            janed "Oh, yeah, [MCname], we're having a bonfire tonight near the woods. You should come by later!"
            janed "It'll be pretty low key. Just a bunch of people sitting around a large fire."
            $ bonfire_invite = True # can now go to the bonfire event at night. used in chapter 5
            mc "I shall consider your invitation."
        "You return to the farm."
    jump CHP4_morning

label CHP4_Creek:
    scene Creek_Bridge
    with fade

    show VampySprite at left
    with dissolve

    show JC at right
    with dissolve

    if Cash < 3:
        jump Creek_Shenanigans
    else: 
        "You spend time catching fish with Johnny."
        mc "{i}If I stay here long enough, will I end up like him?{/i}"
        mc "{i}Will I spend my days in the woods, forever idling?{/i}"

    jump CHP4_morning

label CHP4_Psychic:
    scene Psychic_store
    with fade

    show Anna at right
    with dissolve

    show VampySprite at left
    with dissolve

    jump time_with_ana
    
label Time_with_frank:
    scene Bank_Lobby
    with fade

    show Franklin at right
    with dissolve

    Franklin "Great to see you again, Mr. [MCname]. What can I do for you?"
    
    menu: 
        "Ask about Jane":
            mc "May I inquire about Jane?"
            Franklin "The shopkeeper? I'm afraid I don't know her too well."
            Franklin "She isn't a local. I think she moved into town about a year ago? Two? I'm not quite sure."
            Franklin "She always comes here with a story about some wild party or concert."
            Franklin "Lively one. She's got spirit. Pretty friendly too."
            Franklin "She's even friends with Anna! I guess that's not too interesting to you, but Anna is known to be a bit of a recluse. You rarely see Anna outside of her store."
            if janeD_dead:
                Franklin "I haven't seen Jane recently, though. I noticed her shop was closed when I stopped by the other day."
        "Ask about Anna":
            mc "May I ask about the fortune teller who sets up shop at the mall?"
            Franklin "Oh, Anna? People have a lot of stories about her Grandma."
            Franklin "They all say her grandmother was the real deal. A witch -- the \"double bubble toil and trouble\" type."
            Franklin "I had a lot of customers come in claiming she could see the future. I don't believe myself, but..."
            "He speaks in a hushed voice."
            Franklin "It's a stupid concidence, but the bank made an error in her favor a couple years back. I fixed it and recovered the funds."
            Franklin "Then I got chased around by swarms of hornets for three months. Hornets! Smelled like bugspray the whole time."
            Franklin "Her granddaughter though? Most people think Anna is all show and no tell."
            Franklin "Poor girl. Must be hard living up to a legend. At least she has a friend."
            Franklin "Anna usually stays inside her shop, but not for Jane. Sometimes they sneak out together with a bundle of books and scrolls."
            Franklin "I wonder what they do out there? Some ritual I guess? Or maybe a really fancy reading."
            if ana_dead:
                Franklin "Anna hasn't been around recently. Maybe she closed up shop and moved."
        "Ask about Johnny":
            mc "May I ask about the man at the creek?"
            Franklin "Johnny? Yeah, he's from California. He's been here for a while."
            Franklin "Friendly guy. Keeps to himself mostly. Almost singlehandedly justifies the Bottineau Public Library's existence."
            mc "Fascinating."
            Franklin "My sister works at the library. She says Johnny's the first person who uses ILL's. Had to learn how to fill out the forms because of him."
            mc "ILL's?"
            Franklin "Inter-library loans. Our local library's collection is pretty small. But as a public library, we have access to the entire public library system."
            Franklin "Theoretically, of course. Johnny's the only one that uses it. He gets a lot of use out of that library card."
            mc "What do you suppose he reads?"
            "Franklin shrugs."
            Franklin "I don't know. Privacy regulations and librarian-client confidentiality and all that. Sometimes I see him read a poetry book though."
            Franklin "If he's not reading, he's probably fishing. Sometimes he'll tell me a bunch of weird stuff."
            Franklin "Apparently, a lot of crazy things happen in the woods."
            if jc_dead:
                Franklin "My sister says Johnny hasn't visited the library for a long time though. Must've wandered off somewhere."
    mc "Thank you for your time, sir."
    Franklin "It was a pleasure talking with you. Have a nice day!"
    show Black_Wall with fade
    "You wave goodbye to Franklin and head back towards the farm."
    jump CHP4_morning


label CHP4_end:
    scene Drak_pic
    with fade
    
    "In your dreams, an unknown voice calls out to you."
    unknow "Enjoying your time here, [MCname]?"
    unknow "I promise someday, everything will be revealed."

    jump Start_chp5 #first label of chapter 5
