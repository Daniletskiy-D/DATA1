#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("citati.txt", "r") as file:
        text = file.read()

    quotes = []
    quote = ""
    in_quote = False

    for char in text:
        if char == '"':
            if in_quote:
                quotes.append(quote)
                quote = ""
                in_quote = False
            else:
                in_quote = True
        elif in_quote:
            quote += char

    for q in quotes:
        print(q)
