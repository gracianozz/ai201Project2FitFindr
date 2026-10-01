"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import re

import config  # noqa: F401 — you'll use this in search_listings
from generate import generate
from utils.data_loader import load_listings


# ── Tool 1: search_listings ───────────────────────────────────────────────────

STOPWORDS = {
    
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "he", "in", "is", "it", "its", "of", "on", "that",
    "the", "to", "was", "were", "will", "with", "i", "you", "your", 
    "my", "me", "we", "us",
}


def keywords(text: str) -> set[str]:
    """Lowercase words worth matching on, stopwords removed"""
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    return {w for w in words if w not in STOPWORDS and len(w) > 1}


def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search the listings data for items matching a description, and optionally a
    size and a price ceiling.

    This is the tool that doesn't call the model, which makes it the easiest one
    to test and the one to move onto MCP in unit 4.

    Args:
        description: keywords describing what the user wants
                     (e.g. "vintage graphic tee").
        size:        a size string to filter by, or None to skip size filtering.
                     Match case-insensitively — "M" should match "S/M".

                     ⚠️ Read the sizes in the data before you reach for a plain
                     substring test. `"s" in "us 9"` is True, and so is
                     `"l" in "xl"`. A filter that returns shoes when someone
                     asked for a small top reads like a broken search, and it
                     will quietly cost you in unit 4 when you test criterion 1.
                     What counts as a size match is part of your spec — decide
                     it and write it into your Tool Inventory.
        max_price:   maximum price, inclusive, or None to skip price filtering.

    Returns:
        A list of matching listing dicts, best match first.
        **Returns an empty list when nothing matches — an empty list, not None,
        and not an exception.** Your loop branches on this.

    Each listing dict has these fields:
        id, title, description, category, style_tags (list), size,
        condition, price (float), colors (list), brand (str or None), platform

    Note that `brand` is None for most listings. That is deliberate and
    realistic — thrift listings often have no brand. If something you write
    assumes a brand is always there, you will find out in unit 4.

    TODO:
        1. Load every listing with load_listings().
        2. Filter by max_price and by size, when each is provided.
        3. Score what's left by keyword overlap with `description`.
        4. Drop anything scoring zero.
        5. Sort by score, highest first, and return the listing dicts —
           at most config.SEARCH_RESULT_LIMIT of them.

    Test it from a terminal before you move on:
        python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
    """
    # TODO: replace this with your implementation
    query_words = keywords(description)
    if not query_words:
        return []

    # Normalise the wanted size once: uppercase, no spaces, so "us 9" and
    # "US 9" both become "US9" and compare equal to the listing's "US9".
    wanted_size = re.sub(r"\s+", "", size.upper()) if size else None

    scored: list[tuple[int, dict]] = []
    for listing in load_listings():
        # 1. Price ceiling, inclusive.
        if max_price is not None and listing["price"] > max_price:
            continue

        # 2. Size. Strip notes in parentheses, then split the label into its
        #    parts so we compare whole sizes, not substrings ("S" must not
        #    match "US 9", and "L" must not match "XL").
        if wanted_size:
            label = re.sub(r"\([^)]*\)", " ", listing["size"]).upper()
            if "ONE SIZE" not in label:
                label = re.sub(r"US\s+", "US", label)       # "US 9" -> "US9"
                parts = {p for p in re.split(r"[/\s]+", label) if p}
                if wanted_size not in parts:
                    continue

        # 3. Score by keyword overlap across everything worth matching on.
        haystack = " ".join(
            [
                listing["title"],
                listing["description"],
                listing["category"],
                listing["brand"] or "",
                " ".join(listing["style_tags"]),
                " ".join(listing["colors"]),
            ]
        )
        score = len(query_words & keywords(haystack))

        # 4. Drop anything that matched no words at all.
        if score == 0:
            continue
        scored.append((score, listing))

    # 5. Highest score first.
    scored.sort(key=lambda entry: entry[0], reverse=True)
    return [listing for _, listing in scored[: config.SEARCH_RESULT_LIMIT]]


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
    """
    Given a thrifted item and the user's wardrobe, suggest one or two outfits.

    This one calls the model, through `generate()`. You don't need to think
    about rate limits — the adapter handles pacing for you.

    Args:
        new_item: a listing dict — the item the user is considering.
        wardrobe: a wardrobe dict with an 'items' key holding a list of items.
                  **It may be empty.** Handle that.

    Returns:
        A non-empty string with outfit suggestions.
        With an empty wardrobe, return general styling advice rather than
        raising or returning "". Unit 4 has you trigger the empty wardrobe on
        purpose, so decide now what it should do.

    TODO:
        1. Check whether wardrobe['items'] is empty.
        2. If it is, ask the model for general styling ideas for this item.
        3. If it isn't, format the wardrobe items into the prompt and ask for
           specific combinations naming pieces the user already owns.
        4. Return the model's response.

    Test it from a terminal before you move on:
        python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"
    """
    # TODO: replace this with your implementation

    # Describe the thrifted item once, in plain lines the model can read.
    item_text = "\n".join(
        [
            f"Item: {new_item['title']}",
            f"Description: {new_item['description']}",
            f"Category: {new_item['category']}",
            f"Colors: {', '.join(new_item['colors'])}",
            f"Style: {', '.join(new_item['style_tags'])}",
            f"Brand: {new_item['brand'] or 'unbranded'}",
        ]
    )

    system = (
        "You are a personal stylist helping someone decide whether a thrifted "
        "item is worth buying. Be concrete and specific. Keep it to one or two "
        "outfits, a few sentences each, in plain text."
    )

    # 1. Check whether the wardrobe is empty.
    items = (wardrobe or {}).get("items") or []

    if not items:
        # 2. Nothing to combine with — ask for general styling ideas instead.
        prompt = (
            f"{item_text}\n\n"
            "The user has not saved any wardrobe items yet. Suggest one or two "
            "ways to style this item with common pieces most people own, and "
            "say what kind of occasion each outfit suits."
        )
    else:
        # 3. Format the wardrobe so the model can name the pieces the user owns.
        wardrobe_lines = []
        for piece in items:
            line = f"- {piece['name']} ({piece['category']}; {', '.join(piece['colors'])})"
            if piece.get("notes"):
                line += f" — {piece['notes']}"
            wardrobe_lines.append(line)
        wardrobe_text = "\n".join(wardrobe_lines)

        prompt = (
            f"{item_text}\n\n"
            f"The user already owns these pieces:\n{wardrobe_text}\n\n"
            "Suggest one or two outfits built around the new item, naming the "
            "specific pieces from their wardrobe to pair it with, and say what "
            "kind of occasion each outfit suits."
        )

    # 4. Return the model's response, never an empty string.
    response = generate(prompt, system=system).strip()
    if not response:
        return (
            f"{new_item['title']} is a versatile {new_item['category']} piece. "
            "Pair it with neutral basics and let it be the focus of the outfit."
        )
    return response


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Write a short caption someone would actually post about the find.

    This calls the model too.

    Args:
        outfit:   the outfit suggestion string from suggest_outfit().
        new_item: the listing dict for the item.

    Returns:
        A two-to-four sentence caption.
        If `outfit` is empty or whitespace, return a descriptive message rather
        than raising.

    The caption should read like a real post rather than a product description,
    mention the item and its price and platform once each, and be specific about
    the vibe.

    It should also come out **differently for different inputs**. If you run
    this three times on the same item and get three word-for-word identical
    strings, it's one of two things, and both are near the top of `config.py`:

        • CACHE_ENABLED — the adapter handed back an answer it already had
        • TEMPERATURE   — at 0.0 the model gives the same words every time

    TODO:
        1. Guard against an empty or whitespace-only `outfit`.
        2. Build a prompt with the item details and the outfit.
        3. Call generate() and return the response.

    Test it from a terminal before you move on:
        python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"
    """
    # TODO: replace this with your implementation

    # 1. Guard: no outfit to write about, so describe the item itself instead
    #    of calling the model with a hole in the prompt.
    if not outfit or not outfit.strip():
        return (
            f"Found a {new_item['title']} on {new_item['platform']} for "
            f"${new_item['price']:g}, size {new_item['size']}, in "
            f"{new_item['condition']} condition. No outfit was suggested for "
            f"it yet, but the {', '.join(new_item['style_tags'])} vibe speaks "
            "for itself."
        )

    # 2. Build the prompt from the item details and the outfit.
    item_text = "\n".join(
        [
            f"Item: {new_item['title']}",
            f"Description: {new_item['description']}",
            f"Price: ${new_item['price']:g}",
            f"Size: {new_item['size']}",
            f"Platform: {new_item['platform']}",
            f"Condition: {new_item['condition']}",
            f"Colors: {', '.join(new_item['colors'])}",
            f"Style: {', '.join(new_item['style_tags'])}",
            f"Brand: {new_item['brand'] or 'unbranded'}",
        ]
    )

    system = (
        "You write short, casual social media captions about thrift finds. "
        "Write in first person like a real post, not a product listing. "
        "Two to four sentences, plain text, no hashtags, no bullet points."
    )

    prompt = (
        f"{item_text}\n\n"
        f"How it will be styled:\n{outfit}\n\n"
        "Write a caption about this find. Mention the item, its price, its "
        "size and the platform it came from, each exactly once. Write the "
        f"price as digits with a dollar sign (${new_item['price']:g}) and the "
        f"size exactly as given ({new_item['size']}), not spelled out or "
        "reformatted. Be specific about the vibe of the outfit."
    )

    # 3. Call the model and return the caption, never an empty string.
    #    cache=False so the same item gets a fresh caption every run — a
    #    caption that repeats word for word is a template, not a post.
    response = generate(prompt, system=system, cache=False).strip()
    if not response:
        return (
            f"Thrifted a {new_item['title']} on {new_item['platform']} for "
            f"${new_item['price']:g} in size {new_item['size']}. Styling it "
            f"with {outfit.strip()}."
        )
    return response
