#Jared Clark
label Start_chp4:
    $ jc_info = 0
    $ CurrentChap = 4
    $ bonfire_invite = False
    scene Farmhouse_Day
    "The rooster crows but [MCname] is too exhaugsted to here it.
    \nHard work in the sun makes one really thirsty."
    if jd_dead == True:
        jump Meeting_the_Banker
    show JD at right
    show JDW at left
    jd "[MCname], Jannet and I will be goin to town to get some food for dinner. Tend the crops while we're gone."
    hide JD
    hide JDW
    jump Meeting_the_Banker2
    
label Meeting_the_Banker:
    "Just after a light lunch, there is a knocking at the door"
    show Franklin at left
    newCharacter "Oh I have never seen you here before. Who are you?"
    mc "I am a distant relative. Sir and Madam Doe wenteth to seeth the w'rld and those folk hath asked me to cometh holp those folk on the farm until those folk receiveth backeth"
    mc "Who is't art thee?"

    Franklin "Then nice to meet you, my name is Franklin. I am here to collect your monthly bill on the farm. It was due last week so I came to collect on behalf of the Bank."

    mc "Well I shall alloweth those folk knoweth at which hour those folk waketh up since those folk art traveling at the moment"

    Franklin "I can push the payments on the farm back another day but they have to eventually pay up or the farm will be repossessed like the rest."

    mc "I shall passeth the message 'long. Wh're can I taketh the payment at which hour t is eft?"

    Franklin "Bring it to the Bank next to the mall."

    scene Farmhouse_Night
    show VampySprite
    mc "I bethink I did see wh're those gents hath kept all their wage. Th're shouldst beest enow to payeth in th're"

    scene Farmhouse_Day
    show VampySprite

    mc "Timeth to taketh the wage to the bank"
    jump Going_to_the_Bank


label Meeting_the_Banker2:
    "Just after a light lunch, there is a knocking at the door"
    
    show Franklin at left
    
    newCharacter "Oh I have never seen you here before. Who are you?"
    
    mc "I am a cousin of Sir Doe.  Those folk art out buying food even but now"
    
    mc "Who is't art thee?"
    
    Franklin "Then nice to meet you, my name is Franklin. I am here to collect your monthly bill on the farm. It was due last week so I came to collect on behalf of the Bank."
    
    mc "I shall alloweth those folk knoweth at which hour those gents receiveth backeth from the marketeth"
    
    Franklin "I can push the payments on the farm back another day but they have to eventually pay up or the farm will be repossessed like the rest."

    mc "I shall passeth the message 'long. Wh're can I taketh the payment at which hour t is eft?"

    Franklin "Bring it to the Bank next to the mall."

    scene Farmhouse_Night
    
    show JD_Sleepy at right
    show VampySprite at left

    mc "Franklin from the bank cameth by the present day"
    jd "Well, what did he come for?"
    mc "That gent hath said to bringeth the bill payment to the bank tom'rrow because that gent can't waiteth any longeth'r"
    jd "Alright, I'll get it together in the morning and send you up there."

    scene Farmhouse_Day
    show VampySprite

    mc "Timeth to taketh the wage to the bank"
    jump Going_to_the_Bank

label Going_to_the_Bank:
    scene Bank_Lobby
    show Franklin
    with dissolve

    Franklin "Hey! Nice to see you again. Do you have the payment?"
    mc "Aye h're t is"
    Franklin "Thank you have a great day."
    jump Lets_eat

label Lets_eat:
    scene Ranch_Sunset
    "The sun sets on another hard day's work. However, as night approaches so do the hands of fate."
    scene Black_Wall
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
    $ crops_tended_chp4 = 0
    scene Farmhouse_Day
    show VampySprite
    "It's true, things are always a little easier after the first time."
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
        "It aint much, but it's honest work"
    else:
        jump John_info

label CHP4_Supplies:
#meet jane say im ready to meet your friends go to bonfire later tonight
    with Dissolve(0.3)
    scene Clothing_Store
    show VampySprite at left
    show JaneD at right
    janed "Oh hi there! What can I help you with?"
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
            janed "Although not a lot of people get as much as John does tho."

        janed "Well [MCname], what can I do ya for?"
        "Dost thou have more companions?":
            janed "Oh of course! we are having a Bonfire tonight near the woods. You should come by later."
            $ bonfire_invite = True # can now go to the bonfire event at night. used in chapter 5
            mc "I shall beest sure to stand ho by. I shall beest leaving anon."
    jump CHP4_morning

label CHP4_Creek:
    with Dissolve(0.5)
    scene Creek_Bridge
    show VampySprite at left
    show JC at right
    jc "What's up man, *cough cough* I havent seen you in a while."
    mc "Greetings [jc]."
    default menuset3 = set()
    menu:
        set menuset3
        jc "Somethin' on your mind since you're here again? *cough*"
        "How did you end up here in North Dakota.":
            jc "Awww man, that's an old story"
            jc "I used to live an Cali *cough*. Got into troble with folks I shouldn't have."
            jc "They ruffed me up and tossed me out here."
            jc "*cough* *cough* No good at farmin, No way home, so I jut bum out here."

        "Why do I never see you in the town.":
            jc "I used to go in but I don't like them, and they don't like me"
            jc "It ain't bad though. I fish all day for food and can make my own stuff to smoke.
            jc "I got everything I need out here. The great outdoors."
            jc "You should try it one day."
    jc "Looks like it's getting pretty late."
    mc "I concur. I shalt depart anon"
    jc "Yeeah take care."
    with Dissolve(0.5)
    scene Farmhouse_Bed
    show VampySprite at left
    mc "I learn'd alot from that gent the present day. I bethink i am getting clos'r to the sooth."
    jump CHP4_morning

label CHP4_Psychic:
    scene Psychic_store
    show Anna at right
    show VampySprite at left
    Anna "HI, [MCname], welcome back, what brings you back here?"
    menu:
        "Thy power, yond's wherefore i am cometh back hither":
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust +1

        "I just feeleth boring and tryeth to maketh some excit'ment hither":
            $ total_trust -= 1
            $ trust_for_anna -= 1
            #trust -1

    Anna "Really? Well, let's see what Madame Fate has in store for us. Please ask a question!"
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
            "Who is't is Johnny?":
                Anna "A poor excuse for a human being."

            "Who is't is cloak'd in chaos?":
                Anna "Everyone is cloaked in a little bit of chaos. Don't you agree?"

    if choice_with_ana == 2:
        scene Crystal_ball
        if trust_for_anna >= 5:
            unknow "\nYou probably already know this but..."
            unknow "\nNot everyone can be trusted."
        elif trust_for_anna >= 4:
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
    mc "Yond wast m're helpful than lasteth timeth. \nI wilt figure this out with haste"
    show Anna at right
    Anna "Thanks for visiting again please come again!"
    hide VampySprite
    show Anna at center
    Anna "Does the ball really work? Sometimes, he just stares at it for 10 mintes, thanks me and leaves..."
    Anna "Ah. I really should start charging him for that."
    jump CHP4_morning

label Time_with_frank:
    scene Bank_Lobby
    show Franklin at right
    default menuset4 = set()
    menu:
        set menuset4
        Franklin "Nice to see you again Sir, what would you like to talk about?"

        "Ask about the town.":
            jump the_town
        "Ask about other people's bills.":
            jump collecting_bills
        "Ask about his job at the bank.":
            jump bank_job
    mc "Well thanketh thee f'r thy timeth. I did enjoy our conv'rsation."
    jump CHP4_morning


label the_town:
    Franklin "The town is usually pretty quiet. I thry my best to keep it that way."
    mc "What doth thee cullionly people liketh me?"
    Franklin "Don't worry about that. It's none of your business."
    jump Time_with_frank



label collecting_bills:
    mc "Art most people usually this late on their bills h're?"
    Franklin "Not usuallly, but when they are I have to step in. THe Bank needs it's money."
    mc "Wherefore showeth up at people's homes?"
    Franklin "I know I look like the villian but it's for the greater good. This town needs the Bank"
    jump Time_with_frank


label bank_job:
    mc "Is thy job just to collecteth the bills f'r the bank?"
    Franklin "Yes, it would be easier if people just showed up here, but I do not mind going to them."

    menu:
        Franklin "Did I scare you with my sudden arrival the other day?"
        "Aye, i wast not expecting anyone on the prop'rty":
            Franklin "Hah hah! Don't worry, if you're on time, I'm no threat to you"


        "Nay, t wast just nice meeting a new visage.:
            Franklin "Ah. Well, thank you. It was nice meeting you too."
    Franklin "I will be around again soon. Just take care of the farm."
    jump Time_with_frank

label CHP4_end:
    scene Drak_pic
    unknow "Four are needed. How many have been collected?"

    jump Start_chp5 #first label of chapter 5
