# \*Something
Don't have a title for this just yet, but here goes! A space fantasy game that'll also pretty much be the best dnd--causing folks to foresake all other dnds. Setting ambitions & expectations right about there.

The trick here is that all of this is going to be created and published via things I can do in the command line. Specifically things I can do in the command line of my Raspberry Pi, but in all fairness, some of this will be done in the Window Subsystem for Linux because ssh'ing into my Raspberry Pi can be slooooooow. And I too old for sloooooow.

Part of this is to help me find my way around this environment and learn to use these tools and part of it is for the creative constraints involved. One of these tools is git and I'm going to use this as an opportunity to design out in the open a bit. So I'm putting all this up on GitHub, where you're probably reading this right now. You're welcome to peruse these files, see what I'm up to, and comment on them. Go ahead and use all the usual GitHub features, if you like. It'll be a lovely excuse for me to play with those tools as well.

This particular document, and what follows, will be something of a stream of consciousness exercise. This is typical of how I begin a design. It'll start as a some idea coalescing in my head, uncommitted to text, until I realize I need to organize these thoughts somehow. That somehow usually starts with something that looks like a poorly slapped together instructional text. I'll edit and re-edit this for a while, trying to drill down to what it is I want the rules to do while also trying out different ways of presenting these. Eventually, this document will loose cohesion as I move my more honed text over into something looking a bit more official. At some point, I'll abandon these notes and start all over in a new file. It is possible that using version control software like git will change this behavior. Perhaps this file will evolve and stay up-to-date with the rest of the project. Only time will tell. I'm just leaving this here as a warning, in case it doesn't: this is all pre-first-draftery.

## General Flow
There'll be a GM, but of course, we'll need a new name for them. *Fun game:* see which comes first, the game title or the GM title. For now, let's call them the GM. 

The GM starts the game by picking one of the dice and putting it in the middle of the table showing either a 1 or a 6. A 1 if the PCs are in the thick of it; a 6 if they're showing off how awesome they are. The choice of die is important, so maybe we should talk about these dice.  

There are 5 types of dice, all of them d6s:

* The Compelling Die--For all things gregarious, impressive, dazzling & mesmerizing
* The Daring Die--For all things dangerous, violent, thrilling & scary
* The Expertise Die--For all things clever, thoughful, tricky & technical
* The Sneaky Die--For all things subtle, stealthy, quiet & devious
* The Thriving Die--For all things calm, perservering, hale & hearty

Think of these dice as hewing closer to tones than ability scores. They will, to a limited extent, define some character abilities, but for the most part, they are more about cinematography and soundtrack then they are about C.V.s and grades.

Players who are the GM will have characters--probably one apiece, but who knows--that they champion. These characters will have a subset of these dice available to them, plus a handful of skills. That's right. Skills. From a skill list. With skill scores. Like I was designing this game in the year 1989.

### Rolling and Resolving
When a player wants their character to do something, they speak up. If it's something difficult or dangerous, it might require a roll. This is how we'll put that together:

* The player says what they're doing and trying to achieve. The GM decides what skill this will use and what overall goal might apply to this.
	* There's room for negotiation here, if fact negotiations might be fun, and player can explicitly state that they want to use a specific skill or work towards a specific goal, but ultimately the player's role is to describe the characters action and intent and the GM is responsible for applying those to a skill and a goal.
	* Both the skill and the goal add to the roll. So this isn't a fiddly bit for fiddly's sake.
* The GM will also give you a success threshold. This probably something like 7, 10, 13, 16, 19, etc.
* The player will be rolling two of their dice. These dice must be of different types and neither may be of the same type as the one in the middle of the table.
* The player then chooses one of these two dice to keep and swap the other with the die in the middle of the table.
* Now they should have two dice, one they rolled and the other recently taken from the middle of the table. These two together will give your result:
	* If they are tied, you suffer a dramatic setback but gain a learning experience. More on both of these later. The important bits are: you don't succeed, you probably lose your progress towards your goal, you don't gain any benefit from a highest die, but you get better at the skill you were using.
	* If they aren't tied, check to see what side benefits you get from the highest of the two dice (see below) and then add these two dice together (the die you took from the middle of the table and the die you kept) plus your skill bonus and any progress made towards the goal and compare that against the full success threshold given by the GM.
		* A total of 6 or less means you're not there yet. Add 1 to the goal's progress, the GM will probably tell you what stands in your way, or how things aren't going to plan, and we're going to move on to another player.
		* A total equal to or greater than the full success threshold accomplishes your intent! Well done! You'll probably get to describe what that looks like. Your progress towards the Goal that was applied is zeroed out. And the game moves on to another character, for now.
		* A total between these two, >= 7 but < the full success threshold, is a win you can choose to take. The GM will offer you something short of your intent. You can grab it and run, which zeroes out the progress towards the Goal, but at least gets you something. Or you can choose to treat the result as a 6 or less, keeping your goal's progress and adding 1 to it.

Okay, that's a lot of business about this goal and the progress towards it. We'll talk about that soon. But first, a few more comments about the dice.

### Benefits from High Dice
The game takes place in space, but the characters don't live in a vacuum. To begin with, there's always that die in the middle of the table that they'll be orbiting around. When each player rolls, they incorporate that die into their roll and leave another die in its place for the next player. This should inform their decisions.

If the result of a roll isn't a tie (and in most cases, players will have to actively choose a tie for it to occur) then there will be a highest die. This highest die confers a benefit, depending on the type of die it is:
* Compelling: Someone witness to these events is impressed by you, your presence, or your actions. If this die is showing a 6, you also gain a Hunch Token.
* Daring: You and your allies are unharmed by the current actions being resolved. If this die is showing a 6, you also gain a Initiative Token.
* Expertise: If you take the win instead of going for a full success, this goal's progress is not zeroes out. If this die is showing a 6, you also gain a Foresight Token.
* Sneaky: Your actions go unnoticed by all you wish to hide them from. If this die is showing a 6, you also gain a Clue Token.
* Thriving: In addition to the other results of this roll, you can also take a step towards recovery. I'll worry about what the means later. If this die is showing a 6, you also gain a Focus Token.

These benefits are optional, and importantly, they may not always be applicable. Rolling your Daring die while trying to repair a ship in dry dock does not mean the situation is particularly dangerous. It just means that if it turned out to be, and that Daring die comes out on top, you and your allies can't be harmed by it.

### Tokens
The tokens are a special sort of benefit. Still a little fuzzy on them. But here's the current take. You can only ever have one of each type. You spend them:
* Spend 1 at any time to gain important information.
* Spend 1 when the GM surprises you to ensure that your character is not surprised.
* Spend 2 when the GM surprises you to ensure that your character and their allies in the scene are not surprised.
* Spend 3 when the GM surprises you to turn the tables on the GM's characters and surprise them instead.

Something like that. The point is that there is no rolling for this stuff directly. Just collecting tokens during play and spending them. Probably should start each session with a Token. Got to think on that.

### Learning Experiences
As mentioned before, a tie is bad. It's the main failure mechanic in the game. There's no miss on a 6 or less. Instead, it's an almost there. But on a tie, you suffer a dramatic setback, you lose your progress bonus towards whatever Goal you were working on, and no die is considered a high die, so you don't even get that bonus. Generally, worth avoiding, except...

If the tie is on a number greater than your current skill level, then it's a Learning Experience, which means you can go ahead and raise that skill by 1. You don't have the skill? Then any tie will give you skill at a +1. After that, you'll need dice that tie on 2 or more raise it to a +2. Then dice that tie on a 3 or more to get it to a +3. And so forth.

Should you take the tie? I don't know, but maybe? Or maybe wait for that 1 in 36 chance that you don't have a choice, when the dice you rolled tied and happened to tie on the same value as the die in the middle. Oh I hope that number's high enough to matter for the skill you're using. The thing is...

### ...Dramatic Setbacks...
...are basically free license for the GM to do their worst. Disable your ship halfway into a warp jump. Shoot your favorite laser sword out of your hand and into the gaping maw of a ice worm. Oh no, the even space paladin is your dad! Nothing can prevent or mitigate this.

### Goals
Alright, finally. This is an important piece and I'm going to have to use an example to illustrate it. You got a giant space battle going on. The PCs are a crew of a rogue vessel, well-armed for one-on-one conflict with a stray pirate, but not quite a match for the StarMonarch's Doom Fleet. But here they are, in the middle of it. We've got 3 crew we care about at the moment: Stevelynn, Geophanie, and Bertrude. Stevelynn is an excellent gunner, with a +4 in Gunnery. Geophanie is a fair pilot, with a +2 in Pilot: Space Craft. Bertrude's a cunning spy with a +2 in Comms.

They've been tailing the Doom Fleet. Bertrude has been trying to get a message to an operative aboard the StarMonarch's flagship Scary Name. But they haven't had an opportunity to get close enough to send a localized transmission or some technobabble like that. But fortune favored them as a MegaFederation convoy crossed the Doom Fleet's path and a titanic battle has ensued.

Each character has their own lowercase goal at the moment. Bertrude wants to deliver the encrypted message. Geophanie wants to see them and their rogue vessel safely away from all this blaster fire. And Stevelynn wants to shoot down the Doom Fleet's ace pilot, Lord Wuffington. The GM chooses to map these into two uppercase Goals, because it'll be more fun that way. The first is Transmission, which is all about Bertrude's goal. The second is Battle, which is a combo of Stevelynn and Geophanie's goals.

Any time a character's intent is aligned with one of these goals, they add to that goal's progress bonus if they rolled a 6 or less, they add that goal's progress bonus to their roll, and they risk zeroing that goal's progress bonus out, should they end up with a tie.

Goals and their progress bonuses are shared this way. It doesn't matter who voiced the goal first, and it doesn't matter what the exact wording of that original goal was. The GM takes the voiced goals and coalesces them into Goals with a capital G. These Goals are nebulous and can accomodate a number of related targets, even ones that may be at odds with one another. I mean, if Geophanie is focused on fleeing, that may end up being accomplished before Stevelynn can shoot down Lord Wuffington, but both of these are encompassed by the Battle Goal, so when either of them roll with an intent that furthers their own cause, they benefit from and affect that Goal.

Not all intents need to be focused on a Goal. If during this fight they spot a MegaFederation pilot unconscious and adrift, Geophanie may choose to swing by and pick them up. This could create a new Goal. But I'm getting ahead of myself. Let's put a die on the table and start this example of play.

Sneaky [6] <-- The GM puts this out, partly because they feel sorry for the players being in this situation, and partly because they think that one little vessel can easily be lost in a giant battle like this. Being Sneaky is something that could help all of them, but directly help Geophanie or Bertrude's stated objectives. After some discussion, the team decides to let Bertrude take first crack at this. After all, she'll need to pull this off before Geophanie flies them to safety.

Bertrude tells the GM that her plan is to encode the message in a low-wave beacon and tether that to the Doom Fleet's flagship with the harpoon gun. It's kind of a surprise move. The GM says this is her Gunnery skill, which is at a +0, and Bertrude agrees, perhaps angling for an advancement there. The GM also says this is working towards the Transmission goal, but we already knew that. Finally, the GM assesses the likelihood of Bertrude making this shot. This is based on her intent (to attach the low-wave beacon to the flagship) and her actions (shooting it out of the harpoon gun), and is independent of her overall Goal. The flagship's big and easy to hit, but it's at battle stations with repulsor fire and active shields. All this technobabble makes the GM think this might be kind of difficult. At least a 10?

Wait, let's work this out. A 7 is an almost trivial task. Ignoring the 6 that's already sitting on the table--GM shouldn't be taking that into account anyway--Bertrude's rolling two dice, could just choose the highest, and add that to a number between 1 and 6. Let's pause and work out those odds in Python: see [odds.py](./odds.py)

Right, so roughly speaking, a 7 or more happens 75% of the time. A 10 or more happens about a quarter of the time. So those are our two starting points. A 7 is routine, a 10 is tough, but possible with a lucky shot. Anything higher will need skill or several time, or both.

The GM thinks this requires a bit of skill, but one lucky shot could do it. So they set the threshold at 10, despite a whole section of the rulebook dedicated to convincing them to set it higher.

Since they are in the middle of a star fight, Bertrude chooses to roll her Daring die and her Expertise die. She won't be able to make use of either, because Sneaky is already a 6, but if she rolls well on the Daring, she can pass it along and set someone else up nicely. Time to play a little with Python and roll these dice.
	Daring: [6]
	Expertise: [2]

Here's Bertrude's dilemma. A nice safe bet here would be to keep the Experise of 2 and swap the Daring of 6. That would result in a 8, which doesn't meet the threshold, but it's higher than a 6. That means she could Take the Win. She won't get exactly her intent, but she'll get something. The GM should tell her what, if she asks. Something to tempt her. Perhaps she tethers the beacon, but on a ship near the flagship. Her operative might not encounter it in time. Or perhaps the beacon lands somewhere where it'll eventually be discovered, but not until after her operative got the message. Taking the Win could be all that Bertrude really needs. And that would be fortunate, because Taking the Win has a downside--you lose all your progress; but this is the first roll towards this Goal and there is no progress to lose.

Or she could choose the 6 or less option, which would mean she couldn't get a clean shot just yet, but would add 1 to the progress towards that goal going forward. Maybe next time would be better.

Both of these options include the Sneaky die as the highest die, which means no one will notice her attempt unless she wants them to, and because that die is also a 6, it would give her a Clue Token to be used later one.

BUT if she chooses Daring, that would make it a tie. No highest die. No guarantee they wouldn't be noticed. No Clue Token. All the progress towards this goal would be lost (and again, there is none at the moment, so who cares?). The GM gets to deliver a dramatic setback right now at the very beginning of the session. But most importantly, she would get a Learning Experience in Gunnery, since 6 is definitely larger than 0. That would bring her Gunnery up to +1.

Unlike Taking the Win, the GM doesn't have to, and probably shouldn't, tell her what the Dramatic Setback will be before she chooses.

Which should she choose?

Let's say she plays it cautiously. Takes the 6 or less. The Transmission Progress is now +1 and because Sneaky was the highest die with a 6, no one notices them and Bertrude gains a Clue Token.

She also put the Daring die forward with a [6] on it. It'll be someone else's turn to use that die in a moment, but before that, the GM gets to react. They are still unnoticed, so no one's targeting them, but it's a giant dogfight and lots of beams and debris flying around. The GM decides that one of the reasons Bertrude couldn't get her shot off is because two fighters collided with one another, raining glittering destruction upon their little rogue vessel, knocking out their harpoon array. Now, Bertrude has just earned a Clue Token. She could spend this say she saw the collision coming and retracted the array in time, but she has other plans.

Daring [6]

Who's up next? Can't be Bertrude, she just went. Stevelynn? Geophanie? 
