# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    # Beginning sequence

    scene bg sketchbook with Fade(0.1, 0.5, 1.2)
    scene beginning1 with Dissolve(2.0)
    pause
    scene beginning2 with Dissolve(1.0)
    pause
    scene phone screen1 with Fade(0.5, 0.2, 1.0)
    pause
    scene phone screen2 with Dissolve(1.0)
    pause
    scene phone screen3 with dissolve
    pause
    scene phone screen4 with Dissolve(1.0)
    pause
    scene beginning3 with Fade(0.5, 0.2, 1.0)
    pause
    "..."
    scene beginning4 with Dissolve(1.0)



    # Entering into the first menus/dialogue.

    # Choice 1
    menu:
        # choice 1 (bright)
        "Look on the bright side":
            $ dark = False
            # i'm feeling good. but i don't know, sometimes maybe i should take more time to acknowledge how tough this really all is. on everyone -- so it's okay to think about, sometimes, how it's been tough on me.
            scene bg sketchbook with pixellate
            "My performance in school has been great, it has actually improved a lot since quarantine started."
            scene gpa1 with Dissolve(2.0)
            "Whether it's because engaging with school the way I like to became surprisingly more accessible (that's probably a big reason, actually), I've been consistently more engaged overall, feeling checked in."
            scene gpa2 with Dissolve(1.5)
            "Which feels good. That's what I started off college like, it's what I think of as the default version of \"me\". But I go through cycles; I stray away from that and struggle to get back to it, at times."
            scene gpa2a with Dissolve(1.0)
            scene gpa2b with Dissolve(1.0)
            scene gpa2c with Dissolve(1.0)
            scene gpa2d with Dissolve(1.0)
            scene gpa2e with Dissolve(1.5)
            "It's how I like to think of myself as being; though that's probably too generalizing, a bit of the perfectionist in me."
            scene gpa3 with Dissolve(1.5)
            "But regardless, I like it when I feel like this— even if it's a high I can't always sustain, it feels like I've got my groove back. At least a little. I feel more fueled, energized."
            scene gpa3a with Dissolve(1.0)
            scene gpa3b with Dissolve(1.0)
            scene gpa3c with Dissolve(1.0)
            scene gpa3d with Dissolve(1.0)
            scene gpa3e with Dissolve(1.5)
            "I feel intellectually stimulated, in a good way, and have somehow held the balance thus far to not become {i}too{/i} stimulated and overwhelmed."
            scene gpa4 with Dissolve(1.5)
            "I still lose my energy sometimes, but it's less overreaching than other times in the past. There's always bumps along the road, but I feel good about my direction in general; I'm not getting too derailed."
            scene gpa4a with Dissolve(1.0)
            scene gpa4b with Dissolve(1.0)
            scene gpa4c with Dissolve(1.0)
            scene gpa4d with Dissolve(1.5)
            "Part of it, too, probably has a lot to do with the fact that I entered the finishing stages of my education, finally capping it off {i}FINALLY{/i}, as this all started."
            #make this more explicit, talk about how finishing your education has you feel focused etc, seeing the light at the end of the tunnel, motivated, why and how
            "Like, I'm no longer in the murky middleground of my education! I knew it would take me an ambiguous \"longer time\" to finish a double degree, but \"the end\" still certainly felt far off, still some vague soon-ish future time."
            "You know, a bridge I'll get to eventually. Especially after entering college early, and then going through a dip where I knew I'd have to retake stuff— all this run-up to my eventual degree(s) was just getting perpetual."
            "Six years to get two degrees is super normal, and I'm still gonna be graduating at 22— I'm not lagging by any means, but I kinda realized why college has felt so long for me once my therapist mentioned that like... it's been 36\% of my life."
            "I entered at sixteen. I was but a young babe. So when I took capstone last year, I started actually seeing the light at the end of the tunnel and feeling revved up— ready, {i}excited{/i} to finish up strong."
            "But of course, pandemic started right in between my capstone quarters!{w} Life, huh?{w} But it kind of worked out.{w} I became more focused because I was checked back into my education with capstone, and I guess quarantine let me hone my attention."
            hide gpa4d
            jump choice1_done


        # choice 1 (dark)
        "Let yourself feel the weight of the world":
            $ dark = True
            scene bg sketchbook with pixellate
            "My life has been on pause. It's been suspended in a bubble, like it's not been real."
            "Yet, time's been passing all the way."
            "It's already been a year. Not only do I already feel like I've lost so much time, but I'm afraid of losing my youth."
            scene img then with Dissolve(0.7)
            "Why should I be 22 already, heading towards 23, when I hardly even got to be 21? These years are supposed to be crucial. They're not supposed to be slipping through my fingers like sand, or like something else I can never get back."
            scene img then arrow with Dissolve(0.7)
            "Will another entire age just get fucked down the drain? When this is all over, am I just going to wake up one day and find myself at 25? Because that's what this is feeling like."
            scene img then and now with Dissolve(0.7)
            "Ugh, \"when this is all over\"... I hate saying that now, it just sounds like saying \"once I'm not depressed anymore\" or \"I swear he's gonna change\"."
            scene img then and now all info with Dissolve(0.7)
            "I know everyone else has grown a year older, too. but it's my early twenties... every year right now, from 20-25, feels crucial. Losing a single year in this stage of my life feels like so much. Like I'm losing, {i}wasting{/i} so much."
            "The thought of this going on and continuing to lose time for another year, or (god forbid) two, makes me feel sick. I want to be taking my first steps into establishing my {i}future life{/i} right now."
            "The idea of still feeling this waiting and anticipation, and not being fully or safely able to spread my wings and start my next chapter..."
            "...and then being plopped back into the world having missed my crucial transformative years..."
            "Can't stand it."
            jump choice1_done

##################################################

    # Choice 1 -> Choice 2
    label choice1_done:

        if dark: # let yourself feel the weight of the world (1A)
            "Ugh. I guess I shouldn't start thinking about all this."
            scene thinkin open eye with Fade(0.5, 0.0, 1.0)
            "But when is it good to stop that train of thought? I don't want to ignore these feelings, but I don't know how to engage with them halfway."
            scene thinkin eyes closed with Dissolve(0.7)
            "I'm not an emotionally constipated person, but if I really let myself start to think about it all, it's extremely exhausting. So most of the time, I put it off."
            scene thinkin_menu with dissolve

            # Choice 2 (dark menu)
            menu:
                # choice 2 (med)
                "Think about something else.":
                    hide thinkin_menu
                    #$ med = True
                    $ dark = False
                    "Funnily enough, and maybe it's because of that, but I feel like I've been weirdly more stable during this time; at least in some ways."
                    "I had a check-in last week— the last time I saw the doctor was way back in June 2020. She mentioned that my anxiety screener had gone WAY down, apparently."
                    "I guess I never really thought about it, but I {i}have{/i} been less anxious— overall, on the day-to-day. I guess 'cause I have less going on... but like, in a good way?"
                    "But then of course, in the more broad sense, we're probably ALL more anxious now than ever... I mean, right?"
                    "Weird how that stuff works sometimes, huh?"
                    # or have a separate choice for diversion away from spiraling thoughts-- e.g., immediately trying to seek comfort or distraction
                    jump choice2_done

                # choice 2 (dark)
                "It's okay to introspect.":
                    show thinkin eyes closed with dissolve
                    $ dark = True
                    #$ med = False
                    "Okay. You see, I know our lives have changed, and it's okay to think about it, but the thing is the entire situation is messed up in so many ways, there's so much to think about, it causes pain and anger and frustration..."
                    "and there's nothing I can do to just fix this situation so I just ask myself, \"Do you really want to subject yourself to this train of thought right now?\""
                    jump choice2_done


        else: # look on the bright side (1B)
            # the transition to this train of thought from you talking about your gpas and feeling good about finishing school doesn't make sense.
            # needs to be a clearer transition or remind to bring it back to covid; the switch in topics and emotions seems disjointed and sudden
            # keep on the train of thought of being positive?
            "It's good to feel good. Especially right now, just all things considered.{w} But I don't know, sometimes maybe I should take more time to acknowledge how tough this really all is."
            "Tough on everyone — so it's okay to think about, sometimes, how it's been tough on me."
            "It's not like I'm painstakingly avoiding it all the time or being delusional about this all, though. Even though I don't wish to compartmentalize, I think it's good overall that I don't let it bear down on me all the time?"
            "I mean, it's a weird situation. I wanna make sure I'm coping with this healthily, but also, even if I {i}am{/i} compartmentalizing or whatever, I seem to be coping and functioning pretty well, all things considered."
            "If it ain't broke, don't fix it, right?"

            # Choice 2 (bright menu)
            menu:
                # choice 2 (bright)
                "You may not give yourself enough credit. You've worked hard to be doing well.":
                    $ dark = False
                    "Yeah! Funnily enough, I feel like I've been weirdly more stable during this time, at least in some ways."
                    "I had a check-in last week— the last time I saw the doctor was way back in June 2020. She mentioned that my anxiety screener had gone WAY down, apparently."
                    "I guess I never really thought about it, but I {i}have{/i} been less anxious— overall, on the day-to-day. I guess 'cause I have less going on... but like, in a good way?"
                    "But then of course, in the more broad sense, we're probably ALL more anxious now than ever... I mean, right?"
                    "Weird how that stuff works sometimes, huh?"
                    jump choice2_done

                # choice 2 (dark)
                "It's okay to introspect.":

                    "Hahah, well, of course it is. I always try to be introspective, as a person and just in general. But introspection on a topic like this seems tricky, I think."
                    "I don't want to go down a negative train of thought for the sake of it; start thinking in a way that will make me feel defeated, or sad, just for the sake of \"trying to keep it real\" or something."
                    "There's nothing {i}I{/i} can do to just fix this situation. And I have a hard time engaging with feelings like this halfway."
                    "Sometimes I just gotta ask myself, \"Do you really want to subject yourself to this train of thought right now?\""

##################################################

    # Choice 2 -> Choice 3
    label choice2_done:

        if dark: # it's okay to introspect (2A)
            "I just struggle back and forth because I don't want to be {i}indulgent{/i} with these feelings. I'm very cautious about that."
            "Rationally, I want to engage the bad WITH the good. I want to think about this in a well-rounded way; be realistic, holistic."
            "But how do I do it in a measured fashion? If I'm engaging with my negative feelings, how do I do it in a way that's good for perspective, and not just basically an exercise in self-hatred or flagellation?"

            # Choice 3 (dark menu)
            menu:
                # choice 3 (dark)
                "Feel your feelings.":
                    $ dark = True
                    "Thinking about \"wasting time\", I still feel like I'm wasting so much even though time's already getting wasted out of my control."
                    "I hate it, but at the same time, when time doesn't matter, how hard does that fucking make it to not go ahead and just waste the days yourself, too?"
                    "I don't want to WATCH my life pass me by.{w} It's a paradox; on one hand, I want to be making the most out of my days right now. But on the other hand, I can't bear to watch my precious youth go inert."
                    "There are some days where all I can bear to do is sleep."
                    "Losing time usually makes me feel depressed, oversleeping usually leaves me with shame and guilt, but {i}the time's already been lost.{/i}"
                    "Just going through these motions each day hurts sometimes, feeling constantly that I'm heading nowhere, having to face my {b}devolution{/b} and {b}stagnancy{/b} day after day."
                    "I can't decide how bad it is that in some ways, I'd love to just wake up when this is all over. But at the same time, waking up and it's one year, two years later, would make me wanna die."
                    jump choice3_done

                # choice 3 (bright)
                "Why not focus on what you {i}can{/i} control right now?":
                    #$ med = True
                    "Maybe you're right. You don't have to sound so...{w}{i} plain?{w} flippant?{/i}{w} ...about it, though. It really feels, at first mental glance at least, that there's hardly {i}anything{/i} in my control."
                    "That's kind of what characterizes this moment, isn't it? And why we're struggling? We all got control stripped away from us."
                    jump choice3_done


        #elif med: # think about something else (2B)
        #    "What I don't like is, most of the time, when I catch myself going down a rabbit hole and I reflexively try to \"think about something else\", it feels like a distraction; like a band-aid."
        #    "I can't immediately switch my mood around in that moment— catch all the fallacies in my thinking, rebut each negative thought, become positive and start building myself back up right away."
        #    "Even if that's the more correct train of thought, it takes a minute to {i}transition{/i} like that mentally."
        #    "So that reflexive moment of \"don't think that way\" brings me in the middle: not actively being negative, pushing those thoughts away, but not actively thinking positive either."
        #    "Just doing something else— looking for thoughtful games on itch.io where I can enter some new emotional journey, but one where I'll feel happy at the end; one I can choose, one I can control."
        #    "Or even just placating myself until I feel I can move on or forget about it, or until I feel ready to take the emotions on— and that could be anything."
        #    "Watching YouTube. Doing homework. Drawing. Scrolling Twitter. Taking a bath. Anything at all."

            # Choice 3 (med menu)
        #    menu:
                # choice3 (dark)
        #        "*Emperor Palpatine voice* Feel the darkness inside you!":
        #            $ dark = True
        #            $ med = False
        #            "I just feel like I'm wasting so much precious time, even though time's already getting wasted out of my control."
        #            "I hate it, but at the same time, when time doesn't matter, how hard does that fucking make it to not go ahead and just waste the days yourself, too?"
        #            "I don't want to WATCH my life pass me by.{w} It's a paradox; on one hand, I want to be making the most out of my days right now. But on the other hand, I can't bear to watch my precious youth go inert."
        #            "There are some days where all I can bear to do is sleep."
        #            "Losing time usually makes me feel depressed, oversleeping usually leaves me with shame and guilt, but {i}the time's already been lost.{/i}"
        #            "Just going through these motions each day hurts sometimes, feeling constantly that I'm heading nowhere, having to face my {i}devolution{/i} and {i}stagnancy{/i} day after day."
        #            "I can't decide how bad it is that in some ways, I'd love to just wake up when this is all over. But at the same time, waking up and it's one year, two years later, would make me wanna die."
        #            jump choice3_done

                # choice 3 (bright)
        #        "Why not focus on good things? Something you {i}can{/i} control right now?":
        #            $ dark = False
        #            $ med = True
        #            "I haven't written this part yet."
        #            jump choice3_done


        else: #you don't give yourself enough credit (2C)
            "You don't give yourself enough credit"
            # Choice 3 (bright menu)
            menu:
                # choice3 (bright)
                "..... (bright)":
                    "Haven't written yet"
                    jump choice3_done

                # choice 3 (dark)
                "..... (dark)":
                    "Haven't written yet"
                    jump choice3_done

##################################################

    # Choice 3 -> Choice 4
    label choice3_done:

        if dark: # feel your feelings
            "Ugh. Ugh. I'm thinking negatively again. I know I can't control the situation, and I shouldn't be so hard on myself. I'm really not TRYING to be."

            # Choice 4 (dark menu)
            menu:
                # choice 4 (dark)
                "It's been so much. You've just been floating along since this started; {i}you thought it would be temporary.{/i}":
                    $ dark = True
                    "I know, right? I can't stop thinking about that. I thought I would be back at my dorm with my cat Midge in no time. I was just staying with my dad \"for the week\"!"
                    "I acted {b}so{/b} precautionarily, {b}so{/b} ahead-of-time— which was {i}good{/i}, don't get me wrong— but we acted so {i}fast{/i}. And now... it's March again."
                    "I'm so good at just chugging along, not thinking about it, \"taking it surprisingly well\", but really, I'm on autopilot. Trying to avoid burnout as much as I can."
                    "Like Wile E. Coyote on the cliff, just keep running for now— don't stop to look down."
                    "How long is it gonna be? And will I go back to \"normal\" (whatever that is), remember how to be productive and function again? Or will I stay broken?"
                    "I feel weirdly reverted, like I'm growing more childlike. Ugh.{w} I get it 'cause I had to move back in with my dad, and I've lost the independence I'd set up for myself, but I don't like it.{w} I feel dependent and infantile."
                    scene midge with Dissolve(1.0)
                    "God, I just fucking wish that at least Midge were here. That's what hurts most of all. I just wish she was here."
                    jump choice4_done

                # choice 4 (bright)
                "....":
                    $ dark = False
                    "I haven't written this part yet."
                    jump choice4_done

        # Unfinished #
        else: # why not focus on what you CAN control
            "I haven't written this part yet."
            # Choice 4 (bright menu)
            menu:
                # choice 4 (bright)
                "..... (bright)":
                    "Haven't written yet"
                    jump choice4_done

                # choice 4 (dark)
                "..... (dark)":
                    "Haven't written yet"
                    jump choice4_done

##################################################

    # Unfinished #

    # Choice 4 -> Choice 5
    label choice4_done:
        "I haven't written this part yet."

        if dark: # it's been so much ...
            menu:
                # choice 5 (bright)
                "You're starting to cry. Stop thinking like this.":
                    "I haven't written this part yet."

                ".... (dark)":
                    "Haven't written this yet."



    ########
    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
