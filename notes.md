# \*Something
Don't have a title for this just yet, but here goes! A space fantasy game that'll also pretty much be the best dnd--causing folks to foresake all other dnds. Setting ambitions & expectatio right about there.

The trick here is that all of this is going to be created and published via things I can do in the command line. Specifically things I can do in the command line of my Raspberry Pi, but in all fairness, some of this will be done in the Window Subsystem for Linux because ssh'ing into my Raspberry Pi can be slooooooow. And I too old for sloooooow.

Part of this is to help me find my way around this environment and learn to use these tools and part of it is for the creative constraints involved. One of these tools is git and I'm going to use this as an opportunity to design out in the open a bit. So I'm putting all this up on GitHub, where you're probably reading this right now. You're welcome to peruse these files, see what I'm up to, and comment on them. Go ahead and use all the usual GitHub features, if you like. It'll be a lovely excuse for me to play with those tools as well.

This particular document, and what follows, will be something of a stream of consciousness exercise. This is typical of how I begin a design. It'll start as a some idea coalescing in my head, uncommitted to text, until I realize I need to organize these thoughts somehow. That somehow usually starts with something that looks like a poorly slapped together instructional text. I'll edit and re-edit this for a while, trying to drill down to what it is I want the rules to do while also trying out different ways of presenting these. Eventually, this document will lose cohesion as I move my more honed text over into something looking a bit more official. At some point, I'll abandon these notes and start all over in a new file. It is possible that using version control software like git will change this behavior. Perhaps this file will evolve and stay up-to-date with the rest of the project. Only time will tell. I'm just leaving this here as a warning, in case it doesn't: this is all pre-first-draftery.

## General Flow
There'll be a GM, but of course, we'll need a new name for them. *Fun game:* see which comes first, the game title or the GM title. For now, let's call them the GM. 

The GM starts the game by picking a die--one of the five types listed below--and choosing a face for this die, either 1 or 6. A 1 if the PCs are in the thick of it; a 6 if they're showing off how awesome they are. The choice of die is important, so maybe we should talk about these dice.  

There are 5 types of dice, all of them d6s:

* The Compelling Die--For all things gregarious, impressive, dazzling & mesmerizing
* The Daring Die--For all things dangerous, violent, thrilling & scary
* The Expertise Die--For all things clever, thoughful, tricky & technical
* The Sneaky Die--For all things subtle, stealthy, quiet & devious
* The Thriving Die--For all things calm, perservering, hale & hearty

Think of these dice as hewing closer to tones than ability scores. They will, to a limited extent, define some character abilities, but for the most part, they are more about cinematography and soundtrack then they are about C.V.s and grades.

Let's try out some terminology here. This die type and its value is the Course. As in setting a Course. The next player to roll will have to use this die and its value, but then they will alter the Course by putting one of their dice in its stead.

Players who are *not* the GM will have characters--probably one apiece, but who knows--that they champion. These characters will have a subset of these dice available to them, plus a handful of skills. That's right. Skills. From a skill list. With skill scores. Like I was designing this game in the year 1989.

### Rolling and Resolving
When a player wants their character to do something, they speak up. If it's something difficult or dangerous, it might require a roll. This is how we'll put that together:

* The player says what they're doing and trying to achieve. The GM decides what skill this will use and what overall progress bar might apply to this.
	* There's room for negotiation here, in fact negotiations might be fun, and player can explicitly state that they want to use a specific skill or work towards a specific progress bar, but ultimately the player's role is to describe the characters action and intent and the GM is responsible for applying those to a skill and a progress bar.
	* Both the skill and the progress bar add to the roll. So this isn't a fiddly bit for fiddly's sake.
* The GM will also give you a success threshold. This probably something like 7, 10, 13, 16, 19, etc.
* The player will be rolling two of their dice. These dice must be of different types and neither may be of the same type as the one in the middle of the table.
* The player then chooses one of these two dice to keep and swap the other with the die in the middle of the table.
* Now they should have two dice, one they rolled and the other recently taken from the middle of the table. These two together will give your result:
	* If they are tied, you suffer a dramatic setback but gain a learning experience. More on both of these later. The important bits are: you don't succeed, you probably lose your progress, you don't gain any benefit from a highest die, but you get better at the skill you were using.
	* If they aren't tied, check to see what side benefits you get from the highest of the two dice (see below) and then add these two dice together (the Course die you were saddled with and the one you rolled and chose to keep) plus your skill bonus and any progress made towards the progress bar and compare that against the full success threshold given by the GM.
		* A total of 6 or less means you're not there yet. Add 1 to the current progress bar, the GM will probably tell you what stands in your way, or how things aren't going to plan, and we're going to move on to another player.
		* A total equal to or greater than the full success threshold accomplishes your intent! Well done! You'll probably get to describe what that looks like. Your current progress bar gets zeroed out. And the game moves on to another character, for now.
		* A total between these two, >= 7 but < the full success threshold, is a win you can choose to take. The GM will offer you something short of your intent. You can grab it and run, which zeroes out the progress bar, but at least gets you something. Or you can choose to treat the result as a 6 or less, keeping your progress bar and adding 1 to it.

Okay, that's a lot of business about this progress bar, zeroing it and adding to it. We'll talk about that soon. But first, a few more comments about the dice.

### Benefits from High Dice
The game takes place in space, but the characters don't live in a vacuum. To begin with, there's always that die in the middle of the table that they'll be orbiting around. When each player rolls, they incorporate that die into their roll and leave another die in its place for the next player. This should inform their decisions.

If the result of a roll isn't a tie (and in most cases, players will have to actively choose a tie for it to occur) then there will be a highest die. This highest die confers a benefit, depending on the type of die it is:
* Compelling: Someone witness to these events is impressed by you, your presence, or your actions. If this die is showing a 6, you also gain a Rumor Token.
* Daring: You and your allies are unharmed by the current actions being resolved. If this die is showing a 6, you also gain a Initiative Token.
* Expertise: Taking the Win or getting a full success will not zero out the progress bar. If this die is showing a 6, you also gain a Foresight Token.
* Sneaky: Your actions go unnoticed by all you wish to hide them from. If this die is showing a 6, you also gain a Clue Token.
* Thriving: In addition to the other results of this roll, you can also offer someoone, including yourself, a step towards recovery. I'll worry about what the means later. If this die is showing a 6, you also gain a Focus Token.

These benefits are optional, and importantly, they may not always be applicable. Rolling your Daring die while trying to repair a ship in dry dock does not mean the situation is particularly dangerous. It just means that if it turned out to be, and that Daring die comes out on top, you and your allies can't be harmed by it.

### Tokens
The tokens are a special sort of benefit. Still a little fuzzy on them. But here's the current take. You can only ever have one of each type. You spend them:
* Spend 1 at any time to gain important information.
	* Each token type should have its own set of questions you can ask.
	* You can ask one question from this list when you spend the token, or 2 if you're currently discussing the topic with NPCs.
* Spend 1 when the GM surprises you to ensure that your character is not surprised.
	* This will let you avoid arbitrary harm. Like, if the GM says, "The room is booby-trapped! The floor disentigrates beneath you and you all fall into a laser pit. Everyone advance your Destiny track by one." You can spend any 1 token to say, "Nope, not me, and here's why," followed by an explanation of why that specific token saved you.
* Spend 2 when the GM surprises you to ensure that your character and their allies in the scene are not surprised.
	* This will let you avoid arbitrary harm. Like, if the GM says, "The room is booby-trapped! The floor disentigrates beneath you and you all fall into a laser pit. Everyone advance your Destiny track by one." You can spend any 2 tokens to say, "Nope, not us, and here's why," followed by an explanation of why that specific token saved you.
* Spend 3 when the GM surprises you to turn the tables on the GM's characters and surprise them instead.
	* As above, this will save the lot of you from arbitraty harm, but also will let you turn the tables, "I had heard Rumors that Lord Wuffington had rigged his palace up with deathtraps, so when I kicked a pebble and it fell through the floor I recognized that as a Clue, and I took the Initiative to have us pretending to fall into the trap, but instead, cling to the sides of the pit just below the holo-floor to lay in wait for poor guards who would have to clean this mess up. Might get some official uniforms off of them."

Something like that. The point is that there is no rolling for this stuff directly. Just collecting tokens during play and spending them. Tokens are persistent from session to session. That is, you start each session with the ones you ended the last session with. Oh! That means the 6s you roll when rolling for adventurer type are the tokens your new character starts with!

#### Where do Tokens come from?
There are five tokens you get from each of the five dice. You get them whenever a die you used in your roll (either the Course or the die you keep, or both) is a 6. You *do* get them when you have a tie.
* Compelling Die gives you the Rumor Token, representing insight you have from things you have heard from other folks.
* Daring Die gives you the Initiative Token, representing your danger sense and acute reflexes.
* Expertise Die gives you the Foresight Token, representing you being prepared for this eventuality.
* Sneaky Die gives you the Clue Token, representing your keen eye for deception and trickery in others.
* Thriving Die gives you the Focus Token, representing your spatial awareness and a presence of mind.

There are tokens beyond these five that you might aquire through means other than rolling. For example, those with a Foolhardy Destiny may pick up a Luck Token from time to time, representing pure happenstance.

You may not have more than one of any given token, but all tokens essentially work the same. The only benefit of a rare token is that you are unlikely to already have one, and therefore you won't have to reject it.

### Learning Experiences
As mentioned before, a tie is bad. It's the main failure mechanic in the game. A 6 or less is not an automatic miss. A 6 or less just means you're almost there, which could be a near miss, but could also be you taking your time and doing it right. And probably should, more often, mean exactly that. See my example of a [laser sword duel](#example-laser-sword-slingers) below for more details.

But on a tie, you suffer a dramatic setback, you lose the progress bar you were working on, and no die is considered a high die, so you don't even get that bonus. Generally, worth avoiding, except...

If the tie is on a number greater than your current skill level, then it's a Learning Experience, which means you can go ahead and raise that skill by 1. You don't have the skill? Then any tie will give you skill at a +1. After that, you'll need dice that tie on 2 or more raise it to a +2. Then dice that tie on a 3 or more to get it to a +3. And so forth.

Should you take the tie? I don't know, but maybe? Or maybe wait for that 1 in 36 chance that you don't have a choice, when the dice you rolled tied and happened to tie on the same value as the die in the middle. Oh I hope that number's high enough to matter for the skill you're using. The thing is...

### ...Dramatic Setbacks...
...are basically free license for the GM to do their worst. Disable your ship halfway into a warp jump. Shoot your favorite laser sword out of your hand and into the gaping maw of a ice worm. Oh no, the even space paladin is your dad! Nothing can prevent or mitigate this.

### Progress Bars
Alright, finally. This is an important piece and I'm going to have to use an example to illustrate it. You got a giant space battle going on. The PCs are a crew of a rogue vessel, well-armed for one-on-one conflict with a stray pirate, but not quite a match for the StarMonarch's Doom Fleet. But here they are, in the middle of it. We've got 3 crew we care about at the moment: Stevelynn, Jethany, and Bertrude. Stevelynn is an excellent gunner, with a +4 in Gunnery. Jethany is a fair pilot, with a +2 in Pilot: Space Craft. Bertrude's a cunning spy with a +2 in Comms.

They've been tailing the Doom Fleet. Bertrude has been trying to get a message to an operative aboard the StarMonarch's flagship Scary Name. But they haven't had an opportunity to get close enough to send a localized transmission or some technobabble like that. But fortune favored them as a MegaFederation convoy crossed the Doom Fleet's path and a titanic battle has ensued.

Each character has their own goal at the moment. Bertrude wants to deliver the encrypted message. Jethany wants to see them and their rogue vessel safely away from all this blaster fire. And Stevelynn wants to shoot down the Doom Fleet's ace pilot, Lord Wuffington. The GM chooses to map these into two progress bars, because it'll be more fun that way. The first is Transmission, which is all about Bertrude's goal. The second is Battle, which is a combo of Stevelynn and Jethany's goals.

Any time a character's intent is aligned with one of these progress bars, they add to that progress bar's bonus if they rolled a 6 or less, they add that progress bar's bonus to their roll, and they risk zeroing out that progress bar's bonus, should they end up with a tie.

Progress bars and their bonuses are shared this way. The GM takes the voiced goals of the characters and coalesces them into progress bars. These progress bars are nebulous and can accomodate a number of related objectives, even ones that may be at odds with one another. I mean, if Jethany is focused on fleeing, that may end up being accomplished before Stevelynn can shoot down Lord Wuffington, but both of these are encompassed by the Battle progress bar, so when either of them roll with an intent that furthers their own cause, they benefit from and affect that same progress bar.

Not all intents need to be focused on an overall goal that fits in with a progress bar. If during this fight they spot a MegaFederation pilot unconscious and adrift, Jethany may choose to swing by and pick them up. This could create a new progress bar if Jethany rolls or chooses the 6 or less option. But I'm getting ahead of myself. Let's put a die on the table and start this example of play.

Sneaky [6] <-- The GM puts this out, partly because they feel sorry for the players being in this situation, and partly because they think that one little vessel can easily be lost in a giant battle like this. Being Sneaky is something that could help all of them, but directly help Jethany or Bertrude's stated objectives. After some discussion, the team decides to let Bertrude take first crack at this. After all, she'll need to pull this off before Jethany flies them to safety.

Bertrude tells the GM that her plan is to encode the message in a low-wave beacon and tether that to the Doom Fleet's flagship with the harpoon gun. It's kind of a surprise move. The GM says this is her Gunnery skill, which is at a +0, and Bertrude agrees, perhaps angling for an advancement there. The GM also says this is working towards the Transmission progress bar, but we already knew that. Finally, the GM assesses the likelihood of Bertrude making this shot. This is based on her intent (to attach the low-wave beacon to the flagship) and her actions (shooting it out of the harpoon gun), and is independent of the goal that set her progress bar. The flagship's big and easy to hit, but it's at battle stations with repulsor fire and active shields. All this technobabble makes the GM think this might be kind of difficult. At least a 10?

Wait, let's work this out. A 7 is an almost trivial task. Ignoring the 6 that's already sitting on the table--GM shouldn't be taking that into account anyway--Bertrude's rolling two dice, could just choose the highest, and add that to a number between 1 and 6. Let's pause and work out those odds in Python: see [odds.py](./odds.py)

The odds of 7 or more on 1 roll with no bonus are roughly 74.54%

The odds of 10 or more on 1 roll with no bonus are roughly 26.85%

The odds of an inescapable tie are 2.78%

The odds of an available tie are 30.56%

Odds of a useful tie if the Course is random and...
...your skill is +0 are 30.56%
...your skill is +1 are 25.46%
...your skill is +2 are 20.37%
...your skill is +3 are 15.28%
...your skill is +4 are 10.19%
...your skill is +5 are 5.09%

Right, so roughly speaking, a 7 or more happens 75% of the time. A 10 or more happens about a quarter of the time. So those are our two starting points. A 7 is routine, a 10 is tough, but possible with a lucky shot. Anything higher will need more skill or several rolls, or both.

The GM thinks this requires a bit of skill, but one lucky shot could do it. So they set the threshold at 10, despite a whole section of the rulebook dedicated to convincing them to set it higher.

Since they are in the middle of a star fight, Bertrude chooses to roll her Daring die and her Expertise die. She won't be able to make use of either, because Sneaky is already a 6, but if she rolls well on the Daring, she can pass it along and set someone else up nicely. Time to play a little with [Python](./d.py) and roll these dice.
	Daring: [6]
	Expertise: [2]

Here's Bertrude's dilemma. A nice safe bet here would be to keep the Experise of 2 and swap the Daring of 6. That would result in a 8, which doesn't meet the threshold, but it's higher than a 6. That means she could Take the Win. She won't get exactly her intent, but she'll get something. The GM should tell her what, if she asks. Something to tempt her. Perhaps she tethers the beacon, but on a ship near the flagship. Her operative might not encounter it in time. Or perhaps the beacon lands somewhere where it'll eventually be discovered, but not until after her operative got the message. Taking the Win could be all that Bertrude really needs. And that would be fortunate, because Taking the Win has a downside--you lose all your progress; but this is the first roll towards this progress bar so there's nothing to lose.

Or she could choose the 6 or less option, which would mean she couldn't get a clean shot just yet, but would add 1 to the progress bar going forward. Maybe next time would be better.

Both of these options include the Sneaky die as the highest die, which means no one will notice her attempt unless she wants them to, and because that die is also a 6, it would give her a Clue Token to be used later one.

*But* she chooses Daring, that would make it a tie. No highest die. No guarantee they wouldn't be noticed. No Clue Token. All the progress towards this goal would be lost (and again, there is none at the moment, so who cares?). The GM gets to deliver a dramatic setback right now at the very beginning of the session. But most importantly, she would get a Learning Experience in Gunnery, since 6 is definitely larger than 0. That would bring her Gunnery up to +1.

Unlike Taking the Win, the GM doesn't have to, and probably shouldn't, tell her what the Dramatic Setback will be before she chooses.

Which should she choose?

Let's say she plays it cautiously. Takes the 6 or less. The Transmission Progress is now +1 and because Sneaky was the highest die with a 6, no one notices them and Bertrude gains a Clue Token.

She also put the Daring die forward with a [6] on it. It'll be someone else's turn to use that die in a moment, but before that, the GM gets to react. They are still unnoticed, so no one's targeting them, but it's a giant dogfight and lots of beams and debris flying around. The GM decides that one of the reasons Bertrude couldn't get her shot off is because two fighters collided with one another, raining glittering destruction upon their little rogue vessel, knocking out their harpoon array. Now, Bertrude has just earned a Clue Token. She could spend this say she saw the collision coming and retracted the array in time, but she has other plans.

Daring [6]

Who's up next? Can't be Bertrude, she just went. Stevelynn? Jethany?

## Skills
I'm going to start by borrowing a [skill list](./skills.csv) from an older space fantasy game, yank out all passive skills that will be handled with tokens, and massaged a bit to closer fit the sensibilities I'm looking for. It shouldn't matter too much right now. A skill is a chunk of fictional positioning. A way for a character to say, "I know how to do this this well, so give me some bonus." Under this definition, they'll be pretty flexible. Something the players should be able to make up on the fly. Additionally, all of the player's characters have all of the skills on the list and all other possible skills at at least +0. "Hey, do I know how to play the theremin?" "Yup, you have Performance: Theremin at +0." "Sweet." 

So the list is just a jumping off point. We not going to worry about granularity. We can let individual play groups zero in on what works for them. Since it only takes one tie to bring a 0 to a 1, everyone is just one big mistake away from being skilled in something. We're also not going to worry about overlap. Knowledge: Class--Aristocrat or Knowledge: Culture--MegaFederation Court can both be used to talk your way into some high society intrigue with the MegaFederation's hoity-toity, so just use whichever one you want. Probably your highest, unless you're looking for mischief and want to hit that tie raise up a lower skill.

"Hey Eppy, what if someone tries their hand at something really arcane or weird. Like, does everyone have telekinesis or just space-knight-witches?" That's a very good question. Here's where things are going to get a bit odd. One solution is to just set the minimum thresholds for weird things at 16--out of reach on the first roll for folks with anything less than a +4 in the skill. So you'll have to spend some time rolling 6 or less, building that progress bar to do it. That's fine. I think the game can handle it. Nobody rolls twice in a roll, so if you're sitting there doing the boring, it's very likely the person after you isn't. Plus, all Learning Experiences come with Dramatic Setbacks. So even just spamming the telekinesis roll for ties is going to lead to interesting things.

Another solution is to bundle the weird stuff along with other afforances and constraints and call these packages character classes or playbooks or archetypes or whatever. I think there will be some of this going on. Players love their bundles of affordances and contraints! Under this option, traditionally, the exception that proves the rule property applies. Wizards shoot fire out of their hands, so thieves don't. Sorry, space wizards shoot lightning out of their hands, so scoundrels don't. Why? Because it says space wizards can do that, and it isn't mentioned anywhere that scoundrels can. So we assume space wizards are the exception to the rule that normally lightning stays in your hands. There'll definitely be some of this going on.

### Starting Skills
We've yet to dive into character creation. Not to belabor the metaphor, but this game will sink or swim on the strength of its character creation. It can be fast and loose, but I suspect folks will want something concrete and rigid. Fortunately, with a skill list, the illusion of concrete and rigid is easy to maintain. Let's say choose one skill to have a +3 in, two skills to have +2 in, and three skills to have +1 in. Can't go wrong with the old reverse-a-roo! Folks' definitely want to pool those ten points and spend them willy-nilly (with a +6 here and four +1s there, or whatever), but nope. Not on my watch.

## Example Laser Sword Slingers
Another example to help clarify what I want out of this whole progress bar business as it relates to skills. Let's also try out some different terminology. I'm not satisfied with progress bar, so I'm going to call it Flow here. So we got Jethany, an expert laser sword slinger with a +4 in the skill. (Note that she must have suffered at least one Dramatic Setback while wielding her laser sword, because the highest she can start with is a +3.) And Jethany is facing off against Lord Wuffington, who of course is a master laser sword slinger in his own right. Lord Wuffington is not a player character, and I don't have a provision in the game yet for assigning stats to NPCs. But! We can do that right now. I could set a minimum threshold. I don't want anyone taking Lord Wuffington out with a lucky first shot. Right now, the highest skill a character can have is +6. The highest *successful* roll you can make on 2d6 is 11 (because a 12 is a tie). So, to avoid a lucky first shot situtation, Lord Wuffington's minimum threshold should be higher than a 17. There will probably be bonuses available for equipment and whatnot, which can muddle this a big, but all I need is a baseline. I want a little more breathing room, so let's give Lord Wuffington a minimum threshold of 20, and maybe a bit more for things he's really good at. Ooh, can we use an abbreviation here? Like MT for minimum threshold? Lord Wuffington, MT: 20, space battles & laser swords: 23. Now that's a stat block!

What does this mean for Jethany? Well, she'll be adding +4 to every roll she makes, but in a laser sword duel, even if she rolls that 11, she'll be 8 shy of reaching that threshold. That seems impossible, but we've got our progress bar, which we're now calling our Flow. Every time Jethany rolls, she adds her Laser Sword skill of +4 and the current Flow to the roll. If that is 6 or less, she doesn't vanquish Lord Wuffington, but adds 1 to the Flow. If that's a 7 or more, but less than the threshold of 23, she can Take the Win, whatever win the GM is offering, which would zero out her Flow, but gain her something. Or, if she wants to keep building on her Flow, she can opt for the 6 or less result. How lovely is that?

What does that look like in play? Well, let's set the scene. Let's put Jethany and Lord Wuffington high upon a wind-swept cliff. Below, a violet sea crashes upon emerald and amber rocks. Jethany's companions are elsewhere, dealing with Lord Wuffington's personal guard. This whole battle could be happening together, with each player interacting with the same Flow, but the GM wants a separate Flow for Jethany's goal of slaying Wuff. That's partly for dramatic effect and entirely because it's easier for this example. But keep in mind that Flow can be shared. Let's give Jethany a cool laser sword, too. They're a dime-a-dozen these days, but hers is an ancient relic--difficult to master, but in the right hands, a precise and effective weapon. We'll represent that in the mechanics as a +3 bonus if her Flow is >= 3. (That might be a whole category of bonus, +*x*>=*x*.)

So there's our scene. Since no player can roll twice in a roll, we would be cutting back and forth between that scene and the rest of the star adventurers, but let's focus on these two dueling on the cliff's edge. Jethany's dice are Compelling, Daring, and Expertise. The Course has been set to Thriving [3]. Jethany doesn't want to get hurt and there's no Flow to protect as of yet, so she chooses to roll Daring and Compelling, get a [3] and a [4] respectively.

What does this mean, then? Well, first Jethany probably doesn't want the tie. It ties on a 3 and the skill she's using is a +4, so there's no benefit for her. So she'll pass the Daring [3] on to the Course for someone else to use and she'll add the Thriving [3] to the Compelling [4] for her roll. Compelling is the highest, so someone here has to be impressed with what she's doing. That's tasty since the only person her is Wuff. Her total is 3+4 from the roll +4 from her skill: 11. Not enough to get past that threshold of 23, but we knew it wouldn't be. It is, however, >= 7, so she can take a win. What does the GM offer her? It's early days and she's not much of a threat with no Flow. Plus this is a dangerous situation and the the high die isn't Daring, so the GM can injure Jethany. I don't have those rules quite yet, but I have ideas. We'll worry about the specifics later. So here's what the GM offers: If Jethany takes the win, she'll put Wuff on his heels, unbalancing him long enough to escape unscathed.

Jethany's not biting, right? She takes the 6 or less option, adds 1 to her Flow, and says she's taking her time, prowling around Wuff, looking for an opportunity to strike. Since Jethany's not protected by a high Daring, the GM has Wuff strike out and draw a flesh wound. His laser sword grazes her shoulder as Jethany calmly parries it. The high Compelling die means Wuff is impressed by this. He steps back, sizes her up again, and realizes this will not be an easy fit.

Cut to: Other action!

Back to Jethany with a new Course: Expertise [3]

Jethany rolls her Compelling and Daring: a [2] and a [4], respectively.

Well, the Daring is helpful. So her total is 3+4 from the roll +4 from her skill +1 from her Flow. That's 12, only marginally better than before, but a high Daring means she can't get hurt this time. She doesn't even bother asking what she'd get if she took the win. It's very likely to be more of the same at this point, and she's starting to focus on the prize. So she opts for the 6 or less, increasing her Flow to +2 and describing her approach as leading, drawing Wuff closer and closer to the cliff edge.

Let's take a moment here and talk a bit about the threshold, because we've been assuming it is 23, the minimum for vanquishing Wuff in a laser sword fight. But Jethany doesn't have to make that her goal. She can still use her Flow if she chooses, instead, to trip Wuff up. Perhaps she's just trying to delay him long enough for her companions to get back to their ship? That might have a more reasonable threshold. She can choose that route and tell the GM who will assign a different, probably much lower, threshold for that tact. Or, she can continue pressing her attack and let that result arise naturally as an option for Taking the Win. These are both viable approaches and you can mix and match them no problem.

Let's take a moment here and talk a bit about skills, because we've been assuming Jethany is using her Laser Sword Slinging skill of +4 all the time. But she doesn't have to. She can change her tactic up before she rolls. Perhaps she'll want to tackle Lord Wuffington at some point. The key here is to tell the GM what you intent and how you intend to do it. The GM might, in this case, rule that Brawling covers such a tackle. Jethany's Brawling might only be a +1, but maybe such a surprise tactic would get her a threshold lower than Wuff's minimum for laser sword fighting. Especially if its turning into a brawl. The Flow remains as long as we're still dealing with the same basic situation: dealing with Wuff. So Jethany can back him up to a cliff's edge by laser fencing with him and then, in a shocking turn, tackle him over the side. I don't know what she'll do then, but it's possible.

Okay back to our action. After taking the 6 or less, Jethany has to wait until someone else has rolled. When the Course comes back to here, it's Expertise [4]. She rolls here Compelling and Daring again: a [4] and a [3] respectively.

Again, the tie only means trouble. If it had tied on a 5 or a 6, that might have been different. Jethany might have been tempted by a Learning Experience, getting her Laser Sword Slinging up to a +5 might be desirable. Alas, no Learning Experience here. Also, with a Expertise [4] and Daring [3], she's vulnerable to harm, but as the high die, Expertise has a trick up its sleeve. Right now Jethany's total is 4+3 from the dice +4 from the skill +2 from the Flow, which is 13. Inching up there. It's not 23, but it's meets the 7 or more requirement for Taking a Win. Jethany asks the GM what's on the table. Things are reaching a inflection point. After this Jethany's bonus from her sword is going to kick in, giving her another +3. That doesn't quite threaten Lord Wuffington just yet, but it will soon enough. With Experise being the high die, Jethany will not lose her Flow if she takes the win. The GM offers Lord Wuffington's hand, as is tradition in laser sword fights. If Jethany takes the win, she'll sever Wuff's hand and he'll scream, "NOOOO!" before diving off the cliff to an unknown fate (which we all know means he gets away), leaving Jethany unharmed.

Here's the thing, the rolling and adding and apply the effects of the high die are all about painting us into corners with fictional positioning. Here the GM wants to offer Jethany a win that she'll take that will also keep the Wuff around to menace them in the future. If Jethany takes this deal, she'll take no more harm, but Wuff absolutely would get away, even though there's still points in the Flow, even though she didn't reach his minimum threshold for a laser sword fight. That's probably good enough for her. Or is it? How focused on vanguishing Lord Wuffington is Jethany? If she takes the 6 or less instead, she'll get hit again, and that could be bad (who knows, haven't designed that part yet), but she'll have a Flow of +3, unlocking the +3 bonus from her sword. I mean, she's just getting started.

We'll leave that decisions as an exercise for the reader.

## \*Battles!
Space fights are handled pretty much like everything else in the game, with the following exceptions.

### Damage Matrix
Ships that aren't populated by the player characters work pretty much like other characters do. They have MT that must be exceeded for important things, like vanquishing them or losing them in a chase through an asteroid field. The GM can get as granular as they want here. It might be evocative to just name these MTs. Like Shields 19, Engines 17, Maneuvering 15.

Likewise, non-player ships (NPS) might have Dooms they can assign to the *ships* of their opponents. More about that in a moment.

Player ships, however, work a little differently. They have something akin to a Destiny track call a Damage Matrix. Whereas Destiny tracks tend to be a single linear path, you start at the start and end at your Doom, the Damage Matrix of a ship is made up of 3 or 6 paths.

For Ships:
1. Shields [ ]
2. Engines [ ]
3. Weapons [ ]
4. Sensors [ ]
5. Control [ ]
6. Destiny [ ]

For smaller vehicles and mounts, you can make custom damage matrices with with different catagories. For example, a jousting flamigo might be:
1-2. Verocity
3-4. Velocity
5-6. Destiny
With Verocity tracking the bird's will to stay with you in danger, Velocity tracking it's health and how that affects it's speed, and Destiny being a conduit to the character's Destiny track.

When a ship takes damage from another ship it's own class or larger, roll two d6 and take a hit in each result. If the damage is from a smaller class, only roll one d6.

*Please keep in mind, Eppy:* These are only for player ships. There's no need to figure any of this out for NPS. I know you're tempted to do something like, smaller craft can make more precise strikes on larger craft, so instead of rolling two dice, they choose one result. And that would be cool, if NPS had the same damage system. But they don't. You just have to beat a threshold. Hey, you can hit the exhaust port that leads directly to the battlestation's massive reactor if you can beat a threshold of 28--better build up some flow. It's better that way. After all, you don't want to attack the players with a smaller craft and then have to choose where they get hit. That's just too cruel.

>*Related Aside:* In general, this is how the game works. All things requiring detailed tracking, like Destiny and Damage tracks, are player-facing. Everything not player-facing is handled by thresholds, flows, and the win taking.

Since only player ships have damage tracks, you can lovingly assemble them without taking up too much of your precious time. Here's what I think one ship that can take a crew of ~5 might look like.

1. Shields
	[First hit, no matter the roll, hits here]
	[Ignore all second level hits that don't land here]
	[Ignore all third level hits that don't land here]
	[Shields out, bit display of sparks from panels]
2. Engines
	[Stalled Warp: Until this is repaired, you cannot make the jump to warp.]
	[ ]
	[ ]
	[Stalled Warp: Until this is repaired, you cannot make the jump to warp.]
3. Weapons 
	[ ]
4. Sensors
	[ ]
5. Control
	[Recalibrate: Add +1 to all piloting & gunnery thresholds]
	[Careening: A piloting roll is needed to avoid colliding with something and taking an additional two dice of Damage. The threshold is based on how many things there are out here to collide with.]
	[Misaligned: Add an additional +3 to all piloting & gunnery thresholds]
	[Locking Up: Every hit here hereafter adds an addition +3 to piloting thresholds.]
6. Destiny
	[All crew at the start of their Destiny track mark one Destiny]
	[All crew on the second place for their Destiny mark another Destiny]
	[For every hit here hereafter the crewmember with the least Destiny marked marks another, choose randomly if you have to]

#### Recovery
Let's say how far along a mark is in that damage's track is the level of that mark. So, for example, if the above ship has taken 2 hits in Control, the Recalibrate hit is level 1 and the Careening hit is level 2.

A recovery from a high Thriving die can be spent on a player's ship. This immediately unmarks a Damage track result and removes its effect. The player spending them chooses which hit to remove. It can be of any level.

Additionally, a player can make a Repair skill roll to try to get things back to a better state. The GM should set this threshold based on the intent and current conditions, but a good baseline could be something like 7 plus level of the mark. Marks do not have to be removed in order. And you can remove more than one mark with a single roll if the fictional positioning allows it. You just have to reflect that in the threshold. For example, Stevelynn has a Repair: Starship of +3. He wants to fix the Misaligned Controls and the Stalled Engines. That's 7 + 3 (the Misaligned Controls) + 1 (level 1 Stalled Warp Engines) = 11. That's a tall order, but possible even without flow and there might be a nice win he can take in there.

Just like recovery, you can repair things out of order. In fact, you'll probably want to. For example, if the pilot has already recovered from Careening, there's no reason why you would want to repair it. These sorts of entries will recover on their own between battles, even if the players aren't happy about that.

*Destiny:* Hits on the Destiny track cannot be repaired or recovered. Their effect on the crew is immediate and must be dealt with on an individual basis.

### Sensors & Onboard Tokens
If you're character is part of a crew of a ship, even in an ad hoc or backseat pilot sort of way, you need only spend 1 token for the whole ship to avoid a surprise the GM has just hoisted upon you. This is only possible if you are in direct control of whatever function of the ship you intend to use to avoid the surprise, or whoever is in control of it is paying attention to you. That should usually be the case, but who knows?

This is the equivalent of spending 2 tokens so that the whole party avoids the situation, if the whole party is aboard your ship. If you are aboard multiple ships, 2 tokens can alert your little squadron, as usual. And it still takes 3 tokens to turn the tables.

A ship with a working sensor array can also provide a Sensor Token. Any character operating the sensors can get a Sensor Token by making a roll with their Sensor skill. Under normal circumstances, all that is needed is a >= 7. However, some foes might have a MT related to their ship's cloaking or stealth abilities. Additionally, some Damage results to the ship can increase this threshold. If you beat the threshold, you get a Sensor Token. If one or more of your dice were 6s, you get those Tokens as well. Like all Tokens, you can only ever have 1 Sensor Token at a time, so spend it fast.

Sensor Token Questions:
* What's out there?
* In space, can they hear you scream?
* Where? Where?
*Note:* Obviously write some of these, dude.

## About the Course
When the GM puts that first die out, they are setting the Course. There will be rules throughout the game that are governed by the type of die that is currently the Course. Because of this, it is important that:
a. There is a Course in effect at all times.
b. It is obvious what that Course is.

So, here are the rules:
* Once that first Course is set, there is always a Course in effect until the session has ended.
* The Course always changes *after* the consequences of a roll.

That is, when it is your turn, you are under the Course that is currently set. You will roll, and incorporate that Course into your roll. If there is any fallout from that roll, perhaps most notably harm because Daring was not the highest die, then that fallout is governed by the Course you incorporated into your roll--not the Course you set for the next roll.

The current Course can have an effect on Destiny Tracks and there might be opponents who behave a certain way under different Courses. For example, the majority of Lord Wuffington's marines are not well trained. When there is an Expertise Course showing, they do the smart thing and hold their fire to keep cover--the GM cannot surprise the players with any of Wuff Marines actions while this Course is in play. Conversely, Wuffington's personal guard are zealots and increase their battle-ready thresholds by 3 when the Course is Daring.

These aforementioned details exist to add some mechanical variety to various opponents. They can influence the fiction, both in how the GM plays and the sorts of wins on offer for the taking, but they do not have to. And it's fun to sprinkle an exception to the rule in now and again. Like a veteran among Wuffington's marines who knows what he's doing. So his squad does not suffer the same constraints under Expertise, and instead keep their cover for when the adventurers are feeling more Daring, which is pretty smart.

## Weapons & Equipment
Hey, having gear that affects the mechanics is kind of fun. Here are some examples of ways that can be done.

* A precision ray pistol that offers a flat +1 to shooting.
* Jethany's antique laser rapier that's finicky, but deadly in the hands of a master. It adds a +3 to your roll if your Flow is 3 or greater.
* A rapid-blaster that can temporarily overheat as a consequece of taking a win, or permenantly meltdown as part of a dramatic setback.
* Hover-trike, a beginner-friendly version of the hover-cycle that raises your skill in piloting it to a +2 if your skill was +1 or less.
* A cantankerous cyber-donkey that can wander off as a consquence of taking a win or a dramatic setback, but when it warms to you, it can add an extra +1 to your flow when you roll with a Compelling Course.
