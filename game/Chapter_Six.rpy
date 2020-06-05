####################################################
#   PART 6
#   Primary Author: Chris Goebel
#   Secondary Authors: Chris Goebel, Nichole Wong
####################################################
label Start_chp6:
    $ CurrentChap = 6
    $ visitChoice = 0
    $ answerJane = ""
    $ day += 1
    scene Farmhouse_Bed
    with fade

    show VampySprite at center
    with dissolve

    "COCK-A-DOODLE-DOO!"

    mc "What an odd dream."
    if janeD_dead == False:
        mc "All will be revealed in due time? Listen to your heart?"
    else:
        mc "All will be revealed in due time? Sometimes, the truth hides somewhere close by?"
        
    mc "Whatever can this mean?"

    if janeD_dead == True:
        if jd_dead == False:
            jump JD_Intro_Ending
        elif ana_dead == False:
            jump Anna_Intro_Ending
        elif jc_dead == False:
            jump Johnny_Intro_Ending
    
    else:
        jump Jane_Good_Ending
        
label JD_Intro_Ending:
    "As you ponder your dreams, you hear heavy foosteps."
    "John appears in front of you, looking more tired than usual."
    show VampySprite at left with dissolve
    show JD at right with dissolve
    
    jd "Hey, [MCname]. Are ya busy?"
    if Doe == 3:
        mc "Do you need something, John?"
    else:
        mc "Do you need something, Mr. Doe?" 
        
    jd "Well, I don't know if ya heard the news, but Jane's missin'."
    jd "No one's seen her for weeks."
    jd "Jannet's been beggin' me to go visit, but we gotta shipment of seeds comin' in today."
    jd "So if ya don't mind, [MCname], could ya go check on her?"
    
    if Doe >= 3:
        mc "I shall help in any way I can, John."
    else: 
        mc "I shall help in any way I can, Mr. Doe."
        
    jd "Thanks."
    hide JD with fade
    show VampySprite at center with dissolve
    jump Jane_Ending_Transition
        
label Anna_Intro_Ending:
    "As you ponder your dreams, you hear someone approaching."
    show VampySprite at left with dissolve
    show Anna at right with dissolve
    "Anna appears in front of you."
    Anna "Curse these spirits..."
    mc "Madam, may I help you?"
    "She turns and faces you."
    Anna "Thank you, young man, but I'm afraid this is a psychic problem."
    Anna "For many nights, I have been trying to find Jane."
    mc "Ms. Dough?"
    Anna "Yes. Nobody has seen her for weeks. And she is not the type of person to leave without notice."
    Anna "I've asked the spirits to guide me to her location, but they been dragging me all over the place."
    Anna "The creek, the mall, this farm -- even my own shop! It's baffling."
    "She sighs"
    Anna "I suppose I will have to go back. Have to open the business soon. Excuse me."
    "She leaves."
    
    hide Anna with fade
    show VampySprite at center with dissolve
    jump Jane_Ending_Transition
    
label Johnny_Intro_Ending:
    "As you ponder your dreams, you hear clumsy footsteps."
    show VampySprite at left with dissolve
    show JC at right with dissolve
    "Johnny appears in front of you."
    mc "Mr. Cash?"
    jc "Hey, ghost! Didn't know you knew the Does. I was just walking around."
    jc "The creek didn't seem like a safe place to be."
    jc "There are rumors that people have been disappearing by the creek."
    jc "And I'd like to stay alive, you know?"
    jc "I mean, no offense, ghost, but I dunno if I'm ready to join the Ghost Club."
    jc "Anyway, I'm going to go. Didn't really plan to walk this far. See ya!"
    "He staggers away."
    hide JC with fade
    jump Jane_Ending_Transition
    
label Jane_Ending_Transition:
    mc "It seems like the town is beginning to notice my crimes."
    "For a few minutes, you can't help but wonder if you left any evidence."
    mc "Perhaps I shall visit the store and check again."
    jump Jane_Bad_Ending
    
label Jane_Good_Ending:
    if jd_dead == False:
        # show VampySprite at center with dissolve
        "When you wake up, there's a envelope on the dining table. It has your name on it."
        "John or Jannet must have left it for you."
    else: 
        "When you wake up, there's an envelope in the mailbox. It has your name on it."
    "You open the letter. Inside is a piece of paper with two words:"
    "Find me at the creek. - J"
    mc "What urgent business necessitates a handwritten note?"
    "You hop out of bed and head to the creek."
        
    show Creek_Bridge with fade 
    show VampySprite at left with dissolve    
    show JaneD at center with dissolve
    "When you get to the creek, you see Jane."   
    janed "Hiya [MCname]..."
    mc "A pleasure to see you, Ms. Dough. To what do I owe the pleasure of meeting you here?"
    "She glances and appraoches you. She opens her mouth to say something, closes it, and grins."
    janed "Well, I, uh...you see..."
    "She grinds her heel into the ground. She gives you a piercing look."
    janed "Alright. Have you figured it out?"
    mc "Pardon? Figured out what exactly?"     
    janed "She motions at the scenery around you."
    janed "This. All of this. How you got here? Why every time you try to leave it doesn't work?"
    mc "What are you trying to imply?"
    "She steps back and holds up her hands, palms facing you."
    "On each palm, there's a red hand-drawn circle filled with little interlacing lines and angular shapes."
    janed "Hear me out, [MCname]."
    janed "I'm letting you leave. I actually removed the binding spell on you right before I came here."
    mc "The binding spell?"
    janed "Yes. I got the idea from one of Anna's books. I summoned you here and bound you to the town."
    janed "I just wanted a little fun. We could have fun. Together. But only if you want too..."
    "She gives you an even wider smile."
    janed "Doesn't have to be anything serious. So?"
    menu:
        "Accept her offer":
            mc "What kind of activities do you have in mind?"
            "She bites her lip and says something. She says a lot of things. You blush."
            hide VampySprite with fade 
            hide JaneD with fade
            scene Black_Wall with fade 
            "Even though you're not bound here anymore, perhaps you'll stay in Bottineau for at least a little longer."
            "THE END."
            jump end
        "Decline":
            mc "You bind me to this town for such a trivial manners? You make me wander this town for such foolish pursuits."
            mc "I refuse to play your games! Begone, monster!"
            "You lunge at her, sinking your fangs into her neck. Then you feast."
            "You drink and drink, letting the taste of blood soothe your mind."
            "When you finished, you hurl her body into the lake."
            "You don't bother to hide it. By the time someone finds it, you'll be far away from Bottineau."
            # "At least you have at last finally earned your freedom."
            "THE END."
            jump end
    
label Jane_Bad_Ending:      
    scene Strip_Mall
    show VampySprite at center with dissolve 
    "You walk to Jane's store. You scour for any entrances or exits."
    "A conveniently open back door grants you access into the store. Thank goodness Jane didn't lock it."
    scene Clothing_Store
    show VampySprite at center with dissolve
    "You carefully slide your way into the front of the store."
    "You examine the room carefully. No blood on the counter. No blood on the floor. No blood on the walls."
    "The only objects that look out-of-place are the books scattered across the floor."
    if Jane >= 3:
        "You recognize one of them as the black book Jane was reading the other day."
    mc "What are these?"
    "You bend over to pick them up and flip quickly through the pages. What was Jane reading?"
    "A series of scribbles litter the first book's pages."
    "You don't understand their meanings, but you see the words SUMMON and BIND scribbled in bright red ink across the margins."
    "The second book seems to be written in the same unrecognizable language as the first."
    "A little note in Jane's handwriting reads \"Can't wait to use this on [MCname]!\""
    "The third and smallest book is full of little passages."
    "Little sonnets comparing a tall, pale man (probably you) to precious and sentimental objects."
    mc "So this is how Ms. Jane felt..."
    menu:
        "This is rather foolish":   
            mc "So, Ms. Jane was responsible. And all because she foolishly thought this book would sole her problems..."
            "Time passes. The horribly unsettling realization of your finds kicks in."
            mc "She was the summoner!?"
            mc "DAMN THIS LADY! I could have left this bloody town the whole time!"
            scene Black_Wall with dissolve
            hide VampySprite at center with fade
            "You hurl the books on the floor. You stomp. You howl. If only you had know this earlier!"
            "So many days spent wandering around this little town! So many days lost!"
            "You don't bother cleaning up your mess."
            "By the time someone to investigate, you'll be far away from Bottineau."
            "THE END."
            jump end
        "This is rather pitiful":
            mc "So she bound me here because she wanted love...how pitiful..."
            "Slowly, you close each book and tuck them away to the box. You leave the box on the floor and leave."
            "You're finally free. With Jane's death, the bindings have been broken."
            "You walk on the road heading away from Bottineau."
            "For a brief moment, you anticipate being dragged back again and dropped at the Does' farm."
            "But it never happens. You walk until you no longer can see the town."
            "At last, you're finally free."
            "THE END"
            jump end