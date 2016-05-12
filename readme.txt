Johnson's Little Helper version 1.0
Thomas Bonatti

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        How to run the program:

    1) python
Johnson's Little Helper is written in Python 3, you'll need to have that installed to run this.
If you don't have Python, Google "Install Python 3", it's pretty easy to figure out. (No one's paying me to do this,
don't expect me to hold you hand :D)
Make sure you get python 3. For whatever reason, people use both python 2 & 3, and this program won't work on python 2.

    2) Unzip the folder
Unzip the program to wherever you want it.

    3) Run the program
Run the file "combat_manager.py", and a console will appear with the program running.
If windows is being uncooperative, just tell it to always run this type of file with Python.exe, wherever you installed
that on your computer Make sure you do NOT run the program with Pythonw.exe, this version of Python will run without a
console, for programs with a GUI.

    I recommend you create a shortcut to combat_manager.py somewhere convenient and forget about the details.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        How to use the program:

    There's a help function in the program that I think is super-handy-dandy, but if you don't thinks so email me and
tell me why so I can tell you to slot off. (In all seriousness, if something is unclear, I will actually fix it, WHEN I
GET ARROUND TO IT which might take some time, or might be never, or might be tomorrow )

    For starters, Chummer, there are several "commands" you can use in the program. Most of these are based on there
being an "active combat". The first thing you need to to is make a combat. Either type "new" and press enter, or type
"load" then a space and a save name. If you've never used the program, you won't have any saves of your own, but I've
included a generous "sample" save based on the runners in a game I'm currently running. If you want to save your current
combat, type "save" then the name you want it to be saved under. If you want to load that combat again, type "load" then
the same name.

    The system tracks 1 combat at a time, which is basically just a sorted list of "combatants." Each combatant has a
name, which must be different from any other combatant, and it has a base-initiative score, a number of initiative-dice
rolled, damage, stun-damage, and the current initiative score. If you have no idea what I'm talking about, you should
probably read the Shadowrun 5e Core Rulebook, because this is an app meant to assist in the playing of that game.

    To add combatants, you first need an active combat, then type "add [name] [base-init] [# init dice]". If you want to
see the current init order, just type "view", you'll see the sorted init order. Each entry will look something like
"+ [11] name" with a + indicating that that combatant has not taken an action yet, and a - indicating they have. The
number is the current init-score.
    To get the NEXT person to act, just type "next" it will show who's next and print out little flags whenever you move
to the next turn or the next initiative pass. For all the rest, I leave you to your common sense and the handy-dandy
"help" command I added just for you. If you CAN'T figure it out, and there are more people like you, then I'll add more
instructions.


    Tips and common mistakes for shamans the Matrix inept:
        - there can be no spaces in save names, try using "-" of "_" instead or just having better names.
        - saves do not track damage or current initiative, just base stats (name, base-init, init-dice)
            nothing else (damage, stun, current-init) is saved. You'll have to reenter that, but I imagine you won't
            want to
        - if you press the up arrow in the normal python console, it will pull up the last thing you typed in. This is
            handy if you make the same roll several times (ie. 3 knight errant caught in the same fireball)
        - if you press the up arrow AGAIN you load the thing you typed before the last thing you typed, and so on.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        If you're Mad because there isn't a cool GUI:

    Well slot off chummer, because those take time and this is free. But also, you are wrong because once you learn how
to use it, a console app is way faster to use. BUT, if you're not convinced, and need proof that console apps are
superior, make a charitable donation. If you and enough other people think GUI's are important enough to donate enough
money to make it worth my while, I'll make one. But I really don't want to srew around with Python-graphics if it can be
avoided, so it's probably not worth what it would cost you.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        What is Shadowrun:

    If you don't know what shadowrun is, and still made it this far into the readme, well then you have a reading
problem and should seek help immediately. I'm not a therepist, but I recomend youtube. If that doesn't work, Vine has an
even shorter required attention span, and will probably cure your need to read anything ever again.

    Shadowrun is a table-top roll playing game produced by Catalyst Game Labs. It is set in the near future (~2075) in
an alternate world where magic is real, but also cyberpunk hacking and augmentation etc... Magic did not exist in the
world until "The Awakening" when magic awoke from a long slumber (There are cycles, magic gets stronger and weaker over
time, kinda like earth's magnetic field.)

    Anyway, that was a pretty poor explanation, just Google Shadowrun. If you're reading this, you probably know what it
is, so it's not worth my explaining it to you.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Contact me: kings_of_ahevrayka@hotmail.com

    Bug reports, comments, concerns, suggestions, feature requests, fan-mail, hate-mail, death threats, etc...
    Pretty much anything concerning this program. If it has nothing to do with this program, please slot off. :D
