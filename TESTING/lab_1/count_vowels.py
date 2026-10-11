def count_vowels(text: str) -> int:
    vowels = "aeiouаеєиіїоуюя"
    count = 0
    for i in text.lower():
        if i in vowels:
            count += 1
            
    return count