import tkinter as tk
import random
import time
import sys
from tkinter.messagebox import showinfo, askyesno, showerror

# Author: ubiko
# Version: 0.0.1
# Release Date: 05/02/2022


# Fonts
font1 = ("Goudy Stout", 28)
font2 = ("Britannic Bold", 16)
font2_bigger = ("Britannic Bold", 26)
font3 = ("Eras Demi ITC", 15)  # Berlin Sans FB
font3_smaller = ("Eras Demi ITC", 14)
font4 = ("Britannic Bold", 14)
font5 = ("Eras Demi ITC", 12)
font6 = ("Arial Black", 22)
font7 = ("Berlin Sans FB Demi", 26)
font8 = ("Segoe WP Black", 22)
font9 = ("Segoe WP", 16)

# Colours
colour1 = "#DFDBDB"
colour2 = "#C8C1C0"
colour2_2 = "#B9B8B6"  # DFDEDA
colour3 = "#9F9F9F"  # C2BEBE
colour4 = "#62615E"

# Root window
window_width = 1000
window_height = 600
title_frame_height = 70

window = tk.Tk()
window.geometry(str(window_width) + "x" + str(window_height))
window.resizable(False, False)
window.title("Hangman")

# Graphics
return_arrow_graphic = ""
x_graphic = ""
hangman_graphic = ""


# Cursors
cursor1 = "mouse"

# Variables
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', " "]
current_frame = "main_menu"  # main_menu, game_select, running_game, own_word_game
word_to_guess = ""
entry_width = 40
last_game = ""
special_graphic = False


# Functions
def load_graphics():
    try:
        global return_arrow_graphic
        global x_graphic
        global hangman_graphic
        return_arrow_graphic = tk.PhotoImage(file="./Graphics/return_arrow_resized.png")
        x_graphic = tk.PhotoImage(file="./Graphics/x_resized.png")
        hangman_graphic = tk.PhotoImage(file="./Graphics/Icons/icon_resized.png")
        window.iconbitmap("./Graphics/Icons/icon.ico")
    except tk.TclError:
        showerror("Fehler", "Notwendige Dateien konnten nicht geladen werden. Bitte installieren Sie das Programm neu.")
        window.destroy()
        sys.exit()


load_graphics()


# Frames
end_of_game_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
end_of_game_frame.place(x=0, y=title_frame_height, width=window_width, height=window_height - title_frame_height)

running_game_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
running_game_frame.place(x=0, y=title_frame_height, width=window_width, height=window_height - title_frame_height)

own_word_game_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
own_word_game_frame.place(x=0, y=title_frame_height, width=window_width, height=window_height - title_frame_height)

word_from_list_game_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
word_from_list_game_frame.place(x=0, y=title_frame_height, width=window_width,
                                height=window_height - title_frame_height)

game_select_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
game_select_frame.place(x=0, y=title_frame_height, width=window_width, height=window_height - title_frame_height)

edit_own_list_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
edit_own_list_frame.place(x=0, y=title_frame_height, width=window_width, height=window_height - title_frame_height)

rules_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
rules_frame.place(x=0, y=title_frame_height, width=window_width, height=window_height - title_frame_height)

main_menu_frame = tk.Frame(
    window,
    bg=colour1,
    cursor=cursor1
)
main_menu_frame.place(x=0, y=title_frame_height, width=window_width, height=window_height - title_frame_height)

title_frame = tk.Frame(
    window,
    bg=colour3,
    cursor=cursor1
)
title_frame.place(x=0, y=0, width=window_width, height=title_frame_height)


start_frame = tk.Frame(
    window,
    bg=colour3,
    cursor=cursor1
)
#  start_frame.place(x=0, y=0, width=window_width, height=window_height)


# Functions
def game_select():
    # Goes to the Game Select Frame
    global current_frame
    current_frame = "game_select"
    game_select_frame.lift()


def main_menu():
    # Goes to the Main Menu Frame
    global current_frame
    current_frame = "main_menu"
    main_menu_frame.lift()


def edit_own_list():
    # Goes to the Edit Own List Frame
    clear_entry(entry2)
    invis_wrong_word_label(wrong_word_label2)
    global current_frame
    current_frame = "edit_own_list"
    edit_own_list_frame.lift()


def own_word_game():
    # Goes to the Own Word Game Frame
    global last_game
    last_game = "own_word_game"
    clear_entry(entry1)
    invis_wrong_word_label(wrong_word_label)
    if button_state.get():
        change_show_status()
        cb1.deselect()
    global current_frame
    current_frame = "own_word_game"
    own_word_game_frame.lift()


def word_from_list_game():
    # Goes to the Word from List Frame
    global last_game
    last_game = "word_from_list_game"
    clear_radio_buttons()
    invis_no_option_chosen()
    global current_frame
    current_frame = "word_from_list_game"
    word_from_list_game_frame.lift()


def running_game():
    # Goes to the Running Game Frame
    global current_frame
    current_frame = "running_game"
    running_game_frame.lift()


def end_of_game():
    global current_frame
    current_frame = "end_of_game"
    update_statistics()
    update_win_or_loose_labels()
    end_of_game_frame.lift()


def rules():
    # Shows the rules
    global current_frame
    current_frame = "rules"
    rules_frame.lift()


def start_game():
    # Resets the game status and generates or clears the button list
    running_game()
    global tries
    tries = 0
    global guessed_letters
    guessed_letters = []
    if is_generated("labels"):
        global letter_label_list
        for letter_label in letter_label_list:
            letter_label.destroy()
        letter_label_list = []
        global letter_label_frame_list
        for letter_label_frame in letter_label_frame_list:
            letter_label_frame.destroy()
        letter_label_frame_list = []
    letter_label_gen(len(word_to_guess))
    update_word()
    update_graphic()
    if not is_generated("buttons"):
        button_gen(anchor_x, anchor_y, distance, button_size)
    else:
        for but in button_list:
            but["state"] = "normal"
    global time1
    time1 = time.time()
    random_graphic()


def random_graphic():
    rand = random.randint(1, 42)
    global special_graphic
    if rand == 1:
        special_graphic = True
    else:
        special_graphic = False


def edit_listbox():
    clear_listbox()
    if load_listbox():
        edit_own_list()


# ------------------ Start Frame ------------------


# Buttons
start_button = tk.Button(
    start_frame,
    text="Spiel starten",
    command=main_menu,
    font=font2_bigger,
    bg=colour2,
    activebackground=colour2_2
)
start_button.place(anchor=tk.CENTER, x=window_width/2, y=window_height/2)

# ------------------ Title Frame ------------------


# Functions
def close_window():
    answer = askyesno("Bestätigung", "Wollen Sie das Programm beenden?")
    if answer:
        window.destroy()


def hit_return_button():
    # When return button is hit, different options
    global current_frame
    if current_frame == "main_menu":
        close_window()
    elif current_frame == "game_select":
        main_menu()
    elif current_frame == "own_word_game":
        game_select()
    elif current_frame == "running_game":
        return_to_main_menu()
    elif current_frame == "word_from_list_game":
        game_select()
    elif current_frame == "edit_own_list":
        main_menu()
    elif current_frame == "rules":
        main_menu()
    elif current_frame == "end_of_game":
        same_game_again()
    else:
        print("ERR: Im entsprechenden Menü ist keine Aktion für den Return Button definiert.")
        main_menu()


def return_to_main_menu():
    answer = askyesno("Bestätigung", "Wollen Sie zum Hauptmenü zurückkehren?")
    if answer:
        main_menu()


def game_info():
    showinfo("Information", "Autor: ubiko\nVersion: 0.0.1\nVersionsdatum: 02.05.2022")


# Labels
label = tk.Label(
    title_frame,
    text="Hangman",
    font=font1,
    anchor=tk.CENTER,
    bd=0,
    bg=colour3
)
label.place(anchor="center", x=500, y=35)

# Buttons
return_button = tk.Button(
    title_frame,
    image=return_arrow_graphic,
    command=hit_return_button
)
return_button.place(anchor="center", x=30, y=35, width=40, height=40)

x_button = tk.Button(
    title_frame,
    image=x_graphic,
    command=close_window
)
x_button.place(anchor="center", x=80, y=35, width=40, height=40)

hangman_button = tk.Button(
    title_frame,
    image=hangman_graphic,
    command=game_info
)
hangman_button.place(anchor=tk.CENTER, x=965, y=35, width=40, height=40)

# ------------------ Main Menu Frame ------------------


# Variables
button_width = 300
button_height = 40
button_distance = 20
button_anchor1 = 100


# Functions
def button_y_calc(number, anchor=button_anchor1):
    return anchor + number * (button_distance + button_height)


# Buttons
go_button = tk.Button(
    main_menu_frame,
    text="Spielmodus wählen",
    command=game_select,
    font=font2,
    bg=colour2,
    activebackground=colour2_2
)
go_button.place(x=window_width / 2, y=button_y_calc(0), width=button_width, height=button_height, anchor=tk.N)

edit_own_list_button = tk.Button(
    main_menu_frame,
    text="Eigene Wortliste bearbeiten",
    font=font2,
    bg=colour2,
    activebackground=colour2_2,
    command=edit_listbox
)
edit_own_list_button.place(x=window_width / 2, y=button_y_calc(1), width=button_width, anchor=tk.N,
                           height=button_height)

rules_button = tk.Button(
    main_menu_frame,
    text="Regeln",
    command=rules,
    font=font2,
    bg=colour2,
    activebackground=colour2_2
)
rules_button.place(x=window_width / 2, y=button_y_calc(2), width=button_width, height=button_height, anchor=tk.N)

# ------------------ Game Select Frame ------------------


# Buttons
button_anchor2 = 150

own_word_game_button = tk.Button(
    game_select_frame,
    text="Eigenes Wort",
    command=own_word_game,
    font=font2,
    bg=colour2,
    activebackground=colour2_2
)
own_word_game_button.place(x=(window_width - button_width) / 2, y=button_y_calc(0, button_anchor2), width=button_width,
                           height=button_height)

word_from_list_game_button = tk.Button(
    game_select_frame,
    text="Wort aus der Liste",
    font=font2,
    bg=colour2,
    command=word_from_list_game,
    activebackground=colour2_2
)
word_from_list_game_button.place(x=(window_width - button_width) / 2, y=button_y_calc(1, button_anchor2),
                                 width=button_width, height=button_height)


# ------------------ Own Word Game Frame ------------------


# Functions
def change_show_status():
    # Changes which symbol is shown in the textbox
    if entry1["show"] == "*":
        entry1["show"] = ""
    else:
        entry1["show"] = "*"


def check_word(entry_):
    # Checks if the word the user entered contains only valid letters and has a valid length
    ent = entry_.get().lower()
    error_message = ""
    valid = True
    for letter in ent:
        if (not (letter in letter_list)) and (not letter == "-"):
            valid = False
            error_message = "Bitte verwenden Sie nur Vokale, Konsonanten und Bindestriche."
    if not 0 < len(ent) <= 30:
        valid = False
        error_message = "Bitte wählen sie ein Wort, welches 1-30 Buchstaben enthält."
    if valid:
        if entry_ == entry1:
            word_valid()
        elif entry_ == entry2:
            check_word_already_in(entry_.get())
    else:
        if entry_ == entry1:
            word_not_valid(error_message)
        elif entry_ == entry2:
            word_not_valid2(error_message)


def word_valid():
    # If the user word is valid, then the game is ready to start
    wrong_word_label["fg"] = colour1
    if button_state.get():
        answer = askyesno("Bestätigung", "Wollen Sie das Wort " + entry1.get().upper() + " verwenden?")
        if not answer:
            return
    global word_to_guess
    word_to_guess = entry1.get().lower()
    start_game()


def word_not_valid(error_message):
    # If the user word is not valid, the Wrong Word Label appears
    wrong_word_label["fg"] = "red"
    wrong_word_label["text"] = error_message


def invis_wrong_word_label(label_):
    # Makes the Wrong Word Label invisible
    label_["fg"] = colour1


generated_buttons = False
generated_labels = False


def is_generated(string):
    # Returns if the Letter Buttons are already generated
    if string == "buttons":
        global generated_buttons
        return generated_buttons
    elif string == "labels":
        global generated_labels
        return generated_labels


def clear_entry(entry_):
    # Clears the textbox
    entry_.delete(0, "end")


# Labels
enter_word_label = tk.Label(
    own_word_game_frame,
    text="Bitte geben Sie Ihr Wort ein:",
    bg=colour1,
    font=font3
)
enter_word_label.place(x=20, y=20)

wrong_word_label = tk.Label(
    own_word_game_frame,
    text="Ungültige Eingabe",
    bg=colour1,
    fg=colour1,
    font=font5
)
wrong_word_label.place(x=17, y=80)

# Entries
entry1 = tk.Entry(
    own_word_game_frame,
    width=entry_width,
    bg="white",
    font=font3,
    show="*"
)
entry1.place(x=20, y=55)

# Buttons
button_state = tk.BooleanVar()
cb1 = tk.Checkbutton(
    own_word_game_frame,
    text="Wort zeigen",
    font=font3,
    bg=colour1,
    activebackground=colour1,
    command=change_show_status,
    variable=button_state,
    onvalue=True,
    offvalue=False
)
cb1.place(x=20, y=100)

confirm_button = tk.Button(
    own_word_game_frame,
    text="Wort bestätigen",
    bg=colour2,
    command=lambda: check_word(entry1),
    font=font4,
    activebackground=colour2_2
)
confirm_button.place(x=20, y=145)

# ------------------ Running Game Frame ------------------

# Variables
guessed_letters = []
button_size = 40
distance = 15
anchor_x = 60
anchor_y = 280
button_list = []
letter_label_list = []
letter_label_frame_list = []
tries = 0
max_fails = 9
label_distance = 30
time1 = 0
time2 = 0


# Functions
def current_word():
    # Returns the word with a combination of "_" and letters
    global word_to_guess
    output = ""
    for letter in word_to_guess:
        if letter not in guessed_letters and not letter == '-':
            output += "_"
        else:
            output += letter
    return output


def update_word():
    # Updates the Current Word Label
    word_ = current_word()
    for i in range(len(letter_label_list)):
        letter_label_list[i].config(text=word_[i].upper())


def button_gen(anchor_x_, anchor_y_, distance_, button_size_):
    # Generates the letter buttons
    for i in range(len(letter_list)):
        if i < 9:
            y_ = anchor_y_
            x_ = anchor_x_ + i * (distance_ + button_size_)
        elif i < 18:
            y_ = anchor_y_ + button_size_ + distance_
            x_ = anchor_x_ + i * (distance_ + button_size_) - 9 * (button_size_ + distance_)
        else:
            y_ = anchor_y_ + 2 * (button_size_ + distance_)
            x_ = anchor_x_ + i * (distance_ + button_size_) - 17.5 * (button_size_ + distance_)
        but = tk.Button(
            running_game_frame,
            font=font6,
            text=letter_list[i].upper(),
            bg=colour2,
            activebackground=colour2_2,
            command=lambda c=i: letter_button_pressed(c)
        )
        but.place(x=x_, y=y_, width=button_size_, height=button_size_)

        button_list.append(but)
    global generated_buttons
    generated_buttons = True


def letter_label_gen(word_length):
    # Generates the letter labels
    for pos in range(word_length):
        letter_label_frame = tk.Frame(
            running_game_frame,
            width=26,
            height=40,
            bg=colour1
        )
        letter_label_frame.place(x=25 + pos * label_distance, y=60)
        letter_label_frame.pack_propagate(False)
        letter_label = tk.Label(
            letter_label_frame,
            font=font7,
            bg=colour1,
            text="_",
            anchor=tk.CENTER,
            justify=tk.CENTER,
            width=3,
        )
        letter_label.pack()
        letter_label_list.append(letter_label)
        letter_label_frame_list.append(letter_label_frame)
    global generated_labels
    generated_labels = True


def letter_button_pressed(number):
    # The function that is called when one of the letter buttons is pressed
    button_list[number].config(state="disabled")
    check_for_letter(letter_list[number])
    guessed_letters.append(letter_list[number])
    update_word()
    win_check()
    fail_check()


def check_for_letter(letter):
    # Checks if the letter the user clicked is in the word
    if letter not in word_to_guess:
        # showinfo("Buchstabe nicht enthalten", "Der Buchstabe " + letter.upper() + " ist nicht enthalten.")
        global tries
        tries += 1
        update_graphic()


def update_graphic():
    # Updates the graphic
    global tries
    try:
        if special_graphic:
            new_img = tk.PhotoImage(file="./Graphics/Galgen_States_A/galgen_state_" + str(tries) + ".png")
        else:
            new_img = tk.PhotoImage(file="./Graphics/Galgen_States/galgen_state_" + str(tries) + ".png")
        galgen_label.configure(image=new_img)
        galgen_label.image = new_img
        galgen_label2.configure(image=new_img)
        galgen_label2.image = new_img
    except FileNotFoundError:
        showerror("Fehler", "Notwendige Dateien konnten nicht geladen werden. Bitte installieren Sie das Programm neu.")
        window.destroy()


def fail_check():
    # Checks if the maximum number of fails has been reached
    if tries == max_fails:
        ending("Verloren!", "Du hast das Wort nicht rechtzeitig erraten. Das Wort war\n" + word_to_guess.upper() + ".",
               "Das Männchen ist traurig.")


def win_check():
    # Checks if the user has guessed all the letters in the Current Word and the game is won
    if "_" not in current_word():
        ending("Gewonnen!", "Du hast das Wort erraten!", "Das Männchen ist glücklich.")


# Labels
l1 = tk.Label(
    running_game_frame,
    text="So sieht das Wort bisher aus:",
    font=font3,
    bg=colour1
)
l1.place(x=20, y=20)

l2 = tk.Label(
    running_game_frame,
    text="Bitte wählen Sie einen Buchstaben aus:",
    font=font3,
    bg=colour1
)
l2.place(x=20, y=225)

img = ""
galgen_label = tk.Label(
    running_game_frame
)
galgen_label.place(x=650, y=150, width=250, height=300)


# ------------------ Word From List Game Frame ------------------

# Functions
def confirm_option():
    # If the Confirm Option Button is pressed, this function checks which one of the Radio Buttons is active
    if selected_option.get() == 0:
        no_option_chosen.configure(fg="red")
    elif selected_option.get() == 1:
        choose_random_word("own")
    elif selected_option.get() == 2:
        choose_random_word("prepared")
    elif selected_option.get() == 3:
        choose_random_word("both")


def choose_random_word(chosen_list):
    # Loads the List Files and chooses a random word dependant of the option the user has chosen
    used_list = []
    if chosen_list == "own" or chosen_list == "both":
        try:
            own_file = open("Lists/own_list.txt", "r")
            own_lines = own_file.readlines()
        except FileNotFoundError:
            showerror("Fehler", "Fehler beim Lesen von Dateien")
            return
        for i in range(len(own_lines)):
            if own_lines[i].endswith("\n"):
                own_lines[i] = own_lines[i][0:-1]
            if not is_valid(own_lines[i]):
                showerror("Fehler", "Illegale Ausdrücke gefunden.")
                return
        used_list += own_lines
    if chosen_list == "prepared" or chosen_list == "both":
        try:
            prepared_file = open("Lists/prepared_list.txt")
            prepared_lines = prepared_file.readlines()
        except FileNotFoundError:
            showerror("Fehler", "Fehler beim Lesen von Dateien")
            return
        for j in range(len(prepared_lines)):
            if prepared_lines[j].endswith("\n"):
                prepared_lines[j] = prepared_lines[j][0:-1]
            if not is_valid(prepared_lines[j]):
                showerror("Fehler", "Illegale Ausdrücke gefunden.")
                return
        used_list += prepared_lines
    if not used_list:  # Used List is empty
        showerror("Fehler", "Es sind keine Wörter in der Liste.")
        return
    global word_to_guess
    word_to_guess = random.choice(used_list).lower()
    start_game()


def is_valid(word_):
    # Checks if the random chosen word contains only regular letters
    for letter in word_:
        if (letter.lower() not in letter_list) and (not letter == "-"):
            return False
    if word_ == "" or len(word_) < 1 or len(word_) > 30:
        return False
    return True


def clear_radio_buttons():
    # Resets all Radio Buttons
    selected_option.set(0)
    r_op1.deselect()
    r_op2.deselect()
    r_op3.deselect()


def invis_no_option_chosen():
    # Makes the No Option Chosen Label invisible
    no_option_chosen["fg"] = colour1


# Labels
choose_option_label = tk.Label(
    word_from_list_game_frame,
    text="Mit welchen Wörtern möchten Sie spielen?",
    bg=colour1,
    font=font3
)
choose_option_label.place(x=20, y=20)

no_option_chosen = tk.Label(
    word_from_list_game_frame,
    text="Bitte wählen Sie eine Option aus.",
    bg=colour1,
    fg=colour1,
    font=font5
)
no_option_chosen.place(x=20, y=160)

# Buttons
selected_option = tk.IntVar()
r_op1 = tk.Radiobutton(
    word_from_list_game_frame,
    text="nur mit Wörtern aus der eigenen Liste",
    variable=selected_option,
    value=1,
    font=font3,
    bg=colour1,
    activebackground=colour1
)
r_op1.place(x=20, y=70)

r_op2 = tk.Radiobutton(
    word_from_list_game_frame,
    text="nur mit Wörter aus der vorgefertigten Liste",
    variable=selected_option,
    value=2,
    font=font3,
    bg=colour1,
    activebackground=colour1
)
r_op2.place(x=20, y=100)

r_op3 = tk.Radiobutton(
    word_from_list_game_frame,
    text="mit allen Wörter",
    variable=selected_option,
    value=3,
    font=font3,
    bg=colour1,
    activebackground=colour1
)
r_op3.place(x=20, y=130)

confirm_option_button = tk.Button(
    word_from_list_game_frame,
    text="Auswahl bestätigen",
    command=confirm_option,
    font=font4,
    bg=colour2,
    activebackground=colour2_2
)
confirm_option_button.place(x=20, y=200)

# ------------------ Edit Own List Frame ------------------

# Variables
lines_in_listbox = []
x_wert = 410


# Functions
def load_listbox():
    # Inserts the words from the Own List to the listbox
    try:
        own_file = open("Lists/own_list.txt", "r")
        own_lines = own_file.readlines()
    except FileNotFoundError:
        showerror("Fehler", "Fehler beim Lesen von Dateien")
        return False
    for i in range(len(own_lines)):
        if own_lines[i].endswith("\n"):
            own_lines[i] = own_lines[i][0:-1]
        if not is_valid(own_lines[i]):
            showerror("Fehler", "Illegale Ausdrücke gefunden.")
            main_menu()
            return
        listbox.insert(tk.END, own_lines[i])
    global lines_in_listbox
    lines_in_listbox = own_lines
    own_file.close()
    return True


def clear_listbox():
    # Deletes all elements of the listbox
    listbox.delete(0, tk.END)


def reload_listbox():
    clear_listbox()
    load_listbox()


def delete_items():
    # Deletes the selected items
    curse_selection = listbox.curselection()
    if curse_selection == ():
        showinfo("Information", "Bitte wählen Sie mindestens einen Eintrag aus.")
        return
    answer = askyesno("Bestätigung", "Wollen Sie die ausgewählten Einträge unwiderruflich entfernen?")
    if answer:
        try:
            own_file = open("Lists/own_list.txt", "w")
        except FileNotFoundError:
            showerror("Fehler", "Fehler beim Lesen von Dateien")
            return
        for i in range(len(lines_in_listbox)):
            if i not in curse_selection:
                own_file.write(lines_in_listbox[i] + "\n")
        own_file.close()
        reload_listbox()


def add_item(word):
    lines_in_listbox.append(word)
    try:
        own_file = open("Lists/own_list.txt", "w")
    except FileNotFoundError:
        showerror("Fehler", "Fehler beim Lesen von Dateien")
        return
    for i in range(len(lines_in_listbox)):
        own_file.write(lines_in_listbox[i] + "\n")
    own_file.close()
    reload_listbox()
    invis_wrong_word_label(wrong_word_label2)
    clear_entry(entry2)


def word_not_valid2(error_message):
    # If the user word is not valid, the Wrong Word Label appears
    wrong_word_label2["fg"] = "red"
    wrong_word_label2["text"] = error_message


def check_word_already_in(entry_):
    for element in lines_in_listbox:
        if entry_.lower() == element.lower():
            wrong_word_label2["fg"] = "red"
            wrong_word_label2["text"] = "Das angegebene Wort ist bereits in Ihrer Wortliste."
            return
    add_item(entry_)


# Scroll Bars and List Boxes
scrollbar = tk.Scrollbar(
    edit_own_list_frame,
    width=20
)
scrollbar.place(x=x_wert - 46, y=20, height=404)

listbox = tk.Listbox(
    edit_own_list_frame,
    bg="white",
    font=font5,
    selectmode=tk.MULTIPLE,
    selectbackground=colour4,
    highlightcolor="black",
    width=34,
    height=20,
    activestyle=tk.NONE,
)
listbox.place(x=20, y=20)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Labels
add_element_label = tk.Label(
    edit_own_list_frame,
    text="Geben Sie ein Wort ein, das Sie der Liste hinzufügen wollen:",
    font=font3,
    bg=colour1
)
add_element_label.place(x=x_wert, y=25)

wrong_word_label2 = tk.Label(
    edit_own_list_frame,
    text="Ungültige Eingabe",
    fg="red",
    bg=colour1,
    font=font5
)
wrong_word_label2.place(x=x_wert - 3, y=80)

# Entries
entry2 = tk.Entry(
    edit_own_list_frame,
    bg="white",
    width=entry_width,
    font=font3
)
entry2.place(x=x_wert, y=55)

# Buttons
delete_element_button = tk.Button(
    edit_own_list_frame,
    text="Ausgewählte Einträge löschen",
    bg=colour2,
    font=font4,
    activebackground=colour2_2,
    command=delete_items,
    width=26
)
delete_element_button.place(x=19, y=440)

add_element_button = tk.Button(
    edit_own_list_frame,
    text="Wort hinzufügen",
    font=font4,
    bg=colour2,
    activebackground=colour2_2,
    command=lambda: check_word(entry2)
)
add_element_button.place(x=x_wert, y=115)

# ------------------ Rules Frame ------------------

# Labels
above_rules_label = tk.Label(
    rules_frame,
    text="Regeln:",
    bg=colour1,
    font=font2
)
above_rules_label.place(x=20, y=20)

rules_label = tk.Label(
    rules_frame,
    text="Im Spiel Hangman geht es darum, ein Wort aus dem bereitgestellten Wortschatz bzw. eines Spielers zu\n "
         "erraten. Hierbei darf immer ein Buchstabe genannt werden. Ist der Buchstabe enthalten, so wird er an\n"
         "den entsprechenden Stellen eingezeichnet. Ist er nicht enthalten, so wird der Galgen um einen Strich\n"
         " erweitert. Nach neun Strichen ist der Galgen vollständig und das Spiel ist verloren. Werden davor\n"
         "jedoch alle enthaltenen Buchstaben genannt, so ist das Spiel gewonnen.",
    font=font3_smaller,
    bg=colour1,
    justify=tk.LEFT
)
rules_label.place(x=20, y=50)


# Buttons
got_it_button = tk.Button(
    rules_frame,
    font=font4,
    bg=colour2,
    activebackground=colour2_2,
    command=main_menu,
    text="Verstanden!"
)
got_it_button.place(x=800, y=190)


# ------------------ End of Game Frame ------------------


# Variables
end_status = ""
end_info = ""
man_end = ""


def same_game_again():
    global last_game
    if last_game == "own_word_game":
        own_word_game()
    elif last_game == "word_from_list_game":
        word_from_list_game()
    else:
        main_menu()


def stop_and_reset_time():
    global time1, time2
    time2 = time.time()
    total = time2-time1
    time1 = 0
    time2 = 0
    return total


def ending(ending_status_, end_info_, man_end_):
    global end_status
    end_status = ending_status_
    global end_info
    end_info = end_info_
    if tries > 0:
        global man_end
        man_end = man_end_
    else:
        man_end = ""
    end_of_game()


def guessed_letters_to_string():
    string = ""
    list_length = len(guessed_letters)
    for i in range(list_length):
        if i < list_length-1:
            string += guessed_letters[i].upper() + ", "
        else:
            string += guessed_letters[i].upper()
    return string


def update_statistics():
    statistic_label1["text"] = guessed_letters_to_string()
    statistic_label2["text"] = str(round(stop_and_reset_time(), 3)) + " Sekunden"


def update_win_or_loose_labels():
    win_or_loose_label["text"] = end_status
    win_or_loose_info_label["text"] = end_info
    man_label["text"] = man_end


# Labels
win_or_loose_label = tk.Label(
    end_of_game_frame,
    bg=colour1,
    font=font8,
    text="UNDEFINED",

)
win_or_loose_label.place(x=window_width/2, y=20, anchor=tk.N)

win_or_loose_info_label = tk.Label(
    end_of_game_frame,
    bg=colour1,
    font=font9,
    text="UNDEFINED"
)
win_or_loose_info_label.place(x=window_width/2, y=60, anchor=tk.N)

above_statistic_label1 = tk.Label(
    end_of_game_frame,
    text="Geratene Buchstaben:",
    bg=colour1,
    font=font2
)
above_statistic_label1.place(x=20, y=120)

statistic_label1 = tk.Label(
    end_of_game_frame,
    bg=colour1,
    font=font3,
    text="UNDEFINED",

)
statistic_label1.place(x=20, y=150)

above_statistic_label2 = tk.Label(
    end_of_game_frame,
    text="Zeit:",
    bg=colour1,
    font=font2
)
above_statistic_label2.place(x=20, y=200)

statistic_label2 = tk.Label(
    end_of_game_frame,
    bg=colour1,
    font=font3,
    text="UNDEFINED",

)
statistic_label2.place(x=20, y=230)


man_label = tk.Label(
    end_of_game_frame,
    bg=colour1,
    font=font3,
    text="UNDEFINED"
)
man_label.place(x=625, y=450)


galgen_label2 = tk.Label(
    end_of_game_frame,
    image=img
)
galgen_label2.place(x=650, y=150, width=250, height=300)


# Buttons
to_main_menu_button = tk.Button(
    end_of_game_frame,
    font=font4,
    bg=colour2,
    activebackground=colour2_2,
    command=main_menu,
    text="Zum Hauptmenü",
    width=20
)
to_main_menu_button.place(x=40, y=300)

same_again_button = tk.Button(
    end_of_game_frame,
    font=font4,
    bg=colour2,
    activebackground=colour2_2,
    command=same_game_again,
    text="Nochmal spielen",
    width=20
)
same_again_button.place(x=40, y=350)

# ------------------ Main Loop ------------------

window.mainloop()
