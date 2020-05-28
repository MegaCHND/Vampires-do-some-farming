label Chapter1_End_John_Dead:
    scene Farmhouse_Day
    mc "Forgiveth me Sir Doe and Madam Doe for I needed to dine on thine blood for mine own well-being."
    mc "Noweth mine own problems arise. Surely doth must have companions that worry bout thine well-being."
    mc "I must be wary of thine companions and must come up with a suitable story. But what shalt I doeth first?"
    with Dissolve(.5)
    scene Ranch_Sunset
    "A farm doesn't care if its owners change, what needs to be tended is tended"
    with Dissolve(.5)
    scene Farmhouse_Bed
    show VampySprite at left
    mc "No one hath come in search for now. I am sureth someone will come. Nay... someone will come but I must be ready!"
    mc "Mine own relationship with Sir Doe. What could it be? Ah of course! A relative!"
    mc "I hath come to relieve Sir Doe of his duties here so he mayeth seeth the world!"
    if Jane >= 1:
        hide VampySprite
        "There is a knocking at the front door"
        show VampySprite at left
        mc "I cometh at once!"

        with Dissolve(0.5)
        scene Farmhouse_Night
        show VampySprite at left
        show JaneD at right
        mc "Ah Jane what pleasure doth I receive the from thee on this fine evening?"
        if Jane == 3:
            janed "Hiya [MCname], I was hoping I could see Jannet this evening? I have a gift for her."
            mc "Forgiveth me Madam Jane for Sir and Madam Doe has gone to seeth the world. I am to relieve them of their duties."
            mc "Wouldst thou still like for me to deliver thine gift on thine own behalf?"
            janed "Oh really...Then lets just say this is for you. There's no crime in gifting stuff to a QT like you right?"
            mc "Hmm...Thankst thou Madam Jane. Now if that is all, I wouldst like to get to sleep."
            mc "I must attend to the crops on the morrow. If thou wouldst excuse me."
        else:
            janed "Oh? Hello, I was hoping I could see Jannet this evening? I have a gift for her."
            mc "Forgiveth me Madam for Sir and Madam Doe has gone to seeth the world. I am Sir Doe's relative to relieve them of their duties."
            mc "Wouldst thou still like for me to deliver thine gift on thine own behalf?"
            janed "You know what, you can have this. A QT like you living alone? I can come give you more gifts if you want."
            mc "If thou wouldst excuse me, I wouldst like to get to sleep. I must attend to the crops on the morrow."
        hide VampySprite
        "Jane leaves with a smile on her face and a skip in her step. [MCname] can only shake his head and close the door."
        with Dissolve(0.5)
        scene Farmhouse_Bed
        show VampySprite at left
        mc "It seemth my story has born fruit! I musth keep my story straight or mine own identity shall be discovered."
        mc "I must knoweth what happened to me..."
        mc "Perhaps I shall see someone tomorrow?"
    stop music fadeout 1
    with Dissolve (0.5)
    $ chap_two_days = 0
    jump Chapter_Two_Morning

label Chapter1_End_Jane_Dead:
    scene Farmhouse_Day
    "As always the rooster crows to start the day, however the tapping of John's boots also accompany it"
    show VampySprite at right
    show JD at left
    menu:
        jd "Where'va ya been [MCname]? Darling noticed ya weren't in your room when she came to give you breakfast."
        "I wast out f'r a walketh":
            jd "Oh wanted to get some fresh air before the work day eh? Gotta say it did some wonders for you since you look mighty refreshed! Hahahaha!"
        "I wenteth and hath killed jane":
            jd "YA WHAT?! See Darling, I told ya there was somethin' suspicious 'bout him!"
            menu:
                jd "Stay there [MCname], you're dead meat!"
                "Stay there and let John shoot you?":
                    jump Death_bad_end
                "Run away and find a different place to give you shelter?":
                    jump Coward_bad_end
    jd "Well there's more work to do so hurry up and eat your breakfast so we can get to work"
    "[MCname] eats his breakfast in solitude knowing fully well of the sins he commited last night."
    $ info = False
    $ chap_two_days = 0
    jump John_info

label Chapter1_End_Cash_Dead:
    scene Farmhouse_Day
    "As always the rooster crows to start the day, however the tapping of John's boots also accompany it"
    show VampySprite at right
    show JD at left
    menu:
        jd "Where'va ya been [MCname]? Darling noticed ya weren't in your room when she came to give you breakfast."
        "I wast out f'r a walketh":
            jd "Oh wanted to get some fresh air before the work day eh? Gotta say it did some wonders for you since you look mighty refreshed! Hahahaha!"
        "I wenteth and hath killed Johnny":
            jd "YOU WHAT?! See honey, I told ya there was somethin' suspicious 'bout him!"
            menu:
                jd "Stay there [MCname], you're dead meat!"
                "Stay there and let John shoot you?":
                    jump Death_bad_end
                "Run away and find a different place to give you shelter?":
                    jump Coward_bad_end
    jd "Well hurry up and eat your breakfast. We gotta head back into town because I gotta get more supplies and I need your help with somethin'."
    mc "Didst thou not just go to town recently?"
    jd "I don't want to hear your yappin'. If I'm saying we're going to town, we're going to town!"
    with Dissolve(0.5)
    scene Strip_Mall
    show JD
    jd "Alright we're here. I need you to go over to Jane's shop and pick up the things on this here list for me."
    jd "Here's the money you use to pay."
    "The list is quite long, will 5 dollars really be enough?"
    "If not, maybe Jane will give [MCname] a discount."
    with Dissolve (0.3)
    scene Clothing_Store
    show VampySprite at left
    show JaneD at right
    janed "Heya! What can I do for you?"
    mc "I wouldst liketh to buyeth things from thee. H're is a listeth"
    janed "Oh sure thing sweet thang! Hmm... Hmm... Looks like John sure uses up his supplies quick."
    mc "Thou knowest who this is for from the list? I am impressed."
    janed "Oh you flatter me QT. It's nothing really. John comes in pretty frequently to my shop to resupply for his farm. Been there couple times myself."
    janed "Nice place out there. Clean air, beautiful scenery, and good, old peace and quiet."
    janed "Oh did you hear about the latest rumors hun?"
    mc "Nay doth bid."
    janed "They say that someone who spent time at the creek is no longer there."
    janed "Course this is all just rumors. No one actually knows what really happened down there."
    janed "Specially considering that no one really knows if there was someone who spent time there anyway."
    mc "I willst keep that in mind. I thank thee for the information."
    janed "No problem hun, don't want any QT's like you goin' missin' on me."
    janed "Well anyway, here's what John wanted, that'll be 5 dollars just for you."

    with Dissolve(0.3)
    scene Strip_Mall
    show JD
    menu:
        jd "Did ya get what I needed?"
        "Yes":
            jd "Alright great! Thanks for that. I had to go do some more errands around and didn't want to spend more time than I needed ta."
        "No":
            jd "Don't yank my chain like that! I can see it right there in your hands!"
            jd "Good to see ya got a sense a humor at least."
    jd "Everything's taken care of for today. Let's head back home"
    with Dissolve(0.5)
    scene Farmhouse_Bed
    show VampySprite at left
    mc "It would seemeth that people are wary of my deeds from the prior evening."
    mc "I must be careful the next time I must satisfy myself."
    mc "I seemeth to draw no suspicion to myself but I cannot be too cautious."
    mc "I still do not knoweth where I am. Perhaps I shall ask John tomorrow."
    $ info = False
    $ chap_two_days = 0
    jump Chapter_Two_Morning


label Chapter_Two_Morning:

    $ chap_two_days += 1
    if chap_two_days >= 3:
        jump Start_chp3



    scene Farmhouse_Day
    "To be honest, roosters are pretty annoying. Anyways, new day, new choices!"

    if jd_dead == True:
        menu:
            "Go get supplies?":
                jump time_with_jane
            "Go to the creek?":
                jump time_with_cash

    if janeD_dead == True:
        menu:
            "Tend to the crops?":
                jump John_info
            "Go to the creek?":
                jump time_with_cash

    if jc_dead == True:
        menu:
            "Tend to the crops?":
                jump John_info
            "Go get supplies?":
                jump time_with_jane

label John_info:
    if info == False:
        with Dissolve(0.5)
        scene Ranch_Sunset
        show VampySprite at left
        show JD at right
        $ option1 = 0
        $ option2 = 0
        menu:
            "This place is quiet nice. There's a farm, a creek, and a mall at least. But where is here?"
            "Dost thou knoweth where we are?":
                $ option1 += 1
                "John looks at [MCname] with some confusion. He's be here how long and only now asks that question?"
                jd "Course I do! What do you take me for? Some kinda unedumacated hillbilly?"
                jd "We're in the prime state of North Dakota in the United States of 'Merica"
                "John beams with pride as he says the country"
            "I seeth thou uses this big box that flashes light at night. What is it?":
                $ option2 += 1
                "John looks at [MCname] with some confusion. He use tools without a problem but doesn't know what they are?"
                jd "You don't know what it is? What have you been doing living under a rock?"
                jd "It's a television! After work, I unwind and relax and watch some of my favorite shows!"

        "The rest of the day is filled with small scenes like these"
        with Dissolve(0.5)
        scene Farmhouse_Night
        show VampySprite at left
        mc "That engagement was most enlightening. I learned a lot about whereth I am."
        if option2 >= 1:
            mc "Mine own time period there was not a known thing called a television. I musth be in the future!"
        mc "I will continue to do work as I learn more about this place."
        if chap_two_days == 1:
            scene Farmhouse_Bed
        
            show jd at left
            show jdw at right
            jdw "[MCname] is such a hard worker. We're so lucky he works practically for free."
            jd "I still think he's a wendigo Darling."
            jdw "Oh honey, stop that nonsense and go to sleep."
        
        elif chap_two_days == 2:
            scene Farmhouse_Bed
        
            show jd at left
            show jdw at right
            jd "Darling, I swear, he asks about the most mundane things."
            jdw "Honey, maybe he's just passing the time. Go to sleep."
      
        $ info = True
        if CurrentChap == 2:
            jump Chapter_Two_Morning
        if CurrentChap == 3:
            jump Chapter_Three_Morning
        if CurrentChap == 4:
            jump CHP4_morning
    else:
        with Dissolve(0.3)
        scene Ranch_Sunset
        "Being a hard worker is well, hard but someone needs to tend the crops today."
        if CurrentChap == 2:
            jump Chapter_Two_Morning
        if CurrentChap == 3:
            jump Chapter_Three_Morning
        if CurrentChap == 4:
            jump CHP4_morning

label time_with_jane:
    with Dissolve(0.3)
    scene Clothing_Store
    show VampySprite at left
    show JaneD at right
    janed "Oh hi there! You're John's worker now aren't you? What can I help you with?"
    mc "I am here to seeth you madam Jane."
    if Jane != 3:
        $ Jane = 3
        janed "Oh that's sweet of you hun. I still haven't gotten your name. What was it?"
        mc "My name is [MCname]. Prithee use it well."
        janed "Such a lovely name!"
    menu:
        janed "Well [MCname], what can I do ya for?"
        "Dost thou have more companions?":
            janed "Oh of course! You really should meet Anna. I bet she would love to meet a QT like you!"
            janed "Ah maybe not. I want you all to myself." 
        "Thou has an excellent assortment of wares. Is business well?":
            janed "Hmmm I would say so. I get a decent amount of customers willing to buy my products."
            janed "People like John come by pretty often to get what they need."
            janed "Although not a lot of people get as much as John does though."
    janed "Did ya need anything else hun?"
    mc "No that is all for today. I thank thee for thine company."
    janed "No problem sugar. Come by again if you want to chat!"
    with Dissolve(0.5)
    if chap_two_days == 1:
        scene Clothing_Store
        show JaneD at right
        janed "Oh my gosh. Oh my gosh! He's like out of a fairy tale of I love it! Maybe he can finally wisk me away from this town."
    elif chap_two_days == 2:
        scene Clothing_Store
        show JaneD at right
        janed "Anna's book was great, I wonder if she ahs any more like it?"
    elif chap_two_days == 3:
        scene Clothing_Store
        show JaneD at right
        janed "If he keeps coming here, I'm gonna need to buy supplies myself..."
    scene Farmhouse_Bed
    show VampySprite at left
    mc "What a lovely woman. She certainly knoweth how to make a chat entertaining."
    mc "Jane seemeth to be in touch with many people. I must have her introduce me."
    mc "Perhaps they can satiate my needs when the time comes."
    
     
    if CurrentChap == 2:
        jump Chapter_Two_Morning
    if CurrentChap == 3:
        jump Chapter_Three_Morning
    if CurrentChap == 4:
        jump CHP4_morning

label time_with_cash:
    with Dissolve(0.5)
    scene Creek_Bridge
    show VampySprite at left
    show JC at right
    jc "Oooooh it's THE MAN? *cough cough* Back here to do some fishing?"
    mc "Yes, it helps mine own thoughts to collect."
    if Cash < 2:
        $ Cash = 3
        mc "My name is [MCname]. Prithee use it well."
        jc "Nice to meet ya. *cough cough*"
    menu:
        jc "Somethin' on your mind since you keep comin' here? *cough*"
        "Dost thou enjoy fishing as well?":
            jc "Weeeeell I'm just here so I can get a good smoke by myself."
            jc "No one reeeeeally bothers me out here. You're one of the few people I've seeeeeen walk by."
            jc "There's just something about you that draaaaaws me in I guess."
        "Dost thou knowest the current year?":
            jc "You're kiiiiidding me right? It's the 80s man!"
            jc "What have you been up to that you don't know the yeeeeear?"
            jc "Guuuuuess the way you talk is an indication I suppose."
    jc "Looks like it's getting pretty late."
    mc "I agree. I shall depart now."
    jc "Yeeeeah take care man."
    with Dissolve(0.5)
    if chap_two_days == 1:
        scene Creek_Bridge
        show JC at right
        jc "He's sooooo pale. Fish isn't gonna cut it. Maybe he should get more meat. Like people heh he heh"
    elif chap_two_days == 2:
        scene Creek_Bridge
        show JC at right
        jc "Does he not eat? Sooometimes, he looks paler than me."
    elif chap_two_days == 3:
        scene Creek_Bridge
        show JC at right
        jc "I wooonder, does anyone else think he speeeaks weird?"
    scene Farmhouse_Bed
    show VampySprite at left
    mc "That man is a strange one. He stayeth in the creek in solitude."
    mc "However, his company is not unpleasant."
    mc "Perhaps I shall visit him again and ask him something different."
    if CurrentChap == 2:
        jump Chapter_Two_Morning
    if CurrentChap == 3:
        jump Chapter_Three_Morning
    if CurrentChap == 4:
        jump CHP4_morning


label Death_bad_end:
    "John grabs his gun that was lying around nearby and shoots [MCname] in the head."
    "Nothing sprays out. Well, that's expected if there was nothing there in the first place."
    "Who just stands around after admitting to murder?"
    "THE END"
    jump end

label Coward_bad_end:
    "As John rushes back inside to get his gun, [MCname] slams the front door and sprints away"
    "Johns curses are heard in the distance as bullets wizz by [MCname]'s head"
    "What could have possibly possesed someone to admit to murder?"
    "THE END"
    jump end

label end:
