from_base = [
    {
        'type': "input",
        "name": "word",
        "message": "Which word to start from?"
    },
    {
        'type': "input",
        "name": "mask",
        "message": "How was it masked? Options: B(lack), O(range), G(reen)"
    }
]

yes_no = [
    {
        'type': 'list',
        'name': 'accepted',
        'message': 'Was this word accepted?',
        'choices': ["yes","no"]
    }
]

how_masked = [
    {
        'type': "input",
        "name": "mask",
        "message": "How was it masked? Options: B(lack), O(range), G(reen)"
    }
]