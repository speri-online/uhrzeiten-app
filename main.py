# Prüft daytime und passt die Stunde evtl. an 24h-Format an
# Gibt die Stunde und Minute die übergeben wird in die result_list (als String)


def rewrite_result_list(hour, minute):
    if user_dict["daytime"] == internal_daytime_dict["vormittags"]:
        result_list[0] = str(hour)
        result_list[2] = str(minute)
    else:
        hour = hour + 12
        result_list[0] = str(hour)
        result_list[2] = str(minute)


# Errechnen Stunde und Minute und übergeben sie an rewrite_result_list


def halb():
    hour = user_dict["input_hour"] - 1
    minute = 30
    rewrite_result_list(hour, minute)


def dreiviertel():
    hour = user_dict["input_hour"] - 1
    minute = 45
    rewrite_result_list(hour, minute)


def viertel():
    hour = user_dict["input_hour"] - 1
    minute = 15
    rewrite_result_list(hour, minute)


def viertelvor():
    hour = user_dict["input_hour"] - 1
    minute = 45
    rewrite_result_list(hour, minute)


def viertelnach():
    hour = user_dict["input_hour"]
    minute = 15
    rewrite_result_list(hour, minute)


def check_statement():
    if user_dict["statement"] == internal_statement_dict["Halb"]:
        print("runs statementfunc_halb()")
        halb()
    elif user_dict["statement"] == internal_statement_dict["Dreiviertel"]:
        print("runs statementfunc_dreiviertel()")
        dreiviertel()
    elif user_dict["statement"] == internal_statement_dict["Viertel"]:
        print("runs statementfunc_viertel()")
        viertel()
    elif user_dict["statement"] == internal_statement_dict["Viertel vor"]:
        print("runs statementfunc_viertelvor()")
        viertelvor()
    elif user_dict["statement"] == internal_statement_dict["Viertel nach"]:
        print("runs statementfunc_viertelnach()")
        viertelnach()


def convert():
    check_statement()
    try:
        print("".join(result_list))
    except TypeError:
        print("!!! Fehler in Funktion convert(), da kein String sondern ein anderer Typ weitergegeben wurde !!!")

    global stopper
    stopper = 1


# "statements" und "daytimes" als int codiert (bringt vermutlich eine bessere runtime als Strings)


internal_statement_dict = {"Halb": 0, "Dreiviertel": 1, "Viertel": 2, "Viertel vor": 3, "Viertel nach": 4}
internal_daytime_dict = {"vormittags": 5, "nachmittags": 6}

# Das vom user später über die UI gefüllte dict wird iniziiert
user_dict = {"statement": None, "input_hour": None, "daytime": None}

# Die später zur Ergebnisausgabe verwendete result_list wird iniziiert
result_list = [None, ":", None]

""" Sobald und solang das user_dict mit Werten außer "None" gefüllt ist soll kontinuerlich kovertiert werden,
sodass bei Neueingabe eines der drei Werte gleich aktualisiert wird. """
while [x for x in user_dict.values()] != [None, None, None]:
    convert()
    global stopper
    if stopper > 0:
        break
