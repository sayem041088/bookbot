def get_num_words(path):
    word_count = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            words=line.split()
            word_count += len(words)
        return f"Found {word_count} total words"
            
def get_char_count(path):
    char_counts = {}
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line.lower():   # lowercase to treat 'A' and 'a' the same
                if char.isalpha():      # count only letters
                    char_counts[char] = char_counts.get(char, 0) + 1
        sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        return sorted_char_counts