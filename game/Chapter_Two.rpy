label Chapter1_End_John_Dead:
    scene Farmhouse_Day
    "You wake up after sating their own lust for blood to survive"
    mc "Forgiveth me Sir John Doe and Madam Janneth Doe for I needed to dine on thine blood for mine own well-being."
    mc "Noweth mine own problems arise. Surely doth must have companions that worry bout thine well-being."
    mc "I must be wary of thine companions and must come up with a suitable story. But what shalt I doeth first?"
    with Dissolve(.5)
    scene Ranch_Sunset
    "You work on the farm for the day tending to the needs of the farm just like when John was working on it."
    with Dissolve(.5)
    scene Farmhouse_Bed
    show VampySprite at left
    mc "No one hath come in search for now. I am sureth someone will come. Nay... someone will come but I must be ready!"
    mc "Mine own relationship with Sir John Doe. What could it be? Ah of course! A relative!"
    mc "I hath come to relieve Sir John Doe of his duties here so he mayeth seeth the world!"
    if Jane >= 1:
        hide VampySprite
        "*knock knock*"
        show VampySprite at left
        mc "I cometh at once!"

        with Dissolve(0.5)
        scene Farmhouse_Night
        show VampySprite at left
        show JaneD at right
        mc "Ah Jane what pleasure doth I receive the from thee on this fine evening?"
        if Jane == 3:
            janed "Hello [MCname], I was hoping I could see John this evening? I have a gift for him."
            mc "Forgiveth me Madam Jane for John has gone to seeth the world. I am his relatives to relieve him of his duties."
            mc "Wouldst thou still like for me to deliver thine gift on thine own behalf?"
            janed "Oh that would be lovely [MCname]! I have a bunch of things like this back at my store so I hope you come visit me."
            mc "I shalt keep that in memory. Thankst thou Madam Jane. Now if that is all, I wouldst like to get to sleep."
            mc "I must attend to the crops on the morrow. If thou wouldst excuse me."
        else:
            janed "Hello, I was hoping I could see John this evening? I have a gift for him."
            mc "Forgiveth me Madam Jane for John has gone to seeth the world. I am his relatives to relieve him of his duties."
            mc "Wouldst thou still like for me to deliver thine gift on thine own behalf?"
            janed "Oh that would be lovely! I have a bunch of things like this back at my store so I hope you come visit me."
            mc "I shalt keep that in memory. Thankst thou Madam Jane. Now if that is all, I wouldst like to get to sleep."
            mc "I must attend to the crops on the morrow. If thou wouldst excuse me."
        hide VampySprite
        "*Door closes behind [MCname]*"
        with Dissolve(0.5)
        scene Farmhouse_Bed
        show VampySprite at left
        mc "It seemth my story has born fruit! I musth keep my story straight or mine own identity shall be discovered."
        mc "Now that I haveth a story I must seeth where I am. I know not where I am and I must knoweth what happened to me."
        mc "Perhaps I shall see someone tomorrow?"
    stop music fadeout 1
    with Dissolve (0.5)
    $ chap_two_days = 0
    jump Chapter_Two_Morning

label Chapter1_End_Jane_Dead:
    scene Farmhouse_Day
    "John sees you come in from the front door"
    show VampySprite at right
    show JD at left
    menu:
        jd "Where you been [MCname]? My wife noticed you weren't in your room when she came to give you breakfast."
        "I was out for a walk":
            jd "Oh wanted to get some fresh air before the work day eh? Gotta say it did some wonders for you since you look mighty refreshed! Hahahaha!"
        "I went and killed Jane":
            jd "YOU WHAT?! See honey, I told ya there was somethin' suspicious 'bout him!"
            menu:
                jd "Stay there [MCname], you're dead meat!"
                "Stay there and let John shoot you?":
                    jump Death_bad_end
                "Run away and find a different place to give you shelter?":
                    jump Coward_bad_end
    jd "Well there's more work to do so hurry up and eat your breakfast so we can get to work"
    "You eat your breakfast in solitude knowing what you had done last night."
    "Thankfully it seems that John has no clue about what you were up to last night."
    $ info = False
    $ chap_two_days = 0
    jump John_info

label Chapter1_End_Cash_Dead:
    scene Farmhouse_Day
    "John sees you come in from the front door"
    show VampySprite at right
    show JD at left
    menu:
        jd "Where you been [MCname]? My wife noticed you weren't in your room when she came to give you breakfast."
        "I was out for a walk":
            jd "Oh wanted to get some fresh air before the work day eh? Gotta say it did some wonders for you since you look mighty refreshed! Hahahaha!"
        "I went and killed Johnny":
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
    "John hands you about 5 dollars"
    "With the list and money in hand, you head over to Jane's shop."
    with Dissolve (0.3)
    scene Clothing_Store
    show VampySprite at left
    show JaneD at right
    janed "Heya! What can I do for ya?"
    mc "I would like to buy things from thou. Here is a list."
    janed "Oh sure thing sweet thang! Hmm... Hmm... Looks like John sure uses up his supplies quick."
    mc "Thou knowest who this is for from the list? I am impressed."
    janed "Oh you flatter me hun. It's nothing really. John comes in pretty frequently to my shop to resupply for his farm. Been there couple times myself."
    janed "Nice place out there. Clean air, beautiful scenery, and good, old peace and quiet."
    janed "Oh did you hear about the latest rumors hun?"
    mc "Do tell."
    janed "They say that someone who spent time at the creek is no longer there."
    janed "Course this is all just rumors of course. No one actually knows what really happened down there."
    janed "Specially considering that no one really knows if there was someone who spent time there anyway."
    mc "I willst keep that in mind. I thank thee for the information."
    janed "No problem hun, don't want any cuties like you goin' missin' on me. *wink*"
    janed "Well anyway, here's what John wanted, that'll be 5 dollars."

    with Dissolve(0.3)
    scene Strip_Mall
    show JD
    menu:
        jd "Didja get what I needed?"
        "Yes":
            jd "Alright great! Thanks for that I had to go do some more errands around and didn't want to spend more time than I needed ta."
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
    "You wake up feeling refreshed. What do you do?"

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
            "You tend to the crops with John. Since you still have no clue where you are you decide to engage John in some small talk."
            "Dost thou knoweth where we are?":
                $ option1 += 1
                jd "Course I do! What do you take me for? Some kinda unedumacated hillbilly?"
                jd "We're in the prime state of North Dakota in the United States of 'Merica"
                "John beams with pride as he says the country"
            "I seeth thou uses this big box that flashes light at night. What is it?":
                $ option2 += 1
                jd "You don't know what it is? What have you been doing living under a rock?"
                jd "It's a television! After work, I get to unwind and relax and watch some of my favorite shows!"

        if option1 == 1:
            menu:
                "I seeth thou uses this big box that flashes light at night. What is it?":
                    $ option2 += 1
                    jd "You don't know what it is? What have you been doing living under a rock?"
                    jd "It's a television! After work, I get to unwind and relax and watch some of my favorite shows!"
        else:
            menu:
                "Dost thou knoweth where we are?":
                    $ option1 += 1
                    jd "Course I do! What do you take me for? Some kinda unedumacated hillbilly?"
                    jd "We're in the prime state of North Dakota in the United States of 'Merica"
                    "John beams with pride as he says the country"

        "You continue to engage in small talk throughout the work day."
        with Dissolve(0.5)
        scene Farmhouse_Bed
        show VampySprite at left
        mc "That engagement was most enlightening. I learned a lot about whereth I am."
        mc "It seemth I am in this place known as North Dakota in this United States of 'Merica."
        mc "That flashing box is known as the television. It seems to show entertainment."
        mc "Mine own time period there was not a known thing called a television. I musth be in the future!"
        mc "I will continue to do work as I learn more about this place."
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
        "You tend to the crops with John for the day."
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
    janed "Oh hi there! You're John's new worker aren't you? What can I help you with?"
    mc "I am here to seeth you madam Jane."
    if Jane != 3:
        $ Jane = 3
        janed "Oh that's sweet of you hun. I still haven't gotten your name. What was it?"
        mc "My name is [MCname]. Prithee use it well."
        janed "Such a lovely name!"
    menu:
        janed "Well [MCname], what can I do ya for?"
        "Dost thou have more companions?":
            janed "Oh of course! You really should meet some of my gal pals. I bet they would love to meet a cutie like you!"
        "Thou has an excellent assortment of wares. Is business well?":
            janed "Hmmm I would say so. I get a decent amount of customers willing to buy my products."
            janed "People like John come by pretty often to get what they need."
            janed "Although not a lot of people get as much as John does tho. *chuckles*"
    janed "Did ya need anything else hun?"
    mc "No that is all for today. I thank thee for thine company."
    janed "No problem sugar. Come by again if you want to chat!"
    with Dissolve(0.5)
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
    jc "Oh you're back eh? *cough cough* Back here to do some fishing?"
    mc "Yes, it helps mine own thoughts to collect."
    if Cash < 2:
        $ Cash = 3
        mc "My name is [MCname]. Prithee use it well."
        jc "Nice to meet ya [MCname]. *cough cough*"
    menu:
        jc "Somethin' on your mind since you're here? *cough*"
        "Dost thou enjoy fishing as well?":
            jc "Well I'm just here so I can get a good smoke by myself."
            jc "No one really bothers me out here. You're one of the few people I've seen walk by."
            jc "There's just something about you that draws me in I guess."
        "Dost thou knowest the current year?":
            jc "You're kidding me right? It's the 80s man!"
            jc "What have you been up to that you don't know the year?"
            jc "Guess the way you talk is an indication I suppose."
    jc "Looks like it's getting pretty late."
    mc "I agree. I shall depart now."
    jc "Yep take care [MCname]."
    with Dissolve(0.5)
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
    "John grabs his gun that was lying around nearby and shoots you on the spot."
    "That is the end of this tale."
    "THE END"
    jump end

label Coward_bad_end:
    "You book it out of the house before John has time to get his gun and shoot you."
    "As you run away, you hear him screaming something at you but you do not understand quite what he is saying. (TL Note: he is cursing at you)"
    "As you run, you wonder why you ever told him the truth about what you did"
    "THE END"
    jump end

label end:
