# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define l = Character('Ludwig', color="#c8ffc8")
define e = Character('Emi', color="#C8FFC8")
define p = Character('Playground', color="#c8ffc8")

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
    
label A12:
    l "No one before managed to do it, why should I? How silly of me."

return