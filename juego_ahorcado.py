import random as r
import os

menu = """
 /$$   /$$                                               /$$        /$$$$$$                                   
| $$  | $$                                              | $$       /$$__  $$                                  
| $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$      | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$$$$$$$ |____  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$      | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  | $$      | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$  | $$      | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
|__/  |__/ \_______/|__/  |__/ \____  $$ \_______/ \_______/       \______/  \_______/|__/ |__/ |__/ \_______/
                               /$$  \ $$                                                                      
                              |  $$$$$$/                                                                      
                               \______/    
                                            by Edison Avila

"""
hanged_player_array = ("""
            ||                 ||
            ||                 ||
            ||                 ||
            ||                 ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
"""
            ||        O        ||
            ||                 ||
            ||                 ||
            ||                 ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
"""
            ||        O        ||
            ||        |        ||
            ||                 ||
            ||                 ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
"""
            ||        O        ||
            ||       /|        ||
            ||                 ||
            ||                 ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
"""
            ||        O        ||
            ||       /|\\       ||
            ||                 ||
            ||                 ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
"""
            ||        O        ||
            ||       /|\\       ||
            ||        |        ||
            ||                 ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
"""
            ||        O        ||
            ||       /|\\       ||
            ||        |        ||
            ||       /         ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
"""
            ||        O        ||
            ||       /|\\       ||
            ||        |        ||
            ||       / \\       ||
            ||                 ||
            ||TTTTTTTTTTTTTTTTT||
""",
)


def choose_word(lv, words_array):
    level_words = [element[0] for element in words_array if element[1] >= lv[0] and element[1] <= lv[1] ]

    word = r.choice(level_words)

    return word


def which_levels(array):
    return [array[0],array[len(array)//3],array[(len(array)//3)*2],array[-1]]


def check_word(word):
    
    CONV = {
        'Ã¡': 'a',
        'Ã©': 'e',
        'Ã­': 'i',
        'Ã³': 'o',
        'Ãº': 'u',
        'Ã±': 'ñ',
        '\n': '',
    }

    for keys, values in CONV.items():
        word = word.replace(keys, values)
    # print(word)
    return word


def read_file():
    words = []
    with open("./data.txt", "r", encoding="utf-8") as r:
        for line in r:
            value = check_word(line)
            words.append((value, len(value)))
    return words


def display_menu(levels_array):
    limits = {
        'b': (levels_array[0], levels_array[1]),
        'm': (levels_array[1]+1, levels_array[2]),
        'a': (levels_array[2]+1, levels_array[3]),
    }
    
    hanged_player_menu = f"""
            ||========|
            ||        |
            ||        |                          Niveles de dificultad:
            ||        O                                 (b)bajo    {levels_array[0]} a {levels_array[1]}  letters
            ||       /|\\                                (m)medio   {levels_array[1]+1} a {levels_array[2]}  letters
            ||        |                                 (a)alto    {levels_array[2]+1} a {levels_array[3]} letters 
            ||       / \\
            ||
    """
    level_user_input = input(f'{menu}\n{hanged_player_menu}        ||===============                   Ingresa el nivel de dificultad: ').lower()

    if level_user_input == 'b' or level_user_input == 'm' or level_user_input == 'a':
        return limits[level_user_input]
    
    os.system("clear")
    display_menu(levels_array)


def validate_word(word, first_display, user_letter="", current_display=""):
    ## posibilidad de array de letras usadas
    fail = False
    win = False

    if first_display:
        
        word_array = "_ " * len(word)

    else:
        used_chars.append(user_letter) ## agregar letra al array 
        if user_letter in word :
            ## Verificar cuales letras estan dentro de la palabra
            ## La letra no puede ser repetida
            temp = []
            for letter in word:
                if letter in used_chars:
                    temp.append(letter)
                else:
                    temp.append("_")
            word_array = " ".join(temp)
            if not("_" in word_array):
                win = True
        else:
            fail = True
            word_array = current_display

    return [word_array, fail, win] ## Retorna array de juego && si fallo o no


def playground(word):
    os.system("clear")
    counter = 0
    message = "¡Adivina la palabra!"
    word_array = validate_word(word,True)
    while counter != len(hanged_player_array) -1 :

        ## falta actualizar word_array y la condicion de fallo
        header_player = f"""
            ||========|========||    {message}
            ||        |        ||     
            ||        |        ||    {word_array[0]}              Letras usadas {used_chars}"""

        user_letter = input(f'{menu}\n{header_player}{hanged_player_array[counter]}                                     Ingresa una letra: ').lower()
        
        os.system("clear")
        word_array = validate_word(word,False,user_letter,word_array[0]) ## Retorna array de juego && si fallo o no (False = no fallo; True = fallo)
        if word_array[1]:
            counter += 1
        if word_array[2]:
            break

    if word_array[1]:
        ## si sale del while pierde la partida
        header_player = f"""
            ||========|========||    ¡¡¡Perdiste!!! la palabra era:
            ||        |        ||     
            ||        |        ||    {word}"""
    if word_array[2]:
        header_player = f"""
            ||========|========||    ¡¡¡Ganaste!!! la palabra era:
            ||        |        ||     
            ||        |        ||    {word}"""
    replay = input(f'{menu}\n{header_player}{hanged_player_array[counter]}                                      ¿Quieres volver a jugar? (y / n): ')
    if replay == 'y':
        main()


def main():
    
    global used_chars
    used_chars = []

    os.system("clear")

    words_array = read_file() ## [(word, len),(word2, len2),...]
    len_words = list(set([values[1] for values in words_array])) ## [3, 4, 5, 6, 7, 8, 9, 10, 11, 12] len_words
    
    posible_levels = which_levels(len_words) ## [3,6,9,12] -> [low, mid, max]

    level = display_menu(posible_levels)

    play_word = choose_word(level,words_array)

    playground(play_word)

    # list(enumerate(words_array[1][0])) ## [(0, 'c'), (1, 'a'), (2, 'f'), (3, 'e')]



if __name__ == "__main__":
    main()