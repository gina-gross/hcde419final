﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it:

    scene bg sketchbook with Fade(0.5, 0.5, 1.0)
    scene beginning1 with Dissolve(1.0)
    $ renpy.pause()
    scene beginning2 with Dissolve(1.0)
    $ renpy.pause()
    scene phone screen1 with Fade(0.5, 0.0, 1.0)
    $ renpy.pause()
    scene phone screen2 with Dissolve(1.0)
    $ renpy.pause()
    scene phone screen3 with dissolve
    $ renpy.pause()
    scene phone screen4 with Dissolve(1.0)
    $ renpy.pause()
    scene beginning3 with Fade(0.5, 0.0, 1.0)
    $ renpy.pause()
    "..."
    scene beginning4 with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory:

    #show eileen happy

    # These display lines of dialogue.

    menu:
        # choice 1 (bright)
        "Look on the bright side":
            $ dark = False
            # i'm feeling good. but i don't know, sometimes maybe i should take more time to acknowledge how tough this really all is. on everyone -- so it's okay to think about, sometimes, how it's been tough on me.
            "My performance in school has been great, it has actually improved a lot since quarantine started."
            "Whether it's because engaging with school the way I like to became surprisingly more accessible (that's probably a big reason, actually), I've been consistently more engaged overall, feeling checked in."
            "Which feels good. That's what I started off college like, it's what I think of as the default version of \"me\". But I go through cycles; I stray away from that and struggle to get back to it."
            "It's how I like to think of myself as being; though that's probably too generalizing, a bit of the perfectionist in me."
            "But regardless, I like it when I feel like this— even if it's a high I can't always sustain, it feels like I've got my groove back. At least a little. I feel more fueled, energized."
            "I feel intellectually stimulated, in a good way, and have somehow held the balance to not become {i}too{/i} stimulated and overwhelmed."
            "I still lose my energy sometimes, but it's less overreaching than other times in the past. There's always bumps along the road, but I feel good about my direction in general; I'm not getting too derailed."
            "Part of it, too, probably has a lot to do with the fact that I entered the finishing stages of my education, finally capping it off FINALLY, as this all started."
            jump choice1_done


        # choice 1 (dark)
        "Let yourself feel the weight of the world":
            $ dark = True
            "My life has been on pause. It's been suspended in a bubble, like it's not been real."
            "Yet, time's been passing all the way."
            scene bg sketchbook
            with pixellate
            "It's already been a year. Not only do I already feel like I've lost so much time, but I'm afraid of losing my youth."
            scene img then
            with dissolve
            "Why should I be 22 when I didn't even get to be 21? These years are supposed to be crucial. They're not supposed to be slipping through my fingers like sand, or like something else I can never get back."
            scene img then arrow
            with dissolve
            "Will another entire age just get fucked down the drain? When this is all over, am I just going to wake up one day and find myself at 25? Because that's what this is feeling like."
            scene img then and now
            with dissolve
            "Ugh, \"when this is all over\"... I hate saying that now, it just sounds like saying \"once I'm not depressed anymore\" or \"I swear he's gonna change\"."
            scene img then and now all info
            with dissolve
            "I know everyone else has grown a year older, too. but it's my early twenties... Losing a single year right now feels like so much. I feel like I'm LOSING, WASTING so much."
            jump choice1_done

    label choice1_done:

        if dark: # let yourself feel the weight of the world
            "Ugh. I guess I shouldn't start thinking about all this."
            scene big_thinkin open eye
            with fade
            "But when is it good to stop that train of thought? I don't want to ignore these feelings, but I don't know how to engage with them halfway."
            scene big_thinkin eyes closed
            with dissolve
            "I'm not an emotionally constipated person, but if I really let myself start to think about it all, it's extremely exhausting. So most of the time, I put it off."

            menu:
                # choice 2 (bright)
                "Think about something else.":
                    $ dark = False
                    "Funnily enough, and maybe it's because of that, but I feel like I've been weirdly more stable during this time; at least in some ways."
                    "I had a check-in with one of my doctors last week, the last time I saw her was way back in June 2020, and she mentioned that my anxiety screener had gone WAY down, apparently."
                    "I guess I never really thought about it, but I HAVE been less anxious; overall, on the day-to-day. I guess 'cause I have less going on... but like, in a good way?"
                    "But then of course, in the more broad sense, we're probably ALL more anxious now than ever... I mean, right?"
                    "Weird how that stuff works sometimes, huh?"
                    # or have a separate choice for diversion away from spiraling thoughts-- e.g., immediately trying to seek comfort or distraction
                    jump choice2_done

                # choice 2 (dark)
                "It's okay to introspect.":
                    $ dark = True
                    "Okay. You see, I know our lives have changed, and it's okay to think about it, but the thing is the entire situation is messed up in so many ways, there's so much to think about, it causes pain and anger and frustration..."
                    "and there's nothing I can do to just fix this situation so I just ask myself, \"Do you really want to subject yourself to this train of thought right now?\""
                    jump choice2_done


        else: # look on the bright side
            "It's not like I'm painstakingly avoiding it all the time or being delusional about this all, though. Even though I don't wish to compartmentalize, I think it's good overall that I don't let it bear down on me all the time?"
            "I mean, it's a weird situation. I wanna make sure I'm coping with this healthily, but also, even if I {i}am{/i} compartmentalizing or whatever, I seem to be coping and functioning pretty well all things considered."
            "If it ain't broke, don't fix it, right?"
            menu:
                # choice 2 (bright)
                "You may not give yourself enough credit. You've worked hard to be doing well.":
                    $ dark = False
                    "Yeah; funnily enough, I feel like I've been weirdly more stable during this time, at least in some ways."
                    "I had a check-in with one of my doctors last week, the last time I saw her was way back in June 2020, and she mentioned that my anxiety screener had gone WAY down, apparently."
                    "I guess I never really thought about it, but I HAVE been less anxious; overall, on the day-to-day. I guess 'cause I have less going on... but like, in a good way?"
                    "But then of course, in the more broad sense, we're probably ALL more anxious now than ever... I mean, right?"
                    "Weird how that stuff works sometimes, huh?"
                    jump choice2_done

                # choice 2 (dark)
                "It's okay to introspect.":
                    "haven't writtne it yet"


    label choice2_done:
        if dark: # it's okay to introspect

            menu:
                # choice 3 (dark)
                "Feel your feelings.":
                    $ dark = True
                    "Speaking of wasting time, I still feel like I'm wasting so much even though time's already getting wasted out of my control."
                    "I hate it, but at the same time, when time doesn't matter, how hard does that fucking make it to not go ahead and just waste the days yourself, too?"
                    "I don't want to WATCH my life pass me by. It's a paradox; on one hand, I want to be making the most out of my days right now. But on the other hand, I can't bear to watch my precious youth go inert."
                    "There are some days where all I can bear to do is sleep."
                    "Losing time usually makes me feel depressed, oversleeping usually leaves me with shame and guilt, but all our time's already been lost."
                    "Just going through these motions each day hurts sometimes, feeling constantly that I'm heading nowhere, having to face my {i}devolution{/i} and {i}stagnancy{/i} day after day."
                    "I can't decide how bad it is that in some ways, I'd love to just wake up when this is all over. But at the same time, waking up and it's one year, two years later, would make me wanna die."
                    jump choice3_done

                # choice 3 (bright)
                "Why not focus on what you {i}can{/i} control right now?":
                    $ dark = False
                    "I haven't written this part yet."
                    jump choice3_done
        #else: # think about something else/you don't give yourself enough credit
            #menu:
                # choice3 (bright)
                    #.....
                    #jump choice3_done

                # choice 3 (dark)
                    #....
                    #jump choice3_done


    label choice3_done:
        if dark: # feel your feelings
            menu:
                "Ugh. Ugh. I'm thinking negatively again. I know I can't control the situation, and I shouldn't be so hard on myself. I'm really not TRYING to be."

                # choice 4 (dark)
                "It's been so much. You've just been floating along this whole time; you thought it'd be temporary.":
                    $ dark = True
                    "I know, right? I can't stop thinking about that. I thought I would be back at my dorm, back with my cat in a few weeks. I acted so ahead-of-time that it just felt precautionary, and now... it's March again."
                    "I'm so good at just chugging along, not thinking about it, \"taking it surprisingly well\", but really, I'm just on autopilot. Trying to avoid burnout as much as I can."
                    "How long is it gonna be? And will I go back to \"normal\" (whatever that is), remember how to be productive and function again? Or will I stay broken?"
                    scene midge with dissolve
                    "God, I just fucking wish that at least Midge were here. That's what hurts most of all. I just wish she was here."
                    jump choice4_done

                # choice 4 (bright)
                "":
                    $ dark = False
                    "I haven't written this part yet."
                    jump choice4_done

        #else: # why not focus on what you CAN control
            #menu:
                # choice 4 (bright)
                    #.....
                    #jump choice4_done

                # choice 4 (dark)
                    #....
                    #jump choice4_done

    label choice4_done:
        "I haven't written this part yet."
    #    if dark: # it's been so much ...
    #        menu:
    #            "..."
            # choice 5 (bright): "You're starting to cry. Stop thinking like this."
            # choice 5 (dark):...



    ########
    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
