from tools import compare_listings
"""This is a file to test the Criterion 3 of the project, which is to ensure that compare_listings()
    returns the correct highest scored listing.
"""
cases = [
    (
        [
            {"id": "a", "condition": "fair", "price": 20},
            {"id": "b", "condition": "excellent", "price": 40},
        ],
        "b",
    ),
    (
        [
            {"id": "a", "condition": "good", "price": 20},
            {"id": "b", "condition": "fair", "price": 50},
        ],
        "a",
    ),
    (
        [
            {"id": "first", "condition": "good", "price": 20},
            {"id": "second", "condition": "excellent", "price": 40},
        ],
        "first",
    ),
]

for listings, expected_id in cases:
    selected = compare_listings(listings)
    assert selected["id"] == expected_id

print("Criterion 3: PASS — 3/3")