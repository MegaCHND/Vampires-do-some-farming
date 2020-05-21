#Jared Clark
label Start_chp4:
    $ jc_info = 0
    $ CurrentChap = 4
    scene Farmhouse_Day
    "You wake up feeling tired from the prior days work.
    \nYou will need to feed again soon."
    if jd_dead == True:
        jump Meeting_the_Banker
    show JD at right
    show JDW at left
    jd "[MCname], Jannet and I will be going into town to get some groceries for dinner. Tend the crops while were gone."
    hide JD
    hide JDW

label Meeting_the_Banker:
    "*KNOCK KNOCK KNOCK*"
    show Franklin at left
    newCharacter "Oh I have never seen you here before. Who are you?"
    mc "I am a distant relative. Those gents wenteth to seeth the w'rld and those gents hath asked me to cometh holp those folk on the farm until those gents receiveth backeth"
    mc "Who is't art thee?"

    Franklin "Nice to meet you [MCname], my name is Franklin. I am here to collect your monthly bill on the farm. It was due last week so I came to collect on behalf of the Bank."

    if jd_dead == True:
        mc "Well I shall alloweth those folk knoweth at which hour those gents waketh up since those gents art resting at the moment"
    else:
        mc "I shall alloweth those folk knoweth at which hour those gents receiveth backeth from the marketeth"

    Franklin "I can push the payments on the farm back another day but they have to eventually pay up or the farm will be repossessed."

    mc "I shall passeth the message 'long. Wh're can I taketh the payment at which hour t is eft?"

    Franklin "Bring it to the bank next to the mall."

    scene Farmhouse_Night
    if jd_dead == True:
        show VampySprite
        mc "I bethink I did see wh're those gents hath kept all their wage. Th're shouldst beest enow to payeth in th're"
    else:
        show JD_Sleepy at right
        show VampySprite at left

        mc "Franklin from the bank cameth by the present day"
        jd "Well, what did he come for?"
        mc "That gent hath said to bringeth the bill payment to the bank tom'rrow because that gent can't waiteth any longeth'r"
        jd "Alright, I'll get it together in the morning and send you up there."

    scene Farmhouse_Bed
    show VampySprite

    mc "Timeth to taketh the wage to the bank"
    jump Going_to_the_Bank

label Going_to_the_Bank:
    scene Bank_Lobby
    show Franklin
    with dissolve

    Franklin "Hey [MCname], nice to see you again. Do you have the payment?"
    mc "Aye h're t is"
    Franklin "Thank you have a great day."
    jump Lets_eat

label Lets_eat:
    scene Ranch_Sunset
    "You tend to to crops for the rest of day"
    scene Black_Wall
    menu:
        mc "I am getting fill'd with pangs of hunger. \nit hast been a longeth timeth since I lasteth did feed"
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
    $ crops_tended_chp4 = 0
    scene Farmhouse_Day
    show VampySprite
    mc "Anon yond I'm full, lets wend gath'r some m're inf'rmation"
    hide VampySprite
    default menuset1 = set()
    menu:
        set menuset1
        "Tend to the crops" if crops_tended_chp4 == 0:
            $ crops_tended_chp4 = 1
            jump CHP4_crops
        "Go get supplies" if janeD_dead == False:
            jump CHP4_Supplies
        "Go to the creek" if jc_dead == False and jc_info == 0:
            $ jc_info = 1
            jump CHP4_Creek
        "Go to the Psychic Store" if ana_dead == False:
            jump CHP4_Psychic
        "Go to the Bank":
            jump Time_with_frank
    jump CHP4_end

label CHP4_crops:
    if jd_dead:
        "You tend to the crops as John used to do it."
    else:
        jump John_info

label CHP4_Supplies:
#meet jane say im ready to meet your friends go to bonfire later tonight
    with Dissolve(0.3)
    scene Clothing_Store
    show VampySprite at left
    show JaneD at right
    janed "Oh hi there! You're John's new worker aren't you? What can I help you with?"
    mc "I am h're to seeth thee madam Jane."
    if Jane != 3:
        $ Jane = 3
        janed "Oh that's sweet of you hun. I still haven't gotten your name. What was it?"
        mc "Mine own nameth is [MCname].  Prithee useth t well."
        janed "Such a lovely name!"
    default menuset2 = set()
    menu:
        set menuset2
        "Thou has an excellent assortment of wares. Is business well?":
            janed "Hmmm I would say so. I get a decent amount of customers willing to buy my products."
            janed "People like John come by pretty often to get what they need."
            janed "Although not a lot of people get as much as John does tho. *chuckles*"

        janed "Well [MCname], what can I do ya for?"
        "Dost thou have more companions?":
            janed "Oh of course! we are having a Bonfire tonight near the woods. You should come by later. *chuckles*"
            $ bonfire_invite = True # can now go to the bonfire event at night. used in chapter 5
            mc "I shall beest sure to stand ho by. I shall beest leaving anon."
    jump CHP4_morning

label CHP4_Creek:
    with Dissolve(0.5)
    scene Creek_Bridge
    show VampySprite at left
    show JC at right
    jc "What's up [MCname], *cough cough* I havent seen you in a while."
    mc "Greetings [jc]."
    default menuset3 = set()
    menu:
        set menuset3
        jc "Somethin' on your mind since you're here again? *cough*"
        "How did you end up here in North Dakota.":
            jc "I am not from here originally. I woke up randomly out here one day."
            jc "I asked the people on that farm for help but they ran me off"
            jc "I have stayed out here ever since."
            jc "It feels like to much work to find my way home so im just gonna stay here."

        "Why do I never see you in the town.":
            jc "I used to go in but I fish all day for food and can make my own stuff to smoke."
            jc "I got everything I need out here. The great outdoors."
            jc "You should try it one day."
    jc "Looks like it's getting pretty late."
    mc "I concur. I shalt depart anon"
    jc "Yep take care [MCname]."
    with Dissolve(0.5)
    scene Farmhouse_Bed
    show VampySprite at left
    mc "I did enjoy Johnny's company the present day"
    mc "I learn'd alot from that gent the present day. I bethink i am getting clos'r to the sooth."
    jump CHP4_monrning

label CHP4_Psychic:
    scene Psychic_store
    show Anna at right
    show VampySprite at left
    Anna "Hey, [MCname], welcome back, what brings you back here?"
    menu:
        "Thy power, yond's wherefore i am cometh back hither":
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust +1

        "I just feeleth boring and tryeth to maketh some excit'ment hither":
            $ total_trust -= 1
            $ trust_for_anna -= 1
            #trust -1

    Anna "Fine, let's see what Madame Fate has in store for us, what?"
    menu:
        "Ask some question for you":
            $ choice_with_ana  = 1
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust + 1

        "Get something on the crystal ball":
            $ choice_with_ana = 2
    if choice_with_ana == 1:
        menu:
            "Who is't am i?":
                Anna "You are on the path to discovering yourself, Once the time is up, you will know that for sure"
                $ the_last_choice = 1
            "Wherefore i am hither?":
                Anna "Something led you here, that is your destiny"
                $ the_last_choice = 2
        if the_last_choice == 1:
            menu:
                "Wherefore i am hither?":
                    Anna "Something led you here, that is your destiny"
        if the_last_choice == 2:
            menu:
                "Who is't am i?":
                    Anna "You are on the path to discovering yourself, Once the time is up, you will know that for sure"
    if choice_with_ana == 2:
        scene Crystal_ball
        $unknowName = "*The sound in your mind*"
        unknow "\n
                You will soon play your role in my grand scheme."
        unknow  "\n
                You will return home eventually."
        unknow "\n
                Not everyone you think can be trusted."
        scene Psychic_store
    show VampySprite at left
    mc "Yond wast m're helpful than lasteth timeth. \n
        I wilt figure this out with haste"
    show Anna at right
    Anna "Thanks for visiting again please come again!"
    hide VampySprite
    show Anna at center
    Anna "I really should start charging him for these."
    jump CHP4_morning

label Time_with_frank:
    scene Bank_Lobby
    show Franklin at right
    default menuset4 = set()
    menu:
        set menuset4
        Franklin "Nice to see you again [MCname], what would you like to talk about?"

        "Ask about the town.":
            jump the_town
        "Ask about other people's bills.":
            jump collecting_bills
        "Ask about his job at the bank.":
            jump bank_job
    mc "Well thanketh thee f'r thy timeth. I did enjoy our conv'rsation."
    jump CHP4_morning


label the_town:
    Franklin "The town is usually pretty quiet. People like you show up pretty regularly, but I deal with them pretty quickly."
    mc "What doth thee cullionly people liketh me?"
    Franklin "Don't worry about that. Youll be gone soon enough."
    jump Time_with_frank



label collecting_bills:
    mc "Art most people usually this late on their bills h're?"
    Franklin "Not usuallly, but when they are I have to step in. I need my money."
    mc "Wherefore showeth up at people's homes?"
    Franklin "They need to know I am serious about the money they owe me."
    jump Time_with_frank


label bank_job:
    mc "Is thy job just to collecteth the bills f'r the bank?"
    Franklin "Yes, it would be easier if people just showed up here, but I do not mind going to them."

    menu:
        Franklin "Did I scare you with my sudden arrival the other day?"
        "Yes, I was not expecting anyone on the property.":
            Franklin "Do not worry I am no threat to you."


        "No, it was just nice meeting a new face.":
            Franklin "Well it was nice meeting you too."
    Franklin "I will be around again soon. Just take care of the farm."
    jump Time_with_frank

label CHP4_end:
    scene Drak_pic
    unknow "The plan is coming together nicely now."

    jump Start_chp5 #first label of chapter 5
