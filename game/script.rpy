#'change'
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = Character( "eileen_happy.png"

init:
    
    image black = Image("pics/black.jpg")
    image bg hallway = Image("pics/tu_hallway.jpg")
    image bg office = Image("pics/office.jpg")
    image bg street = Image("pics/street.jpg")
    image lecture = Image("pics/lecture.jpg")
    image richard room = Image("pics/richard_room.jpg")
    image hilfer = Image("pics/maria_hilfer_strasse.jpg")
    image Zentralfriedhof = Image("pics/zentralfriedhof.jpg")
    image wien energie = Image("pics/wien_energie.jpg")
    image cafe = Image("pics/cafe.jpg")
    image boltzmann grab= Image("pics/boltzmann_grab.jpg")
    image confrontation = Image("pics/confrontation.jpg")
    image basement_door = Image("pics/basement_door.jpg")
    image tu parking = Image("pics/tu.jpg")
    image lecture  = Image("pics/lecture.jpg")
    image wolken = Image("pics/black.jpg")
    image playground = Image("pics/black.jpg")
    image ludwig home = Image("pics/ludwig_home.jpg")
    image credits = Image("pics/credits.png")

    image emi sad = im.FactorScale("pics/emi_sad.png", 0.45)
    image emi happy = im.FactorScale("pics/emi_happy.png", 0.45)
    image emi neutral = im.FactorScale("pics/emi_neutral.png", 0.45)
    image emi puzzled = im.FactorScale("pics/emi_puzzled.png", 0.45)
    image emi regular = im.FactorScale("pics/emi_regular.png", 0.45)
    image emi alt regular = im.FactorScale("pics/emi_alt_regular.png", 0.45)
    image emi alt happy = im.FactorScale("pics/emi_alt_happy.png", 0.45)
    image emi alt neutral = im.FactorScale("pics/emi_alt_neutral.png", 0.45)
    image emi alt puzzled = im.FactorScale("pics/emi_alt_puzzled.png", 0.45)
    image emi alt sad = im.FactorScale("pics/emi_alt_sad.png", 0.45)
    

    image emi young neutral = Image("pics/emi_young_neutral.png")
    image emi young angry = Image("pics/emi_young_angry.png")


    image richard neutral = im.FactorScale("pics/richard_neutral.png", 0.45)
    image richard dreamy = im.FactorScale("pics/richard_dreamy.png", 0.45)
    image richard happy = im.FactorScale("pics/richard_happy.png", 0.45)

    image richard alt neutral = im.FactorScale("pics/richard_alt_neutral.png", 0.45)
    image richard alt dreamy = im.FactorScale("pics/richard_alt_dreamy.png", 0.45)
    image richard alt happy = im.FactorScale("pics/richard_alt_happy.png", 0.45)


    image professor happy = im.FactorScale("pics/professor_happy.png", 0.45)
    image professor sad = im.FactorScale("pics/professor_sad.png", 0.45)
    image professor neutral = im.FactorScale("pics/professor_neutral.png", 0.45)
    image professor surprised = im.FactorScale("pics/professor_surprised.png", 0.45)

    image professor alt happy = im.FactorScale("pics/professor_alt_happy.png", 0.45)
    image professor alt sad = im.FactorScale("pics/professor_alt_sad.png", 0.45)
    image professor alt neutral = im.FactorScale("pics/professor_alt_neutral.png", 0.45)
    image professor alt surprised = im.FactorScale("pics/professor_alt_surprised.png", 0.45)


    # Declare characters used by this game.
    $ l = Character('Ludwig', color = "#c8ffc8")
    $ e = Character('Emi', color = "#C8FFC8")
    $ r = Character('Richard', color = "#C8FFC8")
    $ n = Character('Netroufal', color = "#C8FFC8")
    $ ra = Character('Raphael', color = "#C8FFC8")
    $ fb = Character('Facebook', color = "#44619D")
    $ s = Character('Steinmeier', color = "#44619D")

    #Transitions
    $ nextday = Fade(0.5, 2, 0.5)
    $ slowfade = Fade(2, 0, 2)

# The game starts here.
label start:
    
    stop music fadeout 2

    scene wolken
    l "Why?"


    l "Why is there anything, instead of nothing?"
    l "Why do I exist? Is there a purpose?"
    l "Do I really exist? Does anything really exist?"
    l "Is it all just a huge coincidence?"
    l "Is there really a past and future, or is the now the only thing?"
    l "..."
    l "I don't know. I don't the answer to any of these questions."
    l "I don't even know if there is an answer, or if I could understand it."
    l "Most people would tell you that these are all questions for philosophers and theologists. But that doesn't help me."
    l "You see, I do not trust my own thoughts. Or the thoughts of others, no matter how trivial they seem."
    l "Logic can not be proven, because the act of proving is a tool of logic itself."
    l "If a stranger on the street told you to trust him, would you? Just because he told you so?"
    l "Call me paranoid, but I wouldn't. That is why I don't believe in anything, and there is nothing I trust one hundred percent."
    l "What I am looking for is something that can convince me of {i}anything{/i}."
    l "The most promising path to that goal seems to be science."
    l "My words contradict each other, but I can not afford the luxury of living without contradictions right now."

    scene playground with fade
    show emi young neutral at right
    l "Ahh..."
    e "Hey Ludwig, what are you spacing out about?"
    l "Huh? Oh, it's you Emi."
    e "You didn't even see me coming? Where are you with your mind?"
    l "Ehm... Nowhere... I was just thinking about some things."
    e "Like what? How you can concentrate better at school?"
    l "No! Just... about the meaning of existence."
    e "The existence of what?"
    l "Me, the universe,... everything."
    e "Huh? What for? It's pointless."
    l "Pointless? Why?"
    e "Because there is no mystery! It is useless to spend all your life thinking about something that is not there. The way this world works is simple. You are born, go to school, get a job, marry and get kids. Then the cycle restarts. See? There is no place for unneccasary questions. How does thinking about unsolvable questions improve your life?"
    l "Imagine... you were thrown in a complex of white rooms. Together with people of all ages and races. None of them have any memories from before they appeared there, including you. The rooms provide everything you could possibly need in daily life. Do you really say there is no mystery in that? How is this different from reality?"
    e "Hmm... you do have a point there. But still, how could you ever find the truth? It is simply not possible."

menu:
    "How do you know it's impossible?":
        jump A1
    "I'm... abnormal?":
        jump A2

label A1:
    e "Recorded history goes back thousands of years. Many people have tried, but no one found any answers. Most of them were very depressed and had no life. They died sad, because they failed. The same will surely happen to you too, if you try the imposssible."
menu:
    "I don't care":
        jump A11
    "Maybe you are right... ":
        jump A12

label A2:
    hide emi young neutral
    show emi youg angry at right
    e "Of course you are! Look at everyone else, they are enjoying being outside. "
    e "And what are you doing? You always lose yourself in your thoughts. Be it in school or outside, you never concentrate on anything!"
    e "Why can't you just be normal and talk to people?"
    l "I... never really thought about it."
    e "It's time for you to adopt, or you will forever be an outcast."

    menu:
        "You are right...":
            l "I really do behave weird, don't I? Maybe I should start being more normal..."
            e "Glad you came to your senses. Now come, the next lesson starts soon."

            jump BadEnd1

        "Who cares?":
            l "An outcast? Who cares cares about that?"
            l "What does it matter if society rejects me? I choose my own path. I'm sorry you don't like it, but that doesn't change my decision."
            e "Ahhh... you are hopelessly stubborn. You will see where this kind of attitude will get you."
            jump Hallway
    
label A11:
    l "It's still better than living the hollow life that you propose. I would much rather die having tried to pursue my ambition."
    e "What a crazy person..."
    
    jump Hallway
    
label A12:
    l "No one before managed to do it, why should I? How silly of me."
    e "Glad you came to your senses. Now come, the next lesson starts soon."
    jump BadEnd1


label Hallway:
    scene bg hallway with fade
    "I wonder how many weeks it has been now since I joined university? It must be at least eight. I think I am slowly getting used to it here. It is definitely better than school. Finally I can decide by myself what classes I want to attend... This way, I can fully concentrate on my future. I just hope I don't drop out... My grades have always been good to average, but physics is really hard. Wait, what am I thinking? I already decided that I will become a physicist! If I fail I'll try again. How else am I supposed to learn the secret of the walls? What lies beyond them, and who constructed them for what purpose? This is the future I have chosen.... , and I will see it through."
    show emi alt happy at center
    e "Hey, Ludwig! Hi! We don't meet often between lectures, do we? Haha"
    l "Hi, Emi."
    show credits at center
    "This is Emi. We've known each other for several years. We went to the same school for two years."
    "We got along, but I wouldn't say we were friends. When I had to change schools, we lost contact. But now she attends the same university as me, the TU Wien. I study physics, she math. We met by chance soon after we started, and quickly became friends. She changed quite a bit..."
    e "What was that lecture you just came out of about?"
    l "Oh, it was about thermodynamics. An introduction to entropy. What did you have today?"
    e "Sounds like fun. Actually, I wasn't in a lecture today. I just came here to do some research in the library."
    l "What are you working on?"
    e "Ah, just my own little theories on formal systems and completion. I have some ideas that seem really crazy, and now I am trying to find out why they wouldn't work. I'd tell you about them, but I fear a non mathematician wouldn't understand it, haha."
    l "Gee, thanks. And don't call yourself a mathematician yet! You just started studying."
    e "I am a mathematician at heart already. By the way, do you want to hear some rumors?"
    "To be honest, I really don't like rumors. Incomplete or untrustworthy information makes me uncomfortable. But Emi loves them, and I don't think she has many other friends at university, so I can't really reject her."
    l "Not really, but tell me anyway."
    e "Alright! Massive flocks of birds have been sighted, and they are all flying east. East! Birds usually fly either north or south, but not east! And it wasn't just one species of bird, but several. Biologists have no idea what causes it. The internet speculates that this is the first sign of the apocalypse."
    l "Hmm, that is weird, if it's true. But I wouldn't trust the internet's diagnosis on such matters."
    e "Me neither, but it's still cool to think about."
    l "Maybe. Anyway, I have to go to the next lecture. See you later."
    e "See ya!"
    jump Lecture1

label BadEnd1:
    scene black with slowfade
    centered "20 years later..."
    scene bg office with slowfade
    "*click click click*"
    "..."
    "*click click click*"
    "Ugh... I wonder wonder when I can go home? It's already past eight... but I can't leave until I've finished this report on the sales of the last quartal. Well, at least this job pays well."
    "*ring ring*"
    "*pick up cell phone*"
    l "Hey Raphael, what's up?"
    ra "Hi Ludwig! How are the wife and kids doing?"
    l "Fine, thanks for asking."
    ra "I just wanted to ask if you wanted to catch the football game tomorrow."
    l "Sure! It will be an interesting match, there's no way I'm going to miss that."
    ra "Great! Then we'll just call each other tomorrow, alright?"
    l "Yeah. Until then."
    ra "Bye"

    "..."
    "......"
    "........."

    "Why do I feel so empty? I feel like there is something I have forgotten about... Whatever it was, it's too late now. I should just get back to work, so I can catch some sleep at home."

    "*click click click*"
    "..."
    "*click click click*"

    jump game_over


label Lecture1:
    scene lecture 
    show richard dreamy
    "This lecture is special, and one that I've particularly been looking forward to. The lecturer is Professor Dr. Dr. Netroufal. He's been in universities abroad for a few years, and recently came back to Vienna. The subject is quantum mechanics. It usually doesn't start so early in the studies, but that is why this lecture is special. It is the Professors field of expertise, and it is sort of his 'welcome back' gift to us, the students. Anyway, I should find a seat. Damn, I should've come earlier, it's packed in here... The only free seat left is in the center row. I don't really like it there, but there's nothing I can do about it now."

    l "Excuse me, is this seat taken...?"
    hide richard dreamy 
    show richard neutral
    r "Huh? Yeah, sit down if you want. Seems to be the last one."
    l "Yeah. Thanks."
    r "Man, I hate the center row."
    l "Really? Me too!"
    "I like to sit in the last row, where nobody is behind me who could see me. I'm uncomfortable when a lot of people can watch me, even if I'm not at the center of attention."
    r "Aha! I see we are alike! Truly, the first row is the best. I can't stand having to see so many other people in front of me."
    "well..."
    l "It simply disgusts me, you know. Most young people are a disgrace to mankind. All they think about is how they need to have the newest phone, watch TV, repeat what is told to them by the media, and so on. But the worst thing is, they are lazy. They don't have a goal to accomplish. They aren't alive, they just live."
    r "I agree with you. Most of them are just annoying."
    l "Oho! You share my views! This is rare. That must mean that you are different... Say, do you have a dream?"
    r "I guess you could say that. I want to solve the mystery of existence."
    l "You mean... answering the fundamental questions mankind has been asking for millenia?"
    r "Well... yes."
    l "You attempt to do what the most brilliant minds humanity had to offer failed at?"
    r "You think it's foolish, don't you?"
    l "The opposite is true! I admire you for your vigilence! You try to do the impossible, because it is your dream. There is nothing foolish in that."
    "Wow, that is the most motivating thing anyone ever said to me. Everyone else always tried to tell me I should do something normal..."
    jump Lecture2

label Lecture2:
    scene lecture 
    show professor regular
    n "Hello everyone. My name is Professor Dr. Dr. Netroufal. But you can just call me Professor Dr. Netroufal. Ahaha."
    "A few giggles came from the audience, but it remained mostly silent."
    n "I am a Professor of physics, and hold the title of doctor for mathematics and neurology. Today I will give you an overview of what I think is the most important concept of quantum mechanics."
    n "Let's start right away, shall we?"
    
    n "Most of you probably know that very very small object, like atoms, behave differently from the larger ones that we are familiar with. For example, an electron can be at two different places at once, whereas a melon can't. One common error is to think that we just don't know where exactly the electron is. That is partially true, but mostly wrong. We do not know where it is, because it really actually is at both places. But we can never see it in both places. But that is weird, isn't it? If something is, then it should be observable. Sadly, in the world of quantum mechanics everything is weird and different. When we observe an object in such a so called superposition, it seems to suddenly decide for one of the places randomly. We can calculate the probabilities for each event exactly. In fact, quantum mechanics is one of the most tested theories ever. "
    n "And not once has it given a wrong prediction. The results are correct. Every. Single. Time. The only problem is that we don't understand how and why it works. We know a particle jumps to a single place when observed. But it doesn't explain what exactly an observation is. Does it need humans? Does consciosness play a role in the laws of physics? Or is a single photon hitting it enough? This is the Copenhagen interpretation of quantum mechanics, and it leaves quite a few open questions. And yet, for a long time it was what most scientists thought was the correct way to see things. Today, they are not as sure. With good reason. There are alternative explanations for the phenomena we can observe. The most popular one of them is the Everett interpretation of quantum mechanics, also known as the many worlds interpretation."
    n "You may have heard or read about it in various science fiction stories. But I want you to understand that this is NOT just fiction. Now, let's think about what actually happens when we observe something. Let's take the most simple scenario, with a single electron. To measure something, we basically have to throw something at it, and see how that thing comes back to us. In this case we use a photon. But the electron is in superposition! How does it reflect the electron? The answer is simple. The photon is reflected by both states of the electron, and is itself now in two positions at the same time. It is also in superposition. Eventually, it hits one of our detectors. This detector, too, is put into superposition of two states."
    n "And when we look at the results of the detector, our whole brain is put into a superposition of thinking the electron is at either one place or the other. Both of these states are equally real. But because of how our brain works, we can only consciously feel ONE of them. If you want, you can call these other states parallel universes. But they are actually all part of one big, strange universe. And that is the Everett interpretation. If you ask me, it follows a much simpler logic and requires less magic. But of course, it also changes our view of the world completely. And extraordinary claims require extraordinary evidence. Can we produce such evidence? There are some theoretical possibilities. But that is a story for another day."
    n "I'm done here."

    "Wow, what a lecture. I'd like to ask him some questions... but appearently so do many others. Should I try to go and talk to him?"

menu:
    "Yes":
        jump StreetRichard
    "No":
        jump StreetEmi

label StreetRichard:
    scene bg street
    show richard happy
    r "Oh, hello Ludwig. Did you catch the professor?"
    l "Hi Richard. No, too many wanted to talk to him. After the first three people, he just went to his office."
    r "What a shame. If you want, we can go right to my place and battle each other."
    l "I have nothing else to do, so yeah, why not."
    "I am curious what he is referring to when he speaks about battling..."
    r "Alright, then let's go."
    l "So, why do you study physics?"
    r "I honestly am not sure if this is the right direction for me. I changed studies three times now."
    r "Jura, logic, medicine... They all couldn't ignite the spark in me to get me burning. I still haven't found my true passion,"
    r "which is what I really want: finding something that truly fulfills me. Something I can get lost in."
    r "Work that I truly love. Sadly this is not easy to come by. I do not have a dream like you do. So I keep on searching, until I find it."
    r "I must admit, I envy you for already having found yours."
    l "I am sure that you will find your dream soon enough."
    r "I hope so."
    "After walking for a few minutes, we arrived at Richard's home."

    jump HomeRichard

label StreetEmi:
    scene bg street
    show emi happy
    e "Hey Ludwig."
    l "Hey Emi. How was your math lecture?"
    e "Very interesting. Our professor Dr. Steinmeier spoke about randomness and if it could really occur measurably to a larger scale than quanta. It got a little bit philosophical but his opinion is that there is no randomness in math and therefore no randomness in the real world. I brought up the Chaos theory and he said that it only seems random to us and that by knowing all the information about the system from an outside view, it could be predicted perfectly. I argued that we will never be able to do that and and therefore it doesn't matter and is in fact random to us. He replyed with a smile on his face: It is not about us, it never has been. It is about the fact that all the information only leads to one possible outcome, which is already determined and we are only part of a program that is following its rules until it's completion."
    e "I really hate these 'Oh, look at me, I am so smart' kind of people. But it made me think. Does life matter in the end? And how should we use it?"
    l "I have thought about this for a long time as well. Most people say there is no answer, but I think that as long as we do not know everything there is to know about the universe, then we are not allowed to accept an answer like that."
    e "I like that attitude of yours."
    l "Thanks."
    l "(thought)...Since when does she agree with me on such things?"
    e "Anyway, I have to get going now. It was nice chatting with you!"
    l "Yeah, likewise. Bye."
        
    jump HomeRichard

label HomeRichard:
    scene richard room
    show richard at left
    
    r 'Welcome to my home. I am very sorry for the mess, but I did not have enough time to tidy it up.'
    
    hide richard
    
    "..."
    "What mess?"
    
    show richard at left
    
    r "Thank you for accepting my invitation. I do not often have guests. Do you want something to drink? I've got Orange juice, beer, wine and water."
    
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
    hide richard
    "..."
    show richard
    r "Here."
    l "Thank You."
    "Gulp..."
    l "That was refreshing"
    jump battle
    
label nodrink:
    r "Alright."
    jump battle

#battleships

label battle:
    scene richard room
    show richrad ragular at left
    r "Now, we are ready for an epic battle of intellect." 
    r "A one on one in an ancient competition that the smartest brains of all cultures play to determine the very best." 
    r "In world championships, the best player in the world is able to defeat all his opponents and crown himself as king." 
    r "Only those who can put themselves into someone else's mind and understand their opponent's train of thought will have a chance to win." 
    r "Do you know what I am talking about?"
    
menu:
    "It's got to be Chess":
        jump battleship
    "I assume you are talking about Go":
        jump battleship
    "Tic Tac Toe?":
        jump battleship
    
label battleship:
    hide richard
    show richrad happy at left

    r "Ahaha, good joke buddy"
    r "I am of course talking about Battleship!"
    r "Let's start!"
    
    hide richard
    "..."
    "Time has passed."

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
    show richard
    r "The field A3 is occupied by..."
    r "Water, you have missed!"
    r "I shoot the field E7"
    l "Damn. On the field E7 is..."
    scene black
    "*Lights go off*"
    jump lightsoff

label A7:
    $ battleshipwon = True
    show richard
    r "The field C4 is occupied by..."
    r "...the last part of my last destroyer, you have won!"
    r "Congratulations! I am happy to finally have found a worthy opponent."
    r "I hope we can play..."
    scene black
    "*Lights go off*"
    jump lightsoff
    
label lightsoff:
    r "What happened?"
    l "Maybe the bulb died"
    r "No, I bought it from a passionate engineer, who builds them on his own."
    r "The bulb should last longer than the sun."
    r "It must be a blackout. Just look out of the window."
    r "Everything is dark. It seems to be city wide."
    r "I am sorry, but you have to leave."
    r "Chances like this do not present themselves very often."
    l "What are you talking about?"
    r "I can't tell you anything now."
    r "Meet me tomorrow at the Mariahilferstraße near Neubaugasse at 2pm."
    l "Ok..."
    jump Home1

label Home1:
    scene l
    "Ahh, finally home."
    "This blackout is unusually long and seems to affect the entire city."
    "I had to walk by foot, since the trains were stopped."
    "Man, it was chaotic out there..."
    "Everyone was in confusion."
    "Fortunately, I have a flashlight on my phone."
    "Otherwise, I'm not sure if I'd found my way home."
    "But the blackout is over now."
    "I surely can't sleep now."
    "I'm way too curious about what's going on with Richard."
    "What did he suddenly have to do?"
    "Maybe I could cool down a bit by browsing the web."
    "*click*--PC boots"
    "Ok, step by step: First I enter Mr. Braun's Wifi..."
    "*click*--connected"
    "Now I connect to my dutch VPN..." 
    "Wouldn't want the NSA to know everything about me."
    "*click*--connected"
    "Alright, I am in stealth mode. What's next?"
    "What do people do when they browse the web without a specific goal?"
    "Hmm..."
    "I could go to Facebook, it's been a while."
    "..."
    "And I'm logged in"
    "So what have people been up to?"
    fb "\"Melanie Bauer: My teacher tried to tell me that our sun was a star. So stupid, it is a sun, that's why its called sun and not star xD\""
    fb "\"12 people liked this\""
    "Wow"
    "*defriended*"
    fb "\"Gustav Müller: My gf and me *_*\""
    "And that is of interest to me because...?"
    "I remember now why it has been a while."
    fb "\"Emi has sent you a message!\""
    e "Hey!"
    "Oh right, people on this network see when I am online."
    l "Hello"
    e "Did you notice the blackout?"
    l "Yes, I did."
    e "Very mysterious..."
    l "Not really, that happens about every 5 years."
    e "It was the whole city! That has not happened in at least 50 years..."
    l "Random, it will eventually happen, so that's also not very mysterious."
    e "I don't think so. I feel something strange in the air... I want to investigate. Wanna come with me?"
    l "Not really"
    e "..."
    l "Where would you even investigate and what?"
    e "Well, for example, I would start at Wien Energie"
    l "I am sure you could just wait and read the newspaper tomorrow”"
    e "As if they were honest..."
    l "Meh"
    e "Call me if you change your mind, alright?"
    l "Ok"
    jump mariahilferstrasse

label mariahilferstrasse:
    scene hilfer
    "I wonder what Richard was up to last night..."
    show richard neutral at right
    r "Hey Ludwig!"
    l "Hey Richard."
    "He is still wearing the same clothes as yesterday and looks terrible tired."
    "I'm sure he has not caught a lot of sleep last night."
    r "am sorry that I had to made you leave last night."
    r "You know the feeling when you are somewhere in the countryside and there are hardly any lights and you look up to the sky and acknowledge its beauty?"
    r "In Vienna I miss this sight. Yesterday all the lights went out."
    r "It was magnificent."
    r "I once tried to be a photographer, but it wasn't really my passion."
    r "However I liked to take those long exposure night sky pictures where you expose the film for hours to only the night sky and the motive."
    r "In the picture you get, you can see the stars forming circles around the spinning axis of earth."
    r "Getting a picture like that in Vienna is usually impossible. The city is too bright."
    r "The motive Is the most iconic place in Vienna, the TU."
    r "It is just the most perfect picture that I have ever and will ever have taken."
    r "I don't know if there was a picture like that before, it might be the best photo of the TU ever made."
    l "Amazin, show it to me!"
    r "I am very sorry, but i can't do that, Ludwig."
    "What? Why wouldn't he show it to me?"
    r "This photo is nothing the world should se, I will in fact only show it to one person at all"
    l "Aha..."
    l "Which person would that be?"
    r "I don't know yet"
    "Wait a minute, the blackout lasted for 1 hour, and I am pretty sure these photos take time when it comes to set up."
    "Also, how would he know when to stop before the blackout ends?"
    "And he could have gone home afterwards to catch some sleep..."
    "And he surely would have changed his clothes..."
    "Is he telling the truth?"
    "*A loud sound comes from the sky*"
    jump cafe1

#Lukas
#cafe 1
label cafe1:
    scene cafe
    show emi happy at left
    show richard regular at right

    e "I'm glad you reconsidered, Ludwig! Finally, I don't have to do this investigation on my own."

    "Not one minute after that strange noise came from the sky, Emi called me."
    "Such a thing has never happened before, so I agreed to join her investigation."
    e "I would really like to figure out what that was."
    l "No problem. By the way, this is Richard. I met him in class."
    r "Hello"
    e "Oh, hi. I'm Emi, Ludwig's childhood friend."

    "I don't know if I would call it that, but whatever."
    e "Do you think he has the skills to join our team?"
    l "Yes, I'm sure he will be able to provide valueable insight."
    l "But shouldn't you ask him first if he even wants to?"
    r "I would like to join you. This seems like it could become a great adventure..."
    r "...and that is where dreams are born."
    e "Great! Now we just need a strategy. Let's think about what has happened."
    e "Birds have been sighted flying in the wrong direction, en masse."
    e "Also, various electronics were damaged or stopped working, for appearently no reason."
    l "I don't know much about biology or birds, but maybe a weather change urged them to change course?"
    r "Or maybe some evil organization is conducting experiments on the earths core, disrupting the magnetic field."
    r "And the electronics all belonged to their enemies."
    e "You mean like the Illuminati?"
    r "Probably."

    "Doubts about this operation are starting to rise inside me."
    
    r "Anyway, then we had this large scale blackout."
    l "Those things just happen."
    e "Yeah, but the timing is very weird. Just to be safe, we should check out the electricity supplier, Wien Energie."
    e "And a few days before that, there was a blackout in the university."
    r "You think there is a connection?"
    e "It seems plausible."

    "Hmm, I hadn't thought of that. That is suspicious."

    l "But the strangest thing of all is that sound we just heard half an hour ago."
    e "Ah, yes. About that, I did some quick research before I left the house."

    "So that's what kept her so long..."
    e "According to my sources, the epicenter of the sound was the central cemetary."
    l "The cemetery? Why there?"
    e "I don't know. That's why we should go there to check things out."
    r "I recommend that we split up."
    r "You two go to Wien Energie while I do some investigating in the university."
    r "After that we meet up at the central cemetary."
    e "Sounds like a plan."
    l "Alright, let's go."


#wien einergie

label wien_energie:
    scene wien energie
    show emi alt regular at right

    l "We are here. What now? It's not like we can just look at the facility and find out what caused the blackout."
    e "We can't?"
    l "Ehm... I thought you had a more elaborate plan."
    e "Don't worry, I have a plan."
    e "I'll try to find someone who works here and ask him some questions, and you should try to find something out by looking at the facility."

    "..."

    "And she's gone."
    hide emi
    "Well, let's see. There is nothing here."
    "I can't go over the fences, and I see no one I could talk to."
    "Time for browsing the internet on my phone."
    "..."
    "The news say that the blackout happened because a few employees messed up at inconvenient times."
    "Just the kind of thing I expected. But I don't think Emi will believe the news."
    "Ah, she's coming back."
    show emi alt happy
    e "Did you find anything?"
    l "No, how should I? Access is restricted."
    e "Too bad... I had hoped you somehow managed to learn anything anyway."
    e "But it doesn't matter, I just talked to an employee. He said he was terribly sorry, and that the incident was kind of his fault."

    e "Looks like there is more than one way to the truth."
    "..."
    "Now seems to be a good time to ask..."
    l "Hey, Emi. I've been meaning to ask you something."
    e "Huh? What is it?"
    l "Do you remember when we were back in school?"
    e "Sure."
    l "Well, you changed since then..."
    l "Back then you thought it was unreasonable to try to solve the big questions..."
    l " you said that career was everything, and one should just try to be content with what he has."
    e "Oh, it is unreasonable. But I came to the conclusion that not everything has to be reasonable."
    l "How?"
    e "Well, I remember beeing a real grey face, the 'NO FUN ALLOWED' type."
    e "I thought that everything had already been sorted out, that there was one acceptable way to behave and think."
    e "And people who didn't fit that pattern disturbed me."
    e "'Why won't they just be normal?', I thought."
    e "It annoyed me, and made me a grumpy person, without realizing it."
    e "And then, one day, I suddenly understood the reason  why I was always upset with people. And then I thought, 'Maybe everything isn't already sorted out."
    e "Maybe people who act abnormally in my view just don't agree with the views of others."
    e "Maybe every view is valid in its own way."
    e "And, maybe, I shouldn't care so much about that, and let everyone be themself.'"
    e "And as soon as I changed my own view of the world a little bit, I realized I really don't like the standard norm."
    e "Apparently, my personality also changed to show that new view."
    l "I understand... so that's why. But how did you come to this enlightenment?"
    e "Well, it was more of a stretched out process, with several factors, but I'm sure our conversations in school were a large contribution."
    l "Really?"

    "I've always seen myself as more of an observer."
    "I didn't really think"
    "I also affect the people around me..."
    "It seems silly, but only now I fully realize that fact."
    e "Yes, really. Now let's meet Richard and see what he found out."




#zentralfriedhof

    scene Zentralfriedhof
    show richard neutral
    l "Hi Richard."
    e "Hi! Did you find any clues?"
    r "Hello everyone. Yes, I heard some suspicous things, but nothing conclusive I'm afraid."
    r "The blackout happened at around the same time as the city wide blackout, the difference was just ten minutes."
    r "A connection seems plausible, though still unlikely. Some professors who have known him for a long time are worried about Professor Netroufal. Sadly, I don't know about what or why."
    r "Lastly, I heard some rumors about stolen weapons. It was just in passing by, so I'm afraid I can't tell you more."
    e "Wow, that is a whole lot more information than Ludwig and I got. Let's try to make sense of it later, now we should focus on investigating here."
    l "What exactly are we looking for here?"
    e "Anything suspicious! You will know it when you find it. Probably. We should split up again, so we can cover a larger area."

    "15 minutes have passed."
    "Emi said she'd talk to the priests of the church. Richard and I have been aimlessly wandering around."
    "I can't see anything that could have produced such a sound. Did it really come from here?"
    "But it also seemed to come from above... was it a message from God?"
    "What a ridiculous thought."
    "Oh, I found Richard. He's standing in front of some beautifully decorated graves."
    "He looks really lonesome and lost in thought... as if he were lamenting something."
    "Should I go up to him? Or should I leave him alone?"

    menu: 
        "Go":
            $ graveyard_talk_richard = True;
            jump go

        "Let him be":
            $ graveyard_talk_richard = False;
            jump let_him_be


label go:
    scene boltzmann grab
    show richard sad at right
    "Let's see what he's doing there."
    "He looks so deep in thoughts, I don't want to say a word. Better just stand next to him."
    
    "..."
    "..."
    "..."

    r "Do you know who is buried here?"
    l "No."
    r "Take a look at the gravestone."

    l "There is a formula engraved in it..."
    l "S = k * ln W"
    r "This is the formula for entropy."
    r "The one who lies here is none other than Ludwig Boltzmann. One of the greatest scientists of Austria. He's right up there with Schrödinger."

    l "..."
    r "He showed that the second law of thermodynamics is nothing other than a statistical emergence. He also devised this formula for entropy."
    r "But many physicists disregarded his ideas, his entire life's work, because they refused to believe in something such as atoms, which was a vital assumption."
    r "In the end, Boltzmann commited suicide out of great depression."
    r "A few years after his death, the existence of atoms was confirmed."
    l "How sad..."
    r "Humans are machines that turn dreams into reality."
    r "Great souls reside within those with great dreams. But every soul is vulnurable, for it is human."

    l "..."

    "We continued to stand there for some more minutes in silence."
    "At some point Emi joined us. She didn't hear the story, but could read the atmosphere."
    "We then returned to the cafe."

    jump cafe2

label let_him_be:

    "He probably wants to be alone for now. I should go somewhere else."
    
    "walk walk"

    "walk walk"

    "No, I really don't know what I'm doing."
    "But it still was a good idea to come here. The scenery is beautiful, and the atmosphere chilling."
    "..."
    "There comes Emi."
    show emi regular
    e "Hey, Ludwig."
    l "Hey. Any luck with the priests?"
    e "Nope. I walked into the church and spoke to one of them."
    e "He kept talking about his delusions and tried to get me to join his club."
    e "I was annoyed by his close mindedness, so I tried the Turkey Curse on him, but then he threw me out."

    "The Turkey Curse? Is that a thing?"

    e "Anyway, I doubt he knew anything. Let's just return to our base."

    jump cafe2



#cafe2
label cafe2:
    scene cafe 
    show emi alt regular at right
    show richard alt neutral at left

    e "Okay, let's do a status report. I'll start."
    e "The huge blackout seems to have actually been an accident. I got this information by someone who claims to be partially responsible."
    e "No one at the Central Cemetary had any valueable information about the loud sound."
    l "I didn't really know what to look for, so I didn't find anything."
    r "Aside from some rumors, I found out that the blackout at the TU in the week before was at around the same time of day as the city wide one yesterday."
    e "Hmmm..."

    "She looks jealous about the fact that Richard appears to have the best results."

    e "That sounds really suspicious. If someone caused the blackout deliberatley, why would they start at the TU?"
    e"And that hypothesis is also conflicting with the information I received."
    l "Maybe the person you talked to lied? Or he was just part of a much more eleborate plan?"

    "I don't really believe that, it's most likely just a coincidence."
    e "That could be."
    r "It seems that today's investigation brought up some interesting points, but nothing conclusive."
    l "It looks that way."
    e "Yeah, let's try to sleep over this, and maybe we come up with better ideas tomorrow."

    "And so the meeting was adjourned."

    jump home2


#home2
label home2:
    scene home
    "So that whole thing didn't help us at all. But I wouldn't call it a waste of time. I had fun after all."
    "I will relax with some internet for the rest of the evening."

    "let's try a sciencebord." 

    "'Hello /sci/entists. I want to become immortal. What field of science should I study?'"

    "Sage'd."

    "'Hey /sci/, if God doesn't exist, how come bananas are shaped exactly to fit our hands?'"

    "Even if you're being ironic, it's still... agh. Are there only bad threads today?"

    "'How do you know you aren't a Boltzmann brain?'"

    "Oh no, Boltzmann brains. They make me uncomfortable."
    "It's the idea that in an infinite equilibirum, it is more probable that your brain spontainiously pops into existence, instead of the entire universe existing, so it is more probalble, that you are just a produnct of randomness."

    if graveyard_talk_richard:

        "But I visited Boltzmann's grave today. Richard told me a lot about him"
        "I didn't know before..... I should do some research on him."
        "..."
        "He founded the Austrian Mathematical Society? Emi will love to hear this."
        "..."
        "So he commited suicide while he was on vacation with his family..."
        "I can't imagine how hard the pressure from his colleagues must have been to drive him this far."
        "..."
        "Wait, what's this? One of his students was... Bernhard Netroufal?"
        "Could it be?"
        "*click click click*"
        "..."
        "Really... that is Professor Netroufal's grandfather. Who would have thought."

        "Thinking of it, didn't Richard mention the other Professors were worried about him?"
        "...maybe I should research him too."
        "..."
        "I see, so he's been teaching at an American university for the last 20 years."
        "Wait... they threw him out? He didn't leave on his own free will? Why?"
        "They didn't announce the reason to the public it seems."
        "But, according to rumors on the University's forum..."
        "...it's because he was doing dangerous experiments? Even life threatening?"
        "And, I can't really believe this, but, there has been a series of big coincidences, and it stopped once he left..."
        "This can't be..."
        "But since I can not fully believe in anything, there is nothing I can deny absolutely."
        "I at least need to tell the others tomorrow."

        jump following

    else:

        "I've spent enough time thinking about wether I am real or not..."
        "I should just go to bed before I fall into another existential crisis."

        jump bad_end_2

label bad_end_2:
    "I don't understand what is happening."
    "Two days have passed. Today, it was announced that Professor Netroufal is dead. Suicide, they say."
    "Nothing makes sense. I can't imagine a single reason why he would do something like this."
    "But I didn't really know him that well... In fact, we only spoke once, and it was one way communication."
    "Then, why does his death have such a strong impact on me?"
    "Maybe I was just hoping I found someone who thought similarly about the world..."

    "GAME OVER"
    return

#following
label following:
    scene home
    "I've got to tell the news to Emi and Richard. A group message will do."

    l "I found some information, meet me tomorrow at the usual café at 2pm."

    scene cafe
    show richard neutral at left
    show emi neutral at right

    l "Good news everyone! Yesterday I browsed the internet and randomly stumbled upon a thread about Boltzmann brains. And because of that, I thought I'd read about him. As it turns out he founded the Austrian Society of Mathematics"
    hide emi neutral
    show emi happy at right
    e "Oh cool, he did that?"
    
    l "I thought that you would like that. But more importantly, I found out that Professor Netroufal's grandfather was a student of Boltzmann. I was intrigued by that coincidence and did a little research on the professor, and it turns out that he was thrown out of his previous university, supposedly due to \"dangerous experiments\". I know it is not much, but basically anything we have so far. Let\'s shadow the professor, he might lead us to something interesting."
    
    r "I am in."
    
    e "Me too."

    "Wow, they really have no moral issues whatsoever regarding spying on a professor."

    l "Alright, here's the plan: Professor Netroufal finishes his last lecture at 7 pm. He should be leaving around half an hour later through the front door to his car. Then we can follow him and find out if he has something to do with all of this."

    e "Neat!"

    scene tu parking
    show emi neutral at left
    show richard neutral at right

    l "OK, it is 5 past 7, he should come out come out within the next 30 minutes."
    r "Did anyone bring food? I am a bit hungry."
    l "I am afraid not."
    e "But I did, you want some cheese?"
    r "Nah, I hate cheese."
    e "More for me then..."


    "30 min later:"

    l "Still no sign of him, he might be talking to students right now..."

    "10 min later:"

    r "OK, I do not think he is leaving anytime soon, he should already be gone. The professor really doesn't seem to be that  kind of person that talks to students after class. I mean he ended his lecture we attended after just 5 minutes. I think we should go in now."
    l "You are probably right, let's go"

    scene lecture
    show emi neutral at right
    show richard neutral at left
    r "Nothing. He is not speaking to students" 
    s "Hello, are you looking for something?"
    e "Hello Professor Steinmeier! Yes, we are looking for Professor Netroufal."

    "Real stealthy Emi."

    s "Netroufal? For all I know, he could be in the basement. Nobody really knows what's been up with him lately, but I have the feeling he's hiding in the darkness or something messed up like that. Not that I really cared though."
    e "Oh, so that's how it is. Thanks for the info."
    s "No problem. Good evening."
    l "So, let's try the basement."
    r "I think Professor Steinmeier was joking... It was cruel, but still a joke."
    l "Yeah whatever, let's go."
    hide emi neutral
    show emi happy at right
    e "Yay, university basement!"

    scene basement_door
    show emi neutral at right
    show richard neutral at left

    r "Do you hear that? Sounds like someone's actually in there."
    l "Wow, and I just wanted to see what it looks like down here..."
    l "Is the door locked?"
    l "Doesn't seem that way... weird. Let's go in."

    scene confrontion
    show emi neutral at right
    show richard neutral at left
    show professor regular at center

    r "Professor Netroufal! What are you doing?"
    n "What? How did you know I was in here?"

    e "That doesn't matter. We know you are doing something dangerous, and that you are behind the strange things that happened lately."
    n "Sigh. I guess the cat is out of the box.You are right about what I'm doing is suspicious, but it has nothing to with the recent events. At least not in the traditional way."
    l "What do you mean by that?"
    n "You are bright kids, so you deserve to know. Ok, let me explain. This is an experiment that is able to prove the Everett interpretation of quantum   mechanics."
    r "You mentioned something like this in your lecture. Didn't you say it was only  theoretical?"
    n "I did. And it is. Because no reasonable scientist would accept a proof like this. You see, this apparatus creates a quantum event with two possible outcomes. According to Everett, this creates two seperate realities which stand in superposition. It is connected to this machine gun. Whe-"
    e "A machine gun?! Are you insane? Where did you get that from?"
    n "Yes, I am. Surprised you didn't notice. And I stole it. Now if you let me continue... When the quantum measurement is 1, the gun fires. If it is zero, it doesn't. This is done once per second."
    r "For what purpose? How does this prove anything?"
    n "Normally, when I step inside the shooting range, I die after a few seconds. But according to Everett, there is always one world in which I am still alive. That is the  only one I can perceive. So, if I'm not dead after a few minutes, I know with high certainty what the truth looks    like."
    
    r "This is madness! Putting your life on the line so easily..."

    l "...and? Did you already try it?"

    n "Yes, I did. Everett was correct."
    e "But why are you continuing then?"

    n "Simple. There is a neat side effect to this experiment..."
    n "The longer you do it, the higher the probability becomes that something stops the   experiment."
    n "For instance, at some point, it is more likely that a blackout turns the machine off than   instead of me continuing to survive."
    
    r "So that's what caused the city wide blackout two days ago?"
    n "No, you misunderstand. I didn't cause anything."
    n "The loud sound you heard yesterday was caused by a small gamma ray, which had some interesting effects on the atmosphere."
    n "Some disruption in the earths curst changed the magnetic field in this area temporarily, which confused birds. All these things are total complete coincidences. They could happen anytime."
    n "What they had in common though, was that they stopped my experiment. The gamma ray was small, but it directly hit my machine. The magnetic field changes also stopped my machine from working."
    n "And I can guess you know what the blackout did. This machine... it is not just good for proving Everett right, it basically functions as an improbabable scenaria generator."

    l "I see... I think I understand what you are trying to achieve."
    n "Yes. I want to see where the limit is. I want to know how far I can go with this. I shielded myself so that the things that have happened don't happen again..."
    n "The result is that the coincidences become more and more major. There could be laws of physics, undiscovered because they only take effect in extreme situations."
    n "There could be more to this universe than we can see. With this, I can break the walls confining, see beyond!"

    r "This is madness! We can't let you continue."
    e "Right! Killing yourself in every world that is not like you want it? It's stupid, to say the   least."

    "This man... we share the same view on the universe. But he isn't afraid. He boldly goes forward to satisfy his infinite curiosity."
    "But is this really ok? Can I let him continue?"

    menu:
        "Let him do it" :
            jump let_him

        "Stop him" :
            jump stop_him

label let_him:

    l "Let him do it"
    e "What? Have you gone crazy too?"
    l "He already made up his mind. He found his path to the true nature of reality. I don't think we should stop him from achieving his dreams."
    r "His dream..."
    n "Thank you. You and I, we are true scientists."
    e "I don't know about this... but it's not really suicide, right? Maybe it is ok?"
    n "I should say farewell to you then. In a few hours, there will be billions of worlds in which   I have died. You are most likely to find yourself in one of them."
    n "Up to now, it has been one unbelievably large coincidence to you that I survived all of     my experiments. From your perspective, at least."
    n "Good bye. I am sure you will find your own way one day."

    jump mixed_feelings_end

label stop_him:

    l "Professor, there is another reason for this, am I right?"
    n "What do you mean?"
    l "You continue now because you want to see the truth behind our existence."
    l "But when you first did the experiment..."
    l "...there was a very high probability for you to just die, with no other backup versions of yourself."
    l "Wasn't that suicide attempt in disguise?"
    
    n "..."
    l "If you are like me, and don't absolutely believe in anything, then the risks would have been way too high for you to do such an experiment."
    n "You are right... again. Haha. I didn't even want to admit it to myself, but I guess I have to look the truth in the eyes."
    r "So you actually wanted to die?"
    n "Yes, a part of me certainly wanted to die. The other part wanted the experiment to succeed. It was a win-win situation if you think about it, really."
    e "But why?"
    n "My ideas about the universe are grand. My imagination goes beyond that of the regular person. But my colleagues mocked my visions. They mocked my work, and with that, my very existence."
    n "I failed in the past... I had theories everyone said were wrong, because they were too distant from 'reality'. And it turned out I was wrong. But I kept on going, doing allegedly 'crazy' theoretical work."
    n "Most of it is neither provable nor falsyfiable today, so it remains controversial at most."
    l "And so you wanted to prove them wrong."
    n "Exactly. This experiment was not my idea, but it represents the kind of science that is frowned upon. That's why I wanted to show them, show to myself, that reality is stranger than human imagination."
    n "And should I have failed... it wouldn't have mattered anymore."
    r "I am sorry. We didn't know about your hardships. But you understand why we can't let you continue, right?"
    n "Yes, I understand. And it is alright. After all, I expected this to happen. You coming here is also just a huge coincidence. But it is more probable than me continueing to survive my experiment."
    n "In another world, I do continue, and hopefully reach my goal."
    n "There are near infinite worlds, and this happens to be one in which I am stopped. I accept that."
    n "This is just like the inflation field. Ahahah."
    "What does he mean? Well, it doesn't really matter."
    l "Glad you came to your senses, Professor Netroufal."

    "After that, we all continued a mostly normal day, as if nothing happened."

    jump true_end


label mixed_feelings_end:
    scene black
    "It did not come as much of a surprise, but it was a shock still. Instead of giving his lecture, it was announced today that Professor Netroufal commited suicide."

    scene cafe
    show richard sad at right
    show emi sad at left
    
    r "Such dedication... For a single person to kill themself in billions of worlds, in order to achieve their dream. Can it really be called dedication? Or wasn't it just recklessness?"
    e "One thing is for certain. He was filled with madness. He did not care one bit for the conventional ways... it is sad he is gone from this world."
    l "As far as we know, he is still alive, somewhere. It's as if he moved away. Somewhere where he can see beyond... I kind of envy him."
    e "You're not thinking of doing the same as him, do you?"
    l "Don't worry. I won't do it, as long as I have other options."
    "And I'd be too cowardly anyway..."
    l "I know now that the possibilty exists. I'm sure there are other ways to achieve the same goal. Safer ways."
    r "Good to see this whole incident didn't discourage you. Truly, you have a will of iron."
    "I just hope he really reached the world he wished for..."
    
    jump game_over

label true_end:

    scene cafe
    show richard sad at right
    show emi sad at left
    show professor happy at center
    r "Such dedication... For a single person to kill themself in billions of worlds, in order to achieve their dream. Can it really be called dedication? Or isn't it just recklessness?"
    e "One thing is for certain. He is filled with madness. He does not care one bit for the conventional ways... how admirable."
    l "I wonder if he could have done it..."
    l "to observe new physical phenomena in order to learn more about the true nature of this universe. I must admit, I can totally understand his curiosity."
    l "Maybe I would even have done the same if I were in his position, and weren't such a coward."
    e "There is nothing cowardly in not commiting thousands of suicides."
    r "That's a statement I would sign at any time."
    n "Don't worry, you will find your path."
    l "Professor Netroufal!"
    n "Please, I told you you can just call me Professor Dr. Netroufal. Ahaha."
    r "..."
    e "..."
    l "..."

    e "So what are you doing here?"
    n "I was walking on the street when I saw you guys inside. So I thought I'd just appear out of nowhere."
    r "Professor, there is something I've been meaning to ask you. Are you sure it is ok to give up on your dream?"
    n "Give up? Who said I'd give up? This is only the beginning! But, I won't do any life threatening experiments anymore. At least not until I have given all my knowledge to the next generation."
    e "That is very wise of you, Professor N."
    n "What, is Netroufal too long for you to say?"
    e "Nah, but it sounds more mysterious. I think it fits you better."
    n "Hmm... you think so?"
    r "You were driven enough into a corner to risk his own life... and now that we stopped you from your last chance to fulfill your dream, you still don't give up?"
    r "you don't even seem to be distressed about it... Truly, strong dreams create stong men."

    "It seems that everything ended happily. The walls... they don't feel so strong and ominous anymore. Volatile, almost. I know now that I can try to see beyond them. It is not a useless endeavor."
    "In fact, if there is anything I am sure of, it is that I will continue to go on, until I am no longer physically able to."

    jump game_over


label game_over:
    scene black with slowfade
    show credits at center
 #   show credits:
  #      xpos 0.0 ypos 0.0
   #     linear 120.0 ypos -13021.0
    centered "Game Over"

    