from src.cleaner import cleaner

def test_clean_quotes_strips_spaces_and_quotes():
    raw_data = [{ "author": " Author ", "quote": "“  Hello world!  ”"}]

    result = cleaner(raw_data)

    assert result == [{"author": "Author", "quote": "Hello world!"}]

def test_clean_quotes_removes_duplicates_and_empty_records():
    raw_data = [
        {"author": " Author ", "quote": "“  Hello world!  ”"},
        {"author": "", "quote": "“  Hello world!  ”"},
        {"author": " Author  ", "quote": "“  Hello python!  ”"},
        {"author": " Author ", "quote": "“  Hello world!  ”"}    
    ]

    result = cleaner(raw_data)

    assert result == [
        {"author": "Author", "quote": "Hello world!"},
        {"author": "Author", "quote": "Hello python!"}
    ]