####################################################
#   PART 3
#   Primary Author: Enjie Lei
#   Secondary Authors: Chris Goebel, Nam-Giao Nguyen, Nichole Wong
####################################################
label Start_chp3:
    $ CurrentChap = 3
    $ AnnaInfo = False
    $unknowName = "???"

    scene Drak_pic
    with fade

    unknow "I have found you..."

    show VampySprite at left
    with dissolve

    mc "Excuse me!?"

    hide VampySprite
    with dissolve

    unknow "My dreams lie within you.."

    show VampySprite at left
    with dissolve

    mc "Reveal yourself, malevolent presence!"
    jump wake_up


label wake_up:

    scene Farmhouse_Bed
    with fade

    show VampySprite
    with dissolve

    mc "A dream?"
    "COCK-A-DOODLE-DOO!"
    "The rooster crows only amplify your headache"
    mc "Perhaps I should take a walk and get some fresh air..."

    jump meet_anna


label meet_anna:
    $ MeetingAnna = False
    $ trust = 1
    $ trust2 = 1
    scene Strip_Mall
    with fade

    show Anna at right
    with dissolve

    Anna "Excuse me, sir"

    show VampySprite at left
    with dissolve

    mc "Pardon? Are you addressing me?"
    Anna "Do you believe in destiny?"
    mc "Who are you?"
    Anna "The answers to your questions can be found among the stars, traveller."
    $ AnnaName = "Anna"
    Anna "My name is Anna, and I can decipher the stars' cryptic messages."
    Anna "I see you're rather lost. For you, sir, I'll do a free reading."

    menu:
        "Agree":
            $ first_choice = 0
        "Refuse":
            mc "Apologies, madam, but I will not fall for your deceptions."
            $ first_choice = 1

        "Stay silent":
            "You say nothing."
            $ first_choice = 1
            
    if first_choice == 0:
        "Maybe. Just maybe she is a real psychic. Or a fraud."
        "But on the off-chance that her skills are genuine, she might be able to explain why you are trapped in this town."
        mc "Why not? Please tell me my fortune, miss."
        Anna "Of course. Right this way."
        "She leads you into her shop."
        jump in_Psychic_store
    if first_choice == 1:
        Anna "Are you afraid to face your destiny? Are you afraid of what lies in your future."
        "You scoff. What difference will it make knowing tomorrow's events? You have thousands of years to recover from your mistakes."
        mc "I will not be so easily fooled by this talk of destiny!"
        Anna "Really? I guess you don't want to know why you're trapped in this town then..."
        "You stare at her, bewildered."
        mc "How could you possibly know--"
        Anna "The spirits know everything, and I am their messenger."
        Anna "I can see many obstacles ahead of you. I can see the chains that confine you to our town."
        Anna "Come. Let's see if the spirits can help you with your predictament."
        "She leads you into her shop."
        jump in_Psychic_store

label in_Psychic_store:
    scene Psychic_store
    with fade

    show Anna at right
    with dissolve

    show VampySprite at left
    with dissolve
    
    Anna "Welcome to my shop, traveller. Let's see what Madam Fate surprises us with today."
    Anna "My reading works like this: you ask me a question. I call. They answer."
    Anna "What would you like to know?"
    
    menu:
        "Ask about why you're here":
            mc "Every effort to leave this town ends miserably. Why am I here?"
            "Anna closes her eyes and stretches her arms towards the ceiling."
            Anna "Madam Fate! This young man wishes to know what prevents him from leaving this town."
            "After a long pause, she opens her eyes and looks at you."
            Anna "She says you've been called to serve. Someone or something wants you to stay."
            Anna "Unless they reveal themselves to you or you confront them, you shall forever be cursed to wander this place."
            Anna "I suggest you keep your eyes and ears open."
        "Ask about the future":
            mc "Am I forever to walk this town, never to leave?"
            "Anna closes her eyes and stretches her arms towards the ceiling."
            Anna "Madam Fate! This young man wish to know his future."
            "After a long pause, she opens her eyes, looks at you, and frowns."
            Anna "The future looks rather grim, I'm afraid."
            Anna "She says you've been called to serve. Someone or something wants you to stay."
            Anna "Unless they reveal themselves to you or you confront them, you shall forever be cursed to wander this place."
            Anna "I suggest you keep your eyes and ears open."
    
    # mc "Your friends do not seem eager to help me, madam. They are rather vague."
    # Anna "The spirits watch our moves, but they do not have time to interfere in mortal affairs."
    # Anna "They're quite busy too, you know?"
    # "She gives you a cold, hard stare."
    # Anna "Look, let's look at the crystal ball. Perhaps you'll see something you like there instead."
    
    Anna "Did the spirits answer you questions, young man?"
    mc "Not quite. I'd like to make a few more inquiries."
    "She nods."
    Anna "Then perhaps you'd be interested in consulting the crystal ball."
    
    jump ask_crystal_ball


label ask_crystal_ball:
    show VampySprite at left
    with dissolve

    show Anna at right
    with dissolve

    if MeetingAnna == True:
        Anna "Ten dollars please."
        "You hand her the money."
    else:
        $ MeetingAnna = True
        Anna "Normally, I would charge you ten dollars for this. But today, it's free."
        mc "Ten dollars? That's a rather expensive service.?"
        "She glares at you."
        Anna "Quiet, you. The ten dollars go towards a good cause."

    hide VampySprite
    with dissolve

    hide Anna
    with dissolve

    "You glare at the crystal ball."
    "It sits there on the table. You cannot make out anything."

    show VampySprite at left
    with dissolve

    mc "Do you believe me foolish enough to not see this is an ordinary globe of glass?"

    show Anna at right
    with dissolve

    Anna "No, please. Just wait two -- five -- more minutes. The ball will do something, I swear!"

    scene Crystal_ball
    with fade

    "Suddenly Anna disappears as the ball glows with a bright, white light!"
    "It burns your eyes."
    
    $unknowName = "A voice"
    unknow "[MCname], let us examine your predictament."
    unknow "You are trapped in a prison that challenges the laws of space."
    if jc_dead:
        unknow "You have slain an innocent man to satisfy your desires."
    elif janeD_dead:
        unknow "You have slain an innocent woman to satisfy your desires."
    elif jd_dead:
        unknow "You have slain an innocent couple to satisfy your desires."
    unknow "And now you face a unique punishment. You cannot leave. When the town dies, so too, shall you."
    unknow "When everyone leaves, you shall be the last one left, doomed to shrivel into a husk."
    mc "Then what should I do?"
    unknow "Find the one who binds you here, [MCname]. That is your only hope of breaking your curse..."
    
    "The voice fades."

    scene Psychic_store
    with fade

    "The ball immediately stops glowing."
    mc "{i}\"The one who binds me here?\" Who can that be...{/i}"
    show VampySprite at left with dissolve

    show Anna at right
    with dissolve

    Anna "Well, young man. Unfortunately, it seems like the crystal ball is out of energy today."
    Anna "Come back again another time. Maybe then you'll find your answer."
    "You leave the store."

    hide VampySprite
    with dissolve

    # Anna "What a tough customer. No one can be completely satisfied with their fortunes, can they?"
    jump after_meet_anna

label after_meet_anna:
    # scene Strip_Mall
    # with fade

    # show VampySprite
    # with dissolve

    # mc "Hmm. Some of her fortunes may be lies. But perhaps one can find truth in them."
    # mc "After all, some lies can be half truths."
    # mc "I will consider investigating her...even if that costs me most of my paycheck."
    $ MeetingAnna = True
    $ Night_count = 0
    jump Chapter_Three_Morning

label Chapter_Three_Morning:

    $ day += 1
    if Night_count >= 3:
        jump Start_chp4 #chapter start here
    $ Night_count += 1


    scene Farmhouse_Day
    with fade

    "New day, New choices!"

    menu:
        "Tend to the crops" if jd_dead == False:
            $ Doe += 1
            jump John_info
        "Go get supplies" if janeD_dead == False:
            $ Jane += 1
            jump time_with_jane
        "Go to the creek" if jc_dead == False:
            $ Cash += 1
            jump time_with_cash
        "Visit the fortune teller" if money >= 5 and ana_dead == False:
            jump time_with_ana

label time_with_ana:
    scene Psychic_store
    with fade

    show Anna at right
    with dissolve

    show VampySprite at left
    with dissolve

    Anna "Welcome back, traveller! What brings you here?"
    Anna "For five dollars, I will consult Madam Fate. For ten dollars, you can consult the crystal ball."

    menu:
        "Ask for a reading" if AnnaInfo == False:
            if money >= 5:
                jump card_stuff
            elif money < 5:
                Anna "Sorry hun, it appears you don't have enough money. Stop by again another time."
                $ trust -= 1
                if CurrentChap == 3:
                    jump Chapter_Three_Morning

        "Consult the crystal ball" if money >= 10:
            if money >= 10:
                jump ball_stuff
            elif money < 10:
                Anna "Sorry hun, it appears you don't have enough money. Stop by again another time."
                $ trust -= 1
                if CurrentChap == 3:
                    jump Chapter_Three_Morning

label card_stuff:
    menu:
        "Ask who wishes to harm you":
            mc "Who wishes to harm me?"
            Anna "Let me see..."
            "Anna closes her eyes and stretches her arms towards the ceiling."
            "A few seconds later, her eyes open."
            Anna "The spirits say no one wishes to harm you. They say someone wishes to understand you and for you to understand them."
            mc "That's quite vague."
            Anna "Take it or leave it. That's Madam Fate's answer. Five dollars, please."
            "You reluctantly hand her the money."
            $ money = money - 5
        "Ask why you are here":
            mc "Why am I here?"
            Anna "Let me see..."
            "Anna closes her eyes and stretches her arms towards the ceiling."
            "A few seconds later, her eyes open."
            Anna "Ah, the answer seems to be quite simple. Someone has requested your presence."
            Anna "You are bound by a contract, and you cannot leave until that contract is resolved or broken."
            mc "That is rather unhelpful, madam."
            Anna "Don't give me that attitude. That's just what Madam Fate says. Now, hand over the money."
            "You reluctantly hand her the money."
            $ money -= 5
        "Ask about her books":
            mc "Are those books yours?"
            "She looks a bit taken aback by your question, but she obliges."
            $ Annainfo = True
            Anna "Let me see..."
            "Anna closes her eyes and stretches her arms towards the ceiling."
            "A few seconds later, her eyes open."
            Anna "Madam Fate says yes. Those books are mine."
            mc "Ah, are you an avid reader, Anna?"
            Anna "You misunderstand, young man. Those are the tomes of knowledge."
            Anna "Spells to give your enemies boils for days, charms that help you find your true love -- that sort of thing."
            Anna "If you need a reference, ask Jane. They work. And if you want one, that'll be 10000 dollars."
            mc "10000 dollars? I doubt I could afford that!"
            "She nods, as if she was expecting you to refuse."
            Anna "I see we'll never come to a compromise. Very well. I won't bring up the books again."
            Anna "Give me my money at least."
            "You reluctantly hand her the money."
            $ money -= 5
    jump finish_anna_stuff

label ball_stuff:
    menu:
        "Ask who brought you here":
            scene Crystal_ball
            with fade
            mc "Who brought me here?"
            unknow "We see--"
            "Before the ball can answer, Anna snatches it away."
            scene Psychic_store
            show VampySprite at left with dissolve
            show Anna at right with dissolve
            "You thought you saw a hand on the surface on the fall for a second, but it could have been Anna's reflection."
            Anna "Ah, sorry. I forgot to mention that the crystal ball is broken today. Must be the weather."
            Anna "Perhaps you'd like a reading instead?"
            mc "It seemed to be working--"
            Anna "What about a love reading? I'm sure someone like you is looking for a companion."
            "Before you can object, she asks the question."
            Anna "Oh Madam Fate! What will this man's love-life look like?"
            "Anna closes her eyes and stretches her arms towards the ceiling."
            "A few seconds pass. She opens her eyes."
            Anna "There a promising romance lying in the future, [MCname]. Madam Fate says you and Jane would make quite a couple."
            mc "Ms. Dough? The shopkeeper? Surely, you jest?"
            Anna "That's just what destiny says. Don't shoot the messenger."
            Anna "Now go on. Madam Fate and the crystal ball need their rest."
            "She shoos you out of the store. You return to the farm."
        "Ask why you cannot leave":
            scene Crystal_ball
            with fade
            mc "Why can't I leave?"
            "Glowing writing swirls around the surface of the ball. It swirls faster and faster until it contracts into a bright, bright ring."
            "You can barely see a shadowy figure spinning around the ring."

            unknow "A contract binds you to this town. Until it's satisfied, you cannot escape."
            unknow "Whenever you leave, you shall come back. You will be stuck, confined to this area, until you die."
            unknow "Only the one who summoned you can remove your binds."
            unknow "Find out who is responsible."
            if Jane > 0:
                unknow "Perhaps it is someone you know..."
            "The light fades."
            
            scene Psychic_store
            show VampySprite at left with dissolve
            show Anna at right with dissolve
            mc "Isn't the phrase 'Keep your friends close and your enemies closer?'"
            Anna "The spirits speak in mysterious ways. Now, payment please?"
            "She holds her hand out expectingly."
            "You pay Anna her money."
            $ money -= 10
        "Ask how did you get here":
            scene Crystal_ball
            with fade
            mc "How did I get here?"
            "Glowing writing swirls around the surface of the ball. It swirls faster and faster until it contracts into a bright, bright ring."
            "You can barely see a shadowy figure spinning around the ring."

            unknow "Someone asked a question. You became the answer."
            unknow "Through supernatural means, you were pulled to this place and chained to the town."
            unknow "We see that you are confined to the farm, the mall, and the creek. We wonder why."
            unknow "We see the spell. We do not understand why you are allowed to roam."
            unknow "You could have been easily bound to one spot, stuck until your summoner comes."
            
            unknow "Someone may be trying to tell you something. But what kind of message? We do not know."
            "The light fades."
            scene Psychic_store
            with fade
            show VampySprite at left with dissolve
            show Anna at right with dissolve

            "You mutter curses under your breath."
            mc "That is not particularly helpful."
            # Anna "I'll pretend I didn't hear that."
            Anna "But better than nothing, yes? Payment, please."
            "You pay Anna her money."
            $ money -= 10
    jump finish_anna_stuff

label finish_anna_stuff:
    Anna "Thank you for the visit. May fate bring us again soon."
    if CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5
