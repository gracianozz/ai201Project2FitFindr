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

## Tool Inventory

<!-- Four lines per tool. This is worth 2 points and it's the single most
     common place students lose them.

     "Returns a list" earns NOTHING. The description has to say what is IN
     the list.

     The empty case isn't optional either — it's the thing your loop branches
     on, and if you don't decide it here you'll discover it as a crash in
     Milestone 5. -->

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
4. Otherwise, selected_item is chosen from the first result of the returned list
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



<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. matching query completes | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. impossible query stops early | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. Consistent selected item ID | 5 of 5 | PASS | PASS | PASS | FAIL | FAIL | MISSED (3/5) |
| 4. Proper fit card description with price, size, and platform | 4 of 5 | PASS | FAIL | FAIL | PASS | FAIL | MISSED (2/5) |
| 5. Proper price ceiling | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

**Real output from one try**, pasted as text, naming the file and function
that produced it:

```
CRITERION 1 TRY
### matching query completes

- Query: `vintage graphic tee under $30`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

Outfit suggestion:

```
Outfit 1: Pair the butterfly baby tee with your dark wash baggy straight-leg jeans and the brown leather belt to balance the fitted crop top. Throw on your black cropped zip hoodie over your shoulders and finish the look with chunky white sneakers and your black crossbody bag. This gives you an easy, balanced 90s-meets-Y2K silhouette that is perfect for running weekend errands, hanging out at a coffee shop, or casual daytime dates.

Outfit 2: Tuck the baby tee into your wide-leg khaki trousers and layer your vintage black denim jacket on top to add some edge. Lace up your black combat boots and wear your black crossbody bag for a casual vibe that plays with contrasting proportions. This look is great for casual Fridays, heading to a daytime concert, or meeting friends for lunch.
```

Fit card:

```
Just scored this adorable Y2K baby tee with the cutest butterfly graphic on depop and I am obsessed. It is a size S/M and fits like a dream for only $18. I love styling it with baggy jeans and chunky sneakers for the ultimate casual weekend coffee run vibe.
```

Trace:

```
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
      out: Outfit 1: Pair the butterfly baby tee with your dark wash baggy straight-leg jeans and the brown leather belt …
      →    10 wardrobe item(s)
[5] create_fit_card
      in:  Y2K Baby Tee — Butterfly Print ($18.0, depop)
      out: Just scored this adorable Y2K baby tee with the cutest butterfly graphic on depop and I am obsessed. It is a s…
```



CRITERION 2 TRY
### impossible query stops early

- Query: `designer ballgown size XXS under $5`
- Wardrobe: example

**Try 1**

- stopped early: yes — Nothing in the listings matched description 'designer ballgown', size XXS, under $5.
Things to change: try broader words — 'jacket' finds more than 'cropped corduroy jacket'; drop the size, or try a neighbouring one; raise the price ceiling above $5.
- selected_item: (none)
- search_results: 0

Trace:

```
[1] parse_query
      in:  designer ballgown size XXS under $5
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    0 match(es)
[3] branch
      →    search returned []: stopping before suggest_outfit
```



CRITERION 3 TRY
###  Consistent selected item ID

- Query: `leather bomber jacket under $100`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 7

Outfit suggestion:

```
Buy it. This is a 90s staple that will instantly anchor your wardrobe, and the natural creasing gives it an authentic lived-in look that brand-new leather lacks. 

Outfit 1: Layer the oversized grey crewneck sweatshirt over your white ribbed tank top, pair them with your baggy dark-wash straight-leg jeans, and step into the chunky white sneakers. Throw the leather bomber over the grey crewneck, letting the sweatshirt hem peek out the bottom for that effortless, slouchy 90s skater vibe. This outfit is ideal for casual weekend errands, hanging out at a record store, or grabbing coffee.

Outfit 2: Tuck your white ribbed tank top into the wide-leg khaki trousers, cinch your waist with the brown leather belt, and lace up your black combat boots. Top it off with the black leather bomber for a sharp mix of rugged outerwear and tailored, utilitarian bottoms. This look works great for a casual Friday at work, gallery hopping, or a casual dinner date.
```

Fit card:

```
Scored this vintage 90s leather bomber on depop for $75 and it has the absolute best worn-in look. It comes in size M and has that perfect boxy skater fit when I layer it over a grey crewneck and baggy jeans. Honestly the easiest way to add some instant grunge to any outfit.
```

Trace:

```
[1] parse_query
      in:  leather bomber jacket under $100
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: 90s Leather Bomber — Black, 90s Track Jacket — Navy/White Stripe, Denim Jacket — Light Wash, Cropped … +4 more
      →    7 match(es)
[3] select_item
      out: 90s Leather Bomber — Black ($75.0, depop)
[4] suggest_outfit
      in:  90s Leather Bomber — Black ($75.0, depop)
      out: Buy it. This is a 90s staple that will instantly anchor your wardrobe, and the natural creasing gives it an au…
      →    10 wardrobe item(s)
[5] create_fit_card
      in:  90s Leather Bomber — Black ($75.0, depop)
      out: Scored this vintage 90s leather bomber on depop for $75 and it has the absolute best worn-in look. It comes in…
```




CRITERION 4
### Proper fit card description with price,size, and platform

- Query: `low-rise cargo pants`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Low-Rise Cargo Pants — Khaki ($27.0, poshmark)
- search_results: 3

Outfit suggestion:

```
Outfit 1: Pair the khaki cargo pants with your white ribbed tank top and the black cropped zip hoodie layered over it, keeping the hoodie unzipped to show off the low-rise waist. Add the chunky white sneakers and the black crossbody bag to complete an authentic early-2000s streetwear look that works great for casual weekend errands or meeting friends for coffee.

Outfit 2: Lean into the oversized Y2K skater silhouette by wearing the cargos with your oversized grey crewneck sweatshirt dropping low over the waistband, and lace up your black combat boots over the distressed hems. Throw on the vintage black denim jacket and sling the black crossbody bag across your chest for an edgy, comfortable outfit tailored for going to a casual outdoor concert or a casual Friday hangout.
```

Fit card:

```
Scored these ultimate Y2K cargos over on Poshmark for just $27 and I am so obsessed with the early-2000s streetwear vibe. They are a size W29 with the coolest distressed hems and way too many pockets. I love throwing them on with a cropped zip hoodie and chunky sneakers for the easiest weekend coffee run outfit.
```

Trace:

```
[1] parse_query
      in:  low-rise cargo pants
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 3 items: Low-Rise Cargo Pants — Khaki, Corduroy Wide-Leg Pants — Rust, Low-Top Canvas Sneakers — Off-White
      →    3 match(es)
[3] select_item
      out: Low-Rise Cargo Pants — Khaki ($27.0, poshmark)
[4] suggest_outfit
      in:  Low-Rise Cargo Pants — Khaki ($27.0, poshmark)
      out: Outfit 1: Pair the khaki cargo pants with your white ribbed tank top and the black cropped zip hoodie layered …
      →    10 wardrobe item(s)
[5] create_fit_card
      in:  Low-Rise Cargo Pants — Khaki ($27.0, poshmark)
      out: Scored these ultimate Y2K cargos over on Poshmark for just $27 and I am so obsessed with the early-2000s stree…
```



CRITERION 5 TRY
### Proper price ceiling

- Query: `Sneakers under $25`
- Wardrobe: example

**Try 1**

- stopped early: yes — The model couldn't be reached, so the outfit and caption steps didn't run. The search worked — 1 listing(s) were found. Check GEMINI_API_KEY in your .env, then run the same query again.
What the service said: Couldn't reach the model: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- selected_item: Low-Top Canvas Sneakers — Off-White ($20.0, poshmark)
- search_results: 1

Trace:

```
[1] parse_query
      in:  Sneakers under $25
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 1 items: Low-Top Canvas Sneakers — Off-White
      →    1 match(es)
[3] select_item
      out: Low-Top Canvas Sneakers — Off-White ($20.0, poshmark)
[4] model unavailable
      →    stopping, search results kept
```
---




## Verdicts and Diagnoses

<!-- MET or MISSED per criterion against LAST UNIT's target, plus a sentence on
     how you decided.

     Then, for every miss: which of the four places it happened — a tool, the
     loop's branch, the session, or the model's output — AND the mechanism.

     Not a diagnosis:  "The fit card was bad."
     A diagnosis:      "The fit card criterion missed on 2 of 5 items. Both had
                        an empty brand field. My prompt puts the brand in the
                        first sentence, so the card opened with a blank and read
                        like a fragment. The tool worked; the prompt assumed a
                        field that isn't always there."

     Look for a pattern. Three misses on the same tool is one problem, not
     three. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | matching query completes | 4 of 5 | MET | A try would be considered as passed if the trace reached step 5, the create_fit_card tool, and the fit card in the session was not empty. All 5 runs had reached all steps and had a fit card.|
| 2 | impossible query stops early | 5 of 5 | MET | A try that would end in the 3rd trace, showing that no outfit appeared, and suggesting what to properly search for would be considered a pass. Each run stopped at the 3rd trace and did not suggest anything since nothign was returned for the outfit. |
| 3 | Consistent selected item ID  | 5 of 5 | MISSED | A try passed if the item on the select_item matched the input lines of both suggest_outfit and create_fit_card. Tries 4 and 5 never ran create_fit_card, so they were a miss. |
| 4 | Proper fit card description with price, size, and platform  | 4 of 5 | MISSED | A try passed if the results had a price,size, and platform. Tries 2,3, and 5 produced no card because the model could not run.   |
| 5 | Proper price ceiling  | 5 of 5 | MET | A try passed if every listing in the search had a price at or below the ceiling price. Each run met the criteria. |


**Diagnoses**
Criterion 3 (Consistent selected item ID). Missed 2 of 5
- The step: Model's Output
- The Mechanism: in tries 4 and 5, the model call inside create_fit_card returned 503 UNAVAILABLE. The generate.py model gave up instead of retrying, which caused both tries to fail.


Criterion 4(Proper fit card description with price,size, and platfomr). Passed 2 of 5 tries.
- The step: Model's Output
- The Mechanism: In tried 2,3, and 5 the model ALSO returned 503 Unavailable. The generate.py model gave up instead of trying for this case also, so the run ended with fit_card set to None. The agent did not survive the temporary model outage.

Both of these Criteria missed because of ONE reason, which was the Model's Output. This means that the pattern for both of these misses is the agent giving up instead of trying again.
---

## Loop Trace


<!-- One full run, printed step by step, with the MCP call visible in it.

     `python app.py ask '...' --trace` once you've added the trace.step()
     calls in Milestone 2.

     Worth pasting BOTH the happy path and the empty-search path. The empty
     one should be visibly shorter, because it stops. If your two traces are
     the same length, your branch isn't working — and this is the fastest way
     anyone will ever find that out. -->

**Happy path**

```
python app.py ask 'Vintage crewneck for under $25' --trace
[1] parse_query
      in:  Vintage crewneck for under $25
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Oversized Crewneck Sweatshirt — Vintage Navy, Oversized College Crewneck — Faded Red, Y2K Baby Tee — Butterfly Print … +7 more
      →    10 match(es)
[3] select_item
      out: Oversized Crewneck Sweatshirt — Vintage Navy ($20.0, thredUp)
[4] suggest_outfit
      in:  Oversized Crewneck Sweatshirt — Vintage Navy ($20.0, thredUp)
      out: Buy it. A genuine vintage navy crewneck is a foundational piece that adds great texture, and since your other …
      →    10 wardrobe item(s)
[5] create_fit_card
      in:  Oversized Crewneck Sweatshirt — Vintage Navy ($20.0, thredUp)
      out: Scored this vintage navy crewneck on thredUp for just $20 and it's already my new favorite basic. It came in s…

  Found:    Oversized Crewneck Sweatshirt — Vintage Navy — $20.0 on thredUp

  Outfit:   Buy it. A genuine vintage navy crewneck is a foundational piece that adds great texture, and since your other grey sweatshirt is extra long, this will give you a different silhouette. 

Outfit 1:
Pair the navy sweatshirt with your wide-leg khaki trousers, cinched with the brown leather belt, and finish with chunky white sneakers. Layer the white ribbed tank underneath so just the hem and collar peek out for subtle contrast. This is effortless and put-together, perfect for casual coffee runs, running errands, or a relaxed day of working from a cafe.

Outfit 2:
Tuck the front of the navy sweatshirt loosely into your dark wash baggy straight-leg jeans, add the black crossbody bag, and lace up your black combat boots. Throw your vintage black denim jacket on top for extra warmth and texture. It is a sharp, vintage-leaning casual look that works well for weekend hangouts, casual dinners, or going to a concert.

  Fit card: Scored this vintage navy crewneck on thredUp for just $20 and it's already my new favorite basic. It came in size XL (fits oversized) and has that real, perfectly faded look you can't fake. I'm planning to layer it over a white tank with khaki trousers for coffee runs, or pair it with baggy jeans and combat boots for weekend concerts.
```

**Empty search**

```
python app.py ask '...' --trace
[1] parse_query
      in:  ...
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    0 match(es)
[3] branch
      →    search returned []: stopping before suggest_outfit

  Nothing in the listings matched description '...'.
Things to change: try broader words — 'jacket' finds more than 'cropped corduroy jacket'.
```

**On the MCP move:** <!-- what changed in your code, and whether anything
behaved differently afterwards. If the rewire didn't work, say exactly where it
broke — the error text and the last thing that worked. That earns the point in
full. -->

I registered `search_listings` in `mcp_server.py` with `@mcp.tool()`, typed as `description: str`, `size: str | None`, `max_price: float | None`, and it hands off to the real implementation in `tools.py`. In `agent.py::run_agent` the direct call `search_listings(...)` became `call_tool("search_listings", {...})` from `mcp_client.py`, and the trace step is labelled `search_listings (via MCP)` so the seam is visible. `python mcp_client.py` lists the tool with the right types. Nothing behaved differently afterwards: the same queries returned the same lists of dicts, the first result was the same item every time, and the branch rule still fires on an empty list. The one gap is that the server reports no description for the tool, because my docstring sits after the function body instead of inside it, so FastMCP never sees it. That is in What's Still Broken.



---

## The Improvement

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:**
Added 503 to the list of errors that generate.py is willing to retry.

**Which failure it was meant to fix:**
Meant to handle the 503 UNAVAILABLE that was returned on criteria 3 and 4. The model returned 503 UNAVAILABLE and generate.py gave up on the first try, rather than trying again. This change makes it retry the failed model call if there is an outage or a 'high demand' message.

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1.  | matching query completes | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET(5/5) |
| 2.  | impossible query stops early | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET(5/5) |
| 3.  | Consistent selected item ID | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET(5/5) |
| 4.  | Proper fit card description with price, size, and platform | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET(5/5) |
| 5.  | Proper price ceiling | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET(5/5) |

**Did it help, and how do I know:**

<!-- If it made things worse, say that. Honestly reported, that earns full
     credit and is more interesting than one that worked. -->
The change did help. Criterion 3 went from 3/5 to 5/5, and criterion 4 went from 2/5 to 5/5 with the same scenarios. I also did a second after run to see if it scored the same.


After the improvement, I decided to rerun 8 new scenarios covering the criteria I added. The results are found in results (results/run_2026-10-08_1309_diagnostic.md). The 503 UNAVAILABLE error came back in two tries of the leather bomber scenario. The outage lasted longer than 5 attempts, which made the model return the 503. The generate.py raised a RunTimeError instead of a ModelUnavailable, so the run crashed rather than returning the "model couldnt be reached" message.


---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->

Short outages were handled better, but longer outages got worse. An outage that takes more than 5 attempts now crashes the agent instead of returning an error message. A fix would be to raise the ModelUnavailable so the existing handler catches it. I stopped because this is a second change in which I would need to do its own before and after, but due to time constraints I could not.

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
