# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Three or four sentences: what a user asks for, and what they get back. -->

FitFindr takes an input request from the user, something like "vintage graphic tee under $30", and creates style and outfit ideas. It gets the description,size, and price from the input, and then searches for items that can match or satisfy. It obtains details like the title,size,condition, and platform of what is a match. If nothing is matched and returned, the user gets a message explaining that nothing was found, as well as some suggestions on what could help their next search be successful. The end result is a matching listing, an outfit idea based on the listing, and a social-media style caption describing it.

---

## The Shape
The Shape I am picking to extend this system is Shape C. I will be adding a fourth tool to the system, called compare_listings(). This tool will receive the list of dictionaries returned by search_listings() and the user's item description. It scores relevance first, then condition and price, and returns the highest-scoring relevant listing.

## Out of Scope
I will not be touching or editing how the search_listings(),suggest_outfit(), or create_fit_card(). I also thought about a compare_prices() function before, but decided among the compare_listings, because using more factors rather than just price is more realistic when a person is out shopping.


## Instrumentation
10 run log entries, with prompt tokens and output tokens also logged to help towards measuring the cost of each run.
**NOTE**: All the entries successfully ran, none of the 10 runs failed.

{"timestamp": "2026-11-12T04:36:28+00:00", "query": "vintage graphic tee under $30", "output": "Scored this cute braided brown leather belt on thredUp for only $12 and it is so good for adding texture to outfits. It comes in One Size (adjustable) so it works great for cinching high-waisted jeans or wide-leg trousers. I am obsessed with how it gives off that cool 90s-meets-Western vibe whether I am running errands or grabbing coffee.", "seconds": 1.38, "prompt_tokens": 432, "output_tokens": 82, "total_tokens": 514}
{"timestamp": "2026-11-12T04:36:30+00:00", "query": "vintage graphic tee under $30", "output": "Scored this braided brown leather belt for only $12 on thredUp and I am obsessed with the vintage Western vibe. It comes in One Size (adjustable) and adds so much texture whether I am styling it with baggy 90s denim or wide-leg khakis. It is such an easy way to elevate a simple tank top and sneakers look without trying too hard.", "seconds": 2.05, "prompt_tokens": 432, "output_tokens": 78, "total_tokens": 510}
{"timestamp": "2026-11-12T04:36:31+00:00", "query": "vintage graphic tee under $30", "output": "Scored this braided brown leather belt for just $12 on thredUp and I am obsessed with the vintage Western vibe. It comes in One Size (adjustable) and adds so much texture whether I am wearing it with baggy 90s denim or sharp khaki trousers. I love how it instantly pulls together a relaxed weekend look or a cool coffee date outfit.", "seconds": 1.35, "prompt_tokens": 432, "output_tokens": 74, "total_tokens": 506}
{"timestamp": "2026-11-12T04:36:32+00:00", "query": "vintage graphic tee under $30", "output": "Found this braided brown leather belt on thredUp for only $12 and it is such a good texture upgrade from my plain belts. It comes in One Size (adjustable) and adds the coolest 90s Western touch to a simple white tank and baggy jeans. I'm also planning to style it with wide-leg khakis and combat boots for an easy coffee date look.", "seconds": 1.31, "prompt_tokens": 432, "output_tokens": 79, "total_tokens": 511}
{"timestamp": "2026-11-12T04:36:34+00:00", "query": "vintage graphic tee under $30", "output": "Scored this amazing braided leather belt on thredUp for just $12. Since it is One Size (adjustable), it is super easy to throw over baggy jeans and a white tank for that 90s Western casual vibe. I am definitely going to be wearing this non-stop for weekend errands!", "seconds": 1.45, "prompt_tokens": 432, "output_tokens": 63, "total_tokens": 495}
{"timestamp": "2026-11-12T04:36:35+00:00", "query": "vintage graphic tee under $30", "output": "I can't get over this braided brown leather belt I scored on thredUp for only $12. Since it's One Size (adjustable), it cinches my baggy 90s jeans and wide-leg trousers perfectly. Adding that little Western buckle gives the whole outfit such a cool, textured finish for running errands or grabbing coffee.", "seconds": 1.34, "prompt_tokens": 432, "output_tokens": 71, "total_tokens": 503}
{"timestamp": "2026-11-12T04:37:45+00:00", "query": "vintage graphic tee under $30", "output": "Scored this vintage braided brown leather belt on thredUp for just $12 and it is so good for adding texture. It comes in One Size (adjustable) so it works with literally all my high-waisted denim and trousers. I'm obsessed with how it pulls together a 90s casual vibe or adds edge to wide-leg trousers for a record store run.", "seconds": 70.01, "prompt_tokens": 432, "output_tokens": 79, "total_tokens": 511}
{"timestamp": "2026-11-12T04:37:47+00:00", "query": "vintage graphic tee under $30", "output": "Found this gorgeous braided brown leather belt on thredUp for just $12 and it's in the One Size (adjustable) fit. The Western buckle adds the best texture whether I'm tossing it on with baggy dark-wash jeans for a relaxed 90s vibe or styling it with khaki trousers and combat boots. It is such an easy piece to dress up or down.", "seconds": 1.53, "prompt_tokens": 432, "output_tokens": 79, "total_tokens": 511}
{"timestamp": "2026-11-12T04:37:48+00:00", "query": "vintage graphic tee under $30", "output": "Scored this gorgeous braided brown leather belt on thredUp for just $12 and I am obsessed. It comes in One Size (adjustable) so it's super easy to wear low on baggy jeans or cinched over wide-leg trousers. That Western buckle adds just the right amount of texture to pull together a relaxed 90s-meets-edgy coffee date fit.", "seconds": 1.29, "prompt_tokens": 432, "output_tokens": 79, "total_tokens": 511}
{"timestamp": "2026-11-12T04:37:49+00:00", "query": "vintage graphic tee under $30", "output": "Scored this braided brown leather belt for only $12 on thredUp and I am obsessed with the texture. It comes in One Size (adjustable) so it's super easy to throw on with baggy jeans and a white tank for that 90s-meets-Western casual look. It honestly completely changes the vibe compared to my plain belts.", "seconds": 1.26, "prompt_tokens": 432, "output_tokens": 73, "total_tokens": 505}

## What it Costs
Across the 10 logged runs, the system used 5,077 total tokens, which averages to about 507.7 tokens per a single run. I calculated each run's usage of tokens by adding its prompt tokens and output tokens. Then I added the totals from all 10 runs and divided by 10.

If 100 people were to run this system in a day, it would cost about 507,700 tokens. 5,077*100 = 507,700.



### `search_listings`

- **What it does:**
Takes the input regarding a clothes description and searches for a matching description, with sizes and prices that can also be optionally added.
- **Inputs:** <!-- name and type each: `max_price` (float), not "a price" -->
description (str)
size (str)
max_price (float)
- **Returns:**
A list of listing dictionaries, each with the fields: "id,title,description,category,style_tags,size,condition,price,colors,brand,platform"
- **When it has nothing:**
It will return an empty list, since nothing matched.

### `compare_listings`
- **What it does:**
Takes the list of listing dictionaries returned by `search_listings()` and the user's item description. It scores relevance, condition, and price, rejecting listings from the wrong category.

- **Inputs:**
listings (list[dict]), description (str)

- **Returns:**
The listing dictionary with the highest calculated score,

- **When it has nothing:**
It will return 'None'.

### `suggest_outfit`

- **What it does:**
Takes in a thrifted item and the user's wardrobe dict, and suggests outfits.
- **Inputs:**
new_item (dict)
wardrobe (dict)
- **Returns:**
A string of outfit suggestions.
- **When it has nothing:**
Ask model for general styling advice, and return that advice.

### `create_fit_card`

- **What it does:**
Creates a social-media style caption from the outfit suggested and item that matches original description.
- **Inputs:**
outfit (str)
new_item (dict)
- **Returns:**
Two-to-four sentence social-media style caption.
- **When it has nothing:**
Returns a descriptive message about the outfit.

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:**
If search_listings returns an empty list, write a message in the session that states what to change in the description and stop. Otherwise, take the first restult and go to suggest_outfit.

**Where it lives:** `agent.py::run_agent`
It lives in 'agent.py::run_agent'

**How the query is parsed:** <!-- regex, string splitting, or asking the model — say which -->
The query is parsed by regex in agent::parse_query.

**What moves through the session:** <!-- which fields, in what order -->
1. parse_query parses description,size, and max_price from user input
2. _search calls search_listings with the parsed topics and uses that for search_results
3. If the list is empty in search_listings, it runs the _nothing_found_message function and stops the session.
4. Otherwise, selected_item is determined based on the calculated score of relevance, price, and condition in compare_lisitngs
5. suggest_outfit then reads selected_item and 'wardrobe', which then fills 'outfit_suggestion'
6. create_fit_card reads outfit_suggestion(from suggest_outfit) and selected_item, which makes fit_card.


---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**
```
$ python app.py ask 'vintage graphic tee under $30'

[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style, Vintage Band Tee — Faded Grey … +7 more
      →    10 match(es)
[3] select_item
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
[4] suggest_outfit
      in:  Y2K Baby Tee — Butterfly Print ($18.0, depop)
      out: Pair the butterfly baby tee with your dark-wash baggy straight-leg jeans and chunky white sneakers to lean rig…
      →    10 wardrobe item(s)
[5] create_fit_card
      in:  Y2K Baby Tee — Butterfly Print ($18.0, depop)
      out: Just scored the cutest little butterfly baby tee on Depop and I am obsessed. It’s marked S/M and only $18, whi…

  Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop

  Outfit:   Pair the butterfly baby tee with your dark-wash baggy straight-leg jeans and chunky white sneakers tolean right into that Y2K aesthetic. Throw your slightly cropped vintage black denim jacket over top and sling theblack crossbody bag across your chest for an easy, balanced look that plays with proportions. This outfit is perfect for running weekend errands, casual brunch, or meeting up with friends at a café. 

For a slightly warmer or more grounded look, tuck the baby tee into your wide-leg khaki trousers and add the brown leather belt to define your waist. Slip into your black combat boots and layer the black cropped zip hoodie loosely over your shoulders just in case it gets chilly. This combination works great for a casual day on campus, hitting up the local thrift shops, or a casual daytime date. 

Go ahead and buy it—you have plenty of versatile basics in your closet to anchor the loud graphic!

  Fit card: Just scored the cutest little butterfly baby tee on Depop and I am obsessed. It’s marked S/M and only$18, which is an absolute steal for this level of early 2000s nostalgia. I'm totally planning to lean into the Y2K aesthetic by pairing it with baggy straight-leg denim and chunky white sneakers.

```

**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

[{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}]

```


```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

Yes, buy them. Since your existing jeans are baggy dark wash, these medium-wash 501s will give you a completely different, classic straight-leg silhouette that your closet currently lacks. 

Outfit 1: Pair the 501s with your white ribbed tank top tucked in, layered under the slightly cropped vintage black denim jacket, and finish with your chunky white sneakers and black crossbody bag. Cinch the waist with your brown leather belt to pull the denim-on-denim look together. This is an effortless, go-to outfit for running errands, casual weekend coffee runs, or walking around the city.

Outfit 2: Wear the 501s with your really oversized grey crewneck sweatshirt hanging loose over the top, paired with your black combat boots and the black crossbody bag. The structured, straight fit of the vintage Levi'swill balance out the heavy, oversized proportions of the sweatshirt. This is an easy, comfortable look for casual hangouts, travel days, or working from a coffee shop.

```

```
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))""

Run 1: Scored these vintage Levi's 501 jeans on depop for $38 and I am obsessed. They are a size W30 L30 with the absolute best worn-in fade at the knees. I'm going to wear them with crisp white sneakers for the easiest everyday streetwear vibe.

Run 2: Scored these vintage Levi's 501 jeans on Depop for just $38 and they fit like an absolute dream. The wash is perfection, and I'm totally planning to live in them with my chunky white sneakers for the ultimate casual streetwear fit. Grabbed them in size W30 L30 and I'm never taking them off.

Run 3: Scored these vintage Levi's 501 jeans on Depop for just $38 and I am obsessed with the knee fading. They are a size W30 L30 and fit me like an absolute dream. I am totally styling them with crisp white sneakers for thateffortless, casual weekend uniform.

```

---

## How I Used AI

<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for:*
I asked Claude for ideas on how to build and organize the first tool.
- *What came back:*
Working and organized code, but with extra functions: _stem, and _score. These functions were extra steps as to better match certain words, like words with a trailing 's', so 'tee' can match with 'tees'
- *What I changed:*
I suggested that instead of more functions being added, the function can still be implemented inside that function itself. This made it so it matched the TODO list to meet all the requirements.

**Moment 2**

- *What I asked for:*
I asked claude to check if my 4th criterion was too strict, I originally had it as "For 5 different items, each fit card mentions the item's price,size, and platform, and is between 2-4 sentences — for 5 of 5 tries.

- *What came back:*
It suggested that I change the tries to at least 4 of 5. Claude explained to me that there may be cases that the model can write item's price,size, and platform differently than comparing it raw to how the listings has it. This made it so even though the criterion technically passes, it fails due to the similarity check.

- *What I changed:*
I rewrote the criterion to make it so at least 4 of 5 tries to better help with the case of paraphrasing the required topics differently.

**UNIT 4**
- In this unit, I used AI to help me summarize the results of each run that I made from each scenario. Claude helped me understand and better format what each pass in each run meant, as well as misses. This helped me fill in the before and after table to better show the results of any changes.

- Another way I used AI was to better help me understand what could help with the misses and diagnoses I made from the before results. I asked Claude what could be the reason for the criteria 3 and 4 to be missed, and it further explained that the 503 UNAVAILABLE message made it so nothing was returned in certain steps for both criteria, which is what further explained why it was a MISS.



## How I used AI -CAPSTONE
**Moment 1**
- *What I asked for:*
 I asked Github if my ORIGINAL options for scoring on price, condition, and SIZE were measureable.
- *What came back:*
Claude told me that size was already filtered out in search_listings(), which meant that search_listings was already checking price limits on the listings.
- *What I changed:*
That made me choose only the two categories to calculate since size was already being implemented.

**Moment 1**

- *What I asked for:*

- *What came back:*

- *What I changed:*


<!-- ═══════════════════════  THE TEST - CAPSTONE ═══════════════════════

    
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before, With the new extension 

| Criterion | Target | Try 1 | Try 2 | Try 3 | Verdict |
|---|---:|---|---|---|---|
| 1. Matching query completes all four tools | 2 of 3 | PASS | PASS | PASS | MET (3/3) |
| 2. Bad query stops before compare_listings() | 3 of 3 | PASS | PASS | PASS | MET (3/3) |
| 3. compare_listings() calculates the combined score accurately | 3 of 3 | PASS | PASS | PASS | MET(3/3)|
| 4. Selected item has relevance | 3 of 3 | FAIL | FAIL | FAIL | MISSED (0/3) |
| 5. Selected listing is passed consistently | 3 of 3 | PASS | PASS | PASS | MET(3/3) |


**Real output from one try**, pasted as text, naming the file and function
that produced it:

CRITERION 1:
Produced by 'serve.py::ask()' -> 'log_run()'
```json
{"timestamp": "2026-11-12T20:25:21+00:00", "query": "Khaki cargo pants under $40", "output": "Found these amazing olive straight leg trousers on Poshmark and I am obsessed with the fit. They are a size W30 and only cost $29, which is such a steal for how versatile they are. I love styling them with a tucked-in white tank and chunky sneakers for an easy weekend coffee run.", "seconds": 6.01, "prompt_tokens": 626, "output_tokens": 185, "total_tokens": 811}

```

CRITERION 2:
Produced by 'serve.py::ask()' -> 'log_run()'
```json
{"timestamp": "2026-11-12T20:25:52+00:00", "query": "How to make a cheese pizza", "output": "Nothing in the listings matched description 'How to make a cheese pizza'.\nThings to change: try broader words — 'jacket' finds more than 'cropped corduroy jacket'.", "seconds": 0.49, "prompt_tokens": 0, "output_tokens": 0, "total_tokens": 0}
```

CRITERION 3: 
Produced by 'test_compare_listings.py', json produced by 'serve.py::ask() -> 'log_run()'

Criterion 3: PASS — 3/3, 
```json

{"timestamp": "2026-11-12T20:26:16+00:00", "query": "Oversized vintage tee", "output": "Found this absolute dream of a butterfly baby tee on depop and I am obsessed. It’s an S/M and only $18, which is a steal for how much early 2000s energy it brings. I'm picturing it styled with baggy dark-wash jeans and chunky sneakers for the ultimate nostalgic weekend fit.", "seconds": 1.3, "prompt_tokens": 392, "output_tokens": 71, "total_tokens": 463}
```

CRITERION 4:
Produced by 'serve.py::ask()' -> 'log_run()'
```json
{"timestamp": "2026-11-12T20:26:57+00:00", "query": "dark wash baggy pants", "output": "I am so obsessed with this vintage Wrangler denim jacket I just picked up on Poshmark. It has the best structured shoulders and comes in a size S for $42. I am definitely going to layer it over my black hoodie with baggy jeans for running weekend errands.", "seconds": 5.0, "prompt_tokens": 695, "output_tokens": 250, "total_tokens": 945}
```
CRITERION 5:
Produced by 'serve.py::ask()' -> 'log_run()'
```json
{"timestamp": "2026-11-12T20:27:27+00:00", "query": "platform sneakers size 8", "output": "Scored this reversible brown plaid bucket hat on thredUp for just $14 and it is seriously the easiest way to channel some nineties streetwear energy. Since it is One Size, I can just throw it on with a white ribbed tank and baggy dark wash jeans for the ultimate casual coffee run vibe. Can't wait to flip it to the solid tan side and wear it with wide-leg khakis and combat boots for digging through crates at the record store.", "seconds": 6.14, "prompt_tokens": 661, "output_tokens": 240, "total_tokens": 901}
```


## Verdicts and Diagnoses

| Criterion | Target | Verdict | How I decided | 
|---|---|---|---|
| 1.Matching query completes all four tools | 2 of 3 | MET (3/3) | Each matching query returned a fit card. The trace showed the run reached search_listings(), compare_listings(), suggest_outfit(), and create_fit_card(). | 
| 2. Bad query stops before compare_listings() | 3 of 3 | MET (3/3) | Each impossible query returned the no-results message, with no downstream tools called. | 
| 3. compare_listings() calculates the combined score accurately | 3 of 3 | MET(3/3)| test_compare_listings.py used three controlled cases. In each case, the expected highest-scoring listing matched the listing returned by compare_listings(). | 
| 4. Selected item has relevance | 3 of 3 | MISSED (0/3) | The three selected items were not good matches: an oversized tee query returned a baby tee, dark wash baggy pants returned a denim jacket, and platform sneakers returned a bucket hat.  | 
| 5. Selected listing is passed consistently | 3 of 3 | MET(3/3) | In each traced run, the listing ID returned by compare_listings() matched the IDs passed to suggest_outfit() and create_fit_card(). Using the query "python app.py ask 'Khaki cargo pants under $40' --trace", helped me check the same ID was being passed | 


**Diagnoses**
Criterion 4 (Selected item has relevance) was a MISS.
The step: 'tools.py::compare_listings()', after 'tools::search_listings()' returned its matches.

Mechanism: 'search_listings()' returns listings that overlap with keywords, and 'compare_listings()' scores the returned listings only by the condition and the lowest price to determine which one to choose. It does not consider how relevant each listing is to the original query. This makes it so an inxepensive or higher-condition listing can win even if it is the wrong type of item as opposed to the query.
---



## The Improvement, CAPSTONE

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:**
Instead of compare_listings() just calculating the score of each listing returned by search_listings() by price and condition, I added relevance score that will check whether keywords that belong to each category are found in the query. This way, it will higher points, making relevancy the biggest scorer.

**Which failure it was meant to fix:**
The failure was meant to fix the MISS on criterion 4 (Selected item has relevance). All 3 runs failed due to the system returning a fit card that did not match the user's query.

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Verdict |
|---|---:|---|---|---|---|
| 1. Matching query completes all four tools | 2 of 3 | PASS | PASS | PASS | MET (3/3) |
| 2. Bad query stops before compare_listings() | 3 of 3 | PASS | PASS | PASS | MET (3/3) |
| 3. compare_listings() calculates the combined score accurately | 3 of 3 | PASS | PASS | PASS | MET(3/3)|
| 4. Selected item has relevance | 3 of 3 | PASS | PASS | PASS | MET(3/3) |
| 5. Selected listing is passed consistently | 3 of 3 | PASS | PASS | PASS | MET(3/3) |


**Did it help, and how do I know:**

The change did help, Criterion 4 went from MISS with no runs passed, to all passing. The query used for criterion 4: 'Dark Wash Baggy Pants', now returns a similar fit card to what the query was asking for, now recommending black carpenter jeans.

---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] hRun Log — Before, five criteria, five tries eac
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
