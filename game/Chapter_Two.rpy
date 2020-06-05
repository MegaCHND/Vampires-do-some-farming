####################################################
#   PART 2
#   Primary Author: Nam-Giao Nguyen
#   Secondary Authors: Chris Goebel, Nam-Giao Nguyen, Nichole Wong
####################################################
label Chapter1_End_John_Dead:
    $ day += 1
    scene Farmhouse_Day
    with fade
    "COCK-A-DOODLE-DOO!"
    "The rooster crows. Its cry rings loud and clear over the Doe farm."
    "The only other sound that can be heard is the sound of a shovel throwing dirt over the dried corpses of Mr. and Mrs Doe."
    "At least they'll rest together for all of eternity."
    mc "Forgive me, John and Jannet for dining on your blood. You made the most delightful feast. May you both rest in peace."
    "As you put away your shovel, you start planning your next move."
    mc "Now a new problem arises. Someone would certainly notice their disappearances."
    if Doe == 3:
        mc "Especially Jane. John implied that they knew each other. I wonder if she'll visit tonight."
    mc "I must act carefully. First, I shall attend to the crops. Withered fields would ruin this facade."

    scene Ranch_Sunset
    with fade

    "A farm doesn't care if its owners change. What needs to be tended is tended."

    scene Farmhouse_Bed
    with fade

    show VampySprite at left
    with dissolve

    mc "Fortune favors the bold today. Nobody has come asking questions."
    mc "But peace never lasts long. I must craft a suitable story. Now, what could be my relation with Mr. Doe..."
    mc "Ah, a relative! Of course!"
    mc "I shall pose as Mr. Doe's long-lost relative, here to relieve him of his duties so he may explore the world! Genius!"

    if Jane >= 0:
        hide VampySprite
        with dissolve

        "KNOCK. KNOCK."

        show VampySprite at left
        with dissolve

        mc "I'm coming!"

        scene Farmhouse_Night
        with fade

        show VampySprite at left
        with dissolve

        show JaneD at right
        with dissolve

        if Jane >= 1:
            mc "Ah, Mrs. Dough. To what pleasure do I owe the pleasure meeting you this fine evening?"
            janed "Hiya, [MCname]. I came to drop off a gift for Jannet this evening. Would you mind letting me in?"
            mc "Forgive me, Jane. I'm afraid the Does left a few days ago to travel the world. They are allowing me take over the farm in their absence."
            mc "Would you still like me to deliver your gift on their behalf?"
            janed "Oh, no. It's okay. Let's say this gift is for you instead."
            "Jane grins."
            janed "There's no crime in gifting stuff, right? Especially to someone like you..."
            $ money += 10
            mc "Thank you for your generosity, Jane. If that is all, I shall depart."
            mc "Please excuse me."

        else:
            if Jane > 5000:
                janed "Hello? Oh, it's you! Hiya, cutie! I came to drop a gift for Jannet this evening. Would you mind letting me in?"
                mc "Forgive me, Ms.Dough. I'm afraid the Does left a few days ago to travel the world. They are allowing me take over the farm in their absence."
            elif Jane <= 0:
                janed "Hello? Oh, sorry. I was hoping to see Jannet this evening? I have a gift for her."
                mc "Forgive me, Ms...?"
                $ janedName = "Jane"
                janed "Dough. Jane Dough. I run a shop over at the mall!"
                mc "Forgive me, Ms.Dough. I'm afraid the Does left a few days ago to travel the world. They are allowing me take over the farm in their absence."

            mc "Would you still like me to deliver your gift on their behalf?"
            janed "Oh, no. It's okay. Let's say this gift is for you instead."
            "Jane grins."
            janed "There's no crime in gifting stuff, right? Especially to someone like you..."
            $ money += 10
            mc "Thank you for your generosity, Ms. Dough. If that is all, I shall depart."
            mc "Please excuse me."

        hide VampySprite
        with dissolve

        "Jane leaves with a smile on her face and a skip in her step. You can only shake your head and close the door."

        scene Farmhouse_Bed
        with fade

        show VampySprite at left
        with dissolve

        mc "It appears my simple story works!"
        mc "I must be careful while inquiring the townspeople, lest I slip and break this ruse."
        mc "Perhaps I shall see someone tomorrow."

    $ chap_two_days = 0

    jump Chapter_Two_Morning

label Chapter1_End_Jane_Dead:
    $ info = 0
    $ day += 1
    scene Farmhouse_Day
    with fade

    "COCK-A-DOODLE-DOO"
    "TAP. TAP. TAP."

    show VampySprite at right
    with dissolve

    show JD at left
    with dissolve

    menu:
        jd "Where'va ya been [MCname]? Darling noticed ya weren't in your room when she came to give you breakfast."
        "Give an excuse":
            mc "I decided to take a stroll through the fields."
            jd "Oh, ya wanted to get some fresh air before work, eh?"
            jd "Looks like it did wonders for ya! Ya look might refreshed!"
        "Confess":
            mc "I drove off to town and killed Jane. She was becoming quite the nuisence."
            jd "WHAT? See, darling, I told ya there was somethin' suspicious 'bout him!"
            "John wipes out his gun. You didn't know he kept it near him."
            hide JD with fade
            show JD_With_Gun with dissolve
            jd "Stay there, monster! Yer dead meat!"
            "BANG! BANG! BANG!"
            "Before you can react, he fires his gun three times."
            "You scramble away as fast as you can."
            jump Death_bad_end

    jd "Well there's more work to do so hurry up and eat yer breakfast so we can get to work"
    "You eat your breakfast in solitude, knowing fully well the sins you commited last night."

    $ info = False
    $ chap_two_days = 0
    jump Chapter_Two_Morning

label Chapter1_End_Cash_Dead:
    $ info = 0
    $ day += 1
    scene Farmhouse_Day
    with fade

    "COCK-A-DOODLE-DOO"
    "TAP. TAP. TAP."

    show VampySprite at right
    with dissolve

    show JD at left
    with dissolve

    menu:
        jd "Where'va ya been [MCname]? Darling noticed ya weren't in your room when she came to give you breakfast."
        "Give an excuse":
            mc "I decided to take a stroll through the fields."
            jd "Oh, ya wanted to get some fresh air before work, eh?"
            jd "Looks like it did wonders for ya! Ya look might refreshed!"
        "Confess":
            mc "I drove off to town and killed Johnny. He irked me."
            jd "WHAT? See, darling, I told ya there was somethin' suspicious 'bout him!"
            "John wipes out his gun. You didn't know he kept it near him."
            hide JD with fade
            show JD_With_Gun with dissolve
            jd "Stay there, monster! Yer dead meat!"
            "BANG! BANG! BANG!"
            "Before you can react, he fires his gun three times."
            "You scramble away as fast as you can."
            jump Death_bad_end

    jd "Well hurry up and eat yer breakfast. We gotta head back into town. Gotta get more supplies, and I need your help with somethin'."
    mc "Pardon? Didn't you visit the town recently?"
    jd "I don't want to hear yer yappin'. If I'm saying we're going to town, we're going to town!"

    scene Strip_Mall
    with fade

    show JD
    with dissolve

    jd "Alright we're here. I need ya to go over to Jane's shop and pick up these things for me."
    "He hands you a shopping list."
    jd "Here's the money ya use to pay."
    $ money = money + 5

    mc "With all due respect, this list is extensive. Will five dollars cover all these expenses?"
    jd "Fine. Take another 5 dollars. But don't spend the extra money on some random trinket."
    $ money = money + 5

    scene Clothing_Store
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    if Jane == 0:
        $ Jane = 1
        janed "Hiya, cutie. Don't think I've seen you around town before. What's your name?"
        mc "My name is [MCname]. And you are?"
        $ janedName = "Jane"
        janed "Jane Dough. You can me Jane."
        mc "Pleasure to meet you, Ms. Dough."
        janed "Pleasure is all mine! What can I do for you?"
    else:
        janed "Hiya, [MCname]! What can I do for you?"

    mc "I am interested in purchasing some wares. Here is the list."

    "You hand over the list."

    janed "Oh sure thing sweet thang! Hmm, looks like John sure uses up his supplies quick."

    janed "Give me a moment to gather these things for you."

    "As she searches the shelves, she attempts to make pleasant conversation."

    janed "Did you hear about the latest rumors, hun?"

    mc "Rumors? I'm afraid not."

    janed "They say that someone who spent time at the creek is no longer there."
    janed "Course this is all just speculation. No one actually knows what really happened down there."
    janed "Specially considering that no one really knows if there was someone who spent time there anyway."

    mc "How dreadful if true! I shall keep that in mind. Thank you for the information."

    mc "{i}How fortunate! No one has suspected any foul play in Johnny's murder.{/i}"

    janed "No problem hun, don't want any cute guys like you goin' missin' on me."
    janed "Well anyway, here's what John wanted. That'll be 5 dollars, special price just for you."

    "You hand her the money."

    $ money = money - 5

    scene Strip_Mall
    with fade

    show JD
    with dissolve

    menu:
        jd "Did ya get what I needed?"
        "Yes":
            jd "Alright, great! Thanks for that. I had to go do some more errands around and didn't want to spend more time than I needed ta."
        "No":
            jd "Don't yank my chain like that! I can see it right there in yer hands!"
            jd "Good to see ya got a sense a humor at least."

    jd "Everything's taken care of for today. Let's head back home"

    hide JD
    with dissolve

    "You remember the change you got from Jane."

    menu:
        "Give the change back to John":
            show JD
            with dissolve

            $ money = money - 5
            jd "A discount? Jane must've taken a liking to ya."
            jd "Either that or she's gotten a lot of good business lately. Would explain why she's more peppy these days."
        "Keep the change":
            mc "I doubt he needs the cash."

    scene Farmhouse_Bed
    with fade

    show VampySprite at left
    with dissolve

    mc "It seems that people have not formed any suspicions about previous events."
    mc "But I must be careful next time."
    mc "One minor accident may be ignored. A few accidents look suspicious."

    $ info = False
    $ chap_two_days = 0
    jump Chapter_Two_Morning


label Chapter_Two_Morning:
    $ day += 1
    $ chap_two_days += 1
    if chap_two_days > 4:
        jump Start_chp3

    scene Farmhouse_Day
    with fade

    "COCK-A-DOODLE-DOO!"
    "New day! New choices!"

    menu:
        "Tend to crops" if jd_dead == False:
            $ Doe += 1
            $ info += 1
            jump John_info
        "Go get supplies" if janeD_dead == False:
            $ Jane += 1
            jump time_with_jane
        "Go to the creek" if jc_dead == False:
            $ Cash += 1
            jump time_with_cash

label John_info:
    $ option1 = 0
    $ option2 = 0

    if Doe > 3:
        scene Ranch_Sunset
        with fade

        show VampySprite at left
        with dissolve

        show JD at right
        with dissolve
        "You spend the day tending to the crops with John."
        "When you finish your work, he hands you your pay."
        $ money += 5
    elif jd_dead == True:
        "You spend the day working in the fields."
        $ money = money + 5

        if CurrentChap == 2:
            jump Chapter_Two_Morning
        elif CurrentChap == 3:
            jump Chapter_Three_Morning
        elif CurrentChap == 4:
            jump CHP4_morning
        elif CurrentChap == 5:
            jump Start_chp5
    else:
        jump Help_Farm

label John_Response:
    scene Farmhouse_Night
    with fade

    if info == 1:
        scene Farmhouse_Bed
        with fade

        show JD at left
        with dissolve

        show JDW at right
        with dissolve

        jdw "[MCname] is such a hard worker. We're so lucky he doesn't ask for much."
        jd "He might be a good worker, but that doesn't mean he's a saint. For all we know, he could be schemin' to rob us or somethin'."
        jdw "Oh honey, stop that nonsense and go to sleep."

    elif info > 1 and jinfo == False:
        $jinfo = True
        scene Farmhouse_Bed
        with fade

        show JD at left
        with dissolve

        show JDW at right
        with dissolve

        jd "Darling, I swear, he never asks for anything. It's like he even ain't human."
        jdw "Honey, maybe that's just how he is. Go to sleep."

    if CurrentChap == 2:
        jump Chapter_Two_Morning
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5

label time_with_jane:
    scene Clothing_Store
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    if Jane <= 3 and jd_dead == False:
        jump Strip_Mall_Fun
    else:
        janed "What do you need today, hun?"
        mc "I'm here to see you, Ms. Dough."
        "You spend the rest of the day chatting with Jane."
        "You discuss the weather, the news, rumors -- smalltalk."
        "When her clock chimes five times, you bid your farewells and return to the farm."
        jump Jane_Response

label Jane_Response:
    scene Clothing_Store with fade
    show JaneD at center with dissolve

    if chap_two_days == 1:
        janed "Oh my gosh. Oh my gosh! He's like a prince from a fairy tale!"
        janed "Maybe he can finally whisk me away from this dreary town!"

    elif chap_two_days == 2:
        janed "If he keeps coming here, I'm gonna need to buy supplies myself..."

    elif chap_two_days == 3:
        janed "Anna's book was great. I wonder if she has more I could borrow?"

    if CurrentChap == 2:
        jump Chapter_Two_Morning
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5



label time_with_cash:
    $ Cash_info = 0
    scene Creek_Bridge
    with fade

    show VampySprite at left
    with dissolve

    show JC at right
    with dissolve

    if Cash <= 3:
        jump Creek_Shenanigans
    elif janeD_dead == False and Cash_info == 0:
        $ Cash_info += 1
        jc "Ya know 'bout that lady Jane who runs a shop at the mall?"
        mc "Indeed I do. Is there something wrong?"
        jc "Well rumor has it she's been seen heading into some shady shop recently."
        jc "Because of it she seems to be even peppier these days."
        jc "I don't know what her deal is but looks like she's got somethin' to smilin' about recently."
        jc "Kinda started happin' when I met you here."
        jc "But that's probably a coincidence."
        mc "{i}Hmmm it seems Jane has been quite cheerful as of late. All of the sudden as well.{/i}"
        mc "{i}Perhaps she has seen good business lately.{/i}"
    else:
        "You spend the day fishing with Johnny."
        jump Cash_Response

label Cash_Response:
    # scene Farmhouse_Bed
    # with fade

    # show VampySprite at left
    # with dissolve

    # mc "What a strange man. He likes to hang around the creek, doesn't he?"
    # mc "Perhaps I shall visit him again some time."

    if CurrentChap == 2:
        jump Chapter_Two_Morning
    elif CurrentChap == 3:
        jump Chapter_Three_Morning
    elif CurrentChap == 4:
        jump CHP4_morning
    elif CurrentChap == 5:
        jump Start_chp5



label Death_bad_end:
    "You manage to retreat into the woods. Fortunately, John's bullets weren't made of silver."
    "It seems your chances at a life here are ruined. Perhaps next time you should confess to your crimes so quickly."
    "The End"
    jump end


label end:
    return
