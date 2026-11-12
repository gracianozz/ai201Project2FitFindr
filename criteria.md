# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

---

## 1. A matching query completes all FOUR tools

Given a query that matches at least one listing, the agent completes all FOUR tool calls and returns a fit card — in at least 2 of 3 runs.

**Why this target:**

- A search can be vague or plain, which can mean that some words wont be detected.

---

## 2. A bad query stops before the compare_listings() tool.

Given a query that matches no listings, the agent returns an error message,
does not call `compare_listings()`, `suggest_outfit()`, or `create_fit_card()`,
and stops safely in 3 of 3 runs.

**Why this target:**
- The 3 tools do not function without no listings, so the system should stop there every time, instead of making up or generating information.

---

## 3. compare_listings() calculates the combined score accurately

After scoring each listing returned from search_listings(), compare_listings() chooses the listing with the highest score, in 3 of 3 runs.

**Why this target:**
- This ensures the new extension is working as described, and it chooses the top choice with the highest score each time, instead of just the first option in the list as the original system did.



---

## 4. Selected Item has relevance
For 3 runs with clear item types or styles, the user can evaluate whether the listing after compare_listings() is a reasonable match for the original request. The criterion passes when the selected item is relevant to their query, in 3 of 3 runs.

**Why this target:**
- A listing that has the highest price and condition score needs can still have the possibility of being an irrelevant or mismatch to what the user requested. This helps verify that the user is getting the best realistic match instead of just choosing the cheapest high-condition item.


---

## 5. The selected listing is passed consistently

For every successful query, the listing that is selected in compare_listings() has the same ID as the item passed to the later tools suggest_outfit() and create_fit_card(), in 3 of 3 runs.


**Why this target:**
- This ensures that the new tool is properly being worked with the other tools, and ensures smooth flow when a query is passed through.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
