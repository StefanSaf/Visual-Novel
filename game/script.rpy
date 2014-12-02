# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define l = Character('Ludwig', color="#c8ffc8")
define e = Character('Emi', color="#C8FFC8")
define r = Character('Raphael', color="#C8FFC8")
define p = Character('Playground', color="#c8ffc8")
define g = Character(' ', color="#c8ffc8")
define n = Character('Netroufal', color="#C8FFC8")
define ri = Character('Richard', color="#C8FFC8")


image wolken ="sonne_ober_wolken.JPG"
image black ="black.jpg"

# The game starts here.
label start:
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
    l "Logic can not be proven, because the act of prooving is a tool of logic itself."
    l "If a stranger on the street told you to trust him, would you? Just because he told you so?"
    l "Call me paranoid, but I wouldn't. That is why I don't believe in anything, and there is nothing I trust 100."
    l "What I am looking for is something that can convince me of <i>anything</i>."
    l "The most promising path to that goal seems to be science."
    l "My words contradict each other, but I can not afford the luxury of living without contradictions right now."


    scene black
    p ""
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
    l "Recorded history goes back thousands of years. Many people have tried, but noone found any answers. Most of them were very depressed and had no life. They died sad, because they failed. The same will surely happen to you too, if you try the imposssible."
menu:
    "I don't care":
        jump A11
    "Maybe you are right... ":
        jump A12

label A2:
    l "Of course you are! Look at everyone else, they are enjoying being outside. And what are you doing? You always lose yourself in your thoughts. Be it in school or outside, you never concentrate on anything! Why can't you just be normal and talk to people?"
    
label A11:
    l "It's still better than living the hollow life that you propose. I would much rather die having tried to pursue my ambition."
    jump Hallway
    
label A12:
    l "No one before managed to do it, why should I? How silly of me."
    e "Glad you came to your sense. Now come, the next lesson starts soon."
    jump BadEnd1


label Hallway:
    g "I wonder how many weeks it has been now since I joined university? It must be at least eight. I think I am slowly getting used to it here. It is definitely better than school. Finally I can decide by myself what classes I want to attend... This way, I can fully concentrate on my future. I just hope I don't drop out... My grades have always been good to average, but physics is really hard. Wait, what am I thinking? I already decided that I will become a physicist! If I fail I'll try again. How else am I supposed to learn the secret of the walls? What lies beyond them, and who constructed them for what purpose? This is the future I have chosen.... , and I will see it through."
    e "Hey, Ludwig! Hi! We don't meet often between lectures, do we? Haha"
    l "Hi, Emi."
    g "This is Emi. We've known each other for several years. We went to the same school for two years."
    g "We got along, but I wouldn't say we were friends. When I had to change schools, we lost contact. But now she attends the same university as me, the TU Wien. I study physics, she math. We met by chance soon after we started, and quickly became friends. She changed quite a bit..."
    e "What was that lecture you just came out of about?"
    l "Oh, it was about thermodynamics. An introduction to entropy. What did you have today?"
    e "Sounds like fun. Actually, I wasn't in a lecture today. I just came here to do some research in the library."
    l "What are you working on?"
    e "Ah, just my own little theories on formal systems and completion. I have some ideas that seem really crazy, and now I am trying to find out why they wouldn't work. I'd tell you about them, a I fear a non mathematician wouldn't understand it, haha."
    l "Gee, thanks. And don't call yourself a mathematician yet! You just started studying."
    e "I am a mathematician at heart already. By the way, do you want to hear some rumors?"
    g "To be honest, I really don't like rumors. Incomplete or untrustworthy information makes me uncomfortable. But Emi loves them, and I don't think she has many other friends at university, so I can't really reject her."
    l "Not really, but tell me anyway."
    e "Alright! Massive flocks of birds have been sighted, and they are all flying east. East! Birds usually fly either north or south, but not east! And it wasn't just one species of bird, but several. Biologists have no idea what causes it. The internet speculates that this is the first sign of the apocalypse."
    l "Hmm, that is weird, if it's true. But I wouldn't trust the internet's diagnosis on such matters."
    e "Me neither, but it's still cool to think about."
    l "Maybe. Anyway, I have to go to the next lecture. See you later."
    e "See ya!"
    jump Lecture1

label BadEnd1:
    g "– At an office –"
    g "*click click click*"
    g "*click click click*"
    g "Ugh... I wonder wonder when I can go home? It's already past eight... but I can't leave until I've finished this report on the sales of the last quartal. Well, at least this job pays well."
    g "*ring ring*"
    g "*pick up cell phone*"
    l "Hey Raphael, what's up?"
    r "Hi Ludwig! How are the wife and kids doing?"
    l "Fine, thanks for asking."
    r "I just wanted to ask if you wanted to catch the football game tomorrow."
    l "Sure! It will be an interesting match, there's no way I'm going to miss that."
    r "Great! Then we'll just call each other tomorrow, alright?"
    l "Yeah. Until then."
    r "Bye"

    g "..."
    g "......"
    g "........."

    g "Why do I feel so empty? I feel like there is something I have forgotten about... Whatever it was, it's too late now. I should just get back to work, so I can catch some sleep at home."

    g "*click click click*"
    g "*click click click*"

    g "GAME OVER"


label Lecture1:
    g "This lecture is special, and one that I've particularly been looking forward to. The lecturer is Professor Dr. Dr. Netroufal. He's been in universities abroad for a few years, and recently came back to Vienna. The subject is quantum mechanics. It usually doesn't start so early in the studies, but that is why this lecture is special. It is the Professors field of expertise, and it is sort of his 'welcome back' gift to us, the students. Anyway, I should find a seat. Damn, I should've come earlier, it's packed in here... The only free seat left is in the middle row. I don't really like it there, but there's nothing I can do about it now."

    l "Excuse me, is this seat taken...?"
    r "Huh? Yeah, sit down if you want. Seems to be the last one."
    l "Yeah. Thanks."
    r "Man, I hate the middle row."
    l "Really? Me too!"
    g "I like to sit in the last row, where nobody is behind me who could see me. I'm uncomfortable when a lot of people can watch me, even if I'm not at the center of attention."
    r "Aha! I see we are alike! Truly, the first row is the best. I can't stand having to see so many other people in front of me."
    g "well..."
    l "It simply disgusts me, you know. Most young people are a disgrace to mankind. All they think about is how they need to have the newest phone, watch TV, repeat what is told to them by the media, and so on. But the worst thing is, they are lazy. They don't have a goal to accomplish. They aren't alive, they just live."
    r "I agree with you. Most of them are just annoying."
    l "Oho! You share my views! This is rare. That must mean that you are different... Say, do you have a dream?"
    r "I guess you could say that. I want to solve the mystery of existence."
    l "You mean... answering the fundamental questions mankind has been asking for millenia?"
    r "Well... yes."
    l "You attempt to do what the most brilliant minds humanity had to offer failed at?"
    r "You think it's foolish, don't you?"
    l "The opposite is true! I admire you for your vigilence! You try to do the impossible, because it is your dream. There is nothing foolish in that."
    g "Wow, that is the most motivating thing anyone ever said to me. Everyone else always tried to tell me I should do something normal..."

label Lecture2:
    n "Hello everyone. My name is Professor Dr. Dr. Netroufal. But you can just call me Professor Dr. Netroufal. Ahaha."
    g "A few giggles came from the audience, but it remained mostly silent."
    n "I am a Professor of physics, and hold the title of doctor for mathematics and neurology. Today I will give you an overview of what I think is the most important concept of quantum mechanics."
    n "Let's start right away, shall we?"
    
    n "Most of you probably know that very very small object, like atoms, behave differently from the larger ones that we are familiar with. For example, an electron can be at two different places at once, whereas a melon can't. One common error is to think that we just don't know where exactly the electron is. That is partially true, but mostly wrong. We do not know where it is, because it really actually is at both places. But we can never see it in both places. But that is weird, isn't it? If something is, then it should be observable. Sadly, in the world of quantum mechanics everything is weird and different. When we observe an object in such a so called superposition, it seems to suddenly decide for one of the places randomly. We can calculate the probabilities for each event exactly. In fact, quantum mechanics is one of the most tested theories ever. "
    n "And not once has it given a wrong prediction. The results are correct. Every. Single. Time. The only problem is that we don't understand how and why it works. We know a particle jumps to a single place when observed. But it doesn't explain what exactly an observation is. Does it need humans? Does consciosness play a role in the laws of physics? Or is a single photon hitting it enough? This is the Copenhagen interpretation of quantum mechanics, and it leaves quite a few open questions. And yet, for a long time it was what most scientists thought was the correct way to see things. Today, they are not as sure. With good reason. There are alternative explanations for the phenomena we can observe. The most popular one of them is the Everett interpretation of quantum mechanics, also known as the many worlds interpretation."
    n "You may have heard or read about it in various science fiction stories. But I want you to understand that this is NOT just fiction. Now, let's think about what actually happens when we observe something. Let's take the most simple scenario, with a single electron. To measure something, we basically have to throw something at it, and see how that thing comes back to us. In this case we use a photon. But the electron is in superposition! How does it reflect the electron? The answer is simple. The photon is reflected by both states of the electron, and is itself now in two positions at the same time. It is also in superposition. Eventually, it hits one of our detectors. This detector, too, is put into superposition of two states."
    n "And when we look at the results of the detector, our whole brain is put into a superposition of thinking the electron is at either one place or the other. Both of these states are equally real. But because of how our brain works, we can only consciously feel ONE of them. If you want, you can call these other states parallel universes. But they are actually all part of one big, strange universe. And that is the Everett interpretation. If you ask me, it follows a much simpler logic and requires less magic. But of course, it also changes our view of the world completely. And extraordinary claims require extraordinary evidence. Can we produce such evidence? There are some theoretical possibilities. But that is a story for another day."
    n "I'm done here."

    g "Wow, what a lecture. I'd like to ask him some questions... but appearently so do many others. Should I try to go and talk to him?"

menu:
    "YES":
        jump StreetRichard
    "NO":
        jump StreetEmi

label StreetRichard:
    ri "Oh, hello Ludwig. Did you catch the professor?"
    l "Hi Richard. No, too many wanted to talk to him. After the first three people, he just went to his office."
    ri "What a shame. If you want, we can go right to my place and battle each other."
    l "I have nothing else to do, so yeah, why not."
    l "(thoughts)...I am curious what he is referring to when he speaks about battling..."
    ri "Alright, then let's go."
    l "So, why do you study physics?"
    ri "I honestly am not sure if this is the right direction for me. I changed studies three times now. Jura, logic, medicine... They all couldn't ignite the spark in me to get me burning. I still haven't found my true passion, which is what I really want: finding something that truly fulfills me, a passion. Something I can get lost in. Work that I truly love. Sadly this is not easy to come by. I do not have a dream like you do. So I keep on searching, until I find it. I must admit, I envy you for already having found yours."
    l "I am sure that you will find your dream soon enough."
    ri "I hope so."
    g "After walking for a few minutes, we arrived at Richard's home."

    jump RichardHome

label StreetEmi:
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
        
    jump RichardHome

label RichardHome:
    ri "Welcome to my home. I am very sorry for the mess, but I did not have enough time to tidy it up."
    g "pictures of how tidy the room is with sparkling stars of beauty"
    g "What mess?"
    ri "Thank you for accepting my invitation. I do not often have guests. Do you want something to drink? I've got Orange juice, beer, wine and water."
    l "Orange juice, please."
    l "I'll take a beer, please."
    l "I'll take a glass of wine, please.” “I'll take a glass of water, please."
return