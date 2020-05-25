#Vincent Cheng
label Start_chp5:
    $ CurrentChapter = 5
    $ craterInfo = False
    scene Farmhouse_Day
    "After feeding the other day, you wake up refreshed and ready to go."
    if jd_dead == False:
        show VampySprite at left
        show JD at right
        jd "Morning [MCname]! Any plans today?"
        menu:
            "Nay" if bonfire_invite == False: #No
                jd "Well, I don't have anything for you to do today. You can just wander around town."
                jump meetSteve
            "Seeth the crat'r in the woods i hath appeared in": #See the crater in the woods I appeared in
                jd "That sounds like a good plan."
                jump crater
            "Seeth the Psychic" if ana_dead == False: #See the Psychic
                jd "You actually believe in that mumbo jumbo. Well, maybe she might be able to help you."
                jump meetAnna
            "Jane did invite me to a bonfire tonight" if bonfire_invite == True: #Jane invited me to a bonfire tonight
                jd "Already getting to know the townsfolk, huh? Good for you."
                jump bonfire
    else:
        jd "what shalt i doth the present day?" #What shall i do today?
        menu:
            "Wand'r 'round town" if bonfire_invite == False: #Wander around town
                jump meetSteve
            "Seeth the crat'r in the woods i hath appeared in": #See the crater in the woods I appeared in
                jd "That sounds like a good plan."
                jump crater
            "Seekth the Psychic" if ana_dead == False: #See the Psychic
                jump meetAnna
            "Receiveth eft f'r bonefire" if bonfire_invite == True: #Get ready for the bonfire
                jump bonfire

label meetSteve:
    with Dissolve(0.5)
    scene Strip_Mall
    "You are walking down the main street and you hear someone calling you from far away."
    show VampySprite at left
    Steve "Hey, can you stop for a moment? I got to ask you a few questions."
    show Steve at right
    mc "Who is't art thee?" #Who are you?
    Steve "The name's Steve. I am the cop in this area. You new here right? And you are staying with the Doe's?"
    mc "Aye." #Yes
    if jd_dead == True:
        Steve "Have you seen the Doe's these last couple of days?"
        menu:
            "Tell the Truth":
                mc "I hath killed those folk." #I killed them.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I am a relative of John's.  John and Jannet has't gone to traveleth 'round the w'rld" #I am a relative of John's. John and Jannet have gone to travel around the world.
    if janeD_dead == True:
        Steve "Have you seen the clerk at the clothing store? Her name was Jane Dough."
        menu:
            "Tell the Truth":
                mc "I hath killed h'r." #I killed her.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen misseth dough." #I have not seen Miss Dough
    if jc_dead == True:
        Steve "Have you seen [JCname]? He usually hangs around the creek?"
        menu:
            "Tell the Truth":
                mc "I hath killed that gent." #I killed him.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen Mr. Cash." #I have not seen Mr. Cash
    if ana_dead == True:
        Steve "Have you seen [AnnaName]. She's the local Psychic."
        menu:
            "Tell the Truth":
                mc "I hath killed h'r." #I killed her.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen Anna 'round." #I have not seen Anna around.

    Steve "When did you get here?"
    mc "I arriv'd a couple days ago." #I arrived a couple days ago.
    Steve "How did you get here?"
    mc "I am not sure. I doth not rememb'r aught. " #I am not sure. I don't remember anything.
    Steve "Well that's weird. You don't remember anything. So what are you gonna do now?"
    mc "I shall gath'r inf'rmation and figure out how I did get h're." #I will gather information and figure out how I got here.
    Steve "Well I'll see if I can find out more information for you. Also, don't leave town!"

    mc "Well, what shouldst i doth anon?" #Well, what should I do now?
    menu:
        "Check Crater":
            jump crater
        "See Anna" if ana_dead == False:
            jump meetAnna
        "Head Home":
            jump chp5_end

label Arrest:
    with Dissolve(0.5)
    scene Jail
    "You are soon arrested and taken back to the Police Station."
    "While in jail, you break through the wall and escape."
    "Now wanted, you have to now travel across the country without knowing anything about your past"
    "The End"
    jump end

label crater:
    with Dissolve(0.5)
    scene Woods_Sunset
    "You walk through the woods to the crater that you landed at."
    show VampySprite
    mc "wh're shouldst i checketh?" #Where should i check?
    menu:
        "Bushes":
            mc "What is this?"
            "You find a piece of paper that says..."
            "Priority Mission: Creature Extermination"
            $ crater_info = True
        "Crater":
            mc "Th're's nothing h're.  This wast a wasteth of timeth." #There's nothing here. This was a waste of time.
    mc "Timeth to headeth backeth"
    if bonfire_invite == True:
        mc "What doth I doth anon?" #What do I do now?
        menu:
            "Wend to the bonfire": #Go to the bonfire
                jump bonfire
            "Timeth to wend home": #Time to go home
                jump chp5_end
    jump chp5_end

label meetAnna:
    with Dissolve(0.5)
    scene Psychic_store
    show Anna at right
    show VampySprite at left
    Anna "Welcome Back, dear customer. Oh it's you again, [MCname]. What can I do for you today?"
    menu:
        "Thy pow'rs art wond'rful.  Can thee holp me?": #Your powers are wonderful. Can you help me?
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust +1

        "I hadst nay plans the present day so i cameth h're": #I had no plans today so I came here
            $ total_trust -= 1
            $ trust_for_anna -= 1
            #trust -1
    Anna "Of Course! What would you like me to help you with?"
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
        hide Anna
        hide VampySprite
        scene Crystal_ball
        $unknowName = "*The sound in your mind*"
        unknow "\n
                Thy journey is almost at an endeth." #Your journey is almost at an end.
        unknow  "\n
                Followeth thy instincts." #Follow your instincts
        scene Psychic_store
    show VampySprite at left
    show Anna at right
    mc "Once again, thee has't been a most wondrous holp." #Once again, you have been a great help
    Anna "Of course. Please come again."
    hide Anna
    hide VampySprite
    scene Strip_Mall
    show VampySprite
    if bonfire_invite == True:
        mc "Lets wend to the bonfire" #Lets go to the bonfire.
    else:
        mc "Lets head home"
        jump chp5_end

label bonfire:
    with Dissolve(0.5)
    scene bonfire
    show VampySprite at left
    show JaneD at right
    janed "Hi [MCname], I'm glad you could make it."
    mc "Thanketh thee f'r inviting me" #Thank you for inviting me
    janed "How have you been? Are you fitting in ok?"
    mc "I am still trying to figure out wh're i cameth from.  Who is't is this?" #I am still trying to figure out where I came from. Who is this?
    janed "Aw that sucks. Oh, this is my friend, Steve. He is the local cop in our town."
    hide JaneD
    show Steve at right
    Steve "Hi, the name's Steve. You new here right? And you are staying with the Doe's?"
    mc "Aye." #Yes
    Steve "Do you mind stepping aside so I can ask you a couple questions?"
    mc "Sure."
    if jd_dead == True:
        Steve "Have you seen the Doe's these last couple of days?"
        menu:
            "Tell the Truth":
                mc "I hath killed those folk." #I killed them.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I am a relative of John's.  John and Jannet has't gone to traveleth 'round the w'rld" #I am a relative of John's. John and Jannet have gone to travel around the world.
    if janeD_dead == True:
        Steve "Have you seen the clerk at the clothing store? Her name was Jane Dough."
        menu:
            "Tell the Truth":
                mc "I hath killed h'r." #I killed her.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen misseth dough." #I have not seen Miss Dough
    if jc_dead == True:
        Steve "Have you seen [JCname]? He usually hangs around the creek?"
        menu:
            "Tell the Truth":
                mc "I hath killed that gent." #I killed him.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen Mr. Cash." #I have not seen Mr. Cash
    if ana_dead == True:
        Steve "Have you seen [AnnaName]. She's the local Psychic."
        menu:
            "Tell the Truth":
                mc "I hath killed h'r." #I killed her.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen Anna 'round." #I have not seen Anna around.

    Steve "When did you get here?"
    mc "I arriv'd a couple days ago." #I arrived a couple days ago.
    Steve "How did you get here?"
    mc "I am not sure. I doth not rememb'r aught. " #I am not sure. I don't remember anything.
    Steve "Well that's weird. I remember someone having the same situation as you, but I can't remember who it was."
    mc "tis fine.  I can figure it out on mine own owneth." #It's fine. I can figure it out on my own.
    hide Steve
    show JaneD at right
    janed "Come on guys. Stop talking about boring stuff and lets have some fun."
    hide JaneD

    "You hang out with them for a couple more hours until its time to head home."
    show VampySprite at center
    mc "Tis timeth to wend home" #its time to go home
    jump chp5_end

label chp5_end:
    with Dissolve(0.5)
    scene Drak_pic

    unknow "the endeth is nigh"
    jump chp5_end
