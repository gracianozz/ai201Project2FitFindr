from tools import compare_listings
"""This is a file to test the Criterion 3 of the project, which is to ensure that compare_listings()
    returns the correct highest scored listing.
"""
cases = [
    (
        [
            {
                "id": "a",
                "title": "Graphic Tee A",
                "category": "tops",
                "condition": "fair",
                "price": 20,
            },
            {
                "id": "b",
                "title": "Graphic Tee B",
                "category": "tops",
                "condition": "excellent",
                "price": 40,
            },
        ],
        "b",
    ),
    (
        [
            {
                "id": "a",
                "title": "Graphic Tee A",
                "category": "tops",
                "condition": "good",
                "price": 20,
            },
            {
                "id": "b",
                "title": "Graphic Tee B",
                "category": "tops",
                "condition": "fair",
                "price": 50,
            },
        ],
        "a",
    ),
    (
        [
            {
                "id": "first",
                "title": "Graphic Tee First",
                "category": "tops",
                "condition": "good",
                "price": 20,
            },
            {
                "id": "second",
                "title": "Graphic Tee Second",
                "category": "tops",
                "condition": "excellent",
                "price": 40,
            },
        ],
        "first",
    ),
]

for listings, expected_id in cases:
    selected = compare_listings(listings, "graphic tee")
    assert selected["id"] == expected_id

print("Criterion 3: PASS — 3/3")