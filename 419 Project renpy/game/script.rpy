# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it:

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory:

    show eileen happy

    # These display lines of dialogue.

    menu:
        # choice1_bright
        "Look on the bright side":
            $ dark = False
            "I haven't written this part yet."
            jump choice1_done


        # choice1_dark
        "Let yourself feel the weight of the world":
            $ dark = True
            "My life has been on pause, it's been suspended in a bubble, like it's not been real. Yet, time has been passing the whole time."
            "It's already been a year. Not only do I already feel like I've lost so much time, but I'm afraid of losing my youth."
            "Why should I be 22 when I didn't even get to be 21? These years are supposed to be crucial. They're not supposed to be slipping through my fingers like sand, or like something else I can never get back."
            "Is another entire age just going to get fucked down the drain? When this is all over, am I just going to wake up one day and be 25?"
            "Ugh, \"when this is all over\"... I hate saying that now, it just sounds like when you say \"I swear he'll change!\""
            "I know everyone is going through this, but it's my early twenties... Losing a single year right now feels like so much. I feel like I'm LOSING, WASTING so much."
            jump choice1_done

    label choice1_done:
        if dark:
            "Ugh. I guess I shouldn't start thinking about all this."
            "But when is it good to stop that train of thought? I don't want to ignore these feelings, but I don't know how to engage with them halfway."
            "I'm not an emotionally constipated person, but if I really let myself start to think about it all, it's extremely exhausting. So most of the time, I put it off."
            menu:
                # choice2_bright
                "Think about something else.":
                    $ dark = False
                    "I haven't written this part yet."
                    # this is choice2_bright
                    # or have a separate choice for diversion away from spiraling thoughts-- e.g., immediately trying to seek comfort or distraction
                    jump choice2_done

                # choice2_dark
                "It's okay to introspect.":
                    $ dark = True
                    jump choice2_done
        # else:
            # i'm feeling good. but i don't know, sometimes maybe i should take more time to acknowledge how tough this really all is. on everyone -- so it's okay to think about, sometimes, how it's been tough on me.

    label choice2_done:
        if dark:
            "Okay. You see, I know our lives have changed, and it's okay to think about it, but the thing is the entire situation is messed up in so many ways, there's so much to think about, it causes pain and anger and frustration..."
            "and there's nothing I can do to just fix this situation so I just ask myself, \"Do you really want to subject yourself to this train of thought?\""

            menu:
                # choice3_dark
                "Feel your feelings.":
                    $ dark = True
                    "Wasting time... speaking of it, I still feel like I'm wasting so much even though time's already getting wasted out of my control."
                    "I hate it, but at the same time, when time doesn't matter, how hard does that make it to not just fucking waste the days yourself, too?"
                    "I don't want to WATCH my life pass by me. It's a paradox; on one hand, this time means you need to make the most of your days. But on the other hand, I can't bear to watch my 22-year-old self do nothing."
                    "There are some days where all I can bear to do is sleep."
                    "Losing time usually makes me feel depressed, oversleeping usually makes me feel shame and guilt, but all our time's already been lost."
                    "Just going through these motions each day hurts sometimes, feeling constantly that I'm heading nowhere, having to face my devolution and stagnancy day after day."
                    "I can't decide how bad it is that in some ways, I wish I could just sleep and wake up when it's all over. But at the same time, waking up and it's been a year, two years, would make me wanna die."
                    jump choice3_done

                # choice3_bright
                "Why not focus on what you can control right now?":
                    $ dark = False
                    "I haven't written this part yet."
                    jump choice3_done
        #else:
            #menu:
                # choice3_bright:
                    #.....
                    #jump choice3_done
                # choice3_dark:
                    #....
                    #jump choice3_done


    label choice3_done:
        if dark:
            menu:
                "Ugh. Ugh. I'm thinking negatively again. I know I can't control the situation, and I shouldn't be so hard on myself."

                # choice4_dark
                "It's been so much. You've just been floating along this whole time; you thought it'd be temporary.":
                    $ dark = True
                    "I know, right? I can't stop thinking about that. I thought I would be back at my dorm, back with my cat in a few weeks. I acted so ahead-of-time that it just felt precautionary, and now we're coming up on year two."
                    "I'm so good at just chugging along, not thinking about it, \"taking it surprisingly well\", but really, I'm just on autopilot."
                    "How long is it gonna be? And will I go back to \"normal\" (whatever that is), remember how to be productive and function again? Or will I stay broken?"
                    "God, I just fucking wish that at least Midge were here. That's what hurts most of all. I just wish she was here."
                    jump choice4_done

                # choice4_bright
                "You're starting to cry. Stop thinking like this.":
                    $ dark = False
                    "I haven't written this part yet."
                    jump choice4_done
        #else:
            #menu:
                # choice4_bright:
                    #.....
                    #jump choice4_done
                # choice4_dark:
                    #....
                    #jump choice4_done

    label choice4_done:
        "I haven't written this part yet."
    #    if dark:
    #        menu:
    #            "God. Don't even think about Midge right now. Now you're REALLY crying. You're in the middle of it."



    ########
    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
