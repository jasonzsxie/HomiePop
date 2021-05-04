label chapterOneDay5:
    $ whoFirst = ""
    $ whoSecond = ""
    $ whoThird  = ""
    $ girlsTalkedTo = 0
    window hide
    scene day five
    pause

    scene bg clubroom 
    with fade
    pause(.5)
    window show
    show tiffany neutral small at left
    show regina neutral at centerleft
    show maryanne neutral at centerright  
    show kristella neutral at right
    pause(.25)
    mc "Today I'll be assigning roles to all of you."
    "All Females" "Roles?"
    scene bg clubroom
    show kelvin excited
    pause(.25)
    kel "Yup! MC, would you like to explain?"
    mc "Right."
    scene bg clubroom
    mc "LL is a team oriented strategy based game where 5 players fight each other, working their way to the other team's crystal."
    mc "The objective is to break the opponent's crystal before the other team gets to yours."
    mc "There are 3 lanes and a jungle, which contains neutral monsters that can be slain for resources or team buffs"
    mc "Each member of the team has a different role -from top, jungle, mid, adc (short for attack damage carry), and support, which involves different responsibilities."
    mc "For example, I am a Jungle main, so I'm responsible for helping all of my teammates and securing neutral objectives."
    mc "Top makes individual plays and engages teamfights."
    mc "Mid usually controls decision-making and strategy."
    mc "ADC tries to stay safe and do damage later in the game."
    mc "ADC and Support play together in the bottom lane. The Support takes care of the ADC and helps the team maintain vision of the map."
    mc "Sooo, did everyone understand that?"
    scene bg clubroom
    show tiffany confused small at left
    show regina confused at centerleft
    show maryanne confused at centerright  
    show kristella confused at right
    pause(.25)
    "All Females" "Kinda...?" 
    scene bg clubroom
    show kelvin exasperated
    pause(.25)
    mc "You're probably right..."
    mc "We should get roles decided first."
    mc "{i}Who should I talk to? {i}"
    while girlsTalkedTo <= 3: 
        scene bg clubroom
        menu:
            "Tiffany" if whoFirst != "Tiffany" and whoSecond != "Tiffany" and whoThird != "Tiffany":
                jump tiffanyRole 

            "Maryanne" if whoFirst != "Maryanne" and whoSecond != "Maryanne" and whoThird != "Maryanne":
                jump maryanneRole 

            "Regina" if whoFirst != "Regina" and whoSecond != "Regina" and whoThird != "Regina":
                jump reginaRole 

            "Kristella" if whoFirst != "Kristella" and whoSecond != "Kristella" and whoThird != "Kristella":
                jump kristellaRole 

        label tiffanyRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Tiffany"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Tiffany"
            elif girlsTalkedTo == 3:
                $ whoThird = "Tiffany"
            show tiffany nervous
            pause(.25)
            mc "Hey Tiffany."
            t "H-hi."
            mc "No Need to be nervous. Justing going to ask some questions."
            menu:
                "What role sounds fun for you?":
                    jump tiffanyRoleOne
                "Did you understand the point of the game?":
                    jump tiffanyRoleTwo
                "You would be a great ADC player.":
                    jump tiffanyRoleThree

            label tiffanyRoleOne:
                show tiffany shy smile
                pause(.25)
                t "U-uh, I like the role ADC more than all the other roles"
                mc "Oh, why's that?"
                t "B-because I get to stay far away from the enmy and I'm protected."
                mc "But you'll have a lot of pressure later in the game to carry. Do you think you can handle the pressure?"
                show tiffany smile
                pause(.25)
                t "Yeah, I think I can handle the pressure"
                jump endTiffanyRole
            
            label tiffanyRoleTwo:   
                show tiffany nervous
                pause(.25)
                t "Er-r, we just try to destroy the enemy crystal right? And each person has a role to play."
                mc "{i}So she did understand...{/i}"
                mc "Yeah, that's pretty much it. So have you decided on a role?"
                show tiffany slight smile
                pause(.25)
                t "A-ADC sounds kinda fun, b-because I get to be protected and far from the enemy."
                mc "Oh, but you're going to have a large weight on you back late in the game. Are you able to withstand that pressure?"
                show tiffany smile 
                pause(.25)
                t "You can count on me."
                jump endTiffanyRole

            label tiffanyRoleThree:
                show tiffany surprised
                pause(.25)
                t "A-ADC?!?! W-why do you think I would be good at it?"
                mc "Well, you seem like you would enjoy being protected by the team. Plus, there will be someone playing with you to get you through the early stages of the game."
                show tiffany nervous
                pause(.25)
                t "D-don't I have a lot of pressure later in the game to carry?"
                mc "I believe in your ability to withstand that pressure."
                show tiffany smile
                pause(.25)
                t "Thanks. I won't let you down."
                jump endTiffanyRole

            label endTiffanyRole:
                jump endOfRole

        label maryanneRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Maryanne"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Maryanne"
            elif girlsTalkedTo == 3:
                $ whoThird = "Maryanne"
            show maryanne smile
            mc "Hi Maryanne."
            ma "Hey [mc]"
            mc "Let's get to the point."
            menu:
                "Did you understand the point of each role?":
                    jump maryanneRoleOne
                "What role do you think you would enjoy?":
                    jump maryanneRoleTwo
                "I think you should play mid.":
                    jump maryanneRoleThree
                
            label maryanneRoleOne:
                show maryanne excited
                pause(.25)
                ma "Mid sounds fun. I get to help impact all the other lanes and set the tempo of the game."
                mc "Yep, that's essentially what the Mid laner has to do."
                ma "Hmm... I feel like I'll be able to contribute the most playing Mid."
                mc "Sounds great!"
                jump endMaryanneRole

            label maryanneRoleTwo:
                show maryanne smile
                pause(.25)
                ma "I feel like mid would allow me to help everyone and control the pace of the game."
                mc "You can also do that by playing jungle. I can let you jungle if you want."
                show maryanne laugh
                pause(.25)
                ma "What do you think I am? A monkey? You belong in the jungle, not me."
                mc "I can't really argue with that"
                jump endMaryanneRole

            label maryanneRoleThree:
                show maryanne questioning
                pause(.25)
                ma "Huh? But why mid out of all the roles?"
                mc "Well, you seem to enjoy helping other people, and I trust in you to control the pace of the game with your intuition."
                show maryanne blushing
                pause(.25)
                ma "Well... If YOU are suggesting it, I guess I can't refuse."
                mc "Okay then..."
                jump endMaryanneRole
                
            label endMaryanneRole:
                jump endOfRole
        
        label reginaRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Regina"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Regina"
            elif girlsTalkedTo == 3:
                $ whoThird = "Regina"
            show regina glare
            pause(.25)
            mc "Hey Regina."
            r "Hey loser."
            mc "{i}...Why?{/i}"
            mc "Anyways..."
            menu:
                "What role would you enjoy playing?":
                    jump reginaRoleOne
                "Did you understand the game from my explanation?":
                    jump reginaRoleTwo
                "Y-you should consider playing top...":
                    jump reginaRoleThree

            label reginaRoleOne:
                show regina evil smile
                pause(.25)
                r "Oh! Top lane sounds fun since I get to yell at you for help."
                mc "Err, you're supposed to be a tank and help teamfight."
                r "So you're telling me I get to smack people around and not die? Even better."
                mc "{i}She's completely missing the point.{/i}"
                show regina glare
                pause(.25)
                r "Hmph, you got a problem with that?"
                mc "U-uh no, not at all."
                show regina smile
                pause(.25)
                r "Good."
                jump endReginaRole

            label reginaRoleTwo:
                show regina rage
                pause(.25)
                r "What? Did you think I'm an idiot or something? Of course I understood what you were talking about. It's not like I'm stupid or anything."
                mc "I wasn't call- Er, nevermind that."
                show regina neutral #nonchalant if avaliable
                pause(.25)
                r "As for my role, I've already decided on Top."
                mc "Huh, why top?"
                show regina evil smile
                pause(.25)
                r "Because I get to tyell at you for help, duh. Oh and I can smack people around."
                mc "That's not the-"
                show regina crossed arms
                pause(.25)
                r "Well, I already made up my mind and you're not chaning it."
                mc "Understood..."
                jump endReginaRole

            label reginaRoleThree:
                show regina stern
                pause(.25)
                r "First of all, don't tell me what to do."
                r "Secondly, shut up."
                r "But purely out of curiosity, why?"
                mc "U-um... you juh-just seem like a t-top..."
                show regina laugh
                pause(.25)
                r "Haha, that is tr -"
                show regina embarrassed
                pause(.25)
                r "I m-mean, shut up!"
                mc "Bu-"
                show regina hand behind back
                pause(.25)
                r "I already told you! You don't know me!"
                r "S-so don't act like you do!"
                mc "I'm sorry..."
                show regina stern
                pause(.25)
                r "Hmph. Fine, I'll pardon you."
                r "Remind me, what does the top do?"
                mc "W-well, the top engages fights and-"
                show regina evil smile
                pause(.25)
                r "Engages fights? That sounds fun."
                r "I'm in! I'll be the top."
                mc "O-okay, it's d-decided. I'm glad that I could he-"
                show regina embarrassed
                pause(.25)
                r "But not because of you!"
                r "Y-you were completely wrong about me!"
                r "So don't go around thinking th-that you helped me or anything!"
                mc "Y-yes, of c-course not..."
                show regina slight smile
                pause(.25)
                r "Hmph. Good."
                mc "{i}I don't know how to feel...{/i}"
                jump endReginaRole                

            label endReginaRole:
                jump endOfRole

        label kristellaRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Kristella"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Kristella"
            elif girlsTalkedTo == 3:
                $ whoThird = "Kristella"
            show kristella smile
            pause(.25)
            kr "Hey, [mc]~"
            mc "Hi, Kristella."
            menu:
                "Was there a role that stood out to you?":
                    jump kristellaRoleOne
                "How was my explanation?":
                    jump kristellaRoleTwo
                "Hmm... I think you'd be a great support.":
                    jump kristellaRoleThree
            
            label kristellaRoleOne:
                show kristella smile
                pause(.25)
                kr "Actually, yeah! I'd love to play support."
                mc "Really? Why?"
                kr "Well, I enjoy helping and encouraging people, so I think it fits me perfectly."
                mc "I agree. You're umm... very good at taking c-care of others..."
                show kristella giggle
                pause(.25)
                kr "Hehe ~ that's sweet of you, [mc]."
                mc "Ah... y-you too..."
                mc "{i}What am I even saying? {/i}"
                mc "{i}I should leave now...{/i}"
                jump endKristellaRole

            label kristellaRoleTwo:
                show kristella smile
                pause(.25)
                kr "It was a bit confusing, but I think I got it!"
                mc "That's a relief..."
                mc "Well, do you have a role in mind?"
                kr "Support - it sounds super fun to nourish and care for my teammates!"
                mc "That's great! I think you'll enjoy supporting, too."
                show kristella wink
                pause(.25)
                kr "Oh, I'm sure I will~"
                mc "Um, er - b-bb-, e-excuse me..."
                show kristella giggle
                pause(.25)
                kr "Hehe. Bye, [mc]!"
                jump endKristellaRole

            label kristellaRoleThree:
                show kristella smile
                pause(.25)
                kr "Oh? Why do you say that, [mc]?"
                mc "W-well... I think you're really c-caring and kind, so you'd be good at it..."
                show kristella touched
                pause(.25)
                kr "Aww - thank you, [mc]."
                kr "Also, I was thinking the same~"
                show kristella giggle
                pause(.25)
                kr "I'd love to be your support."
                mc "M-m-mine?!? W-what do you mean?" with hpunch
                kr "Well, you're the captain of the team, silly!"
                kr "That means I'm playing for you."
                mc "..."
                mc "..."
                mc "Oh..."
                kr "Well, see you, [mc]~"
                mc "B-bye -"
                mc "{i}How embarrassing...{/i}"
                jump endKristellaRole

            label endKristellaRole:
                jump endOfRole


        label endOfRole:
            if girlsTalkedTo == 4:
                scene bg clubroom
                mc "Okay, that's everyone! It all worked out, so the roles are decided-"
            else:
                scene bg clubroom
                mc "{i}Who should I talk to next?{/i}"
    $ whoFirst = ""
    $ whoSecond = ""
    $ whoThird  = ""
    $ girlsTalkedTo = 0
    scene bg clubroom
    mc "I'll be the jungler."
    mc "Regina is in the top lane."
    mc "Maryanne is our mid."
    mc "Tiffany is the ADC."
    mc "And last but not least, Kristella is our support!"
    show regina smile
    pause(.25)
    r "That's right."
    hide regina smile
    show tiffany smile
    pause(.25)
    t "Y-yeah."
    hide tiffany smile
    show maryanne smile
    pause(.25)
    ma "Sounds great."
    hide maryanne smile
    show kristella laugh
    pause(.25)
    kr "Woo!"
    hide kristella laugh
    show kelvin smile
    pause(.25)
    kel "Okay, we can start training now."
    mc "Yeah, of course!"
    scene bg clubroom
    mc "{i}Who should I train first?{/i}"
    while girlsTalkedTo <= 3: 
        scene bg clubroom
        menu:
            "Tiffany" if whoFirst != "Tiffany" and whoSecond != "Tiffany" and whoThird != "Tiffany":
                jump tiffanyTraining 

            "Maryanne" if whoFirst != "Maryanne" and whoSecond != "Maryanne" and whoThird != "Maryanne":
                jump maryanneTraining 

            "Regina" if whoFirst != "Regina" and whoSecond != "Regina" and whoThird != "Regina":
                jump reginaTraining 

            "Kristella" if whoFirst != "Kristella" and whoSecond != "Kristella" and whoThird != "Kristella":
                jump kristellaTraining

        label tiffanyTraining:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Tiffany"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Tiffany"
            elif girlsTalkedTo == 3:
                $ whoThird = "Tiffany"
            show tiffany shy
            pause(.25)
            t "I-I guess you're here to teach me?"
            mc "Yeah, we'll go through the basics today."
            show tiffany nervous
            pause(.25)
            t "O-okay, I-I might make a lot of mistakes."
            mc "Don't worry. Everyone makes mistakes whenever they're trying something new."
            t "Y-yeah, I guess..."
            mc "{i}Geez, I wonder how she's going to handle the ingame toxicity.{/i}"
            mc "{i}I hope she doesn't get flamed...{/i}"
            scene bg computer 
            with fade
            mc "Uh, have you made an account yet?"
            show tiffany nervous
            pause(.25)
            t "U-uh, yea. M-my username is KawaiiTiff."
            mc "Oh..."
            menu:
                "I like your name":
                    jump tiffanyNameOne
                "What did you base your name on?":
                    jump tiffanyNameTwo
                "Interesting name...":
                    jump tiffanyNameThree

            label tiffanyNameOne:
                show tiffany shy
                pause(.25)
                t "U-uh, t-thanks."
                mc "What does kawaii mean?"
                show tiffany flustered
                pause(.25)
                t "U-uagh, i-it m-means c-c-cute in Japanese."
                mc "Oh, it suits you well."
                show tiffany blush 
                pause(.25)
                t "C-can we get on with the lesson?"
                jump tiffanyNameEnd
            
            label tiffanyNameTwo:
                show tiffany flustered
                pause(.25)
                t "U-uah, K-Kawaii m-means c-c-cute in Japanese."
                mc "Oh, I see, it fits your personality well."
                t "T-thanks. C-can we s-start the lesson now?"
                jump tiffanyNameEnd
            
            label tiffanyNameThree:
                show tiffany shy
                pause(.25)
                t "T-t-thanks..."
                mc "{i}I didn't know she was a weeb...{/i}"
                t "U-uh why are you staring at me."
                mc "Oh, I was just thinking."
                t "O-oh, c-can we s-start the lesson?"
                jump tiffanyNameEnd

            label tiffanyNameEnd:
                scene bg computer

            mc "Alright, we should..."
            menu:
                "Go into a PvP match.":
                    jump tiffanyTrainingOne
                "Play some 1v1s.":
                    jump tiffanyTrainingTwo
                "Have you watch me for a bit.":
                    jump tiffanyTrainingThree

            label tiffanyTrainingOne:
                show tiffany shocked
                pause(.25)
                t "W-wait, a PvP match??? S-shouldn't I practice against bots or something to learn the game?"
                mc "Well, most players do, but since we're playing in a tournament soon, we need to improve quickly and I think by going straight into PvP is the best way to do that."
                show tiffany neutral
                pause(.25)
                t "O-okay. So I just click on this?"
                mc "Yes. Then just accept the game when it pops up."
                show tiffany shocked
                pause(.25)
                t "Oh. I-I got a game."
                mc "Ok so just type that you're playing ADC."
                show tiffany neutral
                pause(.25)
                t "Okay so what champ should I play."
                mc "I think Bane would be a good champion for you."
                scene bg computer game
                with fade
                mc "Alright so you should..."
                menu:
                    "Focus on last hitting the creeps.":
                        jump TiffanyPVPOne
                    "Try to kill the enemy.":
                        jump TiffanyPVPTwo
                
                label TiffanyPVPOne:
                    show tiffany neutral 
                    pause(.25)
                    t "S-so do I just hit them like this."
                    mc "No, no, no, wait until it's low then hit it."
                    t "O-oh so like thi-. I-I didn't get it."
                    mc "Don't worry, it takes time to get used to- oh they're trying to kill you."
                    show tiffany scared
                    pause(.25)
                    t "W-what d-do I do, they're hitting me. [mc] h-help!"
                    mc "Well, you fight bac- oh you died."
                    mc "{i}This is going to be harder than I thought{/i}"
                    jump tiffanyPVPEnd

                label TiffanyPVPTwo:
                    mc "Alright so when you level up start attacking the enemy."
                    show tiffany confused
                    pause(.25)
                    t "D-do I just walk up and-?"
                    mc "NO DON'T WALK-. Well you're dead."
                    t "O-oh, I-I died so fast..."
                    mc "yeah, you have to be careful with their abilities."
                    mc "{i}This is going to be a long day...{/i}"
                    jump tiffanyPVPEnd

                label tiffanyPVPEnd:
                    scene bg computer
                    with fade
                
                show tiffany exhausted
                pause(.25)
                t "W-wow I won, even though I died a lot."
                mc "{i}For a new player, she isn't that bad.{/i}"
                mc "Nice job. I'll point out your mis-."
                scene bg computer
                mc "{i}Wait, why is she typing so much?{/i}"
                mc "{i}???{/i}"
                mc "{i}Whoa whoa, this is the kind of stuff that you have to censor really heavily, just a bit of pixelation won't cut it..."
                show tiffany shy
                pause(.25)
                mc "..."
                t "[mc]? I-is something wrong? You've been staring at me for a bit..."
                mc "..."
                mc "{i}Isn't she usually super quiet?{/i}"
                t "[mc]???"
                mc "..."
                mc "{i}Why is she toxic in game?{/i}"
                t "G-guys? [mc] looks really pale... He stopped breathing! Guys h-help!"
                mc "I-I'm fine. M-maybe we can review your game next time..."
                t "A-are y-you sure?"
                mc "{i}I should disable her chat function{/i}"
                mc "Y-yea, see you."
                t "B-bye."
                jump tiffanyTrainingEnd

            label tiffanyTrainingTwo:
                show tiffany shocked
                pause(.25)
                t "W-wait, a 1v1? W-with you? Aren't you really good at this game?"
                mc "Exactly. I'm Diamond, so I'm farm better than the average player. By playing against better competition, you'll learn quicker."
                t "I guess you're right. S-so what champ should I play?"
                mc "I think Bane is a good champion for you."
                scene bg computer game
                with fade
                mc "{i}Hmm, it's been 5 minutes and she is getting low on health.{/i}"
                mc "{i}I am getting a little bored{/i}"
                mc "{i}Should I...{/i}"
                menu:
                    "Try to kill her.":
                        jump tiffany1v1One
                    "Play patiently.":
                        jump tiffany1v1Two
                    "Let her kill me.":
                        jump tiffany1v1Three

                label tiffany1v1One:
                    mc "{i}Ok, so I will just start my combo off and...{/i}"
                    mc "!!!" with hpunch
                    show tiffany confused
                    pause(.25)
                    t "U-uh, h-how did you miss everything?"
                    mc "{i}How did she dodge everything? Maybe I'll just...{/i}"
                    "You have been slain." #maybe play audio file of league announcer instead
                    t "O-oh, I-I killed you. Y-you went easy on my right?"
                    mc "H-how di...err yeah, I didn't try that hard, good job surviving the assault."
                    mc "{i}I can't believe I died to the turret.{/i}"
                    mc "Anyways, are you ready for round 2?"
                    show tiffany confident
                    pause(.25)
                    t "Bring it on!"
                    jump tiffany1v1End
            
                label tiffany1v1Two:
                    mc "{i}I'll just wait until she makes a mistake and k-"
                    mc "!!!"
                    show tiffany annoyed 
                    pause(.25)
                    t "W-why are you playing so far back?"
                    mc "{i}Wow that was close. Now I can...{/i}"
                    t "S-stop running away from me.L-let me-"
                    "An enemy has been slain."
                    t "O-oh... I died."
                    mc "{i}Phew that was close.{/i}"
                    mc "That was a good try. Next time, make sure to dodge my attacks."
                    t "U-understood."
                    jump tiffany1v1End

                label tiffany1v1Three:
                    mc "{i}Okay, so I just let her attack me and I'll run under her turret. This should be good for her confidence.{/i}"
                    show tiffany confused
                    pause(.25)
                    t "[mc]? W-what are you doing?"
                    mc "Hmm? Doing what?"
                    "You have been slain."
                    mc "Ah, I guess you killed me. Good job."
                    t "Y-you didn’t try very hard did you?"
                    mc "O-of course I was trying..."
                    t "Y-you were just bored of playing right?"
                    mc "Y-yea, I guess. I'm sorry."
                    t "N-next time can you g-go a little harder? I-I promise I w-won’t be boring."
                    mc "Alright."
                    jump tiffany1v1End

                label tiffany1v1End:
                    scene bg computer
                    with fade
                
                mc "{i}She has good mechanics. Just need to work on-{/i}"
                mc "{i}Why is she typing to me?{/i}"
                mc "!!!" with hpunch
                show tiffany smile 
                pause(.25)
                t "W-wow I got completely destroyed. I gu- [mc]?"
                mc "{i}Whoa whoa, this is the kind of stuff that you have to censor really heavily, just a bit of pixelation won't cut it..."
                t "[mc]?!?"
                mc "..."
                mc "{i}I'm surprised she has so much to say when she's usually so quiet.{/i}"
                show tiffany shocked
                pause(.25)
                t "G-guys? I-I think [mc] needs h-help!"
                mc "N-no need. I’m fine. I’ll tell you what you did wrong at the next meeting."
                t "A-are you sure?"
                mc "{i}I should disable her ability to chat in game. I didn’t expect her to be so toxic.{/i}"
                mc "Y-yea, bye."
                jump tiffanyTrainingEnd

            label tiffanyTrainingThree:
                show tiffany confused
                pause(.25)
                t "U-uh shouldn't I play against bots to practice?"
                mc "Well, it helps to watch someone who knows what they are doing."
                show tiffany understanding
                pause(.25)
                t "O-oh I see..."
                mc "Anyways, I'll just queue up as ADC and play Bane."
                show tiffany confused
                pause(.25)
                t "W-who's Bane?"
                mc "He's a playable character that I think fits you."
                scene bg computer game
                with fade
                mc "{i}It's so boring right now. The enemy is low but the support doesn't want to fight. I've already explained the basics to Tiffany.{/i}"
                mc "{i}Should I-{/i}"
                menu:
                    "Start attacking the enemy.":
                        jump tiffanyWatchOne
                    "Wait for the enemy to make a mistake.":
                        jump tiffanyWatchTwo
                    "Tell the support to fight.":
                        jump tiffanyWatchThree

                label tiffanyWatchOne:
                    mc "Alright, Tiffany never imitate what I am about to do because it's reckless."
                    show tiffany confused 
                    pause(.25)
                    t "H-huh, i-isn't the enemy almost dead? W-why don-"
                    hide tiffany confused
                    "You have been slain."
                    mc "Ah, I misplayed that fight. This is why you shou-"    
                    "An enemy has been slain."
                    mc "Ah, he died to creeps. Anyways, never go for that kill because if you die and the enemy doesn't, the game becomes very unplayable."
                    show tiffany understanding
                    pause(.25)
                    t "O-oh, I-I understand now. I-if you have the a-advantage, you shouldn't gamble it away."
                    mc "I guess you could put it that way."
                    mc "{i}Wow, she's a fast learner.{/i}"
                    jump tiffanyWatchEnd

                label tiffanyWatchTwo:
                    mc "Ok Tiffany, now that the enemy is low, I'll wait for him to make a mistake. Then I can kill him."
                    show tiffany confused
                    pause(.25)
                    t "B-but how can y-you tell when he makes a mistake?"
                    mc "Well, you need to- oh he's so dead."
                    hide tiffany confused
                    "An enemy has been slain."
                    mc "Oh? The support is also running in?"
                    "Double Kill."
                    mc "Well, that was two easy kills. As I was saying, you need to be able to tell when he’s in kill range and how far your abilities travel. When he gets a little too close, you can kill him, but make sure you don’t miss."
                    show tiffany understanding
                    pause(.25)
                    t "O-oh, s-so when he gets too close and is low on health, s-start attacking?"
                    mc "Uh, sounds about right."
                    mc "{i}She's grasping the basics pretty fast.{/i}"
                    jump tiffanyWatchEnd

                label tiffanyWatchThree:
                    mc "Ok, so now that the enemy is low, I am going to tell my support to start attacking and I will follow."
                    show tiffany confused
                    pause(.25)
                    t "H-huh? W-why the support? W-why not just go in by yourself?"
                    mc "Well... If I go in by myself, it - oh he missed. Whatever, the enemy is still dead."
                    hide tiffany confused
                    "An enemy has been slain."
                    mc "As I was saying, you should tell the support to start attacking because if you attack by yourself, it becomes a 1v2 and it’s very likely you die. Also, the support typically has abilities that restrain the enemy’s movement."
                    t "U-uh, s-so the support goes in to restrain the enemy so it's easier to kill? I-I'm kind of confused."
                    mc "That's right!"
                    mc "I thought it would be harder to teach her, but she's learning pretty quickly."
                    jump tiffanyWatchEnd

                label tiffanyWatchEnd:
                    scene bg computer
                    with fade
                    mc "Nice, I won. That game was pretty easy since I got a lot of kills."
                    t "C-can I see the keyboard and mouse for a bit?"
                    mc "Oh? You want to see my settings? It's understandable since I'm so g-"
                    pause
                    mc "{i}Wait a minute...{/i}"
                    mc "{i}W-wha? It shounds like she's typing an essay. What is she-{/i}"
                    mc "!!!" with hpunch
                    mc "{i}Woah, woah, woah. This is the type of stuff that you have to censor heavily, just a bit of pixelating won't cut it.{/i}"
                    show tiffany shy
                    pause(.25)
                    t "A-alright you can hav- MC???"
                    mc "..."
                    mc "{i}Wait, I might get chat restricted.{/i}"
                    t "[mc]???"
                    mc "..."
                    mc "{i}Please don't get chat restricted. I still need to get my rewards.{/i}"
                    t "G-guys, help. I-I think [mc] is-"
                    mc "I-I’m fine. Don’t worry about me. I-I think our training session is done."
                    t "B-but I didn't play yet."
                    mc "I'll watch you play next time."
                    t "O-oh, okay. B-bye."
                    mc "See ya."
                    mc "{i}I need to disable her chat or else she might get banned.{/i}"
                    jump tiffanyTrainingEnd

            label tiffanyTrainingEnd:
                jump endOfTraining

        label maryanneTraining:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Maryanne"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Maryanne"
            elif girlsTalkedTo == 3:
                $ whoThird = "Maryanne"
            show maryanne excited
            pause(.25)
            ma "Hey [mc]! I'm ready to learn the basics of the game!"
            mc "{i}She has a lot of energy.{/i}"
            scene bg computer 
            with fade
            mc "Alright, I'm assumiing you have an account already?"
            show maryanne excited
            pause(.25)
            ma "Yep! My account is called Stan Jae."
            mc "{i}She's a koreaboo?{/i}"
            ma "[mc]? What's wrong?"
            menu:
                "Uh, interesting name.":
                    jump maryanneNameOne
                "is that a kpop singer?":
                    jump maryanneNameTwo
                "I like your name!":
                    jump maryanneNameThree
            
            label maryanneNameOne:
                show maryanne excited
                pause(.25)
                ma "O-oh, I'm not very creative with names."
                mc "He's a member of Day6 right?"
                show maryanne blush
                pause(.25)
                ma "Yea! He's so cute and reminds me of someone."
                mc "{i}Why does it feel so hot in this room?{/i}"
                mc "Hmm, I wonder who...?"
                ma "Isn't it pretty obvious?"
                mc "Uhh, not really... Anyways, we're getting off topic."
                show maryanne neutral
                pause(.25)
                ma "Oh right! What do you want me to do again?"
                jump maryanneNameEnd

            label maryanneNameTwo:
                show maryanne excited
                pause(.25)
                ma "Yeah! He's a member of Day6 and he's super cute."
                mc " I didn't know you were into kpop."
                ma "Oh I love kpop! We should listen to it while you coach me!"
                mc "U-uh, I'm good."
                show maryanne pout
                pause(.25)
                ma "You probably listen to EDM or something."
                mc "{i}EDM is good though...{/i}"
                mc "W-we're getting off topic."
                show maryanne neutral
                pause(.25)
                ma "Oh right! What do you want me to do again?"
                jump maryanneNameEnd

            label maryanneNameThree:
                show maryanne excited
                pause(.25)
                ma "Oh really?! You also listen to kpop?!?"
                mc "Well, I occasionally do. Jae's a member of Day6 right?"
                show maryanne blush
                pause(.25)
                ma "Yea! He's so dreamy, like a certain someone."
                mc "{i}I guess kpop idols are pretty hot...{/i}"
                mc "I guess yo- Huh, what are you staring at?"
                show maryanne flustered
                pause(.25)
                ma "O-oh n-nothing!"
                mc "Ah, forget it. We're getting off topic."
                show maryanne neutral
                pause(.25)
                ma "Oh yea! So what should I do?"
                jump maryanneNameEnd

            label maryanneNameEnd:
                scene bg computer
                mc "Well, you should..."
            menu:
                "Play a PvP Game":
                    jump maryanneTrainingOne
                "1v1 me.":
                    jump maryanneTrainingTwo
                "Watch me play a game.":
                    jump maryanneTrainingThree

            label maryanneTrainingOne:
                show maryanne confused
                pause(.25)
                ma "A PvP game? Don’t I need to learn the game first?"
                mc "Well yes, but you’ll learn faster by playing against other people. Besides, I’ll be helping you so don’t worry."
                show maraynne neutral
                pause(.25)
                ma "If you say so... So do I just press this option?"
                mc "Yep! Then we just wait for a game."
                pause(3)
                ma "Oh! I got a game!"
                mc "Okay so now, type mid to let the other players know where you are going."
                ma "Done! So who should I play? Fang? Synk? Pyre?"
                mc "You like to help impact the map right? Hmm, I think Straight Fate would be a good character to play."
                ma "Hmmm, alright if you say so."
                mc "{i}Now to teach her the basics...{/i}"
                scene bg computer game
                with fade
                mc "{i}Seems like the game is going well right now. She hasn’t died, but is around half health, same with her opponent. It seems they are about to level up and get their ultimate moves. I should tell her to…{/i}"
                menu:
                    "Back off and be careful.":
                        jump maryannePvPOne
                    "Go help another lane.":
                        jump maryannePvPTwo
                    "Help her jungler.":
                        jump maryannePvPThree

                label maryannePvPOne:
                    mc "Hey Maryanne, you should back off and play safer."
                    show maryanne confused
                    pause(.25)
                    ma "Huh? Why do I need to back off? I think I'm doi-"
                    mc "WATCH OUT! The enemy just got his ultimate... I'm pretty sure you're dead."
                    hide maryanne confused
                    "You have been slain."
                    show maryanne neutral
                    pause(.25)
                    ma "Oh, well. I guess I died haha. But why should I back off? Wouldn’t I get my ultimate the same time as him?"
                    mc "Uh, well, his ultimate allows him to do more damage while your ultimate is more of a utility that allows you to impact the map."
                    show maryanne understanding
                    pause(.25)
                    ma "Oooohh, so since my ultimate isn’t good for 1v1 and my opponent’s is, I should be careful when he has it?"
                    mc "That's the gist of it."
                    mc "{i}Wow I'm surprised she got all that from just a simple explanation.{/i}"
                    jump maryannePvPEnd

                label maryannePvPTwo:
                    mc "Maryanne, you should go help another lane."
                    show maryanne confused
                    pause(.25)
                    ma "Do I just start walking to the top lane?"
                    mc "No, no, you just got your ultimate, just use it to instantly travel there and kill the enemy."
                    show maryanne understanding
                    pause(.25)
                    ma "Ohhhh, so like this?"
                    mc "NOT UNDER T-"
                    hide maryanne understanding
                    "You have been slain."
                    "An enemy has been slain."
                    mc "I guess you helped kill the enemy so it’s not the worst that can happen. Just make sure not to teleport into a dangerous spot."
                    show maryanne understanding
                    pause(.25)
                    ma "So basically, my ultimate allows me to make a 1v1 into a 2v1 in favor of my teammate, but if I teleport too far away, I put myself at risk of dying?"
                    mc "Sounds about right."
                    mc "{i}That's what I was going to say next...{/i}"
                    jump maryannePvPEnd
                
                label maryannePvPThree:
                    mc "Hey, your jungler is fighting the enemy jungler, you should go help him. You should use your ultimate to teleport there."
                    show maryanne confused 
                    pause(.25)
                    ma "Do I just click here to teleport?"
                    mc "Yep! Now just kill the enemy jungler."
                    hide maryanne confused
                    "An enemy has been slain."
                    mc "Nice! You should always help your jungler if he’s in trouble. It will allow him to push the tempo and make aggressive plays."
                    show maryanne understanding
                    pause(.25)
                    ma "Ohh, so I should go help my jungler win the 1v1, then go impact somewhere on the map since the enemy won’t know where we’re going to go and their jungler can’t answer it?"
                    mc "Basically yeah."
                    mc "{i}I'm surprised she actually understood all of that.{/i}"
                    jump maryannePvPEnd

                label maryannePvPEnd:
                    scene bg computer 
                    with fade
                show maryanne happy
                pause(.25)
                ma "I can't believe we just won."
                mc "Nice job on winning your first game."
                ma "Well, it was all thanks to you. Nii-chan is such a good coach."
                mc "I can’t just take all the credit. You pulled in yo-Wait, did you just call me-"
                show maryanne flustered
                pause(.25)
                ma "N-NO! I DIDN’T SAY ANYTHING. YOU MUST HAVE HEARD SOMETHING WRONG."
                mc "{i}Why is she so flustered?{/i}"
                mc "I-I guess so… Anyways, we’re running out of time. I’ll review your game at the next meeting."
                ma "O-okay, B-bye [mc]."
                mc "S-see ya."
                mc "{i}I wonder why she was in a hurry to get out of there…{/i}"
                jump maryanneTrainingEnd

            label maryanneTrainingTwo:
                show maryanne shocked
                pause(.25)
                ma "1v1 YOU? Aren’t you way out of my league??"
                mc "Well, I am pretty hot."
                show maryanne blushing
                pause(.25)
                ma "I MEAN IN LL YOU DUMMY!!!"
                mc "Oh. I mean, even if I am way better than you, it’ll help you improve and learn the game much quicker."
                show maryanne pout
                pause(.25)
                ma "Sounds like an excuse to just beat me over and over."
                mc "{i}She's not wrong...{/i}"
                mc "Don't worry, I'll take it easy on you."
                ma "You promise?"
                mc "Yes… Ok so I think you should play Straight Fate. Even though he is better to learn in a PvP game, it should be okay to use him to learn the basics."
                ma "It sounds like you're just making it easier to kill me."
                mc "No, no, no, it's for pract-"
                show maryanne giggle #use smile if image not present
                pause(.25)
                ma "Hehe, I know, I was just messing with you."
                mc "..."
                scene bg computer game
                with fade
                mc "{i}I can’t believe she survived for this long. Well, I guess it makes sense since she was playing so safe. Hmm, maybe I should just…{/i}"
                menu:
                    "Go kill her":
                        jump maryanne1v1One
                    "Wait for a bit, then kill her.":
                        jump maryanne1v1Two
                    "Let her kill me.":
                        jump maryanne1v1Three
                
                label maryanne1v1One:
                    mc "{i}Ok, I'll just walk up and unleash my full combo.{/i}"
                    show maryanne panic
                    pause(.25)
                    ma "[mc], w-what are you doing?"
                    mc "Don't worry about it."
                    ma "Wait I'm going to di-"
                    hide maryanne panic
                    "An enemy has been slain."
                    show maryanne pout
                    pause(.25)
                    ma "Hmph, it seems like you just wanted to bully me…"
                    mc "W-well, you were low on health and you were pretty close so I just thought I can just go in for the kill."
                    show maryanne angry #idk
                    pause(.25)
                    ma "Fight me again! This time, I'll make sure to kill you."
                    mc "That's the spirit!"
                    mc "{i}I swear if I die to her somehow...{/i}"
                    jump maryanne1v1End

                label maryanne1v1Two:
                    mc "{i}Alright, I’m about to level up and unlock my ultimate ability. As soon as I get my ultimate, I’ll go in for the kill.{/i}"
                    show maryanne panic
                    pause(.25)
                    ma "[mc], H-how are you higher level tha- STOP ATTACKING ME!!!"
                    mc "Heh. I just kill the creeps faster tha- also you’re dead."
                    hide maryanne panic
                    "An enemy has been slain."
                    show maryanne pout
                    pause(.25)
                    ma "Heyyyy. You were just bullying me the whole time."
                    mc "U-uh, I just got my ultimate and saw the kill potential, so I went for it."
                    show maryanne angry
                    pause(.25)
                    ma "Fine! 1v1 me again! This time, I'll make sure to win!"
                    mc "Bring it!"
                    m "{i}I like that energy.{/i}"
                    jump maryanne1v1End

                label maryanne1v1Three:
                    mc "{i}SO I should just walk into her turret and let her hit me to get the kill.{/i}"
                    show maryanne confused
                    pause(.25)
                    ma "[mc], why are you just walking up and-"
                    hide maryanne confused
                    "You have been slain."
                    mc "Ah, I guess I died. Oh well."
                    show maryanne pout
                    pause(.25)
                    ma "[mc]~, you’re such a meanie. Why are you looking down on me?"
                    mc "{i}A meanie?{/i}"
                    mc "W-what do you mean...?"
                    ma "You weren't trying at all were you."
                    mc "I-I guess..."
                    mc "I'm sorry."
                    show maryanne angry #or neutral? idk
                    pause(.25)
                    ma "If you’re sorry, you’ll fight me again. Maybe the second time will be just as easy as the first haha."
                    mc "Oh you're going down..."
                    mc "{i}She's going to get destroyed.{/i}"
                    jump maryanne1v1End

                label maryanne1v1End:
                    scene bg computer
                    with fade
                    show maryanne exhausted
                    pause(.25)
                    ma "Ah, I got completely destroyed..."
                    mc "That's to be expected. At least you're learning right?"
                    ma "Yep! I feel like if I go into a PvP game I can beat all the other players. Onii-chan really is the best teacher!"
                    mc "Woah, woah, you’re getting ahead of yours- wait, what did you just call me?"
                    show maryanne flustered
                    pause(.25)
                    ma "OH N-NOTHING! I-I JUST SAID YOU’RE A GOOD TEACHER."
                    mc "{i}Did I mishear her? Ah forget it.{/i}"
                    mc "Owww, my ears..."
                    show maryanne apologetic
                    pause(.25)
                    ma "Oh, sorry for yelling. Anyways, when can I play a PvP game against other people?"
                    mc "Ah, we’re running out of time. Maybe you can play a PvP game at the next meeting."
                    show maryanne smile 
                    pause(.25)
                    ma "Okay! See you!"
                    mc "Later."
                    mc "{i}Man, it's exhausting just talking to her...{/i}"
                    jump endOfTraining

            label maryanneTrainingThree:
                scene bg computer
                show maryanne confused
                pause(.25)
                ma "Watch you play? How is that going to help me?"
                mc "Well, it's easier to explain what I want you to do when you can see it with your own eyes."
                show maryanne slight smile
                pause(.25)
                ma "Oh so you want me to learn based on visual cues?"
                mc "Uhh, I guess?"
                mc "{i}Why did she have to put it in complicated terms...{/i}"
                ma "Okay. I kind of wanted to play myself, but I can learn this way as well."
                pause(1)
                ma "Oh, you got a game."
                mc "Ok, so I'll just type mid to let my team know where I'm going."
                mc "Now who should I play..."
                ma "I think Straight Fate looks cool."
                mc "Really? I was thinking of playing Fang, Pyre or Synk…"
                mc "{i}I really don't want to play Straight Fate...{/i}"
                show maryanne excited
                pause(.25)
                ma "Yeah! Let me watch you play Straight Fate."
                mc "I guess I have no other choice..."
                mc "{i}I wanted to have fun with this game...{/i}"
                scene bg computer game
                with fade
                mc "{i}I should probably explain my thought process, so Maryanne can learn.{/i}"
                mc "{i}I think she'll actually understand quickly.{/i}"
                mc "Listen up, Maryanne. The enemy is killing creeps under tower, and he's low on both mana and health."
                mc "I'm goiing to..."
                menu:
                    "Dive under the tower and go for a kill.":
                        jump maryanneWatchOne
                    "Roam to another lane.":
                        jump maryanneWatchTwo
                    "Help my jungler with a neutral objective.":
                        jump maryanneWatchThree
                
                label maryanneWatchOne:
                    mc "..."
                    "An enemy has been slain."
                    mc "Easy! Did you see that, Maryanne."
                    show maryanne excited
                    pause(.25)
                    ma "Yeah, That was cool!"
                    show maryanne thinking
                    pause(.25)
                    ma "So you figured out that the proportion of the derivative of the combined damage of the enemy and the tower to the derivative of your damage output was…"
                    ma "{cps=*3}smaller than the proportion of your health to his health, right?{/cps}"
                    ma "{cps=*3}I assume that you also realized that he would not have the summoner spell “Flash” yet{/cps}"
                    ma "{cps=*3}because he utilized it 4 minutes and 23 seconds ago, and the cooldown is 5 minutes.{/cps}"
                    show maryanne smile
                    pause(.25)
                    ma "Simple calculations, huh?"
                    mc "Uhh, sure..."
                    mc "{i}I just used my intuition...{/i}"
                    mc "Wait, how do you know all that? Summoner spell cooldowns and all that."
                    ma "Oh, I gathered information from LL-Wiki earlier today."
                    mc "Ah..."
                    mc "{i}Math competitions, huh?{/i}"
                    mc "{i}I'm feeling good about this tournament...{/i}"
                    jump maryanneWatchEnd

                label maryanneWatchTwo:
                    show maryanne excited
                    pause(.25)
                    ma "Oh! That's where you move to a side lane to help your teammates, right?"
                    ma "I read about that."
                    mc "Yeah!"
                    mc "{i}She's so prepared...{/i}"
                    mc "It looks like their bot lane is pushed forward, so I'm going to try to kill them."
                    mc "..."
                    mc "..."
                    "An enemy has been slain."
                    pause(.5)
                    "Double Kill."
                    mc "Nice! See, I sacrificed resources Mid to gain an advantage for myself and my team mates."
                    show maryanne slight smile
                    pause(.25)
                    ma "Yeah, I've seen Baker do that."
                    mc "Y-you already watch Baker? Why are you even watching me, then?"
                    show maryanne smile
                    pause(.25)
                    ma "Oh. Well, Baker is obviously better than you, but I still like to watch you, [mc]."
                    show maryanne looking away
                    pause(.25)
                    ma "After all, I've been watching you for a long time..."
                    mc "E-ehrm, uh, wh-wha!??!" with hpunch
                    show maryanne blush
                    pause(.25)
                    ma "Oh, I meant your replays! I found your account and watched some of your recorded games."
                    mc "A-ah, I see."
                    mc "{i}That's still a little weird...{/i}"
                    jump maryanneWatchEnd

                label maryanneWatchThree:
                    mc "My enemy laner is stuck under tower, so I can create a numbers advantage elsewhere on the map."
                    mc "My Jungler is close, so I’m just going to kill the Dragon with him."
                    mc "..."
                    "You have slain the Fire Dragon."
                    show maryanne excited
                    pause(.25)
                    ma "Great! That’s a 5 percent buff to damage for everyone on the team, right?"
                    mc "Yeah...How do you know that?"
                    show maryanne slight smile
                    pause(.25)
                    ma "I studied a little bit beforehand."
                    mc "{i}Wow... I'm impressed.{/i}"
                    mc "Th-that's good."
                    jump maryanneWatchEnd

                label maryanneWatchEnd:
                    scene bg computer
                    with fade
                    mc "So, was that useful?"
                    show maryanne smile
                    pause(.25)
                    ma "Of course! Onii-chan is such a good teacher!"
                    mc "Uh-, ah, than- Wait, what did you just call me?"
                    show maryanne flustered
                    pause(.25)
                    ma "N-NOTHING, YOU'RE JUST A GOOD TEACHER WAS WHAT I SAID!"
                    mc "Uhhh, thanks I guess."
                    show maryanne blush
                    pause(.25)
                    ma "A-anyways, I'll see you later, [mc]."
                    mc "Bye, Maryanne."
                    mc "{i}She's kind of weird...{/i}"
                    jump maryanneTrainingEnd

            label maryanneTrainingEnd:
                jump endOfTraining
                
        label reginaTraining:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Regina"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Regina"
            elif girlsTalkedTo == 3:
                $ whoThird = "Regina"
            show regina arms crossed
            pause(.25)
            r "Hey dummy, are you here to teach me?"
            mc "Y-yeah, and can you not call me-"
            r "I’ll call you what I want. Besides, are you sure you’re good enough to teach me?"
            mc "Hey! I'll have you know that I am Diamond in this gam-"
            r "Yeah, yeah, whatever, can you start teaching now?"
            mc "..."
            scene bg computer
            with fade
            mc "Well, do you have an account yet?"
            show regina arms crossed
            pause(.25)
            r "Obviously. I just made one yesterday."
            mc "Oh, what's your username? I'll send you a friend request."
            show regina flustered
            pause(.25)
            r "U-uh, i-its kiwik47"
            mc "{i}Her username is cute compared to her normal demeanor...{/i}"
            show regina pout
            pause(.25)
            r "Hey! You have a problem with it?"
            menu:
                "N-no, no problems here.":
                    jump reginaNameOne
                "Uh, why did you name yourself kiwik47?":
                    jump reginaNameTwo
                "Your name is kinda cute...":
                    jump reginaNameThree

            label reginaNameOne:
                show regina arm crossed 
                pause(.25)
                r "Good."
                mc "But why-"
                r "It's because I like kiwis and cats. OKAY!? No more questions about my name."
                mc "U-understood."
                show regina neutral
                pause(.25)
                r "So what are we doing today?"
                jump reginaNameEnd

            label reginaNameTwo:
                show regina arms crossed
                pause(.25)
                r "It's not like you will understand or anything."
                mc "But we're a team no-"
                show regina glare
                pause(.25)
                r "Does that mean I need to tell you everything about me?"
                mc "W-well no but-"
                r "If you really want to know, it's because I like cats and kiwis. Now no more personal questions."
                mc "O-okay."
                show regina neutral
                pause(.25)
                r "You still haven't told me what we're doing."
                jump reginaNameEnd

            label reginaNameThree:
                show regina flustered
                pause(.25)
                r "Uagh, i-it's not like I-i tried to m-make it cute."
                mc "What made you make such a cute-"
                show regina annoyed
                pause(.25)
                r "Shut up. I didn’t try to make it cute. I just like cats and kiwis so I combined the two."
                mc "Ooh, I also like c-"
                r "Stop talking. I don’t want to share any similar qualities with an idiot like you."
                mc "W-wait, what's wrong with-"
                r "We’re getting off topic. What are we going to do?"
                jump reginaNameEnd

            label reginaNameEnd:
                mc "Oh, right. We should..."
            menu:
                "Go into a PvP game.":
                    jump reginaTrainingOne
                "Play some 1v1s.":
                    jump reginaTrainingTwo
                "Have you watch me for a bit.":
                    jump reginaTrainingThree
            
            label reginaTrainingOne:
                show regina frown
                pause(.25)
                r "PvP?"
                r "Shouldn't I be practicing against bots first?"
                mc "Most players do, but we need to improve quickly and I think the best way to do that is by jumping straight into matches."
                r "Hmph. I see..."
                scene bg computer
                show regina neutral
                pause(.25)
                r "So you want me to hit this option here?"
                mc "Yep."
                mc "{i}When it comes to learning, she's surprisingly compliant.{/i}"
                mc "Oh, you got a g-"
                show regina annoyed
                pause(.25)
                r "I'm not blind. So do I just click accept?"
                mc "Yep and make sure to claim top."
                show regina evil smile
                pause(.25)
                r "Oh, I always do."
                mc "And make sure to... wait what?"
                r "Shut up."
                mc "..."
                mc "Anyways you should pick Rak."
                show regina neutral
                pause(.25)
                r "Hmm, maybe I will, maybe I won't."
                mc "..."
                mc "{i}I hate this girl.{/i}"
                scene bg computer game
                with fade
                mc "{i}Ok so Regina plays very aggressively and has reduced the enemy to 20 percent health. I’m surprised she hasn’t died yet. I should tell her to…{/i}"
                menu:
                    "Go for the kill.":
                        jump reginaPvPOne
                    "Play safer.":
                        jump reginaPvPTwo
                    "Tell the jungler to come.":
                        jump reginaPvPThree
                
                label reginaPvPOne:
                    mc "Hey Regina, you should go in and ki-"
                    show regina annoyed
                    pause(.25)
                    r "Can't you see I'm tryi- HEY! WHY IS THE JUNGLER HERE!?"
                    mc "{i}Oh I forget to tell her that she was too far up. Well she’s dead.{/i}"
                    mc "Oh, you're so dead."
                    hide regina annoyed
                    "You have been slain."
                    show regina angry
                    pause(.25)
                    r "Hmph, I should've killed him."
                    mc "Well you need to make sur-"
                    r "I know, I know. I need to make sure I go fast before the enemy jungler comes."
                    mc "Uh, yea..."
                    mc "{i}That's not what I was going to say but I guess it works.{/i}"
                    jump reginaPvPEnd

                label reginaPvPTwo:
                    mc "Regina, stop being so far up. You need to-"
                    show regina angry
                    pause(.25)
                    r "Shut up. I'm going to kil- HEY! WHY IS THE JUNGLER HERE!?"
                    mc "{i}And this is why I told her to stay back. Now she gets punished for it.{/i}"
                    mc "Well you're dead now."
                    hide regina angry
                    "You have been slain."
                    show regina angry
                    pause(.25)
                    r "Grr, I would've killed him if the jungler didn't come."
                    mc "This was why I wanted you to stay back. Now the game is go-"
                    r "Hmph, you would've still died."
                    mc "{i}I would've just outplayed them. Their coordination was awful.{/i}"
                    mc "Well, I wouldn't be putting myself in dange-"
                    r "Shut up, I already understand. Kill them faster before the enemy jungler comes."
                    mc "uhh, sure."
                    mc "{i}Uh, that was not what I was trying to say, but whatever works.{/i}"
                    jump reginaPvPEnd

                label reginaPvPThree:
                    mc "Regina, tell your jungler to co-"
                    show regina annoyed
                    pause(.25)
                    r "No need. I'm about to kill hi- WHY IS HE HERE!?"
                    mc "{i}And this is why I wanted her to tell the jungler to come.{/i}"
                    mc "You are so dead."
                    hide regina annoyed
                    "You have been slain."
                    show regina angry
                    pause(.25)
                    r "That's not fair. He asked for help."
                    mc "Well, I did say to tell your jungler to come."
                    r "Hmph, I will admit you were right for once."
                    mc "{i}For once?{/i}"
                    mc "Ok, so now you shou-"
                    show regina evil smile
                    pause(.25)
                    r "Shut up, I know what I'm doing now. I'll just kill him before the jungler comes."
                    mc "Um, yea..."
                    mc "{i}She is way off the mark of what I was saying...{/i}"
                    jump reginaPvPEnd

                label reginaPvPEnd:
                    show regina happy
                    pause(.25)
                    r "Nice, I won, this game is so easy."
                    mc "Congrats. But uh, you died 12 times."
                    show regina annoyed
                    pause(.25)
                    r "Shut up, the enemy just got more help than me."
                    mc "Well you shouldn't be in tha-"
                    r "Hmph, I still won, isn't all that matters?"
                    mc "{i}She's not wrong...{/i}"
                    mc "Er, well yeah, but you still made a lot of mistakes."
                    r "And aren't you supposed to tell me what I did wrong and review the game with me?"
                    mc "Well, we're running out of time. I'll go over your game next meeting."
                    show regina arms crossed
                    pause(.25)
                    r "Whatever, if you got nothing helpful to say, scram."
                    mc "B-b-bye."
                    mc "{i}She's scary...{/i}"
                    jump reginaTrainingEnd

            label reginaTrainingTwo:
                show regina evil smile
                pause(.25)
                r "1v1? You mean I get to beat you over and over again?"
                mc "Uh, the point is to teach you the core gameplay."
                r "Whatever, are you ready to lose?"
                mc "Hey, you should play Rak, I think it sui-"
                show regina annoyed
                pause(.25)
                r "Don't tell me what to do, baka."
                mc "O-oh, okay..."
                r "Luckily for you, I was planning to choose him anyways."
                mc "Anyways, ready to lose?"
                r "HEY! That's my line."
                scene bg computer game
                with fade
                mc "{i}Why does she play so aggressively? She already lost so much health attacking me but she did a lot of damage to me. Maybe I should-{/i}"
                menu:
                    "Go in for the kill.":
                        jump regina1v1One
                    "Let her make a mistake and die.":
                        jump regina1v1Two
                    "Let her kill me.":
                        jump regina1v1Three

                label regina1v1One:
                    mc "{i}Alright, I just unleash my full combo when she walks up...RIGHT NOW!{/i}"
                    show regina shocked
                    pause(.25)
                    r "WOAH! You're finally starting to attack me now? WAIT, NO STAY BACK!"
                    hide regina shocked
                    "An enemy has been slain."
                    mc "NOT EVEN CLOSE!"
                    mc "{i}If she used any attack on me, I would have died.{/i}"
                    show regina anger
                    pause(.25)
                    r "GRR. You got lucky there and surprised me. Fight me again. This time I'll make sure I kill you."
                    mc "HAH. Bring it on."
                    mc "{i}Man it feels good to kill her.{/i}"
                    jump regina1v1End

                label regina1v1Two:
                    mc "{i}She's going to throw an ability there, so I just need to make sure I dodge it and...{/i}"
                    mc "Woah!"
                    show regina annoyed 
                    pause(.25)
                    r "You're boring. If you're not going to come to me, I'll just come to-"
                    hide regina annoyed
                    "An enemy has been slain."
                    mc "Uh, seems like you died."
                    show regina pout
                    pause(.25)
                    r "HEY! IT's NOT FAIR. Your turret killed me."
                    mc "Well, the turret is part of the game."
                    r "Whatever. Fight me again, this time I'll make sure you die."
                    mc "Ha, make sure you don't die to turret again."
                    show regina angry
                    pause(.25)
                    r "GRR!!!"
                    jump regina1v1End
                
                label regina1v1Three:
                    mc "{i}I'll just walk up and let her hit me and die to turret.{/i}"
                    show regina annoyed
                    pause(.25)
                    r "Why aren't you trying to dodge anything?"
                    hide regina annoyed
                    "You have been slain."
                    mc "Oh, I died."
                    show regina angry
                    pause(.25)
                    r "HEY! You didn't even try to fight back."
                    show regina pout
                    pause(.25)
                    r "Do you think I'm that bad?"
                    mc "N-no..."
                    show regina angry
                    pause(.25)
                    r "Liar!"
                    mc "F-fine, I'll take you seriously this time."
                    r "Hmph, I don't believe you."
                    mc "Wha-"
                    mc "{i}I don't understand this girl.{/i}"
                    jump regina1v1End
                                    
                label regina1v1End:
                    scene bg computer
                    with fade
                    mc "Seems like I won."
                    show regina angry
                    pause(.25)
                    r "Grr, it's not like you're better than me or anything."
                    mc "Uh, I am pretty sure I am better."
                    r "Shut up."
                    mc "Y-yes ma'am."
                    show regina neutral
                    pause(.25)
                    r "Anyways, when are you going to review the game with me?"
                    mc "Oh, I was planning on doing that at the next meeting."
                    mc "{i}I'm a little scared of her right now.{/i}"
                    show regina arms crossed
                    pause(.25)
                    r "Ok then. Bye. I don't want to talk to you anymore if you got nothing to say."
                    mc "U-uh bye."
                    mc "{i}Ok, I am very scared of her right now.{/i}"
                    jump reginaTrainingEnd

            label reginaTrainingThree:
                show regina annoyed
                pause(.25)
                r "Watch you? Ugh, it's going to be so boring..."
                mc "I'm pretty sure you're going to learn a lot by wat-"
                r "Yeah, yeah, whatever, you got a game by the way."
                mc "Alright, I'm just going to tell my teammates that I'm top."
                mc "Hmm, now for which character to play."
                show regina neutral
                pause(.25)
                mc "Huh? I was going to pic-"
                r "I don't care, pick Rak, he looks cool."
                mc "{i}Ugh, I hate playing this character.{/i}"
                mc "Fine, I guess I have no choice."
                scene bg computer game
                with fade
                mc "{i}This game is so boring. I already explained everything I am doing and no team has a kill yet. Maybe I should just -{/i}"
                menu:
                    "Go in for the kill.":
                        jump reginaWatchOne
                    "Back off and wait.":
                        jump reginaWatchTwo
                    "Tell the jungler to come.":
                        jump reginaWatchThree

                label reginaWatchOne:
                    mc "Ok, I will just go in an-"
                    show regina neutral
                    pause(.25)
                    mc "{i}Shoot, I forgot about the enemy jungler.{/i}"
                    mc "Well, I have to try to outplay this then."
                    hide regina neutral
                    "You have been slain."
                    "An enemy has been slain."
                    "Double Kill."
                    mc "Nice! Ok Regina, if the enemy jungler comes but you manage to kill bo-"
                    show regina neutral
                    pause(.25)
                    r "Yeah, I saw. I guess you're better than what I initially thought."
                    mc "{i}Wha?{/i}"
                    mc "Uh, what I'm trying to say is that if you ca-"
                    r "I already understand. If I can kill both of them, even if I die, it's very good for me and the team."
                    mc "That's uh, spot on."
                    mc "{i}I'm surprised she already understood everything.{/i}"
                    jump reginaWatchEnd
                
                label reginaWatchTwo:
                    mc "Here I shouldn't keep fighting bec-"
                    show regina confused
                    pause(.25)
                    r "Why are you backing off when you can just kill him? You're being stupid."
                    mc "Well I see the enemy jungler nearby. If I go in right now, I could die. So I'm just going to wait and... attack now!"
                    hide regina confused
                    "First blood."
                    mc "See, by waiting for the enemy jungler to leave, it made it less ris-"
                    show regina arms crossed
                    r "Hmph, can't you just try to kill the jungler if he comes."
                    mc "{i}Huh?{/i}"
                    mc "I mean, yeah, but it's riskier because I have a chance to die without getting a kill."
                    r "Oh so you're just a scaredy cat?"
                    mc "W-w-what? I'm j-"
                    r "Haha, you should've seen your face. You're so dumb, I was obviously just messing with you. You just want to reduce the risks of outside variables right?"
                    mc "Y-yeah, that's right."
                    mc "{i}She actually understood everything?!?!{/i}"
                    jump reginaWatchEnd

                label reginaWatchThree:
                    mc "Alright, I'm just going to tell my jungler to come help."
                    show regina confused
                    pause(.25)
                    r "Huh? Why ask for help when you can kill him by yourself?"
                    mc "Well, it's highly likely the enemy jungler is here and it's easier to fight a 2v2 than an 1v2. Now that he's here, we can..."
                    hide regina confused
                    "An enemy has been slain."
                    "Double kill."
                    mc "Easy! See? It was less risky by making it a 2v2."
                    show regina confused
                    pause(.25)
                    r "Hmph, I sweared you can just kill both of them by yourself."
                    mc "W-well yea, but 2v-"
                    show regina understanding
                    pause(.25)
                    r "Yeah, whatever, I guess if you die and don't get a kill, the game just becomes harder to play?"
                    mc "Yes..."
                    mc "{i}That's what I was saying!!!{/i}"
                    jump reginaWatchEnd    
                
                label reginaWatchEnd:
                    scene bg computer
                    mc "Well, that was an easy win."
                    show regina annoyed
                    pause(.25)
                    r "Ughhh. That was so boring to watch."
                    mc "Didn't you learn anything?"
                    r "Eh, I guess, but still, I want to play."
                    mc "U-uh, unfortunately, we are running out of time."
                    r "Grr, I really wanted to play. Well, whatever, I guess you were useful for a bit. Now that you got nothing more useful to say, get out of my sight."
                    mc "G-goodbye."
                    mc "{i}I swear I was more than just a bit useful. But I’m never saying that to her face. She terrifies me.{/i}"
                    jump reginaTrainingEnd
            
            label reginaTrainingEnd:
                jump endOfTraining
                    

        label kristellaTraining:
            $ kristellaCute = 0
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Kristella"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Kristella"
            elif girlsTalkedTo == 3:
                $ whoThird = "Kristella"
            show kristella giggle
            pause(.25)
            kr "Hey again, [mc]. It's good to see that you've calmed down."
            mc "Y-yea... Anyways, are you ready?"
            show kristella smile
            kr "Of course! Where should we start?"
            mc "Let's head over to the library."
            scene bg computer
            with fade
            show kristella smile
            pause(.25)
            kr "So, how are you going to train me, [mc]?"
            mc "Well first, we'll need to make you an account. What username are you using?"
            kr "Hmm... I think I'll go with Krisquish."
            mc "I l-like that..."
            show kristella giggle
            pause(.25)
            kr "Hehe, it's just my name but squishy~"
            mc "It f-fits you. And I think it's, um, cute."
            show kristella eyes looking up
            pause(.25)
            kr "Aww, [mc]... Are you calling me cute?"
            menu:
                "N-no! That's not what I meant!":
                    jump kristellaNameOne
                "Yeah, I did. And I mean it.":
                    jump kristellaNameTwo
                "Umm... maybe?":
                    jump kristellaNameThree
            
            label kristellaNameOne:
                $ kristellaCute = 1
                show kristella giggle
                pause(.25)
                kr "Hehe~ [mc], I'm just messing with you."
                mc "Oh… y-yea, I, um, knew that…"
                show kristella smile
                pause(.25)
                kr "Oh, I'm sure you did. But you meant it, right?"
                mc "B-bu, I th-th-"
                show kristella laugh
                pause(.25)
                kr "I got you again!"
                mc "F-fine… Let’s just get into the game."
                show kristella excited
                pause(.25)
                kr "Right! What are we doing?"
                jump kristellaNameEnd

            label kristellaNameTwo:
                $ kristellaCute = 2
                mc "Ehr, um - y- , a-a …"
                mc "{i}T-that’s not what I meant to say...{/i}"
                show kristella pout
                pause(.25)
                kr "Hmph. You shouldn’t have said it if you didn’t mean it, [mc]."
                mc "N-no! Of course I muh-meant it!"
                mc "I totally think you’re, ah, c-cute..."
                mc "{i}Oh no... what have I gotten myself into?{/i}"
                show kristella smile
                pause(.25)
                kr "Oh. I was kidding, but that's really sweet of you to say."
                kr "And I think you're kind of cute, too~"
                mc "Wh-what?!?!?!?!" with hpunch
                show kristella giggle
                pause(.25)
                kr "Hehe! But we should start training, right?"
                mc "R-right."
                jump kristellaNameEnd
            
            label kristellaNameThree:
                $ kristellaCute = 3
                show kristella thinking
                pause(.25)
                kr "Hmm... If you’re not sure, then it’s up to me."
                show kristella smile
                pause(.25)
                mc "Wh-what do you mean?"
                kr "You won't tell me what you mean, so I've chosen how to interpret it."
                mc "Oh. I see..."
                mc  "W-well, what's the verdict?"
                show kristella giggle
                pause(.25)
                kr "I'm not telling you, unless you tell me."
                mc "{i}I need to know...{/i}"
                mc "F-fine... I th-think you're c-cute..."
                show kristella laugh
                pause(.25)
                kr "Hehe ~ you admit it! The court declares you guilty!"
                kr "Your sentence is one training session with me. Do you accept?"
                mc "Y-yes, your honor..."
                show kristella giggle
                pause(.25)
                kr "What will we be doing first, prisoner?"
                jump kristellaNameEnd

            label kristellaNameEnd:
                mc "I think we should..."

            menu:
                "Start with a couple 1v1s.":
                    jump kristellaTrainingOne
                "Hop straight into a PvP game.":
                    jump kristellaTrainingTwo
                "Have you watch me for a bit.":
                    jump kristellaTrainingThree

            label kristellaTrainingOne:   
                show kristella giggle
                pause(.25)
                kr "Ooh ~ 1 on 1? That sounds fun!"
                mc "R-right, er... it'll h-help you understand the core gameplay."
                show kristella excited
                pause(.25)
                kr "I'm excited! Let's get right into it."
                scene bg computer game
                with fade
                show kristella excited
                pause(.25)
                kr "Wow! There are so many characters to choose from! Who are we going to play, [mc]?"
                mc "Hmm... you're the support, so let's go with Luna."
                show kristella abashed
                pause(.25)
                kr "Ok ~ Also, promise me one thing."
                mc "Um sure, what is it?"
                kr "Promise that you won't make fun of me if I don't do well."
                mc "{i}Wha-? She's usually so confident.{/i}"
                mc "{i}But this side of her is kind of cute...{/i}"
                mc "Ehr, no! Of course I won't. But the same goes for you."
                show kristella giggle 
                pause(.25)
                kr "Hehe ~ thanks, MC. But wait… are you scared to lose?"
                mc "Ah - well, not really… I am a Diamond player facing a total noob, after all."
                show kristella laugh
                pause(.25)
                kr "What’d you call me?!? Oh, you’d better pray that you don’t lose now!"
                mc "Hmph. The game's starting, so we'll find out soon enough, won't we?"
                show kristella focused
                pause(.25)
                kr "You bet!"
                scene bg computer game
                with fade
                mc "{i}It's been 5 minutes, and I still haven't managed to kill her...{/i}"
                mc "{i}She’s better than expected, but she’s still pretty low on health.{/i}"
                mc "{i}I’m getting bored… What should I do?{/i}"
                menu:
                    "Go all-in.":
                        jump kristella1v1One
                    "Be passive and patient.":
                        jump kristella1v1Two
                    "Let her kill me.":
                        jump kristella1v1Three
                
                label kristella1v1One:
                    mc "{i}Okay, so I'll jump in and use my full combo to finish her off.{/i}"
                    mc "{i}Three...Two...One...{/i}"
                    show kristella panic
                    pause(.25)
                    kr "Ahh! [mc] wh-what are you doing! S-stop it!"
                    hide kristella panic
                    "You have been slain."
                    show kristella neutral
                    pause(.25)
                    kr "..."
                    mc "Wha-? No! This can't be!" with hpunch
                    mc "I-I- died to the tower..."
                    show kristella laugh
                    pause(.25)
                    kr "Hehe ~ I win! Call me a noob again, [mc]!"
                    mc "F-fine. I’m the noob. But please don’t tell anyone…"
                    show kristella wink
                    pause(.25)
                    kr "Okay,  it’ll be our little secret."
                    show kristella giggle
                    pause(.25)
                    kr "But in return, you have to call me “the noobslayer” from now on."
                    mc "Th-thanks, Kristella - um, the noobslayer..."
                    kr "I’m kidding! You don’t actually have to call me that."
                    show kristella eyes looking unplayable
                    pause(.25)
                    kr "But I did well, right? Are you proud of me, [mc]?"
                    mc "Y-yeah, you did great! But I want a rematch!"
                    show kristella smile
                    pause(.25)
                    kr "Okay~"
                    jump kristella1v1End

                label kristella1v1Two:
                    mc "{i}Alright. No need to rush, right? I'll just take it sl-{/i}"
                    mc "W-wha!?!"
                    show kristella laugh
                    pause(.25)
                    kr "Ha! You wouldn't go in, so I decided-"
                    hide kristella laugh
                    "An enemy has been slain."
                    show kristella smile
                    pause(.25)
                    kr "Hmph. It was worth a try."
                    mc "{i}What was that?? I won, but it was really close...{/i}"
                    mc "Haha... N-not even c-close, noob!"
                    show kristella giggle
                    pause(.25)
                    kr "Oh? Why are you sweating, then?"
                    mc "W-what are you ta-... F-fine. It was kind of scary."
                    kr "Hehe! I know~ You didn't expect me to come onto you like that, right?"
                    mc "Ehr, ah , d-d-definitely not.  L-let's just get back to practice, okay?"
                    kr "Of course!"
                    jump kristella1v1End

                label kristella1v1Three:
                    mc "{i}I'll just run it under the tower and let her kill me… It’ll be good for her confidence, right?{/i}"
                    show kristella surprised
                    pause(.25)
                    kr "[mc]? W-why are you doing that?"
                    mc "Me? Doing what?"
                    hide kristella surprised
                    "You have been slain."
                    show kristella pout
                    pause(.25)
                    "Hmph. You're taking it easy on me, aren't you?"
                    mc "Haha n-no, why would I do that?"
                    if kristellaCute == 1:
                        kr "Tell me the truth, [mc]."
                        mc "Alright, I let you win..."
                        show kristella patty eyes
                        pause(.25)
                        kr "Oh, so you lied earlier, didn't you?"
                        mc "Ah, I mean, yeah. I did let you win..."
                        show kristella blush
                        pause(.25)
                        kr "No - not that, silly~"
                        mc "W-what do you mean, then?"
                        show kristella giggle
                        pause(.25)
                        kr "You - you do think I’m cute ~ don’t you? Why else would you let me win, [mc]?"
                        mc "U-uh, e-... Fine. I th-think you're cute..."
                        show kristella smile
                        pause(.25)
                        kr "I knew it! I like it when you’re honest, MC."
                        show kristella blush
                        pause(.25)
                        kr "And... I think you're kind of cute as well."
                        with hpunch
                        mc "A-aha, c-coo,... excuse me for a bit..."
                        show kristella laugh
                        pause(.25)
                        kr "Hehe, okay ~ hurry up, so I can beat you for real!"
                        mc "O-of cou-course..."
                    elif kristellaCute == 2:
                        kr "I can tell that you didn't try."
                        kr "Hmph. I know how you feel, but that doesn’t mean that you should take it easy on me..."
                        mc "Oh. Sorry..."
                        show kristella mischievous smile
                        pause(.25)
                        kr "Hm... I know exactly how you can make it up to me."
                        mc "Oh, what's that?"
                        show kristella giggle
                        pause(.25)
                        kr "Call me cute again."
                        with hpunch
                        mc "B-bu, uh-, aa..."
                        show kristella laugh
                        pause(.25)
                        kr "Hehe~ I'm just kidding, [mc]."
                        mc "Oh..."
                        show kristella smile
                        pause(.25)
                        kr "There is something that you can actually do, though. Come back here and play again!"
                        kr "And actually try this time: I’m not scared of a challenge!"
                        mc "You got it."
                    elif kristellaCute == 3:
                        kr "You were probably tired of the game or something..."
                        mc "O-okay, I admit it..."
                        show kristella giggle
                        pause(.25)
                        kr "Hehe ~ I thought you would’ve learned your lesson with admitting your crimes!"
                        show kristella wink
                        pause(.25)
                        kr "I’m lengthening your sentence, but I’ll let you out on good behavior~"
                        mc "N-not again... I mean, uh, yes, your honor!"
                        show kristella giggle
                        pause(.25)
                        kr "Good. Now play again!"
                        mc "R-right away..."
                    jump kristella1v1End
                
                label kristella1v1End:
                    scene bg computer
                    with fade
                    mc "Okay, I think we can stop here. Good job, Kristella."
                    show kristella giggle
                    pause(.25)
                    kr "It was so much fun! Let's do it again soon! Okay, [mc]?"
                    mc "Right. See you."
                    kr "Bye!"
                    jump kristellaTrainingEnd

            label kristellaTrainingTwo:
                show kristella surprised
                pause(.25)
                kr "W-wha? Are you sure?"
                mc "Yeah. Bot lane is a duo-lane, so as a Support, you need to learn to work with your ADC."
                show kristella nervous
                pause(.25)
                kr "O-okay..."
                mc "Kristella...are you nervous?"
                kr "Yeah... I'm a little scared."
                mc "What? You’re normally so confident..."
                kr "But I've never done this before."
                mc "Well, don't worry. I'm right here to guide you."
                kr "Promise?"
                mc "I promise."
                kr "R-right. Let's do this then."
                mc "Click on play, then join the queue."
                show kristella neutral
                pause(.25)
                kr "Okay... Oh, I got a match!"
                mc "Accept and type in chat 'sup'."
                show kristella confused
                pause(.25)
                kr "Sup? Is this the LL way to greet your team-mates?"
                mc "Haha - no, you noob. You're claiming your role."
                if kristellaCute == 1:
                    show kristella giggle
                    pause(.25)
                    kr "Aww, noob - that's a term of endearment, right?"
                    mc "...You can't fool me again."
                    show kristella laugh
                    pause(.25)
                    kr "Oh? He's learning!"
                elif kristellaCute == 2:
                    show kristella pout
                    pause(.25)
                    kr "Hmph. Don’t call me a noob when I haven’t even shown you my skills yet."
                    mc "Alright, let's see it then."
                elif kristellaCute == 3:
                    show kristella laugh
                    pause(.25)
                    kr "Noob? Is that how you address me, prisoner?"
                    mc "N-no, your honor. Please continue with your game..."
                    kr "That's what I thought."
                pause(2)
                show kristella questioning
                pause(.25)
                kr "Wait, there are so many characters. Who do I pick?"
                mc "Let's see... your ADC picked Sumeera, so I'd choose Luna for the synergy."
                kr "Synergy?"
                show kristella smile
                pause(.25)
                kr "Oh, I know what you mean."
                kr "Our characters work well together, right?"
                mc "Yeah, exactly."
                show kristella questioning
                pause(.25)
                kr "What do we do now?"
                mc "We're just waiting for the game to start."
                show kristella concerned
                pause(.25)
                kr "Okay...[mc]?"
                mc "Yeah?"
                show kristella slight smile
                pause(.25)
                kr "Remember your promise."
                mc "Of course."
                scene bg computer game
                with fade
                mc "{i}Hmm. it’s been six minutes, and nothing has really happened...{/i}"
                mc "{i}It seems like she’s starting to understand the basics, though.{/i}"
                mc "Good job, Kristella. I think you're st-"
                show kristella panic
                pause(.25)
                kr "[mc], help me! They're attacking!"
                mc "Stay calm. You should..."
                menu:
                    "Fight back.":
                        jump kristellaPvPOne
                    "Run away!":
                        jump kristellaPvPTwo

                label kristellaPvPOne:
                    show kristella focused
                    pause(.25)
                    kr "Okay! We're going in!"
                    "..."
                    hide kristella focused
                    "An enemy has been slain."
                    pause(1)
                    "Double Kill."
                    mc "Nice job!"
                    show kristella excited
                    pause(.25)
                    kr "Yay ~ we did it!"
                    mc "Yeah, keep going."
                    jump kristellaPvPEnd

                label kristellaPvPTwo:
                    show kristella scared
                    pause(.25)
                    kr "Alright! Ahh ~ run, run!"
                    "..."
                    hide kristella scared
                    "You have been slain"
                    pause(1)
                    "Enemy double kill."
                    show kristella disappointed
                    pause(.25)
                    kr "..."
                    mc "D-don't worry about it, Kristella. It was a nice try..."
                    show kristella slight smile
                    pause(.25)
                    kr "Yeah... we'll get them next time!"
                    mc "Definitely."
                    jump kristellaPvPEnd

                label kristellaPvPEnd:
                    scene bg computer
                    with fade
                    mc "Good work today, Kristella. You really learned a lot."
                    show kristella smile
                    pause(.25)
                    kr "Thanks, [mc]. You're a good teacher..."
                    if kristellaCute == 3:
                        show kristella giggle
                        pause(.25)
                        kr "I think this is enough to warrant release for good behavior."
                    show kristella smile
                    pause(.25)
                    kr "I'll see you later, [mc]."
                    mc "Bye."
                    mc "{i}She's going to be a good support...{/i}"
                    jump kristellaTrainingEnd

            label kristellaTrainingThree:
                show kristella smile
                pause(.25)
                kr "Sounds good! I can learn a lot by watching since you’re pretty good , right?"
                mc "I'm Diamond, so I'm in the top one percent of players."
                kr "Wow! That's pretty impressive, [mc]."
                show kristella nervous
                pause(.25)
                kr "Also, it's probably better this way..."
                mc "Hm? What do you mean?"
                kr "Well, I'm a little nervous to play by myself..."
                mc "{i}Huh? She's always so confident...{/i}"
                kr "It's just that, um- I've never done this before."
                mc "Hmm... If that's the case, then would you feel better playing your first game with me?"
                mc "I’ll be by your side the whole time."
                if kristellaCute == 1:
                    show kristella patty eyes
                    pause(.25)
                    kr "Aww, you want me by your side?"
                    mc "Eh-ehr, y-yeah, I think it’d be good."
                    show kristella smile
                    pause(.25)
                    kr "Okay, it's decided then. Let's do this!"
                    mc "Right."
                elif kristellaCute == 2:
                    show kristella smile
                    pause(.25)
                    kr "Oh…  I’d really like that. I think we’d do well together, don’t you?"
                    mc "Uh... y-yeah. L-let's do it."
                    show kristella giggle
                    pause(.25)
                    kr "Wait, why are you nervous now, [mc]?"
                    mc "O-oh, it's nothing..."
                elif kristellaCute == 3:
                    show kristella giggle
                    pause(.25)
                    kr "You know what? A game together would fulfill your sentence, prisoner."
                    mc "Coming right up, your honor."
                    kr "Hehe~"
                scene bg computer game
                with fade
                mc "You're a support player, so I'm going to play ADC with you in the bot lane."
                mc "I’ll play Sumeera. Do any of these characters stand out to you?"
                show kristella excited
                pause(.25)
                kr "Yeah! I like the one with the light blue shield."
                mc "Ah, that's Luna. Good choice. She works really well with my character."
                show kristella head tilt slight smile #uh idk if we hv this
                pause(.25)
                kr "Why's that?"
                mc "Oh, our characters have synergy. Our abilities enhance each other’s strengths."
                if kristellaCute == 1:
                    show kristella patty eyes
                    pause(.25)
                    kr "Hm… just like real life, right?"
                    with hpunch
                    mc "A-ah, oh! Look, we’re in game, haha..."
                elif kristellaCute == 2:
                    show kristella giggle
                    pause(.25)
                    kr "Wow ~ I can't wait to play with you, [mc]!"
                    mc "W-well, the game's starting..."
                elif kristellaCute == 3:
                    show kristella giggle
                    pause(.25)
                    kr "Hmph. Who would have thought? A prisoner and a judge working together..."
                    mc "Haha, the game's starting now."
                scene bg computer game
                with fade
                mc "{i}Hmm...our characters are about to hit level three, but our enemies have more HP than us...{/i}"
                mc "{i}What should we do?{/i}"
                menu:
                    "Use everything and go all in.":
                        jump kristellaWatchOne
                    "Ask Kristella what to do.":
                        jump kristellaWatchTwo
                    "Run away.":
                        jump kristellaWatchThree
                
                label kristellaWatchOne:
                    mc "Kristella, let’s use everything to fight them!"
                    show kristella excited
                    pause(.25)
                    kr "Okay. Go, I'm on top of them!"
                    mc "Oh, nice! I'm coming!"
                    hide kristella excited
                    pause(.5)
                    "An enemy has been slain."
                    pause(1)
                    "Double kill."
                    show kristella laugh
                    pause(.25)
                    kr "Ohh, MC ~ that felt good… We did it!"
                    mc "Yeah, nice job, Kristella!"
                    jump kristellaWatchEnd

                label kristellaWatchTwo:
                    show kristella panic
                    pause(.25)
                    kr "U-uh, l-let’s fight, right?"
                    mc "Okay, going in!"
                    kr "..."
                    show kristella disappointed
                    pause(.25)
                    kr "Oh, they're running away..."
                    mc "Ha! They're scared!"
                    show kristella giggle
                    pause(.25)
                    kr "Hehe ~ scaredy-cats!"
                    mc "We'll get them next time."
                    kr "Right."
                    jump kristellaWatchEnd

                label kristellaWatchThree:
                    mc "I don't like the way the enemy is positioning..."
                    mc "Kristella, let's run!"
                    show kristella panic
                    pause(.25)
                    kr "Oka- Ah! MC, help ~ there’s someone else on me!"
                    mc "I knew it... their Jungler is ganking us!"
                    mc "Hey, get off of her Boomumu!"
                    pause(.5)
                    "An enemy has been slain."
                    show kristella excited
                    pause(.25)
                    kr "Oh... nice!"
                    mc "Yeah. We drew their jungler to ur lane, and we killed him."
                    mc "Good job, Kristella."
                    show kristella smile
                    pause(.25)
                    kr "Thanks, you too."
                    jump kristellaWatchEnd

                label kristellaWatchEnd:
                    scene bg computer
                    with fade
                    show kristella giggle
                    pause(.25)
                    kr "Wow~ That was so fun, [mc]!"
                    kr "We should play together again sometime."
                    mc "Of course. Did you add me as a friend?"
                    kr "Yep. XtremeDragonSlayer, right?"
                    mc "{i}Why did she have to say it out loud...{/i}"
                    mc "Yeah..."
                    show kristella smile
                    pause(.25)
                    kr "Okay, see you soon, [mc]."
                    mc "Lata, Kristella."
                    jump kristellaTrainingEnd
  
            label kristellaTrainingEnd:
                jump endOfTraining       

        label endOfTraining:
            if girlsTalkedTo == 4:
                mc "Oh wait, we should head back."
                scene bg clubroom
                with fade                
            else:
                scene bg clubroom
                mc "{i}Who should I talk to next?{/i}"
        
    show kelvin smile
    pause(.25)
    kel "Oh look, they're back."
    mc "Hey, everyone. Great job today - I think we really made some progress."
    show kelvin excited
    pause(.25)
    kel "Yep, definitely!"
    hide kelvin excited
    show regina evil smile
    pause(.25)
    r "I'm going to be even better next time."
    hide regina evil smile
    show tiffany nervous smile
    pause(.25)
    t "...M-me too!"
    hide tiffany nervous smile
    show kristella giggle
    pause(.25)
    kr "Hehe ~ me too, then."
    hide kristella giggle
    show maryanne smile
    pause(.25)
    ma "Right. Anyways, thanks, [mc]."
    hide maryanne smile
    mc "N-no problem. I’m sure we’re all tired, so let’s go home and rest."
    scene bg neighborhood street
    with fade
    pause(.5)
    mc "{i}Wow, what a week...{/i}"
    mc "{i}I'm exhausted. So much has happened-{/i}"
    mc "{i}Made a friend...{/i}"
    scene bg classroom whiteboard
    show kelvin smile
    pause
    hide kelvin smile
    show teacher angry
    pause
    hide teacher angry
    mc "{i}Started a club...{/i}"
    scene bg clubroom
    show tiffany neutral
    pause
    hide tiffany neutral
    show maryanne neutral
    pause
    hide maryanne neutral
    show regina neutral
    pause
    hide regina neutral
    show kristella neutral
    pause
    hide kristella neutral
    mc "{i}Kept that club...{/i}"
    scene bg clubroom
    show kelvin panic
    pause
    hide kelvin panic
    show maryanne thinking
    pause
    hide maryanne thinking
    mc "{i}Made more friends...{/i}"
    scene bg computer
    show tiffany shy
    pause
    hide tiffany shy
    show maryanne blush
    pause
    hide maryanne blush
    show regina arms crossed
    pause
    hide regina arms crossed
    show kristella giggle
    pause
    hide kristella giggle 
    scene bg neighborhood street
    mc "{i}Or is it something more?{/i}"
    scene bg black screen
    with fade
    mc "{i}...{/i}"
    mc "{i}I need some rest.{/i}"

    jump chapterOneDay6to10

    return
