from tkinter import *
import random

PERSON_NUMBER = 0
PERSON_FINAL = 0
PERSON = ""
TENSE_NUMBER = 0
WHOLE_TENSE = ""
BEGIN = ""
ENDING = ""
INFINITIVE = ""
VERB = ""
VERB_SIN_TILDES = ""
USER_RESPONSE = ""
USER_RESPONSE_2 = ""
ORIGINAL_VERB = ""
CHOSEN_TENSE = ""
ATTEMPT = 0
ONLY_I = False

pret_endings = ["preterite", ["", "", "", "", "", ""], ["é", "aste", "ó", "amos", "asteis", "aron", "í", "iste", "ió", "imos", "isteis", "ieron", "í", "iste", "ió", "imos", "isteis", "ieron"]],
imp_endings = ["imperfect", ["", "", "", "", "", ""], ["aba", "abas", "aba", "ábamos", "abais", "aban", "ía", "ías", "ía", "íamos", "íais", "ían", "ía", "ías", "ía", "íamos", "íais", "ían"]],
perf_endings = ["perfect", ["he ", "has ", "ha ", "hemos ", "habéis ", "han "], ["ado", "ado", "ado", "ado", "ado", "ado", "ido", "ido", "ido", "ido", "ido", "ido", "ido", "ido", "ido", "ido", "ido", "ido"]],
pres_endings = ["present", ["", "", "", "", "", ""], ["o", "as", "a", "amos", "áis", "an", "o", "es", "e", "emos", "éis", "en", "o", "es", "e", "imos", "ís", "en"]],
pres_cont_endings = ["present continuous", ["estoy ", "estas ", "está ", "estamos ", "estáis ", "están "], ["ando", "ando", "ando", "ando", "ando", "ando", "iendo", "iendo", "iendo", "iendo", "iendo", "iendo", "iendo", "iendo", "iendo", "iendo", "iendo", "iendo"]],
imm_fut_endings = ["immediate future", ["voy a ", "vas a ", "va a ", "vamos a ", "vais a ", "van a "], ["ar", "ar", "ar", "ar", "ar", "ar", "er", "er", "er", "er", "er", "er", "ir", "ir", "ir", "ir", "ir", "ir"],],
fut_endings = ["future", ["", "", "", "", "", ""], ["aré", "arás", "ará", "arémos", "aréis", "arán", "eré", "erás", "erá", "erémos", "eréis", "erán", "iré", "irás", "irá", "irémos", "iréis", "irán"]],
cond_endings = ["conditional", ["", "", "", "", "", ""], ["aría", "arías", "aría", "aríamos", "aríais", "arían", "ería", "erías", "ería", "eríamos", "eríais", "erían", "iría", "irías", "iría", "iríamos", "iríais", "irían"]],

tenses_list = [pret_endings, imp_endings, perf_endings, pres_endings, pres_cont_endings, imm_fut_endings, fut_endings, cond_endings]
infinitives = ["bailar", "cantar", "hablar", "aprender", "beber", "correr", "compartir", "decidir", "vivir"]
persons = ["I", "you", "he / she", "we", "you all", "they"]


def choose_verb():
    global VERB, WHOLE_TENSE, BEGIN, ENDING, INFINITIVE, VERB_SIN_TILDES, ATTEMPT, tenses_list, ONLY_I
    if ONLY_I == False:
        if len(tenses_list) == 0:
            correct_response_label.config(text="Select at least one tense!", fg="red")
        else:

            ATTEMPT = 0
            correct_response_label.config(text="", fg="black")
            entry.delete(0, END)
            PERSON_NUMBER = random.randint(0, 5)
            PERSON = persons[PERSON_NUMBER]
            TENSE_NUMBER = random.randint(0, len(tenses_list) - 1)
            CHOSEN_TENSE = tenses_list[TENSE_NUMBER]
            WHOLE_TENSE = CHOSEN_TENSE[0]
            INFINITIVE = random.choice(infinitives)
            if INFINITIVE[-2:] == "er":
                PERSON_FINAL = PERSON_NUMBER + 6
            elif INFINITIVE[-2:] == "ir":
                PERSON_FINAL = PERSON_NUMBER + 12
            else:
                PERSON_FINAL = PERSON_NUMBER
            person_label.config(text=PERSON)
            BEGIN = WHOLE_TENSE[1][PERSON_NUMBER]
            ENDING = WHOLE_TENSE[2][PERSON_FINAL]
            VERB = BEGIN + INFINITIVE[:-2] + ENDING

            tense_label.config(text=WHOLE_TENSE[0])
            infinitive_label.config(text=INFINITIVE)
    else:
        if len(tenses_list) == 0:
            correct_response_label.config(text="Select at least one tense!", fg="red")
        else:

            ATTEMPT = 0
            correct_response_label.config(text="", fg="black")
            entry.delete(0, END)
            PERSON_NUMBER = 0
            PERSON = persons[PERSON_NUMBER]
            TENSE_NUMBER = random.randint(0, len(tenses_list) - 1)
            CHOSEN_TENSE = tenses_list[TENSE_NUMBER]
            WHOLE_TENSE = CHOSEN_TENSE[0]
            INFINITIVE = random.choice(infinitives)
            if INFINITIVE[-2:] == "er":
                PERSON_FINAL = PERSON_NUMBER + 6
            elif INFINITIVE[-2:] == "ir":
                PERSON_FINAL = PERSON_NUMBER + 12
            else:
                PERSON_FINAL = PERSON_NUMBER
            person_label.config(text=PERSON)
            BEGIN = WHOLE_TENSE[1][PERSON_NUMBER]
            ENDING = WHOLE_TENSE[2][PERSON_FINAL]
            VERB = BEGIN + INFINITIVE[:-2] + ENDING

            tense_label.config(text=WHOLE_TENSE[0])
            infinitive_label.config(text=INFINITIVE)


def destildar_verbo():
    global ORIGINAL_VERB, VERB
    ORIGINAL_VERB = VERB
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        VERB = VERB.replace(a, b).replace(a.upper(), b.upper())
    return VERB

def destildar_entry():
    global USER_RESPONSE_2, USER_RESPONSE
    USER_RESPONSE_2 = USER_RESPONSE
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        USER_RESPONSE = USER_RESPONSE.replace(a, b).replace(a.upper(), b.upper())

def check():
    global VERB, VERB_SIN_TILDES, USER_RESPONSE, USER_RESPONSE_2, ORIGINAL_VERB, ATTEMPT
    ATTEMPT += 1
    USER_RESPONSE = entry.get().lower()
    destildar_verbo()
    destildar_entry()

    if USER_RESPONSE == VERB:
        correct_response_label.config(text=f"Correct!→{BEGIN + INFINITIVE[:-2] + ENDING}", fg="green")
    else:
        if ATTEMPT > 2:
            solution = BEGIN + INFINITIVE[:-2] + ENDING
            hint_1 = solution
            correct_response_label.config(text=f"Wrong!→{BEGIN + INFINITIVE[:-2] + ENDING}", fg="red")
        else:
            correct_response_label.config(text=f"Wrong!", fg="red")

# Add / remove tenses
def remove_pret():
    global tenses_list
    if pret_endings in tenses_list:
        t2.config(bg="red")
        tenses_list.remove(pret_endings)
    else:
        t2.config(bg="teal")
        tenses_list.append(pret_endings)

def remove_imp():
    global tenses_list
    if imp_endings in tenses_list:
        t3.config(bg="red")
        tenses_list.remove(imp_endings)
    else:
        t3.config(bg="teal")
        tenses_list.append(imp_endings)

def remove_perf():
    global tenses_list
    if perf_endings in tenses_list:
        t4.config(bg="red")
        tenses_list.remove(perf_endings)
    else:
        t4.config(bg="teal")
        tenses_list.append(perf_endings)

def remove_pres():
    global tenses_list
    if pres_endings in tenses_list:
        t5.config(bg="red")
        tenses_list.remove(pres_endings)
    else:
        t5.config(bg="teal")
        tenses_list.append(pres_endings)

def remove_pres_cont():
    global tenses_list
    if pres_cont_endings in tenses_list:
        t6.config(bg="red")
        tenses_list.remove(pres_cont_endings)
    else:
        t6.config(bg="teal")
        tenses_list.append(pres_cont_endings)

def remove_imm_fut():
    global tenses_list
    if imm_fut_endings in tenses_list:
        t7.config(bg="red")
        tenses_list.remove(imm_fut_endings)
    else:
        t7.config(bg="teal")
        tenses_list.append(imm_fut_endings)

def remove_fut():
    global tenses_list
    if fut_endings in tenses_list:
        t8.config(bg="red")
        tenses_list.remove(fut_endings)
    else:
        t8.config(bg="teal")
        tenses_list.append(fut_endings)

def remove_cond():
    global tenses_list
    if cond_endings in tenses_list:
        t9.config(bg="red")
        tenses_list.remove(cond_endings)
    else:
        t9.config(bg="teal")
        tenses_list.append(cond_endings)

# Add / remove persons
def remove_persons():
    global persons, ONLY_I
    if ONLY_I == False:
        ONLY_I = True
        p3.config(bg="red")
        p4.config(bg="red")
        p5.config(bg="red")
        p6.config(bg="red")
        p7.config(bg="red")

    else:
        ONLY_I = False
        p3.config(bg="steel blue")
        p4.config(bg="steel blue")
        p5.config(bg="steel blue")
        p6.config(bg="steel blue")
        p7.config(bg="steel blue")


window = Tk()
window.title("NerdRage Apps - Spanish regular verbs")
window.iconbitmap("images/logo_2UE_icon.ico")
window.config(pady=20, padx=20, bg="#375362")
window.geometry("860x700")

# Delete verbs functions
del_pret = IntVar(value=1)

# Canvas Table
canvas = Canvas(width=620, height=409, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=3)

t1 = Label(canvas, text="TENSES", width=16, font=("Arial", 20, "bold"), bg="black", fg="white")
t1.grid(row=0, column=0)
t2 = Button(canvas, activeforeground="red", width=16, text="Preterite", bg="teal", font=("Arial", 18, "bold"), command=remove_pret)
t2.grid(row=1, column=0)
t3 = Button(canvas, activeforeground="red", width=16, text="Imperfect", bg="teal", font=("Arial", 18, "bold"), command=remove_imp)
t3.grid(row=2, column=0)
t4 = Button(canvas, activeforeground="red", width=16, text="Perfect", bg="teal", font=("Arial", 18, "bold"), command=remove_perf)
t4.grid(row=3, column=0)
t5 = Button(canvas, activeforeground="red", width=16, text="Present", bg="teal", font=("Arial", 18, "bold"), command=remove_pres)
t5.grid(row=4, column=0)
t6 = Button(canvas, activeforeground="red", width=16, text="Present Continuous", bg="teal", font=("Arial", 18, "bold"), command=remove_pres_cont)
t6.grid(row=5, column=0)
t7 = Button(canvas, activeforeground="red", width=16, text="Immediate Future", bg="teal", font=("Arial", 18, "bold"), command=remove_imm_fut)
t7.grid(row=6, column=0)
t8 = Button(canvas, activeforeground="red", width=16, text="Simple Future", bg="teal", font=("Arial", 18, "bold"), command=remove_fut)
t8.grid(row=7, column=0)
t9 = Button(canvas, activeforeground="red", width=16, text="Conditional", bg="teal", font=("Arial", 18, "bold"), command=remove_cond)
t9.grid(row=8, column=0)

i1 = Label(canvas, text="INFINITIVES", width=10, font=("Arial", 20, "bold"), bg="black", fg="white")
i1.grid(row=0, column=2)
i2 = Label(canvas, text="bailar", font=("Arial", 18, "bold"))
i2.grid(row=1, column=2)
i3 = Label(canvas, text="cantar", font=("Arial", 18, "bold"))
i3.grid(row=2, column=2)
i4 = Label(canvas, text="hablar", font=("Arial", 18, "bold"))
i4.grid(row=3, column=2)
i5 = Label(canvas, text="aprender", font=("Arial", 18, "bold"))
i5.grid(row=4, column=2)
i6 = Label(canvas, text="beber", font=("Arial", 18, "bold"))
i6.grid(row=5, column=2)
i7 = Label(canvas, text="correr", font=("Arial", 18, "bold"))
i7.grid(row=6, column=2)
i8 = Label(canvas, text="compartir", font=("Arial", 18, "bold"))
i8.grid(row=7, column=2)
i9 = Label(canvas, text="decidir", font=("Arial", 18, "bold"))
i9.grid(row=8, column=2)
i10 = Label(canvas, text="vivir", font=("Arial", 18, "bold"))
i10.grid(row=9, column=2)

p1 = Label(canvas, text="PERSON", width=14, font=("Arial", 20, "bold"), bg="black", fg="white")
p1.grid(row=0, column=1)
p2 = Button(canvas, text="yo → I", width=15, font=("Arial", 18, "bold"), command=remove_persons, bg="steel blue")
p2.grid(row=1, column=1)
p3 = Button(canvas, text="tú → you", width=15, font=("Arial", 18, "bold"), command=remove_persons, bg="steel blue")
p3.grid(row=2, column=1)
p4 = Button(canvas, text="él/ella → he/she", width=15, font=("Arial", 18, "bold"), command=remove_persons, bg="steel blue")
p4.grid(row=3, column=1)
p5 = Button(canvas, text="nosotros → we", width=15, font=("Arial", 18, "bold"), command=remove_persons, bg="steel blue")
p5.grid(row=4, column=1)
p6 = Button(canvas, text="vosotros → you all", width=15, font=("Arial", 18, "bold"), command=remove_persons, bg="steel blue")
p6.grid(row=5, column=1)
p7 = Button(canvas, text="ellos → they", width=15, font=("Arial", 18, "bold"), command=remove_persons, bg="steel blue")
p7.grid(row=6, column=1)


# Buttons
hint_button = Button(text="Check", font=("Arial", 20, "bold"), command=check)
window.bind("<Return>", lambda event:check())
hint_button.grid(row=2, column=0)

play_button = Button(text="Play", font=("Arial", 20, "bold"), command=choose_verb, padx=13)
window.bind("<Shift_R>", lambda event:choose_verb())
play_button.grid(row=1, column=0)

# User entry
entry = Entry(width=33, font=("calibri", 31, "normal"))
entry.focus()
entry.grid(row=2, column=1, columnspan=3)

# Random choice labels
tense_label = Label(pady=10, padx=9, text="???", width=17, font=("Arial", 18, "bold"))
tense_label.grid(row=1, column=1)

infinitive_label = Label(pady=10, text="???", width=9, padx=12, font=("Arial", 18, "bold"))
infinitive_label.grid(row=1, column=3)

person_label = Label(pady=10, text="???", width=15, padx=9, font=("Arial", 18, "bold"))
person_label.grid(row=1, column=2)


correct_response_label = Label(pady=3, text="Press 'Play'", width=30, font=("Arial", 28, "bold"))
correct_response_label.grid(row=3, column=1, columnspan=3)



window.mainloop()