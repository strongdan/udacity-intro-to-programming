def word_in_pos(blank, parts_of_sample):
    for pos in parts_of_sample:
        if pos in blank:
            return pos
    return None

def play_game(text, blanks):
    replaced = []
    for word in text:
        replacement = word_in_pos(sample, blanks_to_fill)
        if replacement != None:
            n = 0
            blank_nr = 1
            while n < len(answer):
                user_answer = raw_input("What should go in the blank nr." + blank_nr + "?")
                if user_answer == answer[n]:
                    n += 1
                    blank_nr += 1
                    word = word.replace(replacement, user_answer)
                    replaced.append(word)
                else:
                    print "This is not the correct answer. Try again"
                    replaced.append(word)
            replaced = " ".join(replaced)
            return replaced
  
