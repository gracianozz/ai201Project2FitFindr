"""
The runs your test needs. ← UNIT 4, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
the empty-search branch needs an impossible query. One about the fit card needs
the same item run more than once. Working that out is Milestone 3's first step,
and this file is where you write it down.

`run_eval.py` runs everything here five times and writes the run log — five
because your criteria are written out of five.

Three scenarios are filled in to show the shape. Add or change whatever your
own criteria need — these are a starting point, not a fixed set.
"""

SCENARIOS = [
    {
        # A query the data can match. Criterion 1.
        "name": "matching query completes",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "criterion": 1,
    },
    {
        # A query nothing can match. Criterion 2 — the branch.
        "name": "impossible query stops early",
        "query": "designer ballgown size XXS under $5",
        "wardrobe": "example",
        "criterion": 2,
    },

    # ── Scenarios 3–6 from the Before/After runs. Commented out for the
    # diagnostic run so they aren't measured a third time — uncomment when done.
    # {
    #     # A user with nothing saved. One of unit 4's three failure modes.
    #     "name": "empty wardrobe",
    #     "query": "denim jacket under $50",
    #     "wardrobe": "empty",
    #     "criterion": None,
    # },
    # # Criterion 3 Scenario
    # {
    #     "name": "Consistent selected item ID",
    #     "query": "leather bomber jacket under $100",
    #     "wardrobe": "example",
    #     "criterion": 3,
    # },
    # # Criterion 4 Scenario
    # {
    #     "name": "Proper fit card description with price,size, and platform",
    #     "query": "low-rise cargo pants",
    #     "wardrobe": "example",
    #     "criterion": 4,
    # },
    # # Criterion 5 Scenario
    # {
    #     "name": "Proper price ceiling",
    #     "query": "Sneakers under $25",
    #     "wardrobe": "example",
    #     "criterion": 5,
    # },

    # Extra scenarios to press the system and try to break it.
    {
        "name": "fit card: leather bomber (M, $75, depop)",
        "query": "leather bomber jacket",
        "wardrobe": "example",
        "criterion": 4,
    },
    {
        "name": "fit card: chelsea boots (US 8.5, $44, poshmark)",
        "query": "suede chelsea boots",
        "wardrobe": "example",
        "criterion": 4,
    },
    {
        "name": "fit card: bucket hat (One Size, $14, thredUp)",
        "query": "bucket hat",
        "wardrobe": "example",
        "criterion": 4,
    },
    {
        "name": "fit card: knit cardigan (One Size / Oversized, $35, depop)",
        "query": "knit cardigan",
        "wardrobe": "example",
        "criterion": 4,
    },
    {
        "name": "price ceiling: denim jacket under $50 (7 results, max $45)",
        "query": "denim jacket under $50",
        "wardrobe": "example",
        "criterion": 5,
    },
    {
        "name": "price ceiling: vintage tee under $0 (0 results, max $0)",
        "query": "vintage tee under $0",
        "wardrobe": "example",
        "criterion": 5,
    },
    {
        "name": "parser: trailing size shortcut",
        "query": "graphic tee, L",
        "wardrobe": "example",
        "criterion": None,
    },
    {
        "name": "parser: ceiling with no dollar sign (expected to be ignored)",
        "query": "tee under 30",
        "wardrobe": "example",
        "criterion": None,
    },

    # TODO: add what your criteria 3, 4 and 5 need.
    #
    # Set "criterion" to the number in criteria.md that the scenario tests.
    # "criterion": None means a diagnostic run — useful to have, but it isn't
    # one of your five, and run_eval.py marks it as such in the table.
    #
    # For a state criterion, any normal query works — what you're checking is
    # what ends up in the session, not what the user typed.
    #
    # For a fit-card criterion, you probably want the SAME query listed more
    # than once, or several different items, depending on what your criterion
    # actually says.
]

WARDROBES = ("example", "empty")


def validate() -> list[str]:
    """Complain about anything malformed, before a long run rather than during."""
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("query", "").strip():
            problems.append(f"scenario {i} has no query")
        if scenario.get("wardrobe") not in WARDROBES:
            problems.append(
                f"scenario {i} has wardrobe {scenario.get('wardrobe')!r} — "
                f"it should be one of {WARDROBES}"
            )
    return problems
