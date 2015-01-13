

init:
    
    image black = Image("pics/black.jpg")
    image bg hallway = Image("pics/tu_hallway.jpg")
    image bg office = Image("pics/office.jpg")
    image bg street = Image("pics/street.jpg")
    image lecture = Image("pics/lecture.jpg")
    image rich home = Image("pics/richard_room.jpg")
    image hilfer = Image("pics/maria_hilfer_strasse.jpg")
    image friedhof graves = Image("pics/zentralfriedhof.jpg")
    image friedhof path = Image("pics/zentralfriedhof2.jpg")
    image friedhof church = Image("pics/zentralfriedhof_kirche.jpg")
    image friedhof boltzmann = Image("pics/zentralfriedhof3.jpg")
    image friedhof statue = Image("pics/zentralfriedhof_statue.jpg")
    image wien energie = Image("pics/wien_energie.jpg")
    image cafe = Image("pics/cafe.jpg")
    image boltzmann grab= Image("pics/boltzmann_grab.jpg")
    image confrontation = Image("pics/confrontation.jpg")
    image basement door = Image("pics/basement_door.jpg")
    image tu parking = Image("pics/tu.jpg")
    image lecture hall = Image("pics/lecture_hall.jpg")
    image lecture row = Image("pics/lecture.jpg")
    image lecture speak = Image("pics/lecture_speak.jpg")
    image wolken = Image("pics/wolken.jpg")
    image playground = Image("pics/playground.jpg")
    image ludwig home = Image("pics/ludwig_home.jpg")
    image tu nacht = Image("pics/tu_nacht.jpg")

    image emi sad = im.FactorScale("pics/emi_sad.png", 0.42)
    image emi happy = im.FactorScale("pics/emi_happy.png", 0.42)
    image emi neutral = im.FactorScale("pics/emi_neutral.png", 0.42)
    image emi puzzled = im.FactorScale("pics/emi_puzzled.png", 0.42)
    image emi regular = im.FactorScale("pics/emi_regular.png", 0.42)
    image emi angry = im.FactorScale("pics/emi_angry.png", 0.42)
    image emi alt regular = im.FactorScale("pics/emi_alt_regular.png", 0.42)
    image emi alt happy = im.FactorScale("pics/emi_alt_happy.png", 0.42)
    image emi alt neutral = im.FactorScale("pics/emi_alt_neutral.png", 0.42)
    image emi alt puzzled = im.FactorScale("pics/emi_alt_puzzled.png", 0.42)
    image emi alt sad = im.FactorScale("pics/emi_alt_sad.png", 0.42)
    image emi alt angry = im.FactorScale("pics/emi_alt_angry.png", 0.42)
    

    image emi young neutral = im.FactorScale("pics/emi_young_neutral.png", 0.45)
    image emi young angry = im.FactorScale("pics/emi_young_angry.png", 0.45)
    image emi young regular = im.FactorScale("pics/emi_young_regular.png", 0.45)
    image emi young happy = im.FactorScale("pics/emi_young_happy.png", 0.45)

    image richard neutral = im.FactorScale("pics/richard_neutral.png", 0.45)
    image richard dreamy = im.FactorScale("pics/richard_dreamy.png", 0.45)
    image richard happy = im.FactorScale("pics/richard_happy.png", 0.45)

    image richard alt neutral = im.FactorScale("pics/richard_alt_neutral.png", 0.45)
    image richard alt dreamy = im.FactorScale("pics/richard_alt_dreamy.png", 0.45)
    image richard alt happy = im.FactorScale("pics/richard_alt_happy.png", 0.45)


    image professor happy = Image("pics/professor_happy.png")
    image professor sad = Image("pics/professor_sad.png")
    image professor regular = Image("pics/professor_regular.png")
    image professor surprised = Image("pics/professor_surprised.png")

    image professor alt happy = Image("pics/professor_alt_happy.png")
    image professor alt sad = Image("pics/professor_alt_sad.png")
    image professor alt regular = Image("pics/professor_alt_regular.png")
    image professor alt surprised = Image("pics/professor_alt_surprised.png")

    image bad credits = Image("pics/bad_credits.png")
    image good credits = Image("pics/good_credits.png")

    # Declare characters used by this game.
    $ l = Character('Ludwig', color = "#c8ffc8")
    $ e = Character('Emi', color = "#8762B4")
    $ ey = Character('Emi', color = "#C67C50")
    $ r = Character('Richard', color = "#CEC2B9")
    $ n = Character('Netroufal', color = "#CBBE00")
    $ ra = Character('Raphael', color = "#CD3333")
    $ fb = Character('Facebook', color = "#44619D")
    $ s = Character('Steinmeier', color = "#802A2A")

    #Transitions
    $ nextday = Fade(0.5, 2, 0.5)
    $ slowfade = Fade(2, 0, 2)

# The game starts here.
label start:
    
    stop music fadeout 1

    scene wolken with slowfade
    play music "music/graveyard.mp3" fadein 2
    l "Why?"
    l "Why is there anything, instead of nothing?"
    l "Why do I exist? Is there a purpose?"
    l "Do I really exist? Does anything really exist?"
    l "Is it all just a huge coincidence?"
    l "Is there really a past and future, or is the now the only thing?"
    l "..."
    l "I don't know. I don't know the answers to any of these questions."
    l "I don't even know if there is an answer, or if I could understand it."
    l "Most people would tell you that these are all questions for philosophers and theologists. But that doesn't help me."
    l "You see, I do not trust my own thoughts. Or the thoughts of others, no matter how trivial they seem."
    l "Logic can not be proven, because the act of proving is a tool of logic itself."
    l "If a stranger on the street told you to trust him, would you? Just because he told you so?"
    l "Call me paranoid, but I wouldn't. That is why I don't believe in anything, and there is nothing I trust one hundred percent."
    l "What I am looking for is something that can convince me of {i}anything{/i}."
    l "The most promising path to that goal seems to be science."
    l "My words contradict each other, but I can not afford the luxury of living without contradictions right now."

    stop music fadeout 2

    scene playground with slowfade
    show emi young regular at center

    play music "music/happy.mp3" fadein 2

    l "Ahh..."
    ey "Hey Ludwig, what are you spacing out about?"
    l "Huh? Oh, it's you Emi."
    ey "You didn't even see me coming? Where did your mind go?"
    l "Ehm... Nowhere... I was just thinking about some things."
    ey "Like what? How you can concentrate better at school?"
    l "No! Just... about the meaning of existence."
    ey "The existence of what?"
    l "Me, the universe,... everything."

    hide emi young regular
    show emi young neutral

    ey "Huh? What for? It's pointless."
    l "Pointless? Why?"

    hide emi young neutral
    show emi young angry

    ey "Because there is no mystery! It is useless to spend all your life thinking about something that is not there."
    ey "The way this world works is simple. You are born, go to school, get a job, marry and have kids. "
    ey "Then the cycle restarts. See? There is no place for unnecessary questions. "
    ey "How does thinking about unsolvable questions improve your life?"
    l "Ugh..."
    show emi young neutral
    l "Imagine... you were thrown in a complex of white rooms."
    l "There is nothing there, except for these rooms and what is inside of them. There is no exit."
    l "You could call it a closed universe."
    l "You are not alone, but together with people of all ages and races."
    l "None of them have any memories from before they appeared there, including you."
    l "The rooms provide everything you could possibly need in daily life."
    l "You could of course live there until you die, probably even happily."
    l "But... wouldn't you want to know what is behind these walls? Who put them there? For what purpose?"
    l "Why does this construction exist? You could say that the answer to that question is not essential for life."
    l "This is a hypothetical scenario of course, but is it really that distant from the reality we find ourself in?"
    l "Do you really not want to know what's behind those walls?"
    l "Can you really live without asking yourself what is behind this existence? "
    ey "Eh? I don't really get what you mean... how would you even do that?"
    ey "You want to know what's behind your existence? That's impossible!"
    ey "Even if there was an answer, there is no way you could get to it."
    show emi young angry
    ey "And when will you ever stop being so abnormal? White rooms, huh? What does that have to do with anything?"
    ey "You push everyone away with your crazy talk!"

menu:
    "How do you know it's impossible?":
        jump A1
    "I'm... abnormal?":
        jump A2

label A1:
    show emi young neutral
    ey "Recorded history goes back thousands of years. Many people have tried, but no one found any answers. "
    ey "Most of them were very depressed and had no life. They died sad, because they failed. "
    ey "The same will surely happen to you too, if you try the imposssible."
menu:
    "I don't care":
        jump A11
    "Maybe you are right... ":
        jump A12

label A2:

    ey "Of course you are! Look at everyone else, they are enjoying being outside. "
    ey "And what are you doing? You always lose yourself in your thoughts, or talk about weird things."
    ey "Be it in school or outside, you never concentrate on anything!"
    show emi young neutral
    ey "Why can't you just be like everyone else and socialize?"
    l "I... never really thought about it."
    ey "It's time for you to adopt, or you will be an outcast forever."

    menu:
        "You are right...":
            l "I really do behave weird, don't I? Maybe I should start being more normal..."

            show emi young happy

            ey "Glad you came to your senses. Now come, the next lesson starts soon."

            jump BadEnd1

        "Who cares?":
            l "An outcast? Who cares about that?"
            l "What does it matter if society rejects me? I choose my own path. "
            l "I'm sorry you don't like it, but that doesn't change my decision."
         
            show emi young neutral

            ey "Ahhh... you are hopelessly stubborn. You will see where this kind of attitude will get you."
            jump Hallway
    
label A11:
    l "It's still better than living the hollow life that you propose. "
    l "I would much rather die having tried to pursue my ambition."
    hide emi young angry
    show emi young neutral
    ey "What a crazy person..."
    
    jump Hallway
    
label A12:
    l "No one before managed to do it, why should I? How silly of me."
    hide emi young angry
    show emi young happy
    ey "Glad you came to your senses. Now come, the next lesson starts soon."
    jump BadEnd1


label Hallway:
    stop music fadeout 2
    scene black with slowfade

    centered "Seven years later..."
    scene bg hallway with slowfade
    play music "music/science.mp3" fadein 2
    "I wonder how many weeks it has been now since I joined university? It must be at least eight. I think I am slowly getting used to it here."
    "It is definitely better than school. Finally I can decide by myself what classes I want to attend..."
    "This way, I can fully concentrate on my future. I just hope I don't drop out..."
    "My grades have always been good to average, but physics is really hard."
    "Wait, what am I thinking? I already decided that I will become a physicist! If I fail I'll try again."
    "How else am I supposed to learn the secret of the walls? What lies beyond them, and who constructed them for what purpose?"
    "This is the future I have chosen, and I will see it through."
    show emi happy at center
    e "Hey, Ludwig! Hi! We don't meet often between lectures, do we? Haha"
    l "Hi, Emi."
    "This is Emi. We've known each other for several years. We went to the same school for two years."
    "We got along, but I wouldn't say we were friends. When I had to change schools, we lost contact."
    "But now she attends the same university as me, the TU Wien. I study physics, she studies mathematics. We met by chance soon after we started, and quickly became friends. She changed quite a bit..."
    show emi regular at center
    e "What was that lecture you just came out of about?"
    l "Oh, it was about thermodynamics. An introduction to entropy. What did you have today?"
    e "Sounds like fun. Actually, I wasn't in a lecture today. I just came here to do some research in the library."
    l "What are you working on?"
    e "Ah, just my own little theories on formal systems and completion. I have some ideas that seem really crazy, and now I am trying to find out why they wouldn't work."
    hide emi regular
    show emi alt happy at center
    e "I'd tell you about them, but I fear a non-mathematician wouldn't understand them, haha."
    l "Gee, thanks. And don't call yourself a mathematician yet! You just started studying."
    e "I am a mathematician at heart already. By the way, do you want to hear some rumors?"
    "To be honest, I really don't like rumors. Incomplete or untrustworthy information makes me uncomfortable."
    "But Emi loves them, and I don't think she has many other friends at university, so I can't really reject her."
    l "Not really, but tell me anyway."
    hide emi alt happy
    show emi alt regular
    e "Alright! Massive flocks of birds have been sighted, and they are all flying east. East! Birds usually fly either north or south, but not east!"
    e "And it wasn't just one species of bird, but several. Biologists have no idea what causes it. The internet speculates that this is the first sign of the apocalypse."
    l "Hmm, that is weird, if it's true. But I wouldn't trust the internet's diagnosis on such matters."
    e "Me neither, but it's still cool to think about."
    l "Maybe. Anyway, I have to go to the next lecture. See you later."
    hide emi alt regular
    show emi alt happy
    e "See ya!"
    jump Lecture1

label BadEnd1:
    stop music fadeout 2
    scene black with slowfade
    centered "20 years later..."
    scene bg office with slowfade
    "*click click click*"
    "..."
    "*click click click*"
    "Ugh..."
    "I wonder when I can go home? It's already past eight..."
    "But I can't leave until I've finished this report on the sales of the last quarter. Well, at least this job pays well."
    "*ring ring*"
    "*pick up cell phone*"
    l "Hey Raphael, what's up?"
    ra "Hi Ludwig! How are the wife and kids doing?"
    l "Fine, thanks for asking."
    ra "I just wanted to ask if you wanted to catch the football game tomorrow."
    l "Sure! It will be an interesting match, there's no way I'm going to miss that."
    ra "Great! Then we'll just call each other tomorrow, alright?"
    l "Yeah. Until then."
    ra "Bye."
    
    "..."
    "......"

    "........."

    "Why do I feel so empty? I feel like there is something I have forgotten about..."
    "Whatever it was, it's too late now. I should just get back to work, so I can catch some sleep at home."

    "*click click click*"
    "..."
    "*click click click*"

    jump game_over


label Lecture1:
    stop music fadeout 2
    scene lecture hall with slowfade
    play music "music/happy.mp3" fadein 2
    "This lecture is special, and one that I've particularly been looking forward to. The lecturer is Professor Dr. Dr. Netroufal."
    "He's been in universities abroad for a few years, and recently came back to Vienna. The subject is quantum mechanics."
    "This topic isn't usually taught this early in the studies, but that is why this lecture is special. "
    "It's the professor's field of expertise, and it is sort of his 'welcome back' gift to us, the students."
    "Anyway, I should find a seat. Damn, I should've come earlier, it's packed in here..."
    "Why is it in such a small room? I thought he was more popular..." 
    "The only free seat left is in the center row. I don't really like it there, but there's nothing I can do about it now."

    scene lecture row with fade
    show richard dreamy

    l "Excuse me, is this seat taken...?"
    show richard neutral
    r "Huh? Yeah, sit down if you want. Seems to be the last one."
    l "Yeah. Thanks."
    r "Man, I hate the center row."
    l "Really? Me too!"
    "I like to sit in the last row, where nobody is behind me who could see me. "
    "I'm uncomfortable when a lot of people can watch me, even if I'm not at the center of attention."
    show richard happy
    r "Aha! I see we are alike! Truly, the first row is the best. I can't stand having to see so many other people in front of me."
    "Well..."
    show richard alt neutral
    r "It simply disgusts me, you know. Most young people are a disgrace to mankind."
    r "All they think about is how they need to have the newest phone, watch TV, repeat what is told to them by the media, and so on."
    r "But the worst thing is, they are lazy. They don't have a goal to accomplish. They aren't alive, they just live."
    l "I agree with you. Most of them are just annoying."
    show richard happy
    
    r "Oho! You share my views! This is rare. That must mean that you are different... "
    r "Say, do you have a dream?"
    l "I guess you could say that. I want to solve the mystery of existence."
    show richard alt neutral
    r "You mean... answering the fundamental questions mankind has been asking for millenia?"
    l "Well... yes."
    r "You attempt to do what the most brilliant minds humanity had to offer failed at?"
    l "You think it's foolish, don't you?"
    show richard alt happy
    r "The opposite is true! I admire you for your dedication! "
    r "You try to do the impossible, because it is your dream. There is nothing foolish in that."
    "Wow, that is the most motivating thing anyone ever said to me. "
    "Everyone else always tried to tell me I should do something normal..."
    
    r "I like your style. What so you say, do you want to visit my place later today, in order to test our intellect and wits against each other in a game?"
    "I don't have anything else planned tonight."
    l "Sure, why not."
    r "Marvelous! I will tell you where I live after the lecture is over. "
    show richard neutral
    r "Speaking of which, it seems to start now."

    jump Lecture2

label Lecture2:
    stop music fadeout 2
    scene lecture speak with slowfade
    play music "music/science.mp3" fadein 2
    show professor happy
    n "Hello everyone. My name is Professor Dr. Dr. Netroufal. But you can just call me Professor Dr. Netroufal. Ahaha."
    "A few giggles came from the audience, but it remained mostly silent."
    show professor regular
    n "I am a Professor of physics, and hold the title of doctor for mathematics and neurology."
    n "Today I will give you an overview of what I think is the most important concept of quantum mechanics."
    n "Let's start right away, shall we?"
    
    n "Most of you probably know that very very small objects, like atoms, behave differently from the larger ones that we are familiar with."
    n "For example, an electron can be at two different places at once, whereas a melon can't." 
    n "One common error is to think that we just don't know where exactly the electron is."
    n "That is partially true, but mostly wrong." 
    n " We do not know where it is, because it really actually is at both places. But we can never see it in both places."

    show professor alt regular

    n "But that is weird, isn't it? If something is, then it should be observable. " 
    n "Sadly, in the world of quantum mechanics everything is weird and different."
    n "When we observe an object in such a so called superposition, it seems to suddenly decide for one of the places randomly. " 
    n "We can calculate the probabilities for each event exactly."
    n "In fact, quantum mechanics is one of the best tested theories ever."
    n "And not once has it given a wrong prediction. The results are correct. Every. Single. Time."
    n "The only problem is that we don't understand how and why it works. We know a particle jumps to a single place when observed."
    n "But it doesn't explain what exactly an observation is. "

    show professor alt surprised
     
    n "Does it need humans? Does consciousness play a role in the laws of physics? Or is a single photon hitting it enough?"

    show professor alt regular

    n "This is the Copenhagen interpretation of quantum mechanics, and it leaves quite a few open questions. " 
    n "And yet, for a long time it was what most scientists thought was the correct way to see things."
    n "Today, they are not as sure. With good reason. There are alternative explanations for the phenomena we can observe."
    n "The most popular one of them is the Everett interpretation of quantum mechanics, also known as the many worlds interpretation."

    show professor regular

    n "You may have heard or read about it in various science fiction stories." 
    n "But I want you to understand that this is NOT just fiction."
    n "Now, let's think about what actually happens when we observe something. " 
    n "Let's take the most simple scenario, with a single electron."
    n "To measure something, we basically have to throw something at it, and see how that thing comes back to us. In this case we use a photon."
    n "But the electron is in superposition! How does it reflect the electron? The answer is simple. " 
    n "The photon is reflected by both states of the electron, and is itself now in two positions at the same time."
    n "It is also in superposition. Eventually, it hits one of our detectors. This detector, too, is put into superposition of two states."

    show professor alt happy

    n "And when we look at the results of the detector, our whole brain is put into a superposition of thinking the electron is at either one place or the other. " 
    n "Both of these states are equally real."

    show professor regular

    n "But because of the way our brain works, we can only consciously feel ONE of them."
    n "If you want, you can call these other states {i}parallel universes{/i}."
    n "But they are actually all part of one big, strange universe."
    n "And that is the Everett interpretation. If you ask me, it follows a much simpler logic and requires less magic. "
    n "But of course, it also changes our view of the world completely."
    n "And extraordinary claims require extraordinary evidence. Can we produce such evidence?"
    n "There are some theoretical possibilities. But that is a story for another day."

    show professor regular

    n "I'm done here."

    hide professor

    "What an interesting lecture. But pretty short... "
    "I'd really like to ask him some questions. But appearently so do many others. "
    "Should I try to go and talk to him?"

menu:
    "Yes":
        jump StreetRichard
    "No":
        jump StreetEmi

label StreetRichard:
    stop music fadeout 2
    scene bg street with slowfade
    show richard happy
    play music "music/happy.mp3" fadein 2

    r "Oh, hello Ludwig. Did you catch the professor?"
    l "Hi Richard. No, too many wanted to talk to him. After the first three people, he just went to his office."

    show richard neutral

    r "What a shame. If you want, we can go right to my place and battle each other."
    l "I have nothing else to do, so yeah, why not."
    "I am curious what he is referring to when he speaks about battling..."

    show richard happy

    r "Alright, then let's go."
    l "So, why do you study physics?"

    show richard neutral

    r "I honestly am not sure if this is the right direction for me. I changed studies three times now."
    r "Law, logic, medicine... They all couldn't ignite the spark in me to get me burning. I still haven't found my true passion,"
    r "Which is what I really want: finding something that truly fulfills me. Something I can get lost in."
    r "Work that I truly love. Sadly this is not easy to come by. "
    show richard alt neutral
    l "I do not have a dream like you do. So I keep on searching, until I find it."
    r "I must admit, I envy you for already having found yours."
    l "I am sure that you will find your dream soon enough."
    r "I hope so."

    scene black with fade

    "After walking for a few minutes, we arrived at Richard's home."

    jump HomeRichard

label StreetEmi:
    stop music fadeout 2
    scene bg street with slowfade
    show emi happy
    play music "music/happy.mp3" fadein 2
    e "Hey Ludwig."
    l "Hey Emi. How was your math lecture?"
    show emi regular
    e "Very interesting. Our professor Dr. Steinmeier spoke about randomness and if it could really occur measurably to a larger scale than quanta."
    show emi neutral
    e "It got a little bit philosophical but his opinion is that there is no randomness in math and therefore no randomness in the real world."
    e "I brought up the chaos theory, and he said that it only {i}seems{/i} random to us and that by knowing all the information about the system from an outside view, it could be predicted perfectly."
    e "I argued that we will never be able to do that, and therefore it doesn't matter and is in fact random to us. "
    e "He replied with a smile on his face: 'It is not about us, it never has been.'"
    e "'It is about the fact that all of the information only leads to one possible outcome, which is already determined and we are just a part of a program that is following its rules until it's completion.'"
    e "I really hate these 'Oh, look at me, I am so smart' kind of people. "

    show emi puzzled

    e "But it made me think. Does life matter in the end? And how should we use it?"

    show emi alt regular

    l "I've thought about this for a long time as well. "
    l "Most people say there is no answer, but I think that as long as we do not know everything there is to know about the universe, then we are not allowed to accept an answer like that."
    
    show emi alt happy

    e "I like that attitude of yours."
    l "Thanks."
    "...Since when does she agree with me on such things?"

    show emi alt regular

    e "Anyway, I have to get going now. It was nice chatting with you!"
    l "Yeah, likewise. Bye."

    scene black with slowfade

    "After walking for a few more minutes, I arrived at Richard's home."
        
    jump HomeRichard

label HomeRichard:

    scene rich home with slowfade
    show richard happy

    r 'Welcome to my home. I am very sorry for the mess, but I did not have enough time to tidy it up.'
    
    hide richard happy
    
    "..."
    "What mess?"
    
    show richard happy
    
    r "Do you want something to drink? I've got Orange juice, beer, wine and water."
    
menu:
    "Orange juice, please.":
        jump drink
    "I'll take a beer, please.":
        jump drink
    "I'll take a glass of wine, please.":
        jump drink
    "I'll take a glass of water, please.":
        jump drink
    "I'll have nothing, thanks.":
        jump nodrink

label drink:
    hide richard happy
    "..."
    show richard happy
    r "Here."
    l "Thank you."
    "Gulp..."
    l "That was refreshing."
    jump battle
    
label nodrink:
    r "Alright."
    jump battle

#battleships

label battle:

    show richard neutral
    r "Now, we are ready for an epic battle of intellect." 

    show richard dreamy

    r "A one on one in an ancient competition that the smartest brains of all cultures play to determine the very best." 
    r "In world championships, the best player in the world is able to defeat all his opponents and crown himself as king." 
    r "Only those who can put themselves into someone else's mind and understand their opponent's train of thought will have a chance to win." 

    show richard neutral

    r "Do you know what I am talking about?"
    
menu:
    "It's got to be Chess.":
        jump battleship
    "I assume you are talking about Go.":
        jump battleship
    "Tic Tac Toe?":
        jump battleship
    
label battleship:

    show richard happy

    r "Ahaha, good joke, buddy!"
    r "I am of course talking about Battleship!"
    r "Let's start!"
    
    stop music fadeout 2
    scene black with slowfade
    centered "17 minutes later"
    scene rich home with slowfade
    show richard dreamy at center
    play music "music/science.mp3" fadein 2

    l "I've hit all of his ships except the last part of one of his destroyers."
    l "It could be on A3 or A7. If I hit it, I'll win."
    l "But if I miss, Richard will be able to eliminate my last submarine."
    l "I need to make a decision now."

menu:
    "I shoot the field A3":
        jump A3
    "I shoot the field A7":
        jump A7
        
label A3:
    $ battleshipwon = False
    r "The field A3 is occupied by..."

    show richard happy

    r "Water, you have missed!"

    show richard neutral

    r "I shoot the field E7"
    l "Damn. On the field E7 is..."
    jump lightsoff

label A7:
    $ battleshipwon = True
    r "The field A7 is occupied by..."
    r "...the last part of my last destroyer, you have won!"

    show richard happy

    r "Congratulations! I am happy to finally have found a worthy opponent."
    r "I hope we can play..."
    jump lightsoff
    
label lightsoff:
    scene black
    stop music
    r "What happened?"
    l "Maybe the bulb died."
    r "No, I bought it from a passionate engineer, who builds them on his own."
    r "The bulb should last longer than the sun."
    r "It must be a blackout. Just look out of the window."
    r "Everything is dark. It seems to be city wide."
    r "I am sorry, but you have to leave."
    r "Chances like these do not present themselves very often."
    l "What are you talking about?"
    r "I can't tell you anything now."
    r "Meet me tomorrow at Mariahilferstraße near Neubaugasse at 2pm."
    r "Then I can explain."
    l "Ok..."
    jump Home1

label Home1:

    stop music fadeout 2
    scene ludwig home with slowfade
    play music "music/happy.mp3" fadein 2

    "Ahh, finally home."
    "This blackout was unusually long, and seems to have affected the entire city."
    "I had to walk by foot, since the trains were stopped."
    "Man, it was chaotic out there..."
    "Everyone was in confusion."
    "Fortunately, I have a flashlight on my phone."
    "Otherwise, I'm not sure if I would have found my way home."
    "But the blackout is over now."
    "Usually I'd go right to bed, but I am way too worked up."
    "I'm also curious about what's going on with Richard."
    "What did he suddenly have to do?"
    "Maybe I could cool down a bit by browsing the web."
    "Ok, step by step: First I enter Mr. Braun's open WiFi..."
    "{i}*click*{/i}"
    "Now I connect to my dutch VPN..." 
    "Wouldn't want the NSA to know everything about me."
    "{i}*click*{/i}"
    "Alright, I am in stealth mode."
    "I really don't want to be one of those see-through citizens."
    "Even if I have nothing to hide, there is no way I'll let any government or corporation know what I'm doing."
    "And since I can not trust closed sourced software, my entire computer is a freedom machine."
    "I'm running an obscure Linux distribution, with exclusively free software."
    "My WiFi disconnects every few hours, but it's a small price to pay."
    "So... What do people do when they browse the internet without a specific goal?"
    "Hmm..."
    "I could go to Facebook, it's been a while."
    "Of course, Facebook is the worst regarding privacy and surveillance."
    "But I don't use my real name, haven't uploaded any personal information, and generally don't past anything."
    "I use it only for a few friends and family members."
    "..."
    "And I'm logged in."
    "So what have people been up to?"
    fb "\"Melanie Bauer: My teacher tried to tell me that our sun was a star. So stupid, it is a sun, that's why its called sun and not star xD\""
    fb "\"12 people liked this\""
    "Wow. Unfriended."
    fb "\"Gustav Müller: My lunch today. I love sushi *_*\""
    "Fascinating. Just how could I have gone to bed without knowing what he ate today?"
    "Ugh."
    "..."
    "What's that image?"
    fb "\"You have been visited by the funny banana! Happiness will come to you and your family!\""
    fb "\"But ONLY if you repost this in the next 10 seconds!\""
    "And in the trash it goes."
    "I remember now why it has been a while."
    fb "\"Emi has sent you a message!\""
    e "Hey!"
    "Oh right, people on this network see when I am online."
    l "Hi."
    e "That's rare, to see you online."
    e "Did you notice the blackout?"
    l "Yes, I did."
    e "Very mysterious..."
    l "Not really, that happens about every five years."
    e "It was the whole city! That has not happened in at least 50 years..."
    l "Randomly, it will eventually happen, so that's also not very mysterious."
    e "I don't think so. I feel something strange in the air... I want to investigate. Wanna come with me?"
    l "Not really."
    e ";_;"
    l "Where would you even investigate and what?"
    e "Well, for example, I would start at the energy center, Wien Energie."
    l "I am sure you could just wait and read the newspaper tomorrow."
    e "As if they were honest..."
    l "Meh."
    e "Call me if you change your mind, alright?"
    l "Ok."
    jump mariahilferstrasse

label mariahilferstrasse:

 #   stop music fadeout 2
    scene hilfer with slowfade
 #   play music "music/happy.mp3" fadein 2
    "I wonder what Richard was up to last night... and what he's going to tell me..."
    show richard happy
    r "Hey Ludwig!"
    l "Hey Richard."
    "He is still wearing the same clothes as yesterday and looks terribly tired."
    "I'm sure he has not caught a lot of sleep last night."
    show richard neutral
    r "I am sorry that I had to make you leave last night."
    r "You know the feeling when you are somewhere in the countryside and there are hardly any lights, and you look up to the sky and realize its beauty?"
    r "In Vienna I miss this sight. Yesterday all the lights went out."
    show richard dreamy
    r "It was magnificent."
    show richard alt neutral
    r "I once tried to be a photographer, but it wasn't really my passion."
    show richard alt happy
    r "However I liked to take those long exposure night sky pictures where you expose the film for hours to only the night sky and the motive."
    show richard alt dreamy
    r "In the picture you get, you can see the stars forming circles around the spinning axis of earth."
    r "Getting a picture like that in Vienna is usually impossible. The city is way too bright."
    r "The motive is the most iconic place in Vienna, the Stephansdom."
    r "It is just the most perfect picture that I have ever and will ever have take."
    show richard neutral
    r "I don't know if there was a picture like that before, it might be the best photo of the Stephansdom ever made."
    l "That sounds amazing. Can I see it?"
    r "I am very sorry, but I can't do that, Ludwig."
    "What? Why wouldn't he show it to me?"
    r "This photo is nothing the world should see."
    r "I will only show it to one single person on this planet."
    l "Aha... Who would that be?"
    r "I don't know yet."
    "Wait a minute, the blackout lasted for one hour, and I am pretty sure these photos take time when it comes to set up."
    "Also, how would he know when to stop before the blackout ends?"
    "And he could have gone home afterwards to catch some sleep..."
    "And he surely would have changed his clothes..."
    "Is he telling the truth?"
    stop music
    play sound "music/gammaray.wav"
    centered " "
    l "What was that?!"
    jump cafe1

#Lukas
#cafe 1
label cafe1:

    stop music fadeout 2
    scene cafe with slowfade
    show emi happy
    show richard neutral at right
    play music "music/science.mp3" fadein 2


    e "I'm glad you reconsidered, Ludwig! Finally, I don't have to do this investigation on my own."

    "Not one minute after that strange noise came from the sky, Emi called me."
    "Such a thing has never happened before, so I agreed to join her investigation."

    show emi alt regular

    e "I would really like to figure out what that was."
    l "No problem. By the way, this is Richard. I met him during a physics lecture."
    show richard happy at right
    r "Hello."

    show emi alt happy

    e "Oh, hi. I'm Emi, Ludwig's childhood friend."

    "I don't know if I would call it that, but whatever."

    show emi regular

    e "Do you think he has the skills to join our team, Ludwig?"
    l "Yes, I'm sure he will be able to provide valuable insight."
    l "But shouldn't you ask him first if he even wants to?"

    r "Yeah, I would like to join you. This seems like it could become a great adventure..."
    show richard dreamy
    r "...and that is where dreams are born."
    show richard happy
    e "Great! Now we just need a strategy. Let's think about what has happened."
    show emi neutral
    e "Birds have been seen flying in the wrong direction, en masse."
    e "Also, various electronics were damaged or stopped working, for apparently no reason."
    l "I don't know much about biology or birds, but maybe a weather change urged them to change course?"
    show richard neutral
    r "Or maybe some evil organization is conducting experiments on the earths core, disrupting the magnetic field."
    show richard dreamy
    r "And the electronics all belonged to their enemies."
    show emi regular
    e "You mean like the Illuminati?"
    show richard neutral
    r "Probably."

    "Doubts about this operation are starting to rise within me."
    

    r "Anyway, then we had this large scale blackout."
    l "Those things just happen."
    show emi puzzled
    e "Yeah, but the timing is very weird. Just to be safe, we should check out the electricity supplier, Wien Energie."
    e "And a few days before that, there was a blackout in the university."
    r "You think there is a connection?"
    show emi neutral
    e "It seems plausible."

    "Hmm, I hadn't heard of that. That is kind of suspicious."

    l "But the strangest thing of all is that sound we just heard twenty minutes ago."
    show emi alt happy
    e "Ah, yes. About that, I did some quick research before I left the house."
    "So that's what kept her so long..."
    show emi alt regular
    e "According to my sources, the epicentre of the sound was the central cemetery."
    show richard alt neutral
    l "The cemetery? Why there?"
    e "I don't know. That's why we should go there to check things out."
    r "I recommend that we split up."
    r "You two go to Wien Energie, while I do some investigating in the university."
    r "After that we meet up at the central cemetery."
    show emi regular
    e "Sounds like a plan."
    l "Alright, then let's go."


#wien einergie

label wien_energie:

    stop music fadeout 2
    scene wien energie with slowfade
    show emi alt regular
    play music "music/science.mp3" fadein 2

    l "We are here. What now? It's not like we can just look at the facility and find out what caused the blackout."
    show emi alt puzzled
    e "We can't?"
    l "Ehm... I thought you had a more elaborate plan."
    show emi alt happy
    e "Don't worry, I have a plan."
    show emi alt regular
    e "I'll try to find someone who works here and ask him some questions, and you try to find something out by looking at the facility."
    l "Ehm... how?"
    show emi alt happy
    e "Good luck!"

    hide emi alt happy
    "..."
    "And she's gone."    
    "Well, let's see. There is nothing here."
    "I can't climb over the fences, and I see no one I could talk to."
    "Time for browsing the internet on my phone."
    "..."
    "The news says that the blackout happened because a few employees messed up at inconvenient times."
    "Just the kind of thing I expected. But I don't think Emi will believe the news."
    "I can't really fault her for that though. It's not like I trust the media."
    "Ah, she's coming back."
    show emi happy
    e "Did you find anything?"
    l "No, how should I? Access is restricted."
    show emi neutral
    e "Too bad... I had hoped you somehow managed to learn something anyway."
    show emi regular
    e "But it doesn't matter, I just talked to an employee."
    show emi neutral
    e "He said he was terribly sorry, and that the incident was kind of his fault."
    e "Appearently it really was just an accident..."

    "Looks like there is more than one way to the truth."
    "..."
    "Now seems to be a good time to ask..."
    l "Hey, Emi. I've been meaning to ask you something."
    show emi alt regular
    e "Huh? What is it?"
    l "Do you remember when we were back in school?"
    e "Sure."
    l "Well, you changed since then..."
    l "Back then you thought it was unreasonable to try to solve the big questions..."
    l "You said that career was everything, and you should just try to be content with what you have."
    e "Oh, it is unreasonable. But I came to the conclusion that not everything has to be reasonable."
    l "How?"
    show emi neutral
    e "Well, I remember beeing a real grey face, the 'NO FUN ALLOWED' type."
    e "I thought that everything had already been sorted out, that there was one acceptable way to behave and think."
    e "And people who didn't fit that pattern disturbed me."
    show emi puzzled
    e "'Why won't they just be normal?', I thought."
    show emi neutral
    e "It annoyed me, and made me a grumpy person, without realizing it."
    e "And then, one day, I suddenly understood the reason  why I was always upset with people."
    e "And then I thought, 'Maybe everything isn't already sorted out.'"
    e "'Maybe people who act abnormally in my view just don't agree with the views of others.'"
    e "'Maybe every view is valid in its own way.'"
    e "'And, maybe, I shouldn't care so much about that, and let everyone be themselves.'"
    show emi regular
    e "And as soon as I changed my own view of the world a little bit, I realized I really don't like the standard norm."
    show emi alt happy
    e "Apparently, my personality also changed to show that new view."
    l "I understand... so that's why. But how did you come to this enlightenment?"
    show emi alt regular
    e "Well, it was more of a stretched out process, with several factors, but I'm sure our conversations in school were a large contribution."
    l "Really?"

    "I've always seen myself as more of an observer."
    "I didn't really think I also affect the people around me..."
    "It seems silly, but only now I fully realize that fact."
    show emi alt happy
    e "Yes, really. Now let's meet Richard and see what he found out."

#zentralfriedhof

label zentralfriedhof:
    stop music fadeout 2
    scene friedhof graves with slowfade
    play music "music/graveyard.mp3" fadein 2
    show richard neutral
    show emi regular at right
    l "Hi Richard."
    e "Hi! Did you find any clues?"
    r "Hello everyone. Yes, I heard some suspicous things, but nothing conclusive I'm afraid."
    show richard alt neutral
    r "The blackout at the university happened at around the same time as the city wide one, the difference was just ten minutes."
    r "A connection seems plausible, though still unlikely."
    r "Some professors who have known him for a long time said they are worried about Professor Netroufal."
    r "Sadly, I don't know about what or why."
    show richard neutral
    r "Lastly, I heard some rumors about stolen weapons. It was just in passing by, so I'm afraid I can't tell you more."
    show emi neutral
    e "Wow, that is a whole lot more information than Ludwig and I got. Let's try to make sense of it later, now we should focus on investigating here."
    l "What exactly are we looking for here?"
    show emi alt regular
    e "Anything suspicious! You will know it when you find it."
    show emi regular
    e "Probably. We should split up again, so we can cover a larger area."
    l "Alright."
    show richard alt neutral
    r "No objections."

    scene friedhof path with slowfade

    "15 minutes have passed."
    "Emi said she'd talk to the priests of the church. Richard and I have been aimlessly wandering around."
    "I can't see anything that could have produced such a sound. Did it really come from here?"
    "But it also seemed to come from above... was it a message from God?"
    "What a ridiculous thought."
    "Oh, I found Richard. He's standing in front of some beautifully decorated graves."
    "He looks really lonesome and lost in thought... as if he were lamenting something."
    "Should I go up to him? Or should I leave him alone?"

    menu: 
        "Go.":
            $ graveyard_talk_richard = True;
            jump go

        "Let him be.":
            $ graveyard_talk_richard = False;
            jump let_him_be


label go:
    scene friedhof boltzmann with fade
    show richard alt neutral

    "Let's see what he's doing there."
    "He looks so deep in thought, I don't want to say a word. Better just stand next to him."
    
    "..."
    "..."
    "..."

    r "Do you know who is buried here?"
    l "No."
    r "Take a look at the gravestone."

    hide richard alt neutral
    scene boltzmann grab with fade

    centered ""
    l "There is a formula engraved in it..."
    l "S = k * log W"
    r "This is the formula for entropy."

    scene friedhof boltzmann with fade

    show richard alt neutral
    r "The one who lies here is none other than Ludwig Boltzmann. "
    r "One of the greatest scientists of Austria. He's right up there with Schrödinger."
    l "..."
    r "He showed that the second law of thermodynamics is nothing other than a statistical emergence. "
    r "He also devised this formula for entropy."
    r "But many physicists disregarded his ideas, his entire life's work, because they refused to believe in something such as atoms, which was a vital assumption for his theories."
    r "In the end, Boltzmann commited suicide out of great depression."
    show richard neutral
    r "A few years after his death, the existence of atoms was confirmed."
    l "How sad..."
    show richard dreamy
    r "Humans are machines that turn dreams into reality."
    r "Great souls reside within those with great dreams. But every soul is vulnurable, for it is human."

    l "..."

    scene black with fade

    "We continued to stand there for some more minutes in silence."
    "At some point Emi joined us. She didn't hear the story, but could read the atmosphere and silenty mourned with us."
    "Then we returned to the cafe."

    jump cafe2

label let_him_be:

    "He probably wants to be alone for now. I should go somewhere else."
    
    scene friedhof statue with fade

    centered ""

    scene friedhof graves with fade

    centered ""

    scene friedhof church with fade

    "Nope, I really don't know what I'm doing."
    "But it still was a good idea to come here. The scenery is beautiful, and the atmosphere chilling."
    "..."
    "There comes Emi."
    show emi alt regular
    e "Hey, Ludwig."
    l "Hey. Any luck with the priests?"
    show emi alt neutral
    e "Nope. I walked into the church and spoke to one of them."
    e "He kept talking about his delusions and tried to get me to join his club."
    e "I was annoyed by his close mindedness, so I tried the Turkey Curse on him, but then he threw me out."

    "The Turkey Curse? Is that a thing?"

    show emi alt regular
    e "Anyway, I doubt he knew anything. Let's just find Richard and return to our base."

    scene black with slowfade
    "That base turned out to be the cafe."

    jump cafe2



#cafe2
label cafe2:

    stop music fadeout 2
    scene cafe  with slowfade
    show emi alt regular
    show richard alt neutral at right
    play music "music/happy.mp3" fadein 2
    e "Okay, let's do a status report. I'll start."
    show emi alt neutral
    e "The huge blackout seems to have actually been an accident. "
    e "I got this information by someone who claims to be partially responsible."
    e "No one at the Central Cemetery had any valuable information about the loud sound."
    l "I didn't really know what to look for, so I didn't find anything."
    show richard alt neutral
    r "Aside from some rumors, I found out that the blackout at the TU in the week before was at around the same time of day as the city wide one yesterday."
    e "Hmmm..."

    "She looks like she's jealous of Richard for being a better detective."

    show emi puzzled
    e "That does sound really suspicious. If someone caused the blackout deliberately, why would they start at the TU?"
    show emi neutral
    e "And that hypothesis is also conflicting with the information that I received."
    l "Maybe the person you talked to lied? Or he was just part of a much more elaborate plan?"

    "I don't really believe that, it's most likely just a coincidence."

    e "That could be."
    r "It seems that today's investigation brought up some interesting points, but nothing conclusive."
    l "Yeah."
    show emi regular
    e "Let's try to sleep over this, and maybe we come up with better ideas tomorrow."

    scene black with fade

    "And so the meeting was adjourned."

    jump home2


#home2
label home2:

    stop music fadeout 2
    scene ludwig home with slowfade
    play music "music/science.mp3" fadein 2
    "So that whole thing didn't help us at all. "
    "But I wouldn't call it a waste of time. I had fun after all."
    "I will relax with some internet for the rest of the evening."

    "Let's try the science board." 

    "\"Hello /sci/entists. I want to become immortal. What field of science should I study?\""

    "Sage'd."

    "\"Hey /sci/, if God doesn't exist, how come bananas are shaped exactly to fit our hands?\""

    "Even if you're being ironic, it's still... agh. Are there only bad threads today?"

    "\"How do you know you aren't a Boltzmann brain?\""

    "Oh no, Boltzmann brains. They make me uncomfortable."
    "It's the idea that in an infinite equilibirum, it is more probable that your brain spontainiously pops into existence, instead of the entire universe existing."
    "In other words, statistically, you and all of your memories are probably just a fluctuation within a gas, and will disappear after a few moments."

    if graveyard_talk_richard:

        "But I visited Boltzmann's grave today. Richard told me a lot about him I didn't know before... "
        "I should do some research on him."
        "..."
        "He founded the Austrian Mathematical Society? Emi will love to hear this."
        "..."
        stop music fadeout 2
 
        "So he commited suicide while he was on vacation with his family..."
        "I can't imagine how hard the pressure from his colleagues must have been to drive him this far."

        play music "music/graveyard.mp3" fadein 2
        "..."
        "Wait, what's this? One of his students was... Bernhard Netroufal?"
        "Could it be?"
        "..."
        "....."
        "......."
        "Really... that is Professor Netroufal's grandfather. Who would have thought."

        "Thinking of it, didn't Richard mention the other professors were worried about him?"
        "...maybe I should research him a bit too."
        "..."
        "I see, so he's been teaching at an American university for the last 20 years."
        "Wait... they threw him out? He didn't leave on his own free will? Why?"
        "They haven't announce the reason to the public it seems."
        "But, according to rumors on the university's forum..."
        "...it's because he was doing dangerous experiments? Even life threatening?"
        "And, I can't really believe this, but, there has been a series of big coincidences, and it stopped once he left..."
        "This can't be..."
        "But since I can not fully believe in anything, there is nothing I can deny absolutely."
        "I at least need to tell the others tomorrow."

        jump following

    else:

        "I've spent enough time thinking about whether I am real or not..."
        "I should just go to bed before I fall into another existential crisis."

        jump bad_end_2

label bad_end_2:

    stop music fadeout 2
    scene black with slowfade

    "I don't understand what is happening."
    "Two days have passed. Today, it was announced that Professor Netroufal is dead. Suicide, they say."
    "Nothing makes sense. I can't imagine a single reason why he would do something like this."
    "But I didn't really know him that well... In fact, we only spoke once, and it was a one way communication."
    "Then, why does his death have such a strong impact on me?"
    "Maybe I was just hoping I found someone who thought similarly about the universe..."

    jump game_over

#following
label following:
    scene black with slowfade
    "On the next day, I sent them a message to meet me at the cafe."

    stop music fadeout 2
    scene cafe with slowfade
    show richard alt neutral at right
    show emi regular
    play music "music/happy.mp3" fadein 2


    l "Good news everyone! Yesterday I browsed the internet and randomly stumbled upon a thread about Boltzmann brains. "
    l "And because of that, I thought I'd read about him."
    l "It turns out he founded the Austrian Society of Mathematics."
    show emi happy
    e "Oh cool, he did that?"
    
    l "I thought that you would like that. "
    l "But more importantly, I found out that Professor Netroufal's grandfather was a student of Boltzmann."
    show richard neutral at right
    show emi neutral
    l "I was intrigued by that coincidence and did a little research on the professor."
    l "He was thrown out of his previous university, supposedly due to \"dangerous experiments\". "
    l "Also, I'm very sceptical about this, but according to rumors, strange events have occured while he stayed there."
    l "And they stopped once he left."
    l "I know, it is not much, and I usually dislike rumors, but it's basically anything we have so far. "
    l "Let\'s shadow the professor, he might lead us to something interesting."
    
    show emi alt happy
    r "I am in."
    
    show richard happy at right
    e "Me too."

    "Wow, they really have no moral issues whatsoever regarding spying on a professor."

    l "Alright, here's the plan: Professor Netroufal finishes his last lecture at 7 pm. "
    l "He should be leaving around half an hour later through the front door to his car. "
    l "Then we can follow him and find out if he has something to do with all of this."

    e "Neat!"

    stop music fadeout 2
    scene tu nacht with slowfade
    show emi regular at left
    play music ("music/science.mp3") fadein 2
    show richard neutral at right

    l "OK, it is five past seven, he should come out come out within the next 30 minutes."

    r "Did anyone bring food? I am a bit hungry."
    l "I am afraid not."
    e "But I did, you want some cheese?"
    show richard alt neutral at right
    r "Nah, I hate cheese."
    show emi happy at left
    e "More for me then..."

    scene black with fade
    hide emi happy at left
    hide richard alt neutral at right
    "30 minutes have passed."
    scene tu nacht with fade
    show emi neutral at left
    show richard neutral at right

    l "Still no sign of him, he might be talking to students right now..."
    r "By the way, is anyone here with a car?"
    e "Nope."
    l "No, why?"
    show richard alt neutral at right
    r "The Professor is going to leave by car."
    r "How do you plan on following him?"
    show emi happy at left
    l "Oh... I did not consider that..."
    show richard alt happy at right
    r "Well, we'll figure something out when we see him."

    scene black with fade
    hide emi happy at left
    hide richard alt neutral at right
    "Another 10 minutes have passed."
    scene tu nacht with fade
    show emi alt neutral at left
    show richard alt neutral at right

    e "Ok, I don't think he is leaving anytime soon, he should already be gone."
    "The professor really doesn't seem to be the kind of person that talks to students after class."
    "I mean, as soon as the lecture we attended ended, he fled to his office."
    l "You are probably right, let's go inside."

    scene lecture with slowfade
    show emi neutral at right
    show richard neutral at left
    r "Nothing. He is not speaking to any students."
    "Again this small room... Can't they plan it so he gets a proper lecture hall?"
    "Before he got back to Vienna, I heard that he's a very good scientist."
    "But that was only on the internet, maybe he is more of an underdog?"
    s "Are you looking for something?"
    show emi regular at right

    e "Hello Professor Steinmeier! Yes, we are looking for Professor Netroufal."

    "Real stealthy Emi."

    s "Netroufal? For all I know, he could be in the basement."
    s "Nobody really knows what's been up with him lately, but I hear he's been seen in that area a few times."
    s "Not that I really cared though."
    show emi alt happy at right
    e "Oh, so that's how it is. Thanks for the info."
    s "No problem. Good evening."
    show emi regular at right
    e "Good evening."
    l "Well, let's try the basement."
    r "Ok."
    show emi happy at right
    e "Yay, university basement time!"

    stop music fadeout 2
    scene basement door with slowfade

    show emi alt neutral at right
    show richard neutral at left

    r "Do you hear that? Sounds like someone's actually in there."
    l "Wow, and I just wanted to see what it looks like down here..."
    l "Is the door locked?"
    l "Doesn't seem that way... weird. Let's go in."

    stop music fadeout 2
    scene confrontation with slowfade
    show emi neutral at right
    show richard neutral at left
    show professor surprised at center

    play music "music/delusion.mp3" fadein 2


    r "Professor Netroufal! What are you doing?"
    n "What? How did you know I was in here?"

    e "That doesn't matter. "
    e "We know you are doing something dangerous, and that you are behind the strange things that happened lately."
    show professor sad at center
    n "Sigh. I guess the cat is out of the box. "
    show professor regular at center
    n "You are right about what I'm doing is suspicious, but it has nothing to with the recent events. "
    n "At least not in the traditional way."
    l "What do you mean by that?"
    n "You are bright kids, so you deserve to know. Ok, let me explain. "
    "Huh? He's only seen Richard and me once, and he doesn't even know Emi... "
    show professor alt regular at center
    n "This here is an experiment that is able to prove the Everett interpretation of quantum  mechanics."
    show richard alt neutral at left
    r "You mentioned something like this in your lecture. Didn't you say it was only  theoretical?"

    n "I did. And it is. Because no reasonable scientist would accept a proof like this. "
    show professor regular
    n "You see, this apparatus here creates a quantum event with two possible outcomes."
    n "According to Everett, this creates two seperate realities which stand in superposition. "
    n "It is connected to this machine gun. Whe-"
    show emi angry at right
    e "A machine gun?! Are you insane? Where did you get that from?"
    show professor alt surprised
    n "Yes, I am. Surprised you didn't notice. "
    show professor alt regular
    n "And I stole it. Now if you let me continue... "
    show emi neutral at right
    n "When the quantum measurement is 1, the gun fires. If it is 0, it doesn't. This is done once per second."
    r "For what purpose? How does this prove anything?"
    n "Normally, when I step inside the shooting range, I die after a few seconds, right? "
    n "But according to Everett, there is always one world in which I am still alive. "
    n "That is the  only one I can perceive. "
    n "So, if I'm not dead after a few minutes, I know with extremely high certainty if Everett was right or not."

    show professor alt regular at center
    
    r "This is madness! Putting your life on the line so easily..."

    l "...and? Did you already try it?"

    show professor alt happy at center
    n "Yes, I did. Everett was correct."
    show emi alt neutral at right
    e "But why are you continuing then?"
    show professor alt regular at center
    n "Simple. There is a neat side effect to this experiment..."
    n "The longer you do it, the higher the probability becomes that something, {i}anything{/i}, stops the experiment."
    n "For instance, at some point, it is more likely that a blackout turns the machine off than it is me continuing to survive."
    show richard neutral at left
    r "So that's what caused the city wide blackout two days ago?"
    show professor regular at center
    n "No, you misunderstand. I didn't cause anything."
    n "The loud sound you heard yesterday was caused by a small gamma ray, which had some interesting effects on the atmosphere."
    n "Some disruption in the earths crust changed the magnetic field in this area temporarily, which confused birds. "
    n "All these events are complete coincidences. They could happen anytime."
    n "What they had in common though, was that they stopped my experiments. "
    n "The gamma ray was small, but it directly hit my machine. "
    n "The changes in the magnetic field also stopped my machine from working."
    n "And I can guess you know what the blackout did. "
    show professor happy at center
    n "This machine... it is not just good for proving Everett right, it basically functions as an 'improbable scenario generator'."

    l "I see... I think I understand what you are trying to achieve."
    show professor regular at center
    n "Yes. I want to see where the limit is. "
    n "I want to know how far I can go with this. "
    n "I shielded myself so that the things that have happened won't happen again..."
    n "The result is that the coincidences become more and more major. "
    show professor alt regular at center
    n "There could be laws of physics, undiscovered because they only take effect in extreme situations."
    n "There could be more to this universe than we can see. With this, I can break the walls confining us, see beyond!"
    show richard alt at left
    r "This is madness! We can't let you continue."
    show emi angry at right

    e "Right! Killing yourself in every world that is not like you want it? It's stupid, to say the least."
    stop music fadeout 2
    "This man... we share the same view on the universe. But he isn't afraid. He boldly goes forward to satisfy his infinite curiosity."
    "But is this really ok? Can I let him continue?"

 
    menu:
        "Let him do it." :
            jump let_him

        "Stop him." :
            jump stop_him

label let_him:
    
    play music "music/graveyard.mp3" fadein 2
    l "Let him do it."
    e "What? Have you gone crazy too?"
    l "He already made up his mind. He found his path to the true nature of reality. "
    show emi neutral at right
    l "I don't think we should stop him from achieving his dreams."
    show richard dreamy at left
    r "His dream..."
    show professor happy at center
    show richard alt neutral at left
    n "Thank you. You and I, we are true scientists."
    show emi puzzled at right
    e "I don't know about this... but it's not really suicide, right? Maybe it is ok?"
    show professor regular at center
    n "I should say farewell to you then. In a few hours, there will be billions of worlds in which I have died. "
    show professor sad at center
    n "You are most likely to find yourself in one of them."
    show professor regular at center
    n "Up to now, it has been one unbelievably large coincidence to you that I survived all of my experiments. "
    n "From your perspective, at least."
    n "Good bye. I am sure you will find your own way one day."

    jump mixed_feelings_end

label stop_him:
    
    play music "music/graveyard.mp3" fadein 2
    show emi neutral at right
    l "Professor, there is another reason for this, am I right?"
    show professor regular at center
    n "What do you mean?"
    l "You continue now because you want to see the truth behind our existence."
    l "But when you first did the experiment..."
    l "...there was a very high probability for you to just die, with no other backup versions of yourself."
    l "Wasn't that a suicide attempt in disguise?"
    
    show professor sad at center
    n "..."
    l "If you are like me, and don't absolutely believe in anything, then the risks would have been way too high for you to do such an experiment."
    show professor happy at center
    n "You are right... again. Haha. "
    show professor sad at center
    n "I didn't even want to admit it to myself, but I guess I have to look the truth in the eyes."
    show richard alt neutral at left
    r "So you actually wanted to die?"
    n "Yes, a part of me certainly wanted to die. "
    n "The other part wanted the experiment to succeed. "
    n "It was a win-win situation if you think about it, really."
    show emi alt puzzled at right
    e "But why?"
    show emi alt neutral at right
    show professor alt regular at center
    n "My ideas about the universe are grand. My imagination goes beyond that of the regular person. "
    show professor alt sad at center
    n "But my colleagues mocked my visions. They mocked my work, and with that, my very existence."
    n "I failed in the past... I had theories everyone said were wrong, because they were too distant from their so called 'reality'. "
    n "And it turned out I was wrong. But I kept on going, doing allegedly 'crazy' theoretical work."
    show professor alt regular at center
    n "Most of it is neither provable nor falsyfiable today, so it remains controversial at most."
    n "This machine is my only success in life."

    l "And so you wanted to prove them wrong."
    n "Exactly. This experiment was not my idea, but it represents the kind of science that is frowned upon. "
    show professor regular at center
    n "That's why I wanted to show them, show to myself, that reality is stranger than human imagination."
    show professor sad at center
    n "And should I have failed... it wouldn't have mattered anymore."
    show richard neutral at left
    r "I am sorry. We didn't know about your hardships. "
    r "But you understand why we can't let you continue, right?"
    show professor regular at center
    n "Yes, I understand. And it is alright. After all, I expected this to happen. "
    show professor happy at center
    n "You coming here is also just a huge coincidence. But it is more probable than me continuing to survive my experiments."
    n "In another world, I do continue, and hopefully reach my goal."
    show professor alt happy at center
    n "There are near infinite worlds, and this happens to be one in which I am stopped. I accept that."
    n "It's just like the inflation field. Ahahah."
    "What does he mean? Well, it doesn't really matter."
    show emi alt regular at right
    l "Glad you came to your senses, Professor Netroufal."

    scene black with slowfade

    "After that, we all continued a mostly normal day, as if nothing happened."

    jump true_end


label mixed_feelings_end:

#    stop music fadeout 2
    scene black with slowfade
#    play music "music/graveyard.mp3" fadein 2
    "It did not come as much of a surprise, but it was a shock still."
    "Instead of giving his lecture, it was announced today that Professor Netroufal commited suicide."

    scene cafe with slowfade
    show richard dreamy at right
    show emi sad
    
    r "Such dedication... For a single person to kill themself in billions of worlds, in order to achieve their dream. "
    r "Can it really be called dedication? Or was it just recklessness?"
    show richard neutral at right
    e "One thing is for certain. He must have been mad inside to continue with his experiment."
    e "He did not care one bit for the conventional ways... it is sad he is gone from this world."
    show emi neutral
    l "As far as we know, he is still alive, somewhere. It's as if he moved away. "
    l "Somewhere where he can see beyond... I kind of envy him."
    e "You're not thinking of doing the same as him, do you?"
    l "Don't worry. I won't do it, as long as I have other options."
    "And I'd be too cowardly anyway..."
    l "I know now that at least one possibilty exists. "
    l "I'm sure there are other ways to achieve the same goal. Safer ways."
    show richard happy at right
    r "Good to see this whole incident didn't discourage you. "
    r "Truly, you have an iron will."
    "I just hope he really reached the world he wished for..."
    
    jump game_over

label true_end:

    stop music fadeout 2
    scene cafe with slowfade
    show richard dreamy at right
    show emi neutral
    play music "music/happy.mp3" fadein 2
    r "Such dedication... For a single person to kill themself in billions of worlds, in order to achieve their dream. "
    r "Can it really be called dedication? Or isn't it just recklessness?"
    show richard neutral at right
    show emi regular
    e "One thing is for certain. He is filled with madness. "
    e "He does not care one bit for the conventional ways... how admirable."

    l "I wonder if he could have done it..."
    show emi neutral
    l "To observe new physical phenomena in order to learn more about the true nature of this universe. "
    l "I must admit, I can totally understand his curiosity."
    l "Maybe I would even have done the same if I were in his position, and weren't such a coward."
    show emi alt regular
    e "There is nothing cowardly in not commiting billions of suicides."
    show richard happy at right
    r "That's a statement I would sign at any time."
    show professor happy at left
    n "Don't worry, you will find your path."
    l "Professor Netroufal!"
    n "Please, I told you you can just call me Professor Dr. Netroufal. Ahaha."
    show emi alt neutral
    show richard neutral at right
    r "..."
    show professor regular at left
    e "..."
    l "..."
    show emi regular
    show richard happy at right
    e "So what are you doing here?"
    show professor alt happy at left
    n "I was walking on the street when I saw you guys inside. "
    n "I thought I'd just appear out of nowhere."
    show richard neutral at right
    r "Professor, there is something I've been meaning to ask you. "
    show richard dreamy at right
    r "Are you sure it is ok to give up on your dream?"
    show richard neutral at right
    show professor happy at left
    n "Give up? Who said I'd give up? This is only the beginning! "
    n "But, I won't do any life threatening experiments anymore. "
    n "At least not until I have given all my knowledge to the next generation."
    show emi alt happy 
    show richard alt neutral at right
    e "That is very wise of you, Professor N."
    show professor alt regular at left
    n "What, is Netroufal too long for you to say?"
    show emi alt regular
    e "Nah, but it sounds more mysterious. I think it fits you better."
    n "Hmm... you think so?"
    show richard alt dreamy at right
    "This might be my chance..."
    "Now I can ask him my question, which I couldn't get to do after the lecture."
    show emi alt regular
    l "Ehm... Professor Netroufal? There is something I've been meaning to ask you..."
    show professor regular at left
    n "Yes? What is it?"
    l "You are a {i}theoretical{/i} physicist, right?"
    n "That's right."
    l "Then, why are you wearing a lab coat?"
    show professor alt regular at left
    n "What do you mean?"
    n "Sorry, I don't understand your question."
    l "Huh?"
    show richard alt neutral at right
    r "You were driven enough into a corner to risk your own life... "
    show professor regular at left
    "But... even outside... why?"
    r "...and now that we stopped you from your last chance to fulfill your dream, you still don't give up?"
    r "You don't even seem to be distressed about it... Truly, strong dreams create stong men."

    scene black with slowfade

    "It seems that everything ended happily."
    "The walls that confine us to this existence, and hide what lies beyond... "
    "They don't feel so strong and ominous anymore. "
    "Volatile, almost."
    "I know now that I can try to see beyond them. It is not a useless endeavor."
    "In fact, if there is anything I am sure of, it is that I will continue to go on, until I am no longer physically able to."

    jump true_game_over


label true_game_over:
    stop music fadeout 2
    scene black with slowfade
    
    play music ("music/walls.mp3")

    show good credits:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        linear 240.0 ypos -13021
    centered ""

    stop music fadeout 1
    return

label game_over:
    stop music fadeout 2
    scene black with slowfade
    
    play music ("music/repitition.mp3")

    show bad credits:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        linear 240.0 ypos -13021
    centered ""
    centered "Try Again"

    stop music fadeout 1
    return
