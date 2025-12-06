import random

def ask_questions(dict):
    dict_keys = list(dict.keys())

    correct_count = 0
    wrong_count = 0

    for j in range(len(dict_keys)):
        word = dict_keys[random.randint(0,len(dict_keys)-1)]
        dict_keys.remove(word)
        finish=0
        while (not finish):
            answer = input(word+"\n>>").upper()
            if answer!='':
                finish=1
        if answer == dict[word].upper():
            print("Correct")
            correct_count += 1
        else:
            print(f"u so stupid, correct answer is {dict[word]}")
            wrong_count += 1

    print(f"Correct: {correct_count}, Wrong: {wrong_count}")
    print(f"Percentage: {correct_count/(correct_count+wrong_count)*100}%")