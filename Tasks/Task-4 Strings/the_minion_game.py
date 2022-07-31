def minion_game(string):
    # your code goes here
    vowels = "AEIOU"

    pts_kevin = 0
    pts_stuart = 0

    for pts, letter in enumerate(reversed(string), start=1):
        if letter.upper() in vowels:
            pts_kevin += pts
        else:
            pts_stuart += pts

    if pts_kevin > pts_stuart:
        print(f"Kevin {pts_kevin}")
    elif pts_stuart > pts_kevin:
        print(f"Stuart {pts_stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
