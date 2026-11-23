
# NOTE SORTER

BOXES = {
    "Sports": "the team won the football match and the crowd cheered the goal "
              "she runs fast in the race and wins the gold medal for the team",

    "Food": "we cook pasta with tomato sauce and the soup is hot "
            "he bakes bread and the cake tastes sweet with cream",

    "Music": "the band plays a loud song and the singer sings with the guitar "
             "she learns the piano and sings a song in the choir",
}

TEST_NOTES = [
    ("the goal won the match", "Sports"),
    ("he bakes the cake and the bread", "Food"),
    ("the singer plays the guitar", "Music"),
    ("pasta with sweet cream", "Food"),
    ("the band wins the match", "Music"),
    ("", "unknown"),
]

THRESHOLD = 0.2


# PART 1: COUNT WORDS
def word_counts(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


PROFILES = {
    box: word_counts(text)
    for box, text in BOXES.items()
}


# PART 2: COSINE SIMILARITY
def cosine(a, b):
    dot = sum(a[word] * b.get(word, 0) for word in a)

    size_a = sum(x * x for x in a.values()) ** 0.5
    size_b = sum(x * x for x in b.values()) ** 0.5

    if size_a == 0 or size_b == 0:
        return 0.0

    return dot / (size_a * size_b)


# PART 3: CLASSIFY NOTES
def classify(note):
    note_counts = word_counts(note)

    best_box = "unknown"
    best_score = 0.0

    for box, profile in PROFILES.items():
        score = cosine(note_counts, profile)

        if score > best_score:
            best_score = score
            best_box = box

    if best_score < THRESHOLD:
        return "unknown"

    return best_box


# PART 4: MAIN FUNCTION
def main():

    print("PART 1: Word counts")
    print(PROFILES["Food"].get("the", 0),
          PROFILES["Food"].get("goal", 0))

    print("\nPART 2: Cosine")
    print(round(
        cosine(word_counts("the team"), PROFILES["Sports"]), 2
    ))

    print("\nPART 3: Classify")
    print(classify("the goal won the match"), "|",
          classify("zzz"))

    print("\nPART 4: Test all notes")

    mistakes = 0

    for note, wanted in TEST_NOTES:
        answer = classify(note)

        if answer != wanted:
            mistakes += 1

        print(answer, "|", note)

    print("Mistakes:", mistakes, "out of", len(TEST_NOTES))


# MAIN GUARD
if __name__ == "__main__":
    main()
