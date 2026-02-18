<p align="center">
  <img src="https://images.ygoprodeck.com/images/cards/89631139.jpg" width="120">
  <img src="https://images.ygoprodeck.com/images/cards/46986414.jpg" width="120">
  <img src="https://images.ygoprodeck.com/images/cards/6150044.jpg" width="120">
  <img src="https://images.ygoprodeck.com/images/cards/44508094.jpg" width="120">
  <img src="https://images.ygoprodeck.com/images/cards/1861629.jpg" width="120">
</p>

<h1 align="center">🃏 Yu-Gi-Oh! Cards — Exploratory Data Analysis</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Plotly-5.x-3F4F75?logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/Matplotlib-3.x-11557C" alt="Matplotlib">
  <img src="https://img.shields.io/badge/NumPy-1.x-013243?logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Dataset-Kaggle-20BEFF?logo=kaggle&logoColor=white" alt="Kaggle">
</p>

<p align="center"><i>📊 Click on any chart to open the interactive Plotly version</i></p>

---

## 📑 Table of Contents

| # | Section | Description |
|:-:|:--------|:------------|
| 1 | [🎮 Introduction](#-introduction) | What is Yu-Gi-Oh? Card structure |
| 2 | [📊 Dataset](#-dataset) | 27 variables description |
| 3 | [🔍 EDA - Level & Stats](#-eda---level--stats) | Level distribution, ATK vs DEF |
| 4 | [🃏 Card Types](#-analysis-of-the-types-of-yu-gi-oh-cards) | Spell, Trap, Extra Deck, Main Deck |
| 5 | [🌗 Attributes](#-analysis-of-yu-gi-oh-card-attributes) | Attribute frequency and preference |
| 6 | [⚔️ Races](#-race-analysis) | Race distribution and popularity |
| 7 | [👁️ Views & Votes](#-analysis-between-views-and-votes-of-yu-gi-oh-cards) | Ash Blossom, Black Luster Soldier |
| 8 | [🚫 Banned Cards](#-analysis-of-banned-limited-and-semi-limited-yu-gi-oh-cards) | Banned, Limited, Semi-Limited, Exodia |
| 9 | [🪤 Trap Monsters](#-analysis-of-cards-trap-monster) | Special trap-monster cards |
| 10 | [💎 Rarity](#-analysis-card-rarity) | Tyler the Great Warrior, rare cards |
| 11 | [⭐ Staple Cards](#-analysis-of-card-staple) | 64 staple cards analysis |
| 12 | [🔄 Treated As](#-analysis-of-card-treated_as) | Cards with alternate names |
| 13 | [📅 Temporal Analysis](#-temporal-analysis) | Evolution across 7 anime series |
| 14 | [📝 Conclusion](#-conclusion) | Final insights |

---

## 🎮 Introduction

**👇 About the Yu-Gi-Oh! card game**

Yu-Gi-Oh! is a card game where two players try to defeat each other by reducing the opponent's Life Points (down to 0) using a collection of monster, magic, and trap cards.

In addition to your decks, you'll need some extra items to assist you in the game. These items include:

- **A coin**: Some cards require flipping a coin.
- **Dice**: Some cards require a dice roll.
- **Counters**: Any small object that can be used as an indicator to keep track of certain metrics that may affect some cards.
- **Monster Tokens**

For more information on the card game, visit the following link [How to Play Yu-Gi-Oh! 🎲](https://www.dacardworld.com/gaming/yu-gi-oh-cards/how-to-play#:~:text=%2DGi%2DOh!-,Yu%2DGi%2DOh!,%2C%20spell%2C%20and%20trap%20cards.)

**🃏 How is a Yu-Gi-Oh card structured?**

- **Name**: Each card has its unique name, used to identify the card.
- **Attribute**: All monsters in the game have one of the 7 attributes: DARK, LIGHT, FIRE, WATER, EARTH, WIND, and DIVINE. Spells/Traps do not have Attributes but indicate whether the card is a Spell or a Trap.
- **Image**: The image used to represent the card.
- **Level**: Most monsters in Yu-Gi-Oh have a Level, indicated by the number of stars below the name.
- **Type**: Enclosed in square brackets, denotes the characteristic of the card.
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

---

## 📊 Dataset

**📋 Dataset variables (27 columns)**

| Variable | Description |
|:---------|:------------|
| `Id` | Card identification number |
| `Name` | Card name |
| `Type` | Card type |
| `Desc` | Card description |
| `Atk` | Attack value |
| `Def` | Defense value |
| `Level` | Monster card level |
| `Race` | Monster card race |
| `Attribute` | Monster card attribute |
| `Scale` | Pendulum scale value |
| `Archetype` | Cards that share a specified name string in a card's effect |
| `Linkval` | The Link value of the card if it's a "Link Monster" |
| `LinkMarkers` | Represented by red arrows radiating outward from the artistic frame of the Link Monster |
| `Image_url` | Card image link |
| `Image_url_small` | Small card image link |
| `Ban_Tcg` | Card status in the TCG Forbidden List |
| `Ban_Ocg` | Card status in the OCG Forbidden List |
| `Ban_Goat` | Card status in the GOAT Format Forbidden List |
| `Staple` | Refers to a card that is generally powerful and can be played in any deck |
| `Views` | Number of card views |
| `ViewsWeek` | Number of card views per week |
| `Upvotes` | Number of positive votes for the card |
| `Downvotes` | Number of negative votes for the card |
| `Formats` | Card format |
| `Treated_as` | Card that, in the description, can be called by another name |
| `Tcg_Date` | Publication date of the card in TCG (America, Europe) |
| `Ocg_Date` | Publication date of the card in OCG (Japan, Asia, China, Korea) |
| `Has_effect` | Has an effect (1 yes & 0 no) |

---

## 🔍 EDA - Level & Stats

[![Chart](images/chart_01.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_01.html)

[![Chart](images/chart_02.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_02.html)

**In the histogram, it's evident that the majority of monster cards fall into level 4.** However, it's noteworthy that a card's level doesn't necessarily determine its strength. In fact, the analysis of the scatterplot reveals that many cards gain power through their unique effects. An example of this is represented by the following cards:

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/15397015.jpg"><img src="https://images.ygoprodeck.com/images/cards/15397015.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/16428514.jpg"><img src="https://images.ygoprodeck.com/images/cards/16428514.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/53143898.jpg"><img src="https://images.ygoprodeck.com/images/cards/53143898.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/86120751.jpg"><img src="https://images.ygoprodeck.com/images/cards/86120751.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/60303688.jpg"><img src="https://images.ygoprodeck.com/images/cards/60303688.jpg" width="150"></a></td>
</tr></table>

**On the other hand, it's important to observe in the scatterplot that as the card level increases, so do the values of ATK and DEF.** It's crucial to keep in mind that some cards don't follow this trend, as their ATK and DEF values (represented as "???") depend on specific effects indicated on the card. This is the case for cards like:

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

These data confirm that a card's power is not exclusively tied to ATK and DEF values but is strongly influenced by special effects that can disrupt opponents' strategies.

---

## 🃏 Analysis of the types of Yu-Gi-Oh! cards

**📖 Spell & Trap card type descriptions**

I begin by examining the **Spell & Trap Zone**, which encompasses various types of cards:

- **Quick-Play Spells:** Allow the turn player to activate Quick-Play Spell Cards from their hand during any Phase of their turn. Recognizable by the lightning bolt symbol.
- **Equip Spells:** Can be equipped to face-up monsters on the field. Marked with a target symbol.
- **Continuous Spells:** Remain on the field once activated. Recognizable by the infinity symbol.
- **Field Spells:** Often focused on boosting ATK and/or DEF for cards with specific attributes, types, or archetypes. Distinguished by the compass rose symbol.
- **Normal Spells:** Allow the turn player to set a Normal Spell Card and activate it in the same turn. No distinctive symbols.
- **Ritual Spells:** Used to ritually summon Ritual Monsters. Characterized by the flaming chalice symbol.

**Trap Cards:**

- **Normal Traps:** Can be activated in response to the effects of Effect Monsters, Spell Cards, as well as most other Trap Cards and Quick-Play Spell Cards. No distinctive symbols.
- **Counter Traps:** Most can only be activated to negate or punish the activation of other cards or the Summoning of monsters. Recognizable by the curved arrow symbol.
- **Continuous Traps:** Remain on the field after activation. Effects remain active until the owner is unable to pay the cost or fulfill conditions, OR until destroyed.

[![Chart](images/chart_03.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_03.html)

[![Chart](images/chart_04.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_04.html)

[![Chart](images/chart_05.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_05.html)

From the following histograms, it is evident that normal Spell and Trap cards are the most common, followed by Continuous and Quick-Play Spell cards. Regarding monsters in the Extra Deck, Xyz monsters are the most frequent, followed by Fusion monsters, with Synchro monsters in third place.

The reason Xyz monsters are more common and appreciated is that they do not require the use of Spell cards for summoning, only monsters whose levels are indicated on the card. What makes Xyz monsters unique is their ability to detach the monsters used for the summoning to activate an additional effect.

In the third histogram, the most common type consists of monsters with effects capable of triggering a chain reaction for summoning other monsters or annihilating the opponent's cards. As for Ritual monsters, their minority is due to the fact that they can only be summoned through Ritual Spell cards.

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

---

## 🌗 Analysis of Yu-Gi-Oh! card attributes

[![Chart](images/chart_06.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_06.html)

[![Chart](images/chart_07.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_07.html)

**What are the most common attributes and which ones are the most favored?**

In both histograms, the "Dark" attribute takes the first position, followed by "Earth," "Light," "Water," "Wind," and "Fire." However, when focusing on preference, the "Light" attribute is more appreciated than "Earth," while "Wind" is less popular than "Fire."

- **Darkness:** It stands out as the best attribute, both for the effectiveness of the cards and for deck or archetype creation, creating a powerful synergy with spells and traps. Konami strives to integrate cards from other attributes into this, as demonstrated in the "PredaPlant" archetype.
- **Light:** Includes various races, including fairies, machines, warriors, dragons, and demons. Two notable examples are the "Cyber Dragon" and "ABC" archetypes.
- **Earth:** Most monsters specialize in negating the effects of other monsters, spells, and traps. Evident in archetypes such as "Ancient Gear," "Naturia," and "Infinity Track."
- **Water:** Thanks to their versatility, water monsters can be used in various strategies. The predominant strategy for "Water" decks is to build a defensive wall while accumulating resources. A tangible example is the 'Nubian' archetype (one of my favorites).
- **Fire:** "Fire" monsters often focus on the "Burn" mechanic, inflicting effect damage. Less appreciated due to the scarcity of notable archetypes.
- **Wind:** Takes the penultimate position, with the fewest support cards compared to other attributes (excluding "DIVINE").
- **Divine:** Ranks last, represented by only six monsters, including the famous three Egyptian deities.

Here is a list of cards by attribute:

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/66309175.jpg"><img src="https://images.ygoprodeck.com/images/cards/66309175.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/1546123.jpg"><img src="https://images.ygoprodeck.com/images/cards/1546123.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/33198837.jpg"><img src="https://images.ygoprodeck.com/images/cards/33198837.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/20003527.jpg"><img src="https://images.ygoprodeck.com/images/cards/20003527.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/32543380.jpg"><img src="https://images.ygoprodeck.com/images/cards/32543380.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/73125233.jpg"><img src="https://images.ygoprodeck.com/images/cards/73125233.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/10000080.jpg"><img src="https://images.ygoprodeck.com/images/cards/10000080.jpg" width="150"></a></td>
</tr></table>

In conclusion, the preference for attributes is influenced by a combination of card effects and gameplay strategies.

---

## ⚔️ Race analysis

[![Chart](images/chart_08.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_08.html)

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/15180041.jpg"><img src="https://images.ygoprodeck.com/images/cards/15180041.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/83104731.jpg"><img src="https://images.ygoprodeck.com/images/cards/83104731.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/31764700.jpg"><img src="https://images.ygoprodeck.com/images/cards/31764700.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/40737112.jpg"><img src="https://images.ygoprodeck.com/images/cards/40737112.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/61257789.jpg"><img src="https://images.ygoprodeck.com/images/cards/61257789.jpg" width="150"></a></td>
</tr></table>

From the histogram, it's noticeable that the "warrior" category takes the first place, followed by "machine," "demon," "spellcaster," and "dragon."

**What makes this category better than the others?**

- **Warrior:** Diverse, versatile, and popular. There are Warriors of every Attribute, mainly EARTH, DARK, and LIGHT. Their varied strategies make them arguably one of the best types.
- **Machine:** Rely on high ATTACK values and a variety of powerful effects. They often negate the effects of specific opponent's cards and/or destroy them.
- **Demon:** Most focus on offensive "beatdown" tactics, putting pressure with stunning effects, lockdown, banishment effects, or deck milling.
- **Spellcaster:** Very versatile, often used with Magic Card support. Most present in current Forbidden and Limited lists.
- **Dragon:** Tend to be the strongest boss monsters, known for having higher ATTACK values than any other monster type.

**Why are some races less common?**

Positive:
- **Zombie:** Some of the best generic support cards, like "Uni-Zombie" and "Mezuki." "Zombie World" can lock the opponent from summoning non-Zombie types.
- **Cyberse:** Latest type to enter Yu-Gi-Oh!, "Salamangreat" has consistently been on top since its introduction.

Negative:
- **Divine-Beast:** Only the iconic Egyptian God Cards.
- **Pyro:** Very little support over the years. Only "Volcanic" was usable.
- **Reptile:** Has potential with archetypes like "Aliens" and "Worms," but none came close to being good.
- **Fish:** There has never been a good Fish-type archetype.

However, there's a key reason why some types of cards are more common than others, and it's closely tied to the release dates of the cards. Over the years, new card types and races have been introduced, a topic I'll delve into in the [Temporal Analysis](#-temporal-analysis) section.

---

## 👁️ Analysis between views and votes of Yu-Gi-Oh! cards

[![Chart](images/chart_09.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_09.html)

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

[![Chart](images/chart_10.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_10.html)

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

**In both charts, a card stands out, "Ash Blossom & Joyous Spring,"** which, despite having a significant number of views, is also the least rated compared to others.

<img src="https://images.ygoprodeck.com/images/cards/14558127.jpg" width="150">

**Why is Ash Blossom so discussed? And why is Black Luster Soldier so beloved?**

**Ash Blossom & Joyous Spring:**
- **Secret Rare Edition:** Originally printed in the "Maximum Crisis" series in May 2017, a set of three copies could cost up to €200.00.
- **Triple Effect:** Allows countering: (1) Special summon a monster from the deck, (2) Send a card from the deck to the graveyard, (3) Add a card from the deck to the hand.

**Black Luster Soldier** — the card with the highest number of positive votes, despite having no special effect:
- **Absence of the Identification Number:** One of the rare cards that lacks the eight-digit ID at the bottom left.
- **The Card's History:** In the first Yu-Gi-Oh! tournament (1999), the winner received a copy printed in stainless steel. One copy was put up for sale in 2013 at the staggering price of 20 million dollars — settled for "only" 2 million dollars.

<table><tr>
<td><a href="https://i.ebayimg.com/images/g/fDAAAOSwUJtgy0B6/s-l1600.jpg"><img src="https://i.ebayimg.com/images/g/fDAAAOSwUJtgy0B6/s-l1600.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/5405694.jpg"><img src="https://images.ygoprodeck.com/images/cards/5405694.jpg" width="150"></a></td>
<td><a href="https://cdn.idntimes.com/content-images/community/2022/11/819gmmoupzl-ac-sy500-56965fbaa68adf470a17cc45ea5d328d-85149eced310f2e3793970d105f0aab1.jpg"><img src="https://cdn.idntimes.com/content-images/community/2022/11/819gmmoupzl-ac-sy500-56965fbaa68adf470a17cc45ea5d328d-85149eced310f2e3793970d105f0aab1.jpg" width="150"></a></td>
</tr></table>

**Ultimately, the value of cards is not determined solely by gameplay effects but also by the story surrounding the card itself and the type of print.** In the second scatterplot, "Imperial Order" and "True King of All Calamities" accumulate the most negative votes — their powerful effects can block the use of monsters and spells, and both cards have been banned in both TCG and OCG.

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/61740673.jpg"><img src="https://images.ygoprodeck.com/images/cards/61740673.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/88581108.jpg"><img src="https://images.ygoprodeck.com/images/cards/88581108.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/11384280.jpg"><img src="https://images.ygoprodeck.com/images/cards/11384280.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/76375976.jpg"><img src="https://images.ygoprodeck.com/images/cards/76375976.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/50588353.jpg"><img src="https://images.ygoprodeck.com/images/cards/50588353.jpg" width="150"></a></td>
</tr></table>

---

## 🚫 Analysis of Banned, Limited and Semi-Limited Yu-Gi-Oh! cards

- **Banned:** These cards cannot be used in any official duel, often due to their unfair power.
- **Semi-Limited:** You are allowed to include only two copies of any Yu-Gi-Oh! card in your deck.
- **Limited:** You can include in your deck only one copy of any Yu-Gi-Oh! card with a limited edition.

[![Chart](images/chart_11.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_11.html)

[![Chart](images/chart_12.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_12.html)

**In both graphs, most cards with an effect fall into the "Bannable," "Semi-Limited," and "Limited" categories.** However, to great surprise, there are 4 effectless cards that are Limited — the pieces of **"Exodia the Forbidden One."**

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/8124921.jpg"><img src="https://images.ygoprodeck.com/images/cards/8124921.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/70903634.jpg"><img src="https://images.ygoprodeck.com/images/cards/70903634.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/33396948.jpg"><img src="https://images.ygoprodeck.com/images/cards/33396948.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/7902349.jpg"><img src="https://images.ygoprodeck.com/images/cards/7902349.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/44519536.jpg"><img src="https://images.ygoprodeck.com/images/cards/44519536.jpg" width="150"></a></td>
</tr></table>

The fear is due to the effect of Exodia the Forbidden One, which allows you to win the game if you have all 5 pieces in your hand. For more details: 👉🏻 [Exodia Strategy Site](https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=49ce8d50627a96108420c3cb3695c4f2&dno=1&request_locale=it)

---

## 🪤 Analysis of cards trap-monster

It's important to remember that there is a category of special trap cards that can be summoned as monster cards and, at the same time, function as trap cards.

They may seem useless, but some slightly crazy players (for example, me) have exploited the effects of these cards to create a deck. For more information: [Trap Monster Deck 🎲](https://ygoprodeck.com/deck/trap-monster-deck-70608)

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/87772572.jpg"><img src="https://images.ygoprodeck.com/images/cards/87772572.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/23626223.jpg"><img src="https://images.ygoprodeck.com/images/cards/23626223.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/98414735.jpg"><img src="https://images.ygoprodeck.com/images/cards/98414735.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/49514333.jpg"><img src="https://images.ygoprodeck.com/images/cards/49514333.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/38761908.jpg"><img src="https://images.ygoprodeck.com/images/cards/38761908.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/35035481.jpg"><img src="https://images.ygoprodeck.com/images/cards/35035481.jpg" width="150"></a></td>
</tr></table>

---

## 💎 Analysis card rarity

[![Chart](images/chart_13.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_13.html)

Common cards are the most widespread, followed by super rare, ultra rare, rare, and secret rare cards. The value of a card increases the rarer it is, but is also influenced by the card's effect, printing method, copies in existence, and the story behind it.

There is another extremely rare card: **"Tyler the Great Warrior"**. There is only one copy in circulation, created by Tyler Gressle in 2005 as part of a Make-a-Wish request when he was 14 years old and battling a rare form of liver cancer. 18 years later, the final auction offer raised a whopping **$311,211**.

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/68811206.jpg"><img src="https://images.ygoprodeck.com/images/cards/68811206.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/89631139.jpg"><img src="https://images.ygoprodeck.com/images/cards/89631139.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/46986414.jpg"><img src="https://images.ygoprodeck.com/images/cards/46986414.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/57728570.jpg"><img src="https://images.ygoprodeck.com/images/cards/57728570.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/30100551.jpg"><img src="https://images.ygoprodeck.com/images/cards/30100551.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/69015963.jpg"><img src="https://images.ygoprodeck.com/images/cards/69015963.jpg" width="150"></a></td>
</tr></table>

---

## ⭐ Analysis of card staple

[![Chart](images/chart_14.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_14.html)

'Staple' cards represent a set of cards that play a crucial role during a duel. Overall, there are 64 of these special cards, but it's interesting to note that 20 of them fall into the categories of 'Limited,' 'Semi-Limited,' and 'Forbidden.'

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/12580477.jpg"><img src="https://images.ygoprodeck.com/images/cards/12580477.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/83764719.jpg"><img src="https://images.ygoprodeck.com/images/cards/83764719.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/24224830.jpg"><img src="https://images.ygoprodeck.com/images/cards/24224830.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/37818794.jpg"><img src="https://images.ygoprodeck.com/images/cards/37818794.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/35261759.jpg"><img src="https://images.ygoprodeck.com/images/cards/35261759.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/70369116.jpg"><img src="https://images.ygoprodeck.com/images/cards/70369116.jpg" width="150"></a></td>
</tr></table>

---

## 🔄 Analysis of card treated_as

[![Chart](images/chart_15.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_15.html)

Cards falling under the **'treated_as'** category are those whose description can be considered with a **different name** or with the **same name but a different image.** Out of the 106 cards in this category, only 4 are classified as 'Limited,' 'Semi-Limited,' or 'Forbidden.'

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/27927359.jpg"><img src="https://images.ygoprodeck.com/images/cards/27927359.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/295517.jpg"><img src="https://images.ygoprodeck.com/images/cards/295517.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/80316585.jpg"><img src="https://images.ygoprodeck.com/images/cards/80316585.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/68679595.jpg"><img src="https://images.ygoprodeck.com/images/cards/68679595.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/17732278.jpg"><img src="https://images.ygoprodeck.com/images/cards/17732278.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/13857930.jpg"><img src="https://images.ygoprodeck.com/images/cards/13857930.jpg" width="150"></a></td>
</tr></table>

---

## 📅 Temporal Analysis

In this section, I break down the dataset based on the release dates of the cards in the OCG format, taking into account the releases of animated series as well.

<img src="https://i.ytimg.com/vi/E6ci1y1K5uI/maxresdefault.jpg" width="700">

Reference sources: [🔗 OCG Set Release Order](https://yugioh.fandom.com/wiki/Order_of_Set_Release#2002) | [🔗 Animated Series](https://en.wikipedia.org/wiki/Yu-Gi-Oh!)

| OCG Release Date Range | Animated Series Release Date Range | Series Name |
|:-----------------------|:----------------------------------|:------------|
| **04/02/1999 - 30/12/2004** | 18/04/2000 - 29/09/2004 | Yu-Gi-Oh! |
| **20/01/2005 - 08/03/2008** | 06/09/2004 - 26/03/2008 | Yu-Gi-Oh! GX |
| **15/03/2008 - 26/02/2011** | 02/04/2008 - 30/03/2011 | Yu-Gi-Oh! 5D's |
| **19/03/2011 - 20/03/2014** | 11/04/2011 - 23/03/2014 | Yu-Gi-Oh! Zexal |
| **21/03/2014 - 24/03/2017** | 06/04/2014 - 26/03/2017 | Yu-Gi-Oh! Arc-V |
| **25/03/2017 - 02/04/2020** | 10/12/2017 - 25/09/2019 | Yu-Gi-Oh! VRAINS |
| **04/04/2020 - 23/12/2023** | 27/03/2020 - 27/03/2023 | Yu-Gi-Oh! Sevens |

[![Chart](images/chart_16.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_16.html)

### 📺 Yu-Gi-Oh!

[![Chart](images/chart_17.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_17.html)
[![Chart](images/chart_18.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_18.html)
[![Chart](images/chart_19.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_19.html)

In the context of the type and race of cards, currently there are not many variations, as the only cards present are fusion monsters and ritual monsters.

### 📺 Yu-Gi-Oh! GX

[![Chart](images/chart_20.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_20.html)
[![Chart](images/chart_21.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_21.html)
[![Chart](images/chart_22.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_22.html)

### 📺 Yu-Gi-Oh! 5D's

[![Chart](images/chart_23.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_23.html)
[![Chart](images/chart_24.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_24.html)
[![Chart](images/chart_25.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_25.html)

With the introduction of Yu-Gi-Oh! 5D's, **Synchro** monsters and **Tuner** monsters were introduced, while the new "Psychic" race was also introduced.

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/44508094.jpg"><img src="https://images.ygoprodeck.com/images/cards/44508094.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/70902743.jpg"><img src="https://images.ygoprodeck.com/images/cards/70902743.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/9012916.jpg"><img src="https://images.ygoprodeck.com/images/cards/9012916.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/73580471.jpg"><img src="https://images.ygoprodeck.com/images/cards/73580471.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/2403771.jpg"><img src="https://images.ygoprodeck.com/images/cards/2403771.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/25862681.jpg"><img src="https://images.ygoprodeck.com/images/cards/25862681.jpg" width="150"></a></td>
</tr></table>

### 📺 Yu-Gi-Oh! Zexal

[![Chart](images/chart_26.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_26.html)
[![Chart](images/chart_27.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_27.html)
[![Chart](images/chart_28.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_28.html)

With Yu-Gi-Oh! Zexal, **Xyz monsters** were introduced. They do not require Spell cards, but only monsters that share the same level.

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/84013237.jpg"><img src="https://images.ygoprodeck.com/images/cards/84013237.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/31801517.jpg"><img src="https://images.ygoprodeck.com/images/cards/31801517.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/65676461.jpg"><img src="https://images.ygoprodeck.com/images/cards/65676461.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/88120966.jpg"><img src="https://images.ygoprodeck.com/images/cards/88120966.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/9161357.jpg"><img src="https://images.ygoprodeck.com/images/cards/9161357.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/86848580.jpg"><img src="https://images.ygoprodeck.com/images/cards/86848580.jpg" width="150"></a></td>
</tr></table>

### 📺 Yu-Gi-Oh! Arc-V

[![Chart](images/chart_29.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_29.html)
[![Chart](images/chart_30.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_30.html)
[![Chart](images/chart_31.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_31.html)
[![Chart](images/chart_32.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_32.html)

With Yu-Gi-Oh! Arc-V, a new race **"Wyrm"** and a new card type **Pendulum** cards were introduced.

**Pendulum Monsters:** This type of card can be used as both a monster and a spell card. It is characterized by a dual color (orange/yellow and green) and the concept of 'scales.'

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/16178681.jpg"><img src="https://images.ygoprodeck.com/images/cards/16178681.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/47198668.jpg"><img src="https://images.ygoprodeck.com/images/cards/47198668.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/25629622.jpg"><img src="https://images.ygoprodeck.com/images/cards/25629622.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/47075569.jpg"><img src="https://images.ygoprodeck.com/images/cards/47075569.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/40318957.jpg"><img src="https://images.ygoprodeck.com/images/cards/40318957.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/96227613.jpg"><img src="https://images.ygoprodeck.com/images/cards/96227613.jpg" width="150"></a></td>
</tr></table>

### 📺 Yu-Gi-Oh! VRAINS

[![Chart](images/chart_33.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_33.html)
[![Chart](images/chart_34.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_34.html)
[![Chart](images/chart_35.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_35.html)
[![Chart](images/chart_36.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_36.html)
[![Chart](images/chart_37.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_37.html)

With the sixth Yu-Gi-Oh! series, the **Cyberse** race and **Link Monsters** were introduced.

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/1861629.jpg"><img src="https://images.ygoprodeck.com/images/cards/1861629.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/31833038.jpg"><img src="https://images.ygoprodeck.com/images/cards/31833038.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/41463181.jpg"><img src="https://images.ygoprodeck.com/images/cards/41463181.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/78437364.jpg"><img src="https://images.ygoprodeck.com/images/cards/78437364.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/32448765.jpg"><img src="https://images.ygoprodeck.com/images/cards/32448765.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/93503294.jpg"><img src="https://images.ygoprodeck.com/images/cards/93503294.jpg" width="150"></a></td>
</tr></table>

### 📺 Yu-Gi-Oh! Sevens

[![Chart](images/chart_38.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_38.html)
[![Chart](images/chart_39.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_39.html)
[![Chart](images/chart_40.png)](https://imkun-on.github.io/Yu-Gi-Oh-Cards/charts/chart_40.html)

'Skill cards' were introduced in 2019, a tribute to the popular video game Yu-Gi-Oh! Duel Links, where playable characters possess unique abilities.

<table><tr>
<td><a href="https://images.ygoprodeck.com/images/cards/300302026.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302026.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302062.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302062.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302028.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302028.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302022.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302022.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300302042.jpg"><img src="https://images.ygoprodeck.com/images/cards/300302042.jpg" width="150"></a></td>
<td><a href="https://images.ygoprodeck.com/images/cards/300201008.jpg"><img src="https://images.ygoprodeck.com/images/cards/300201008.jpg" width="150"></a></td>
</tr></table>

---

## 📝 Conclusion

The value of a card depends on various factors, including: the story behind it, the printing type, the rarity, the card's effect, and the available copies.

During the temporal analysis, we noted how new types of cards and races have been introduced over the years. For example, in Yu-Gi-Oh! 5D's and Arc-V, the machine race predominates over the warrior race. In Yu-Gi-Oh! VRAINS, the cyberse race prevails over the warrior race.

It's important to note that over the years, particular attention has been given to the dragon race. If other races are less distributed, it doesn't mean they are weak — the reptile race proves strong thanks to the "alien" archetype (an interesting archetype with which I won a tournament).

Furthermore, the more a card's effect can lead to victory, the greater the chances that it falls into the Limited, Semi-Limited, and Forbidden categories. Through the word cloud, we discovered that there are more cards influencing cards in hand than those on the field, and that some cards include the term "Special Summon" in the text.

Unfortunately, this dataset does not include a variable related to the price of the cards.

---

<p align="center"><i>Made with ❤️ for the Yu-Gi-Oh! community</i></p>
