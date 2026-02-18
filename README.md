# Yu-Gi-Oh Cards Game
**👇🏻 If you're not familiar with the Yu-Gi-Oh card game, then I recommend reading this brief introduction 👇🏻**
Yu-Gi-Oh! is a card game where two players try to defeat each other by reducing the opponent's Life Points (down to 0) using a collection of monster, magic, and trap cards.

In addition to your decks, you'll need some extra items to assist you in the game. These items include:


- **A coin**: Some cards require flipping a coin.
- **Dice**: Some cards require a dice roll.
- **Counters**: Any small object that can be used as an indicator to keep track of certain metrics that may affect some cards.
- **Monster Tokens**

For more information on the card game, visit the following link [ How to Play Yu-Gi-Oh! 🎲](https://www.dacardworld.com/gaming/yu-gi-oh-cards/how-to-play#:~:text=%2DGi%2DOh!-,Yu%2DGi%2DOh!,%2C%20spell%2C%20and%20trap%20cards.)

# How is a Yu-Gi-Oh card structured?

- **Name**: Each card has its unique name, used to identify the card.
- **Attribute**: All monsters in the game have one of the 7 attributes: DARK, LIGHT, FIRE, WATER, EARTH, WIND, and DIVINE (located at the top right of the card).Spells/Traps do not have Attributes but indicate whether the card is a Spell or a Trap.
- **Image**: The image used to represent the card.
- **Level**: Most monsters in Yu-Gi-Oh have a Level, indicated by the number of stars below the name.
- **Type**: Enclosed in square brackets, denotes the characteristic of the card. For monsters, it is located between the image and the card's description, while for spells and traps, it is located between the name and the image.
- **Description**: The text indicating the effect of a card or its lore without having any impact on the game.
- **Attack and Defense**: The offensive and defensive power of a monster.
- **ID**: An 8-digit identification number of the card. It is found at the bottom left.
- **Set Number**: All Yu-Gi-Oh cards have a set number. It is located below the bottom right corner of the image.
- **Eye of Anubis**: The hologram of the Eye of Anubis is a foil security symbol placed at the bottom right of all official Yu-Gi-Oh! cards.
- **Border**: The colored area to identify the cards at a glance.

To enlarge, click on the various cards you find 👇


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/89631139.jpg"><img src="https://images.ygoprodeck.com/images/cards/89631139.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/55410871.jpg"><img src="https://images.ygoprodeck.com/images/cards/55410871.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/43228023.jpg"><img src="https://images.ygoprodeck.com/images/cards/43228023.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/59822133.jpg"><img src="https://images.ygoprodeck.com/images/cards/59822133.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/17655904.jpg"><img src="https://images.ygoprodeck.com/images/cards/17655904.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/56920308.jpg"><img src="https://images.ygoprodeck.com/images/cards/56920308.jpg" width="150"></a></td>
</tr></table>


# Yu-Gi-Oh Dataset

|Variables   |Description|
|:----------|:---------------:|
|*```Id```*| Card identification number.
|*```Name```*| Card name.
|*```Type```*| Card type.
|*```Desc```*| Card description.
|*```Atk```*| Attack value.
|*```Def```*| Defense value.
|*```Level```*| Monster card level.
|*```Race```*| Monster card race.
|*```Attribute```*| Monster card attribute.
|*```Scale```*| Pendulum scale value.
|*```Archetype```*| Cards that share a specified name string in a card's effect.
|*```Linkval```*| The Link value of the card if it's a "Link Monster".
|*```LinkMarkers```*| Represented by red arrows radiating outward from the artistic frame of the Link Monster.
|*```Image_url```*| Card image link.
|*```Imagew_url_small```*| Small card image link.
|*```Ban_Tcg```*| Card status in the TCG Forbidden List.
|*```Ban_Ocg```*| Card status in the OCG Forbidden List.
|*```Ban_Goat```*| Card status in the GOAT Format Forbidden List.
|*```Staple```*| Refers to a card that is generally powerful and can be played in any deck.
|*```Views```*| Number of card views.
|*```ViewsWeek```*| Number of card views per week.
|*```Upvotes```*| Number of positive votes for the card.
|*```Downvotes```*| Number of negative votes for the card.
|*```Formats```*| Card format.
|*```Treated_as```*| Card that, in the description, can be called by another name.
|*```Tcg_Date```*| Publication date of the card in TCG (America, Europe).
|*```Ocg_Date```*| Publication date of the card in OCG (Japan, Asia, China, Korea).
|*```Has_effect```*| Has an effect (1 yes & 0 no).


# Dataset Import

# Cleaning Dataset

# EDA


![Chart](images/chart_01.png)


![Chart](images/chart_02.png)


**In the histogram, it's evident that the majority of monster cards fall into level 4.**
**However, it's noteworthy that a card's level doesn't necessarily determine its strength. In fact, the analysis of the scatterplot reveals that many cards gain power through their unique effects. An example of this is represented by the following cards:**

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/15397015.jpg"><img src="https://images.ygoprodeck.com/images/cards/15397015.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/16428514.jpg"><img src="https://images.ygoprodeck.com/images/cards/16428514.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/53143898.jpg"><img src="https://images.ygoprodeck.com/images/cards/53143898.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/86120751.jpg"><img src="https://images.ygoprodeck.com/images/cards/86120751.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/60303688.jpg"><img src="https://images.ygoprodeck.com/images/cards/60303688.jpg" width="150"></a></td>
</tr></table>
**On the other hand, it's important to observe in the scatterplot that as the card level increases, so do the values of ATK and DEF.**
**It's crucial to keep in mind that some cards don't follow this trend, as their ATK and DEF values (represented as "???") depend on specific effects indicated on the card. This is the case for cards like:**

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/15862758.jpg"><img src="https://images.ygoprodeck.com/images/cards/15862758.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/8400623.jpg"><img src="https://images.ygoprodeck.com/images/cards/8400623.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/71544954.jpg"><img src="https://images.ygoprodeck.com/images/cards/71544954.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/5008836.jpg"><img src="https://images.ygoprodeck.com/images/cards/5008836.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/85115440.jpg"><img src="https://images.ygoprodeck.com/images/cards/85115440.jpg" width="150"></a></td>
</tr></table>
**It's also important to note that most cards with ATK and DEF values equal to zero possess extraordinary effects, such as:**

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/78371393.jpg"><img src="https://images.ygoprodeck.com/images/cards/78371393.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/64631466.jpg"><img src="https://images.ygoprodeck.com/images/cards/64631466.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/8062132.jpg"><img src="https://images.ygoprodeck.com/images/cards/8062132.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/72677437.jpg"><img src="https://images.ygoprodeck.com/images/cards/72677437.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/3657444.jpg"><img src="https://images.ygoprodeck.com/images/cards/3657444.jpg" width="150"></a></td>
</tr></table>

**These data confirm that a card's power is not exclusively tied to ATK and DEF values but is strongly influenced by special effects that can disrupt opponents' strategies.**


## Analysis of the types of Yu-Gi-Oh! cards


**Due to the diverse range of card types available, I've chosen to divide this column into different sections, thus reflecting the structure of the playing arena.**

**This allows me to gain a clearer insight into the following aspects:**

- Extra Deck
- Main Deck
- Spell & Trap Zone

I begin by examining the Spell & Trap Zone, which encompasses various types of cards:


- **Quick-Play Spells:** Allow the turn player to activate Quick-Play Spell Cards from their hand during any Phase of their turn. Additionally, each player can activate Set Quick-Play Spell Cards during any Phase in any player's turn. Quick-Play Spell Cards are recognizable by the lightning bolt symbol.
- **Equip Spells:** Can be equipped to face-up monsters on the field. These cards are marked with a target symbol.
- **Continuous Spells:** Remain on the field once activated. They are recognizable by the infinity symbol.
- **Field Spells:** Often focused on boosting ATK and/or DEF for cards with specific attributes, types, or archetypes. They are distinguished by the compass rose symbol.
- **Normal Spells:** Allow the turn player to set a Normal Spell Card and activate it in the same turn. This option is useful if the player intends to use the effects of cards that require discarding cards from the hand to protect their cards on the field. Normal Spell Cards do not have any distinctive symbols.
- **Ritual Spells:** Used to ritually summon Ritual Monsters and are characterized by the flaming chalice symbol.

Now, let's move on to Trap Cards:


- **Normal Traps:** Can be activated in response to the effects of Effect Monsters, Spell Cards, as well as most other Trap Cards and Quick-Play Spell Cards. Normal Trap Cards do not have any distinctive symbols.
- **Counter Traps:** Most of these cards can only be activated to negate or punish the activation of other cards or the Summoning of monsters. These cards are recognizable by the curved arrow symbol.
- **Continuous Traps:** Remain on the field after activation. The effects of these cards will remain active until the owner is unable to pay the cost or fulfill the conditions specified on the card (if any) OR until it is destroyed.


As for the Extra Deck zone, I will examine this area in detail in the temporal analysis.


![Chart](images/chart_03.png)


![Chart](images/chart_04.png)


![Chart](images/chart_05.png)


From the following histograms, it is evident that normal Spell and Trap cards are the most common, followed by Continuous and Quick-Play Spell cards. For Traps, Continuous Traps follow Quick-Play Traps.


The reason for this distribution is simply because some Spell cards include elements necessary to summon monsters from the Extra Deck through Fusion or Synchro, as well as for the special summoning of monsters that can only be summoned using a specific Spell or Trap card.


Regarding monsters in the Extra Deck, Xyz monsters are the most frequent, followed by Fusion monsters, with Synchro monsters in third place.


The reason Xyz monsters are more common and appreciated is that they do not require the use of Spell cards for summoning, only monsters whose levels are indicated on the card. This feature also applies to Synchro monsters. However, what makes Xyz monsters unique is their ability to detach the monsters used for the summoning to activate an additional effect.


It should be noted that among Fusion monsters, some do not require Spell cards to be summoned.


As for Link Monsters, being recently introduced, there are 30 fewer in total compared to Synchro monsters, suggesting that in the future, this new type might secure the third position.


In the third histogram, the most common type consists of monsters with effects capable of triggering a chain reaction for summoning other monsters or annihilating the opponent's cards. As for Ritual monsters, their minority is due to the fact that they can only be summoned through Ritual Spell cards. In fact, even in the first histogram, Ritual Spell cards occupy the last position.


Here's a list for better understanding:


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/80796456.jpg"><img src="https://images.ygoprodeck.com/images/cards/80796456.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/6150044.jpg"><img src="https://images.ygoprodeck.com/images/cards/6150044.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/24094653.jpg"><img src="https://images.ygoprodeck.com/images/cards/24094653.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/91998119.jpg"><img src="https://images.ygoprodeck.com/images/cards/91998119.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/60800381.jpg"><img src="https://images.ygoprodeck.com/images/cards/60800381.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/98978921.jpg"><img src="https://images.ygoprodeck.com/images/cards/98978921.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/64631466.jpg"><img src="https://images.ygoprodeck.com/images/cards/64631466.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/41426869.jpg"><img src="https://images.ygoprodeck.com/images/cards/41426869.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/8062132.jpg"><img src="https://images.ygoprodeck.com/images/cards/8062132.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/16067089.jpg"><img src="https://images.ygoprodeck.com/images/cards/16067089.jpg" width="150"></a></td>
</tr></table>
## Analysis of Yu-Gi-Oh! card attributes


![Chart](images/chart_06.png)


![Chart](images/chart_07.png)


### What are the most common attributes and which ones are the most favored?

In both histograms, the "Dark" attribute takes the first position, followed by "Earth," "Light," "Water," "Wind," and "Fire." However, when focusing on preference, it is noticeable that the "Light" attribute is more appreciated than "Earth," while "Wind" is less popular than "Fire."


But what makes one attribute more appreciated than the other? Let's examine them one by one:

- **Darkness:** It stands out as the best attribute, both for the effectiveness of the cards and for deck or archetype creation, creating a powerful synergy with spells and traps. Konami strives to integrate cards from other attributes into this, as demonstrated in the "PredaPlant" archetype, where plant monsters are part of the "Darkness" attribute instead of the "Earth" attribute.
- **Light:** Similarly to darkness, the "Light" attribute includes various races, including fairies, machines, warriors, dragons, and demons. These two attributes stand out for the versatility of their abilities. Two notable examples are the "Cyber Dragon" and "ABC" archetypes.
- **Earth:** Most monsters of this attribute specialize in negating the effects of other monsters, spells, and traps. This aspect is evident in archetypes such as "Ancient Gear," "Naturia," and "Infinity Track."
- **Water:** Thanks to their versatility, water monsters can be used in various strategies due to their diverse abilities. The predominant strategy for "Water" decks is to build a defensive wall on the opponent's field while accumulating resources. This tactic makes most "WATER" decks oriented towards a more defensive play, but it takes time to properly execute the combos. A tangible example is provided by the cards of the 'Nubian' archetype (one of my favorites).
- **Fire:** "Fire" monsters often focus on the "Burn" mechanic, inflicting effect damage to the opponent. However, this attribute is less appreciated due to the scarcity of notable archetypes, such as "Infernable Knight," "Vulcanics," "Flamewell," "Shiranouiu," and "Hazy Flames." The reason for Konami's low consideration of this attribute remains a mystery.
- **Wind:** This attribute takes the penultimate position, with the fewest support cards compared to other attributes (excluding "DIVINE"). The amount of support cards for spells and traps is significantly lower than other attributes, despite the generally limited presence of spell and trap cards related to existing attributes and the minimum requirements to dedicate a significant number of these cards to a specific attribute family.
- **Divine:** This attribute ranks last, represented by only six monsters, including the famous three Egyptian deities. The "Winged Dragon of Ra" even offers two alternative forms, while the "Creator" completes the group. Only two of these cards are widely recognized as significant, namely "Sphere Mode of Ra" and "Creator."

Here is a list of cards by attribute to have a clearer view of what you've read.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/66309175.jpg"><img src="https://images.ygoprodeck.com/images/cards/66309175.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/1546123.jpg"><img src="https://images.ygoprodeck.com/images/cards/1546123.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/33198837.jpg"><img src="https://images.ygoprodeck.com/images/cards/33198837.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/20003527.jpg"><img src="https://images.ygoprodeck.com/images/cards/20003527.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/32543380.jpg"><img src="https://images.ygoprodeck.com/images/cards/32543380.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/73125233.jpg"><img src="https://images.ygoprodeck.com/images/cards/73125233.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/10000080.jpg"><img src="https://images.ygoprodeck.com/images/cards/10000080.jpg" width="150"></a></td>
</tr></table>

In conclusion, the preference for attributes is influenced by a combination of card effects and gameplay strategies. Each of these attributes has its own role and unique characteristics within the game, offering enthusiasts a wide variety of tactical options.

## Breed analysis


![Chart](images/chart_08.png)


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/15180041.jpg"><img src="https://images.ygoprodeck.com/images/cards/15180041.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/83104731.jpg"><img src="https://images.ygoprodeck.com/images/cards/83104731.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/31764700.jpg"><img src="https://images.ygoprodeck.com/images/cards/31764700.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/40737112.jpg"><img src="https://images.ygoprodeck.com/images/cards/40737112.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/61257789.jpg"><img src="https://images.ygoprodeck.com/images/cards/61257789.jpg" width="150"></a></td>
</tr></table>


### Yu-Gi-Oh! and Its Races: What Makes Some More Popular Than Others?


From the histogram, it's noticeable that the "warrior" category takes the first place, followed by "machine," "demon," "spellcaster," and "dragon."

### What makes this category better than the others?

- **Warrior:** "Warrior" is a diverse, versatile, and popular Monster Card type. There are Warriors of every Attribute, mainly EARTH, DARK, and LIGHT. Their varied and versatile strategies make them arguably one of the best types.
- **Machine:** "Machine" monsters rely on high ATTACK values and a variety of powerful effects. Their general strategy varies, but they often have the ability to negate the effects of specific opponent's cards and/or destroy them.
- **Demon:** "Demons" are one of the most established and powerful Types in the Yu-Gi-Oh! franchise. Most demons focus on offensive "beatdown" tactics and destroying opponent's cards, putting pressure with stunning effects, lockdown, banishment effects, or deck milling.
- **Spellcaster:** Most of these creatures have effects and can be very versatile, often used with Magic Card support. Among all types, Spellcasters are the most present in current Forbidden and Limited lists.
- **Dragon:** "Dragons" tend to be the strongest boss monsters or have remarkable effects, being one of the most established and powerful Monster types in the entire franchise. Dragon monsters are known for having higher ATTACK values than any other monster type in the game and being one of the most popular monster types.

### So why are all the other cards not falling into this category less common?
To answer this question, I consider only the most relevant types positively and negatively.

Regarding the positive points:


- **Zombie:** Zombie types have some of the best generic support cards in the entire game, like "Uni-Zombie" and "Mezuki" present in every Zombie deck. "Zombie World" on the field (which turns all cards into Zombie types) can also lock the opponent in summoning any non-Zombie type monsters when "Rivalry Of Warlords" is on the field.
- **Cyberse:** It's the latest type to enter Yu-Gi-Oh!, and despite its young age, it's one of the best. The Cyberse type is a significant part of the Link Monster mechanics, with most Monsters being Link Monsters. When it comes to dedicated Cyberse decks, "Salamangreat" has consistently been on top since its introduction, despite some of its cards being banned.

Regarding the negative points:


- **Divine-Beast:** The only cards that make up the Divine-Beast Type are the iconic Egyptian God Cards. The only Divine-Beast card that sees some utility is "The Winged Dragon of Ra - Sphere Mode" as a way to clear the opponent's field.
- **Pyro:** It's one of the unluckiest. Over the years, it has received very little support, and what it got had a very limited impact on the metagame. The only usable Pyro-type deck was "Volcanic," which has long surpassed its peak.
- **Reptile:** It's a type that has the potential to be one of the best types in the entire game. Reptiles have many great archetypes like "Aliens" and "Worms," but none of them come close to being good. Maybe one day Reptiles will get the "Rock" type treatment where a new archetype makes them one of the best, but for now, Reptiles are at the bottom of the barrel.
- **Fish:** There has never been a good Fish-type archetype, with the only exception being some Mermail cards, consisting of Fish, Sea Serpent, and Aqua. Despite that, there are no good Fish-type decks that can make use of these powerful cards, leaving them as the worst of the worst when it comes to types.

### However, there's a key reason why some types of cards are more common than others, and it's closely tied to the release dates of the cards. Over the years, new card types and races have been introduced, a topic I'll delve into in detail later. (Temporal Analysis section)
## Analysis between views and votes of Yu-Gi-Oh! cards


![Chart](images/chart_09.png)


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/5405694.jpg"><img src="https://images.ygoprodeck.com/images/cards/5405694.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/46986414.jpg"><img src="https://images.ygoprodeck.com/images/cards/46986414.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/62873545.jpg"><img src="https://images.ygoprodeck.com/images/cards/62873545.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/72989439.jpg"><img src="https://images.ygoprodeck.com/images/cards/72989439.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/54484652.jpg"><img src="https://images.ygoprodeck.com/images/cards/54484652.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/77498348.jpg"><img src="https://images.ygoprodeck.com/images/cards/77498348.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/10000020.jpg"><img src="https://images.ygoprodeck.com/images/cards/10000020.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/12580477.jpg"><img src="https://images.ygoprodeck.com/images/cards/12580477.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/2099841.jpg"><img src="https://images.ygoprodeck.com/images/cards/2099841.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/89631139.jpg"><img src="https://images.ygoprodeck.com/images/cards/89631139.jpg" width="150"></a></td>
</tr></table>
![Chart](images/chart_10.png)


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/61740673.jpg"><img src="https://images.ygoprodeck.com/images/cards/61740673.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/88581108.jpg"><img src="https://images.ygoprodeck.com/images/cards/88581108.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/89631139.jpg"><img src="https://images.ygoprodeck.com/images/cards/89631139.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/11384280.jpg"><img src="https://images.ygoprodeck.com/images/cards/11384280.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/46986414.jpg"><img src="https://images.ygoprodeck.com/images/cards/46986414.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/2099841.jpg"><img src="https://images.ygoprodeck.com/images/cards/2099841.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/76375976.jpg"><img src="https://images.ygoprodeck.com/images/cards/76375976.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/71791814.jpg"><img src="https://images.ygoprodeck.com/images/cards/71791814.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/34541863.jpg"><img src="https://images.ygoprodeck.com/images/cards/34541863.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/50588353.jpg"><img src="https://images.ygoprodeck.com/images/cards/50588353.jpg" width="150"></a></td>
</tr></table>


**In both charts, a card stands out, "Ash Blossom & Joyous Spring," which, despite having a significant number of views, is also the least rated compared to others.**


<img src="https://images.ygoprodeck.com/images/cards/14558127.jpg" width="150">
But why is this card so discussed?

There are several reasons:


- **Secret Rare Edition:** Originally printed in the "Maximum Crisis" series in May 2017, this card was only available in Secret Rare edition, and a set of three copies could cost up to €200.00.
- **Triple Effect:** "Ash Blossom & Joyous Spring" is known for its triple effect, allowing it to counter various opponent's effects:
- **(1)** Special summon a monster from the deck.
- **(2)** Send a card from the deck to the graveyard.
- **(3)** Add a card from the deck to the hand.


**However, this doesn't necessarily mean that monster cards with effects are the most discussed. For instance, in the first scatterplot, the card with the highest number of positive votes is "Black Luster Soldier," which, unlike "Ash Blossom & Joyous Spring," has no special effect.**
So, why is "Black Luster Soldier" so beloved despite having a considerable number of views?

The reasons are intriguing:


- **Absence of the Identification Number:** "Black Luster Soldier" is one of the rare Yu-Gi-Oh! cards that lacks the eight-digit identification number at the bottom left, at least until its reprint in the "Legendary Collection 3: Yugi's World" series.
- **The Card's History:** In the first Yu-Gi-Oh! tournament dated 1999, the winner was awarded a copy of the "Black Luster Soldier" card printed in stainless steel. It is said that only a few copies of this card exist, and one of them was put up for sale in 2013 by its original winner at the staggering price of 20 million dollars. Although the original seller had initially asked for a much higher price, it is said that they settled for an offer of "only" 2 million dollars.


<table><tr>
<td><a href="https://i.ebayimg.com/images/g/fDAAAOSwUJtgy0B6/s-l1600.jpg"><img src="https://i.ebayimg.com/images/g/fDAAAOSwUJtgy0B6/s-l1600.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/5405694.jpg"><img src="https://images.ygoprodeck.com/images/cards/5405694.jpg" width="150"></a></td>
<td><a href="https://cdn.idntimes.com/content-images/community/2022/11/819gmmoupzl-ac-sy500-56965fbaa68adf470a17cc45ea5d328d-85149eced310f2e3793970d105f0aab1.jpg"><img src="https://cdn.idntimes.com/content-images/community/2022/11/819gmmoupzl-ac-sy500-56965fbaa68adf470a17cc45ea5d328d-85149eced310f2e3793970d105f0aab1.jpg" width="150"></a></td>
</tr></table>

**Ultimately, the value of cards is not determined solely by gameplay effects but also by the story surrounding the card itself and the type of print. These factors drive collectors to desire particular cards beyond players.**
**However, we shouldn't focus exclusively on card values. In the second scatterplot, we notice that the cards "Imperial Order" and "True King of All Calamities" are the only ones accumulating a significant number of negative votes.**
But what is the reason behind this poor popularity?

The reason lies in their powerful effects, which can block the use of monsters and spells. These effects are so potent that both cards have been banned in both the TCG and OCG formats.

(Therefore, if you wish to use these cards, I recommend doing so exclusively in friendly matches.)

It's interesting to note that in the table, there are three other cards with a limited number of negative votes, but they are also banned in both TCG and OCG. These cards include "Mystic Mine" and "Crystron Halqifibrax," whose ban status is due to equally astonishing effects. The exception is "Soldier Cannon," which happens to be banned only in the "OCG" format.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/61740673.jpg"><img src="https://images.ygoprodeck.com/images/cards/61740673.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/88581108.jpg"><img src="https://images.ygoprodeck.com/images/cards/88581108.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/11384280.jpg"><img src="https://images.ygoprodeck.com/images/cards/11384280.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/76375976.jpg"><img src="https://images.ygoprodeck.com/images/cards/76375976.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/50588353.jpg"><img src="https://images.ygoprodeck.com/images/cards/50588353.jpg" width="150"></a></td>
</tr></table>


**In the upcoming charts, I will delve further into this category to understand if the decision to ban these cards is strictly related to their effects or if there are other factors at play.**


## Analysis of Banned, Limited and Semi-Limited Yu-Gi-Oh! cards

**As mentioned earlier, I proceed with the analysis using these two scatterplots to understand whether cards are limited, banned, or semi-limited due to their effect or for other reasons.**

To further clarify the meaning of these terms:


- **Banned:** These cards cannot be used in any official duel, often due to their unfair power.
- **Semi-Limited:** You are allowed to include only two copies of any Yu-Gi-Oh! card in your deck.
- **Limited:** You can include in your deck only one copy of any Yu-Gi-Oh! card with a limited edition.


These definitions will help you better understand the restrictions that can be applied to cards within the game.


![Chart](images/chart_11.png)


![Chart](images/chart_12.png)


**In both graphs, most cards with an effect, including those discussed earlier, fall into the "Bannable," "Semi-Limited," and "Limited" categories.**
**However, to great surprise, in both graphs, there are 4 effectless cards that are Limited, and they are none other than the pieces of "Exodia the Forbidden One."**

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/8124921.jpg"><img src="https://images.ygoprodeck.com/images/cards/8124921.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/70903634.jpg"><img src="https://images.ygoprodeck.com/images/cards/70903634.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/33396948.jpg"><img src="https://images.ygoprodeck.com/images/cards/33396948.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/7902349.jpg"><img src="https://images.ygoprodeck.com/images/cards/7902349.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/44519536.jpg"><img src="https://images.ygoprodeck.com/images/cards/44519536.jpg" width="150"></a></td>
</tr></table>


**Why are these effectless cards so feared?**
The fear is due to the effect of Exodia the Forbidden One, which allows you to win the game if you have all 5 pieces in your hand. Moreover, new strategies exploiting various card effects have been discovered, making it easier to draw a large number of cards from the deck and simplifying the possibility of obtaining all 5 pieces of Exodia in the fewest number of turns.

For more details on one of the strategies, visit the following site: 👉🏻 [Exodia the Forbidden One Strategy Site](https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=49ce8d50627a96108420c3cb3695c4f2&dno=1&request_locale=it).


## Analysis of cards trap-monster


It's important to remember that monster cards are not the only ones present; in fact, there is a category of special trap cards that can be summoned as monster cards and, at the same time, function as trap cards.

They may seem useless, but some slightly crazy players (for example, me) have exploited the effects of these cards to create a deck. The reason? To have the chance to immediately summon Xyz monsters (which require monsters with the same level to be summoned). For more information, visit the following link [ Trap Monster Deck 🎲](https://ygoprodeck.com/deck/trap-monster-deck-70608)


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/87772572.jpg"><img src="https://images.ygoprodeck.com/images/cards/87772572.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/23626223.jpg"><img src="https://images.ygoprodeck.com/images/cards/23626223.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/98414735.jpg"><img src="https://images.ygoprodeck.com/images/cards/98414735.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/49514333.jpg"><img src="https://images.ygoprodeck.com/images/cards/49514333.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/38761908.jpg"><img src="https://images.ygoprodeck.com/images/cards/38761908.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/35035481.jpg"><img src="https://images.ygoprodeck.com/images/cards/35035481.jpg" width="150"></a></td>
</tr></table>


## Analysis card rarity


![Chart](images/chart_13.png)


It can be noted that common cards are among the most widespread, followed by super rare, ultra rare, rare, and secret rare cards. At the end of the graph, there are 5 categories, each composed of a single card: 10000 Secret Rare, Super, Duel Terminal Normal Rare Parallel Rare, C, and Ultra Secret Rare, indicating that there are only 5 cards in these categories.

It is well known that the value of a card increases the rarer it is, but this value is not only due to its rarity but also to the card's effect, printing method, the number of copies in existence, and the story behind the card. (An example of this can be found in the card 'Black Luster Soldier').

However, there is another extremely rare card in addition to the one mentioned earlier, namely **"Tyler the Great Warrior"**. There is only one copy in circulation, and it was created by Tyler Gressle, who drew the card in 2005 as part of a Make-a-Wish request when he was 14 years old and battling a rare form of liver cancer. 18 years later, he decided to sell the card. The final auction offer raised a whopping $311,211.

Here is a list of other rare and expensive cards.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/68811206.jpg"><img src="https://images.ygoprodeck.com/images/cards/68811206.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/89631139.jpg"><img src="https://images.ygoprodeck.com/images/cards/89631139.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/46986414.jpg"><img src="https://images.ygoprodeck.com/images/cards/46986414.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/57728570.jpg"><img src="https://images.ygoprodeck.com/images/cards/57728570.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/30100551.jpg"><img src="https://images.ygoprodeck.com/images/cards/30100551.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/69015963.jpg"><img src="https://images.ygoprodeck.com/images/cards/69015963.jpg" width="150"></a></td>
</tr></table>


## Analysis of card staple


![Chart](images/chart_14.png)


'Staple' cards represent a set of cards that play a crucial role during a duel, as they can significantly influence the opponent's turn or provide greater consistency to one's deck.

Overall, there are 64 of these special cards, but it's interesting to note that 20 of them fall into the categories of 'Limited,' 'Semi-Limited,' and 'Forbidden.'


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/12580477.jpg"><img src="https://images.ygoprodeck.com/images/cards/12580477.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/83764719.jpg"><img src="https://images.ygoprodeck.com/images/cards/83764719.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/24224830.jpg"><img src="https://images.ygoprodeck.com/images/cards/24224830.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/37818794.jpg"><img src="https://images.ygoprodeck.com/images/cards/37818794.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/35261759.jpg"><img src="https://images.ygoprodeck.com/images/cards/35261759.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/70369116.jpg"><img src="https://images.ygoprodeck.com/images/cards/70369116.jpg" width="150"></a></td>
</tr></table>


## Analysis of card treated_as


![Chart](images/chart_15.png)


Cards falling under the **'treated_as'** category are those whose description can be considered with a **different name** or with the **same name but a different image.**

Out of the 106 cards in this category, only 4 are classified as 'Limited,' 'Semi-Limited,' or 'Forbidden,' and some of these also fall into the 'staple' category.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/27927359.jpg"><img src="https://images.ygoprodeck.com/images/cards/27927359.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/295517.jpg"><img src="https://images.ygoprodeck.com/images/cards/295517.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/80316585.jpg"><img src="https://images.ygoprodeck.com/images/cards/80316585.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/68679595.jpg"><img src="https://images.ygoprodeck.com/images/cards/68679595.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/17732278.jpg"><img src="https://images.ygoprodeck.com/images/cards/17732278.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/13857930.jpg"><img src="https://images.ygoprodeck.com/images/cards/13857930.jpg" width="150"></a></td>
</tr></table>


## Temporal Analysis


In the previous study, I examined the various monster races in the Yu-Gi-Oh! card game and hinted that I would dedicate further attention to why some of these races are more common than others.

In this section, I will break down the dataset based on the release dates of the cards in the OCG format, taking into account the releases of animated series as well. This approach is crucial because, as mentioned earlier, it allows us to understand how new monster races have been introduced into the game over time.

In the context of this section, I will also examine the different game formats that have been introduced over the years. This is particularly relevant because, in addition to the traditional card game, mobile and PC games based on Yu-Gi-Oh!, such as "Yu-Gi-Oh! Duel Links" and "Yu-Gi-Oh! Master Duel," have been developed. The reason for this is that the extraordinary popularity of "Yu-Gi-Oh! Duel Links," known for its faster-paced matches, has led to the introduction of the "Yu-Gi-Oh! Speed Duel" game format, which includes a new type of cards that I will analyze shortly.

<img src="https://i.ytimg.com/vi/E6ci1y1K5uI/maxresdefault.jpg" width="700">


To divide the dataset, I relied on two reference sources:


- **Regarding the release dates of Yu-Gi-Oh! cards in the OCG format, I used the following site** [[🔗 🎲 🪙]](https://yugioh.fandom.com/wiki/Order_of_Set_Release#2002)
- **For information regarding the releases of animated series (in Japan), I relied on this site** [[🔗 🎲 🪙]](https://en.wikipedia.org/wiki/Yu-Gi-Oh!)

This approach allowed me to create an explanatory table that provides a clear overview of the dataset division.

| OCG Release Date Range | Animated Series Release Date Range | Series Name       |
|:-----------------------|:----------------------------------|:------------------|
| **04/02/1999 - 30/12/2004** | 18/04/2000 - 29/09/2004 | *```Yu-Gi-Oh!```* |
| **20/01/2005 - 08/03/2008** | 06/09/2004 - 26/03/2008 | *```Yu-Gi-Oh! GX```* |
| **15/03/2008 - 26/02/2011** | 02/04/2008 - 30/03/2011 | *```Yu-Gi-Oh! 5D's```* |
| **19/03/2011 - 20/03/2014** | 11/04/2011 - 23/03/2014 | *```Yu-Gi-Oh! Zexal```* |
| **21/03/2014 - 24/03/2017** | 06/04/2014 - 26/03/2017 | *```Yu-Gi-Oh! Arc-V```* |
| **25/03/2017 - 02/04/2020** | 10/12/2017 - 25/09/2019 | *```Yu-Gi-Oh! VRAINS```* |
| **04/04/2020 - 23/12/2023** | 27/03/2020 - 27/03/2023 | *```Yu-Gi-Oh! Sevens```* |


![Chart](images/chart_16.png)

### Yu-Gi-Oh!


![Chart](images/chart_17.png)


![Chart](images/chart_18.png)


![Chart](images/chart_19.png)

In the context of the type and race of cards, currently there are not many variations for both this series and the next, as the only cards present are fusion monsters and ritual monsters.


### Yu-Gi-Oh! GX


![Chart](images/chart_20.png)


![Chart](images/chart_21.png)


![Chart](images/chart_22.png)

### Yu-Gi-Oh! 5D


![Chart](images/chart_23.png)


![Chart](images/chart_24.png)


![Chart](images/chart_25.png)


With the introduction of Yu-Gi-Oh 5D, a new category of monsters was introduced for the first time, namely **Synchro** monsters and **Tuner** monsters, while the new "Psychic" race was also introduced.

Regarding Synchro monsters, they can be summoned without the use of spell cards, unlike fusion monsters, but only by following the specifications on the card and requiring at least one Tuner monster. In fact, most Tuner monsters are used for summoning these Synchro monsters.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/44508094.jpg"><img src="https://images.ygoprodeck.com/images/cards/44508094.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/70902743.jpg"><img src="https://images.ygoprodeck.com/images/cards/70902743.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/9012916.jpg"><img src="https://images.ygoprodeck.com/images/cards/9012916.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/73580471.jpg"><img src="https://images.ygoprodeck.com/images/cards/73580471.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/2403771.jpg"><img src="https://images.ygoprodeck.com/images/cards/2403771.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/25862681.jpg"><img src="https://images.ygoprodeck.com/images/cards/25862681.jpg" width="150"></a></td>
</tr></table>


### Yu-Gi-Oh! ZEHAL


![Chart](images/chart_26.png)


![Chart](images/chart_27.png)


![Chart](images/chart_28.png)


With the introduction of Yu-Gi-Oh! Zexal, another category of monsters was introduced, namely the **Xyz monsters**. Similar to Synchro monsters, these monsters do not require the use of spell cards, but only monsters that share the same level as the card.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/84013237.jpg"><img src="https://images.ygoprodeck.com/images/cards/84013237.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/31801517.jpg"><img src="https://images.ygoprodeck.com/images/cards/31801517.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/65676461.jpg"><img src="https://images.ygoprodeck.com/images/cards/65676461.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/88120966.jpg"><img src="https://images.ygoprodeck.com/images/cards/88120966.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/9161357.jpg"><img src="https://images.ygoprodeck.com/images/cards/9161357.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/86848580.jpg"><img src="https://images.ygoprodeck.com/images/cards/86848580.jpg" width="150"></a></td>
</tr></table>


### Yu-Gi-Oh! V


![Chart](images/chart_29.png)


![Chart](images/chart_30.png)


![Chart](images/chart_31.png)


![Chart](images/chart_32.png)


With the release of Yu-Gi-Oh! ARC-V, a new race, the **"Wyrm,"** and a new card type, **Pendulum** cards, were introduced.

The presence of only one card of the **"Cyberse"** type is due to the promotion of the new Yu-Gi-Oh! card series.

**Pendulum Monsters:** This type of card has the unique feature of being used as both a monster and a spell card. It is characterized by a dual color (orange/yellow and green) and gains different effects depending on the role in which it is used. The concept of 'scales' serves as unique indicators for Pendulum monsters, represented by two symbols, one red and one blue.

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/16178681.jpg"><img src="https://images.ygoprodeck.com/images/cards/16178681.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/47198668.jpg"><img src="https://images.ygoprodeck.com/images/cards/47198668.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/25629622.jpg"><img src="https://images.ygoprodeck.com/images/cards/25629622.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/47075569.jpg"><img src="https://images.ygoprodeck.com/images/cards/47075569.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/40318957.jpg"><img src="https://images.ygoprodeck.com/images/cards/40318957.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/96227613.jpg"><img src="https://images.ygoprodeck.com/images/cards/96227613.jpg" width="150"></a></td>
</tr></table>


### Yu-Gi-Oh! Link


![Chart](images/chart_33.png)


![Chart](images/chart_34.png)


![Chart](images/chart_35.png)


![Chart](images/chart_36.png)


![Chart](images/chart_37.png)


With the arrival of the sixth Yu-Gi-Oh! series, the latest types of cards and races have been introduced, namely the **Cyberse** and the **Link Monsters**.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/1861629.jpg"><img src="https://images.ygoprodeck.com/images/cards/1861629.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/31833038.jpg"><img src="https://images.ygoprodeck.com/images/cards/31833038.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/41463181.jpg"><img src="https://images.ygoprodeck.com/images/cards/41463181.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/78437364.jpg"><img src="https://images.ygoprodeck.com/images/cards/78437364.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/32448765.jpg"><img src="https://images.ygoprodeck.com/images/cards/32448765.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/93503294.jpg"><img src="https://images.ygoprodeck.com/images/cards/93503294.jpg" width="150"></a></td>
</tr></table>


### Yu-Gi-Oh! Sevens


![Chart](images/chart_38.png)


![Chart](images/chart_39.png)


![Chart](images/chart_40.png)


In the table, I noticed that the card category I mentioned earlier, namely 'skill cards', is represented by only one item. This is because this card is the only one with an OCG (Official Card Game) release date, while in reality, there are 124 cards of this type for the TCG version.

'Skill cards' were introduced into the world of Yu-Gi-Oh! starting in 2019. It could be speculated that this addition is a tribute to the popular video game Yu-Gi-Oh! Duel Links, where playable characters possess unique abilities. In fact, these 'skill cards' allow the player to embody their favorite Yu-Gi-Oh! character and use a special ability during duels.


<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/300302026.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302026.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302062.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302062.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302028.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302028.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302022.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302022.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302042.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302042.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300201008.jpg"><img src="https://images.ygoprodeck.com/images/cards/300201008.jpg" width="150"></a></td>
</tr></table>


# Conclusion


Therefore, we can conclude this analysis by confirming that the value of a card depends on various factors, including:


- The story behind it.
- The printing type.
- The rarity.
- The card's effect.
- The available copies.


Furthermore, during the temporal analysis, we noted how new types of cards and races have been introduced over the years. Also, in this analysis, we observed that over the years, some races have been distributed more frequently than others. For example, in the Yu-Gi-Oh! 5D and ARC V series, the machine race predominates over the warrior race, which has always held the top spot. Additionally, in the Yu-Gi-Oh! Link series, the cyberse race prevails over the warrior race, being introduced more recently.


It's important to note that over the years, particular attention has been given to the dragon race. As mentioned earlier, if other races are less distributed in this game, it doesn't mean they are weak. For instance, the reptile race, although less distributed, proves to be strong thanks to the "alien" archetype (an interesting archetype with which I won a tournament), or the pyro race (thanks to the volcanic archetype or others mentioned earlier).


Furthermore, we noticed that the more a card's effect can lead to victory, the greater the chances that it falls into the Limited, Semi-Limited, and Forbidden categories. During the analysis, we also discovered, through the word cloud, that there are more cards influencing cards in hand than those on the field, and that some cards include the term "Special Summon" in the text.


Unfortunately, this dataset does not include a variable related to the price of the cards.
