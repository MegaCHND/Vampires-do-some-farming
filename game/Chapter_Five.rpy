####################################################
#   PART 5
#   Primary Author: Vincent Cheng
#   Secondary Authors: Chris Goebel, Nichole Wong
####################################################
label Start_chp5:
    $ CurrentChapter = 5
    $ craterInfo = True
    $ chp5crops = 0
    $ day += 1

    scene Farmhouse_Day
    with fade

    "COCK-A-DOODLE-DOO!"
    if jd_dead == False:
        if JohnGreetCh5 == False:
            $ JohnGreetCh5 = True
            show VampySprite at left
            with dissolve

            show JD at right
            with dissolve

            jd "Mornin' [MCname]! Any plans today?"
        else:
            mc "What shall I do today?"

        menu:
            "Tend to the crops" if c51 == False:
                $ c51 = True
                $ Doe += 1
                mc "I planned to work the fields today, Mr. John."
                jd "That so? Thought ya be tired of the work by now."
                jd "Let's go then."
                "You follow John to the fields."
                jump CHP5_crops
            "Walk around town": #Wander around town
                mc "I think I shall go on a walk."
                jd "Alright. Have fun."
                hide JD
                hide VampySprite
                scene Black_Wall
                "You walk around the edges of your cage."
                "When will you be able to get out of this damn place?"
                jump chp5_end
            "Visit the fortune teller" if ana_dead == False and money >= 5 and c52 == False: #See the Psychic
                $ c52 = True
                mc "I planned to visit Ms. Anna, the fortune-teller."
                jd "Ya actually believe in that mumbo jumbo she spews? That girl's a hack. Her grandma was pretty good, but she ain't. She just says whatever her customers want to hear."
                mc "Sometimes truth hides among lies, Mr. Doe."
                jump time_with_ana
            "Attend a party" if bonfire_invite == True: #Jane invited me to a bonfire tonight
                mc "Jane invited me to a bonfire. I think I may join her."
                jd "Oh, got a date, huh? Good for ya."
                mc "We're not dating, Mr. Doe."
                jd "Ya haven't known Jane as long as I have, [MCname]."
                jd "Usually Jane uses parties as an excuse to hook up with strangers."
                jd "So if she's already invitin' ya to a party, she must fancy ya a bit."
                mc "While fascinating, Mr. Doe, I'm afraid you're mistaken."
                mc "I'm certain all Jane wants is someone to chat with at the party."
                jd "So ya say. Well, have fun!"
                jump bonfire
    else:
        mc "What shall I do today?" #What shall i do today?
        menu:
            "Tend to the crops" if c51 == False:
                $ c51 = True
                $ chp5crops = 1
                jump CHP5_crops
            "Visit the fortune teller" if ana_dead == False and money >= 5 and c52 == False: #See the Psychic
                $ c52 = True
                "You decide to visit the fortune teller."
                jump time_with_ana
            "Walk around town": #Wander around town
                "You walk around the edges of your cage."
                "When will you be able to get out of this damn place?"
                jump chp5_end
            "Prepare for the party" if bonfire_invite == True: #Get ready for the bonfire
                "You smooth out the wrinkles in your shirt and check your teeth in the mirror."
                "Then you go meet Jane at her shop."
                jump bonfire

label CHP5_crops_thing:        
    menu:
        "Tend to the crops":
            $ chp5crops = 1
            jump CHP5_crops
        "Visit the fortune teller" if ana_dead == False and money >= 5: #See the Psychic
            "You decide to visit the fortune teller."
            jump time_with_ana
        "Walk around town": #Wander around town
            "You walk around the edges of your cage."
            "When will you be able to get out of this damn place?"
            jump chp5_end
        "Prepare for the party" if bonfire_invite == True: #Get ready for the bonfire
            "You smooth out the wrinkles in your shirt and check your teeth in the mirror."
            "Then you go meet Jane at her shop."
            jump bonfire

label CHP5_crops:
    $ day += 1
    if jd_dead:
        "The harvest is rather small, but at least the crops can be sold for profit."
        $ money = money + 5
        if chp5crops == 1:
            jump CHP5_crops_thing
        elif chp5crops == 2:
            jump CHP5_crops_thing_two
    else:
        jump John_info
    
label CHP5_crops_thing_two:
    $ day += 1
    menu: 
        "Tend to the crops":
            $ chp5crops = 2
            jump CHP5_crops
        "Visit the fortune teller" if ana_dead == False and money >= 5:
            jump time_with_ana
        "Return home":
            "You head back to the farm to retire."
            jump chp5_end

label meetAnna:
    jump time_with_ana
    
    scene Strip_Mall
    with fade

    show VampySprite
    with dissolve

    if bonfire_invite == True:
        mc "Ah, the bonfire party starts soon, doesn't it?"
        mc "I better hurry."
        "You rush off to the bonfire party."
    else:
        "You return to the farm."
        jump chp5_end

label bonfire:
    scene Clothing_Store
    with fade

    "You meet up with Jane inside her shop. She gives you a smile."
    
    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve
    
    janed "You made it! Woo!"
    
    mc "Apologies for arriving early--"

    janed "Don't worry about that. I'll clock out early. Nobody is likely to come anyways."
    
    janed "Let me just grab my books and then we can go!"
    
    "She grabs a few books from behind the counter and packs them into her bag. Then she grabs your arm and drags you out to her car."
    
    scene bonfire with fade 
        
    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve
    
    "A few people are already sitting around the bonfire when you and Jane arrive. You don't recognize them. Their faces are a blur."
    
    "Someone passes around bottles of beer. As the sun sets, one of the partygoers lights the bonfire with a flamethrower. There are cheers."
    
    "Jane clings next to you and asks you questions about your hopes, your dreams, your hobbies, your love life. You respond vaguely."
    
    scene Farmhouse_Night

    "When the party is over, she drives you and two particularly drunk guests back to town, dropping you off at the Does."
   
    "She gives you another inscrutable look before driving off into the night."
    
    "You decide to retire for the night."
   
    jump chp5_end

label chp5_end:
    scene Drak_pic
    with fade

    if janeD_dead == False:
        unknow "Tomorrow, my dreams come true."
        mc "What is this talk of \"my dreams\"? Reveal yourself!"
        unknow "All will be revealed in due time, [MCname]. Listen carefully..."
        mc "I refuse to listen to voices that lead me to my doom."
        unknow "Not me, silly! Your heart."
        
    if janeD_dead == True:
        unknow "Tomorrow, you shall find the truth."
        mc "What is this talk of the truth? Reveal yourself!"
        unknow "All will be revealed in due time, [MCname]."
        unknow "Observe. Listen. Think. Sometimes, the truth hides somewhere close by."
        
    jump Start_chp6
