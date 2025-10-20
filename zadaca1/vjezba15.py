def count_vowels_consonants(text):
    text = text.lower() 
    vowels = "aeiou"
    result = {"samoglasnici": 0, "suglasnici": 0}

    for char in text:
        if char.isalpha(): 
            if char in vowels:
                result["samoglasnici"] += 1
            else:
                result["suglasnici"] += 1

    return result

text="Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(text))
