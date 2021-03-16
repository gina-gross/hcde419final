# The script of the game goes in this file.

# The game starts here.

label start:

    # Beginning sequence

    scene bg sketchbook with Fade(0.1, 0.5, 1.2)
    scene beginning1 with Dissolve(2.0)
    pause
    scene beginning2 with Dissolve(2.0)
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

##################################################
    # Entering into the first menus/dialogue.

    # Choice 1
    menu:
        # choice 1 (bright)
        "Look on the bright side":
            $ dark = False
            # i'm feeling good. but i don't know, sometimes maybe i should take more time to acknowledge how tough this really all is. on everyone -- so it's okay to think about, sometimes, how it's been tough on me.
            scene bg sketchbook with pixellate
            "My performance in school has been great, it has actually improved a lot since quarantine started."
            scene gpa1 with Dissolve(1.5)
            "Whether it's because engaging with school the way I like to became surprisingly more accessible—{w} that's probably a big reason, actually—{w} I've been consistently more engaged overall, feeling checked in."
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
            "Like, I'm no longer in the murky middleground of my education! I knew it would take me an ambiguous \"longer time\" to finish a double degree, but \"the end\" still certainly felt far off, still some vague, soon-ish future time."
            "You know, a bridge I'll get to eventually. Especially after entering college early, and then going through a dip where I knew I'd have to retake stuff—{w} all this run-up to my eventual degree(s) was just getting perpetual."
            "Six years to get two degrees is super normal, and I'm still gonna be graduating at 22— I'm not lagging by any means, but I kinda realized why college has felt so long for me once my therapist mentioned that like... it's been 36\% of my life."
            "I entered at sixteen. I was but a young babe. So when I took capstone last year, I started actually seeing the light at the end of the tunnel and feeling revved up— ready, {i}excited{/i} to finish up strong."
            "But of course, pandemic started right in between my capstone quarters!{w} Ah, life...{w} But it kind of worked out.{w} I became more focused because I was checked back into my education with capstone, and I guess quarantine let me hone my attention."
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
                # choice 2 (bright)
                "Think about something else.":
                    scene lean_on_hand with Dissolve(1.0)
                    $ dark = False
                    "What I don't like is, most of the time, when I catch myself going down a rabbit hole and I reflexively try to \"think about something else\", it feels like a distraction; like a band-aid."
                    "I can't immediately switch my mood around in that moment— catch all the fallacies in my thinking, rebut each negative thought, become positive and start building myself back up right away."
                    "Even if that's the more correct train of thought, it takes a minute to {i}transition{/i} like that mentally."
                    "So that reflexive moment of \"don't think that way\" brings me in the middle: not actively being negative, pushing those thoughts away, but not actively thinking positive either."
                    "Just doing something else— looking for thoughtful games on itch.io where I can enter some new emotional journey, but one where I'll feel happy at the end; one I can choose, one I can control."
                    "Or even just placating myself until I feel I can move on or forget about it, or until I feel ready to take the emotions on— and that could be anything."
                    "Watching YouTube. Doing homework. Drawing. Scrolling Twitter. Taking a bath. Anything at all."
                    # or have a separate choice for diversion away from spiraling thoughts-- e.g., immediately trying to seek comfort or distraction
                    jump choice2_done

                # choice 2 (dark)
                "It's okay to introspect.":
                    scene thinkin eyes closed with dissolve
                    $ dark = True
                    "Okay. You see, I know our lives have changed, and it's okay to think about it, but the thing is the entire situation is messed up in so many ways, there's so much to think about, it causes pain and anger and frustration..."
                    "and there's nothing I can do to just fix this situation so I just ask myself, \"Do you really want to subject yourself to this train of thought right now?\""
                    jump choice2_done


        else: # look on the bright side (1B)
            # the transition to this train of thought from you talking about your gpas and feeling good about finishing school doesn't make sense.
            # needs to be a clearer transition or remind to bring it back to covid; the switch in topics and emotions seems disjointed and sudden
            # keep on the train of thought of being positive?
            "It's good to feel good. Especially right now, just all things considered.{w} But I don't know, sometimes maybe I should take more time to acknowledge how tough this really all is."
            "Tough on everyone — so it's okay to think about, sometimes, how it's been tough on me, too."
            "It's not like I'm painstakingly avoiding it all the time or being delusional about this all, though. Even though I don't wish to compartmentalize, I think it's good overall that I don't let it bear down on me all the time?"
            "I mean, it's a weird situation. I wanna make sure I'm dealing with this healthily, but also, even if I {i}am{/i} compartmentalizing or whatever, I seem to be coping pretty well, all things considered."
            "If it ain't broke, don't fix it, right?"

            # Choice 2 (bright menu)
            menu:
                # choice 2 (bright)
                "You may not give yourself enough credit. You've worked hard to be doing well.":
                    $ dark = False
                    "Yeah! Funnily enough, I feel like I've been weirdly more stable during this time, at least in some ways."
                    "I had a check-in last week— the last time I saw the doctor was way back in June 2020. She mentioned that my anxiety screener had gone WAY down, apparently."
                    "I guess I never really thought about it, but I {i}have{/i} been less anxious— overall, on the day-to-day.{w} I guess 'cause I have less going on... but like, in a good way?"
                    "But then of course, in the more broad sense, we're probably ALL more anxious now than ever... I mean, right?"
                    "Weird how that stuff works sometimes, huh?"
                    jump choice2_done

                # choice 2 (dark)
                "It's okay to introspect.":
                    $ dark = True
                    "Hahah, well, of course it is. I always try to be introspective, as a person and just in general. But introspection on a topic like this seems tricky, I think."
                    "I don't want to go down a negative train of thought for the sake of it; start thinking in a way that will make me feel defeated, or sad, just for the sake of \"trying to keep it real\" or something."
                    "There's nothing {i}I{/i} can do to just fix this situation. And I have a hard time engaging with feelings like this halfway."
                    "Sometimes I just gotta ask myself, \"Do you really want to subject yourself to this train of thought right now?\""
                    scene lean_on_hand with Dissolve(1.0)
                    jump choice2_done

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
                    "Just going through these motions each day hurts sometimes, feeling constantly that I'm heading nowhere, having to face my {i}devolution{/i} and {i}stagnancy{/i} day after day."
                    "I can't decide how bad it is that in some ways, I'd love to just wake up when this is all over. But at the same time, waking up and it's one year, two years later, would make me wanna die."
                    jump choice3_done

                # choice 3 (bright)
                "Why not focus on what you {i}can{/i} control right now?":
                    $ dark = False
                    "Maybe you're right. You don't have to sound so...{w}{i} plain?{w} flippant?{/i}{w} ...about it, though.{w} It really feels, at first mental glance, that there's hardly {i}anything{/i} in my control."
                    "That's kind of what characterizes this moment, isn't it? And why we're struggling? We all got control stripped away from us."
                    "But yeah, you're right. There's still good things, actually still a lot of positive in this whole mess."
                    jump choice3_done


        else: #you don't give yourself enough credit (2B)
            scene lean_on_hand with Dissolve(1.0)
            "I guess I have a hard time being self-congratulatory. Like, in a meaningful way."
            "When I'm accomplishing, it's something I already expect of myself. So, I don't know, I don't bask in it. It just makes me feel like I'm on the right track."
            "I do acknowledge it, but I don't know, it's kind of an unsaid given. I don't really let it sink in or give credit to the fact that no, this was due to {i}my{/i} actual work and effort."
            "{i}I{/i} did this. {i}I{/i} made it happen, it didn't just happen {i}to{/i} me."
            "Of course, it's paradoxical and not actually conducive to more success because by doing this, I give more mental attention to my failures."
            "Worrying about it, hoping I don't fail, chastising myself when I do.{w} My success goes left unsaid but hoo boy, my failure sure doesn't."
            "But spending more energy worrying about failing and punishing myself for it makes my default self-talk more negative, disproportionate to what I probably actually deserve."
            "It {i}reinforces{/i} that dumb thought pattern because I'm not recognizing my successes."
            "Anyway, all this to say that I KNOW I really should give myself way more credit, including and especially in this pandemic.{w} But even a benign comment like that feels weird to say!"
            "It makes me shy, I guess? I don't know, man!{w} But to be serious, my grades, my improvement in school, my pretty-good mental health, my stable outlook are all {i}not an accident{/i}."
            "It actually took me {i}work{/i} to get there, and it takes work to stay there."
            "Even if it's work that feels invisible to me (i.e., the vague \"I've just been more engaged somehow/have more capacity now, I guess\" mechanism), it's still not a given. I {i}have{/i} worked hard to be doing well."

            # Choice 3 (bright menu)
            menu:
                # choice3 (bright)
                "That's more like it. It's easy to write off the good as \"the usual\", but it's not. Right now, the little things are what makes the difference. Focus on the little wins, which are all around you.":
                    $ dark = False
                    "Yeah, you're right. When I think about it, there's still weird positives in this whole mess. A lot, actually."
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
                    scene baby with Dissolve(1.0)
                    "I feel weirdly reverted, like I'm growing more childlike. Ugh.{w} I get it 'cause I had to move back in with my dad, and I've lost the independence I'd set up for myself, but I don't like it.{w} I feel dependent and infantile."
                    scene midge with Dissolve(1.0)
                    "God, I just fucking wish that at least Midge were here. That's what hurts most of all. I just wish she was here."
                    jump choice4_done

        else: # why not focus on what you CAN control
            "I've been fortunate, for one. {i}We{/i} (my family) have been fortunate, but {i}I've{/i} been fortunate too.{w} There's a lot to be grateful about right now."
            "I {i}had a place to go{/i}... we can just start right there.{w} Not everybody could say that. Not everyone had that luxury."
            "Even if we don't have a \"family home\", and it's not like we have a ton of money—{w} as in, the kind of money that gives you, like... {i}stability{/i}—{w} I'm in an extremely privileged position that my dad could take me in."
            "That he lives in Seattle— I have people here, I'm not stranded. And that he had the {i}ability{/i} to take me in.{w} Even though, at the time, we DEFINITELY didn't think I'd be here on the long term... Haha."
            "But really. The fact that one week I thought maybe I had a cold or something, so by that weekend I had my worst-case plan set in place—{w} the fact I had {i}options{/i}, people to go to, to help me—{w} that's something to be grateful for."
            scene midge with Dissolve(1.0)
            "And Midge. Oh god, Midge, my heart.{w} That's the hardest subject for me. The thorniest feelings of this whole topic."

            # Choice 4 (bright menu)
            menu:
                # choice 4 (bright)
                "You acted quickly and kept Midge safe. You protected her and made the right choice, even though it was difficult. Your feelings over it only show how much you care about her, how important she is to you.":
                    $ dark = False
                    "I {b}{u}did not{/u}{/b} plan to separate with Midge. I only expected to stay with my dad for maybe a month, tops. I couldn't take her with me then, not just 'cause I'd be on the couch of a single-bed apartment (aka space), but also 'cause my dad's allergic."
                    "If I did take her there, it would have been extremely temporary. Plus, there's no pets allowed at the complex."
                    "Originally, I was just gonna ask my friend Juno if Midge could stay with her family for that bit, since they live and have stayed in the same family home for years, and already have cats."
                    "That was the best I could think of, but it would really be asking a lot out of them. I could only hope that the need would be extremely brief.{w} But I'm glad we didn't end up doing that."
                    "Even though it was a scary thought, if I {i}did{/i} suddenly become dependent again, and actually {i}move in{/i} to my dad's officially with no more dorm as an option, we would need an {i}actual{/i} Midge contingency plan."
                    "It was impossible to know the future at that time. So making real plans was hard, with so much up in the air.{w} But there needed to be a {i}place{/i} and a {i}plan{/i} for Midge."
                    "So that even in the worst case, she wouldn't be at the mercy of {i}my{/i} changing situations. I'm not gonna do that to her, there's just no way."
                    scene midgey_kiss with Dissolve(1.0)
                    "All this uncertainty and change is already enough for any human— I'd rather brave it, not her.{w} She deserves stability and safety and comfort.{w} And stability.{w} Did I mention stability?"
                    "My aunt Susan had just done a huge move from California to Washington that January. She loves cats as much as I do, understands them. But she'd only just moved, so I didn't think of her as an option."
                    "She already had full hands. But she had been talking about adopting a cat after her move; she's living in a cabin-like place on Vashon by herself."
                    "It was my dad's idea to have Midge stay with Susan. It ended up being the best situation that could have possibly happened, I think."
                    "She had the space, the literal {i}ability{/i} and capacity for Midge— and not just that, but the willingness. She wanted a kitty friend anyway."
                    "So even though it was still an imposition on her, a big ask, it was less so than maybe for someone else.{w} She's also owned cats before; logistically, this could actually work."
                    scene midge with Dissolve(1.0)
                    "And it did. It totally did. Midge is safe, warm and EXTREMELY loved with Susan. {w}And she gets to explore the outside world, the beautiful countryside of a Vashon yard, something she never did before."
                    "She's on an adventure. She's probably one of the only people whose world got bigger with the pandemic, haha."
                    "But also, more seriously, Midge has been there for Susan. That's the other key way this has worked out beyond what we planned.{w} None of us were expecting the {i}extent{/i} of this all."
                    "Even though it's been hard for me to be separated from Midge for a full year now{w} (and I mean, {i}extremely{/i} hard){w}, how hard would it have been for Susan to go through this entire thing alone?!"
                    "She had JUST moved her whole life up here before the pandemic started. We have family on Vashon, but Susan's immunocompromised. Her social circle is in California."
                    "She originally was gonna go on a road trip with her friends, then of course that got axed. She would have literally been alone in her house this full year. Thank {i}God{/i} she's with Midge!"
                    "I couldn't imagine doing it alone, and there's {i}no one{/i} else better to be with than Midge. That's my bias speaking, but now Susan knows and loves Midge just as much as me, so of course she agrees."
                    "I got Midge as an emotional support animal (yes, recommended by the doctor) and that's how I could live with her in dorms.{w} Even though I wish she was with me now, she's doing her job with someone else who needs it."
                    jump choice4_done

                # choice 4 (dark)
                "You let Midge down.":
                    $ dark = True
                    "I know.{w} That's how I feel. Even though I know that {i}literally{/i} it's not true, I can't help but feel that way."
                    scene midgey_kiss with Dissolve(1.0)
                    "I adopted her myself, she's the biggest \"adult\" move I've made in my life. I love her so much, we are so close, she has been there for me through everything. When I adopted her, I made her a promise."
                    "That I could take on the responsibility, that I would always be there for her. It's not something I take lightly. Yet I've gone back on that promise. How could I do that to her?"
                    jump choice4_done

##################################################

    # Choice 4 -> Choice 5
    label choice4_done:

        if dark: # it's been so much ...
            scene midgey_kiss with Dissolve(1.0)
            "I {b}{u}did not{/u}{/b} plan to separate with Midge. I only expected to stay with my dad for maybe a month, tops. How foolish I was back then."
            "I couldn't take her with me then, not just because I was imposing myself on my dad's single-bedroom apartment, but also because he's allergic. And there's no pets allowed at the complex."
            "If I did take her with me then, it would have been temporary at best. We wouldn't be able to put off finding an {i}actual{/i} solution for very long."
            "I can't overstate how thankful I am for my aunt Susan taking her in. It's good that we acted so quickly, ultimately. And the situation really worked out better than we could have hoped for."
            "Susan loves and understands cats just like I do, and she had just moved up to Washington. She was there by herself, with all her friends in California."
            "She already was in need of a kitty friend. And she knew how to take care of cats, it wasn't crazy out of nowhere. So really, it was perfect."
            "Plus, with how everything turned out, thank God that Midge was with her. She literally would have been {i}alone this whole year{/i} without her. Midge is still giving emotional support, even if not to me."
            "I {i}know{/i} it was the right thing to do, and it's actually a miracle how well it all worked out. So why do I still feel so deeply like I failed Midge?"
            "I know there's not a realistic situation where I would have been able to keep everything the same. Stay living on my own, stay living with her. But I feel like I should have done more. Tried harder."
            "It's not realistic, whatever. I {i}know{/i} that intellectually. But my love for her...{w} I feel like I just shipped her off when things got hard. I feel like I abandoned her."
            menu:
                # choice 5 (dark)
                "You're starting to cry. Stop thinking like this.":
                    $ dark = True
                    "God, I know. Now I'm {i}really{/i} just entering the realm of self-flagellation.{w} But God, it's true. I feel that way."
                    "I'm not going to spend time rewarding those thoughts, because even I know they're unrealistic. But it all just kind of started hitting me at once when it began to approach a full year, you know?"
                    "Maybe it's a projection of my worry for the future too. It's so fucked because Midge has been mine for three years, and now there's a full year of being away from me. An entire quarter of how long I've had her?!"
                    "I really don't want her time away from me to grow equal, God forbid even SURPASS the time she's been with me!"
                    jump choice5_done

                # choice 5 (bright)
                "You're feeling grief, and that's real. It's okay. But you know those things aren't true.":
                    $ dark = False
                    "Yeah... I know. And I know the choice I made is actually a testament of responsibility, and of doing the right thing. I'd say \"sacrifice\" but that sounds extreme."
                    "It just really started getting to me when it began to come up on a year.{w} It all just hit me, I don't know. The whole situation really started to sink in."
                    "The future feels so uncertain too. Especially with graduating college— I'm not going to be living in a dorm apartment anymore. Where am I gonna live? What will my next chapter actually look like?"
                    jump choice5_done

##################################################

    # After Choice 5
    label choice5_done:
        scene beginning3 with pixellate
        "At least there's actually hope on the horizon."
        "The worst part of this all, I think, was{w} (is?){w} the uncertainty— as in; the rough situation itself is okay maybe, but having {i}no{/i} mental concept of a timeline isn't."
        "Not being able to plan ahead, or knowing when you CAN or even should start planning; only being able to watch and wait, literally only existing in the moment."
        "I like to plan, to prepare myself for things, to at least have some mental concept of my next steps. Knowing what's coming, you know? But obvs, in the pandemic, we can't do that. We HAVE to take it one day at a time."
        "Which gets boring! I hate such a sustained feeling of waiting, anticipation— it feels so unnatural. Feelings like that aren't supposed to be perpetual!"
        "But finally, we have our first {i}concrete{/i} next step in the timeline:{w} the vaccine.{w} I don't know how quickly this pandemic will really get handled, but dear God, at {i}LEAST{/i} there's another data point for the mental map."
        "I have another point of reference from which to conceptualize the situation, for once. It's not PURELY just endless ambiguity with no respite."
        "And while \"going back to normal\" for real is going to be its own crazy transition— I definitely, weirdly, don't feel ready— that's not really something to think about yet."
        "Allegedly, starting May 1st all adults will become eligible for the vaccine. Who knows how long it'll actually take after that to go through the line and get it, but man, whatever."
        "It'll be nice to be able to see more of my friends finally! I can't even imagine it right now, haha.{w} Nothing big or fancy, but just something. It's just good for the heart."
        scene midgey_kiss with dissolve
        "And best of all. {w} {i}Drumroll please...{/i} {w} I'll get to spend MUCH more time with Susan! My Midge infusions will go up significantly.{w} As it should be. It's what the doctor ordered, after all."
        "And hey, right now, that's... kind of all I need."
        "It's not the light at the end of the tunnel, but at least we have our first mile marker."
        "We have an idea of where we are now. Roughly, but it's there.{w} That sounds like a little, but it's a lot."
        "And we have a place to go next."
        scene black with Dissolve(1.0)
        "The end.{w}.. for now?"




    ########
    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
