from project import library_status, borrow, return_book
import csv
import pytest

username = 'jag'


def test_library_status(monkeypatch, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "Y")

    try:
        library_status()
    except SystemExit:
        pass

    captured = capsys.readouterr().out

    assert "All Tomorrows (C.M. Kosemen | 2006)" in captured

def test_borrow(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "3")

    with pytest.raises(SystemExit):
        borrow(username)

    with open("books.csv", "r") as bookscsv:
        books = list(csv.DictReader(bookscsv))
    assert books[2]["Borrowed by"] == username

def test_return_book(monkeypatch):

    with open("books.csv", "r") as bookscsv:
        books = list(csv.DictReader(bookscsv))
    for book in books:
        if book["ID"] == '1':
            book["Borrowed by"] = username

    with open("books.csv", "w") as bookscsv:

        fieldnames = ["ID", "Category", "Details", "Borrowed by"]
        writer = csv.DictWriter(bookscsv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    input = iter(["1"])
    monkeypatch.setattr('builtins.input', lambda _: next(input, "4"))

    try:
        return_book(username)
    except SystemExit:
        pass

    with open("books.csv", "r") as bookscsv:
        books = list(csv.DictReader(bookscsv))
    assert books[0]["Borrowed by"] == 'N/A'
