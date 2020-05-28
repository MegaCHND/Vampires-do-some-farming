label Start_chp3:
    $ CurrentChap = 3
    $unknowName = "???"
    scene Drak_pic
    unknow "I have found you.."
    show VampySprite at left
    mc "what?!"
    hide VampySprite
    unknow "My dreams lie within you.."
    show VampySprite at left
    mc "who is't art thee??!"
    jump wake_up


label wake_up:

    scene Farmhouse_Bed
    show VampySprite

    mc "T's a dream?"
    "The rooster crows but it only amplifies [MCname]'s headache"
    mc "Fie, i shouldst wend f'r a walkethk"

    jump meet_anna


label meet_anna:

    scene Strip_Mall
    show Anna at right
    Anna "Excuse me, sir"
    show VampySprite at left
    mc "I understand you not? didst thee talk to me?"
    Anna "Do you believe destiny?"
    mc "What? who is't art thee?"
    Anna "I am a fortune teller, my name is Anna, follow me and I will show the path of your destiny."
    $AnnaName = "Anna"
    menu:
        "Nay, wend hence from me.": #trust - 1
            $ total_trust -= 1
            $ trust_for_anna -=1
            $ first_choice = 1

        "...":
            $ first_choice = 1

        "Very well? showeth me something": #trust + 2
            $ total_trust += 2
            $ trust_for_anna += 2
            $ first_choice = 0

    if first_choice == 0:
        jump in_Psychic_store
    if first_choice == 1:
        Anna "Are you afraid to face your destiny, the depths of your self?"
        menu:
            "Hmph, art thee gravely? I gonna drop of sorrow down thy lies": #trust -1
                $ total_trust -= 1
                $ trust_for_anna -= 1
                Anna "You won't"
                jump in_Psychic_store

            "Forsooth not!": #trust + 1
                $ total_trust += 1
                $ trust_for_anna += 1
                Anna "Good"
                jump in_Psychic_store

label in_Psychic_store:
    scene Psychic_store
    show Anna at right
    show VampySprite at left
    Anna "Welcome to my place, let's see what Madame Fate has in store for us. Please ask a question!"
    menu:
        "Who is't am i?":
            Anna "A being bound by fate. But if you can break free from your binds, you will be who you are"
        "Wherefore am i h're?":
            Anna "You are fate's hand, it's reason is yours"
    mc "Hmm..."
    jump ask_crystal_ball


label ask_crystal_ball:
    show VampySprite at left
    show Anna at right
    Anna "Okay, at a 10 to 1 ratio...that'll be 10 dollars, please."
    mc "Wait, what? yond's all thee did get? thee wanteth me payeth ten dollats f'r just bullshit?"
    Anna "Yes...oh, fine, since you're kind of cute,you can look at the crystal ball, it will tell you your destiny...I guess"
    mc "Fine."
    hide VampySprite
    hide Anna
    "[MCname] glares at crystal ball. Will it crack under pressure? No, such supernatural powers don't work yet."
    show VampySprite at left
    mc "Well enow, t's time to leaveth, i wanteth not to playeth a fartuous game with such swindler"
    show Anna at right
    Anna "No...just wait for 2 more... 5 more minutes. The ball's going to do something I swear!"

    scene Crystal_ball
    "Suddenly Anna disappears as the ball realy does something. Though, it's not cracking, it's glowing!"
    $unknowName = "A Voice"
    unknow "\nQuite brightly at that."
    unknow  "\nAh, ahem, [MCname] must destroy those cloaked in chaos or..."
    scene Psychic_store
    "The ball stopped glowing...how unreliable..."

    show Anna at right
    Anna "*fake cough fake cough* Unfortunately, I out of power today but the crystal ball will work for next time, I guarantee you!"
    show VampySprite at left
    mc "Wait, what? thee cullionly the crystal ball doesn't worketh?! but i heareth some..."
    Anna "I'm sorry! Please dont be mad. Here how about this one be on the house since its you're first time?"
    mc "Er.."
    Anna "Thanks for the visit, and I'll see you next time!"
    hide VampySprite
    Anna "Scary, he glared at the ball for like another 10 minutes..."
    jump after_meet_anna

label after_meet_anna:
    scene Strip_Mall
    show VampySprite
    mc "Hmm... Yond sound seemeth has't some connection with the present day's dream"
    mc "I needeth to figure t out."
    $ Night_count = 0
    jump Chapter_Three_Morning

label Chapter_Three_Morning:

    if Night_count >= 3:
        jump Start_chp4 #chapter start here
    $ Night_count += 1


    scene Farmhouse_Day
    "New day, New choices!"

    if jd_dead == True:
        menu:
            "Go get supplies?":
                jump time_with_jane
            "Go to the creek?":
                jump time_with_cash
            "Go to Psychic store?":
                jump time_with_ana

    if janeD_dead == True:
        menu:
            "Tend to the crops?":
                jump John_info
            "Go to the creek?":
                jump time_with_cash
            "Go to Psychic store?":
                jump time_with_ana

    if jc_dead == True:
        menu:
            "Tend to the crops?":
                jump John_info
            "Go get supplies?":
                jump time_with_jane
            "Go to Psychic store?":
                jump time_with_ana

label time_with_ana:
    scene Psychic_store
    show Anna at right
    show VampySprite at left
    Anna "Welcome back! What brings you here?"
    menu:
        "Thy power, yond's wherefore i am cometh back hither":
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust +1

        "I just feeleth bored and tryeth to maketh some excit'ment hither":
            $ total_trust -= 1
            $ trust_for_anna -= 1
            #trust -1

    Anna "Ok, let's see what Madame Fate has in store for us, what exactly do you want to do?"
    menu:
        "Ask Anna some questions":
            $ choice_with_ana  = 1
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust + 1

        "Consult the crystal ball":
            $ choice_with_ana = 2

    if choice_with_ana == 1:
        menu:
            "Who is't wishes to harmeth me?":
                Anna "Those you've sinned against surely curse you"
            "wh're am i from?":
                Anna "Is that important? Or shouldn't you focus on where you will be?"
    if choice_with_ana == 2:
        #for here the message will change when the trust of anna increase more
        if trust_for_anna >= 4:
            scene Crystal_ball
            unknow "\nAh make sure to feed [MCname] every now and again"
        if trust_for_anna >= 3:
            scene Crystal_ball
            unknow "\nThat's the entire ominous message for [MCname]"
        elif trust_for_anna >= 2:
            scene Crystal_ball
            unknow "\nOh hello. [MCname] is back. Oh yes!"
            unknow  "\n...Or rid them of their cloak."
        scene Psychic_store
    show VampySprite at left
    mc "Thanketh thee f'r the answ'rs. Farewell"
    show Anna at right
    Anna "Thanks for the visit, see you again next time!"
    if CurrentChap == 3:
        jump Chapter_Three_Morning
