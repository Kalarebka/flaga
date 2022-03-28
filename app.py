import json
import random

from flask import Flask, render_template, redirect, url_for, request

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    text="xD podstrona xd"
    return render_template("xd.html", text=text)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/info')
def info():
    ludzie = [{'ludz': 'Hilarion (metropolita kijowski)', 'opis': 'Przed objęciem urzędu metropolity służył w cerkwi domu książecego na Berestowie. Wyróżniał się pobożnością oraz posiadanym wykształceniem. Według hagiografii prowadził życie ascetyczne: wykopał dla siebie pieczarę nad brzegiem Dniepru i spędzał w niej długie godziny na modlitwie. Śluby mnisze miał złożyć przed św. Antonim Pieczerskim. Hilarion  przywiązywał znaczną wagę do kształcenia społeczeństwa. Hilarion został uznany za świętego przez Kościół prawosławny; jego wspomnienie przypada 28 lipca (według kalendarza juliańskiego)', 'url_portretu': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/Enthronement_of_Hilarion_of_Kiev.jpg'},
{'ludz': 'Nestor (kronikarz)', 'opis': 'Nestor także Nestor Kronikarz, Nestor z Kijowa (ros. i ukr. Нестор, ur. ok. 1050, zm. ok. 1114) – kronikarz, mnich pieczerskiego monasteru. Redaktor jednego z najstarszych ruskich latopisów – Powieść minionych lat (Повѣсть времяньныхъ лѣтъ), powstałego ok. 1113 r., w którym Nestor opisał historię Rusi od IX do XII wieku. Powieść zawiera opisy różnych wydarzeń, m.in. przybycia Ruryka na ziemie ruskie, początków Rusi Nowogrodzkiej i rodu Rurykowiczów oraz powstania Wielkiego Księstwa Kijowskiego. Jego latopis zawiera także wiele wiadomości o początkach innych państw, m.in. Polski. Nestor był również autorem innych, mniej znanych dzieł literackich. Inspirował się m.in. twórczością czeskiego kronikarza Kosmasa z Pragi. Jego kronika została po raz pierwszy wydana drukiem w 1767 roku. Pochowany jest w Ławrze Pieczerskiej w Kijowie.', 'url_portretu': 'https://upload.wikimedia.org/wikipedia/commons/9/92/Prp._Nestor_Letopisec_Rossiski.png'},
{'ludz': 'Melecjusz Smotrycki', 'opis': 'Melecjusz (w j. pol. także Meletiusz Smotriski, Smotrzyski, Smotrziski; ukr. Мелетій Смотрицький, biał. Мялецій Сматрыцкі, ros. Мелетий Смотрицкий, łac. Meletius Smotrickij, Smotriscky, Smotrysky; ur. ok. 1577 na Podolu, zm. 27 grudnia 1633 w Dermaniu) – prawosławny, a następnie unicki duchowny działający w Rzeczypospolitej, w latach 1620–1629 prawosławny arcybiskup połocki, archimandryta dermański w 1627 roku. Autor gramatyki języka cerkiewnosłowiańskiego zaliczanej do najważniejszych opracowań w tej tematyce', 'url_portretu': 'https://upload.wikimedia.org/wikipedia/commons/4/44/Mialeci_Smatrycki._%D0%9C%D1%8F%D0%BB%D0%B5%D1%86%D1%96_%D0%A1%D0%BC%D0%B0%D1%82%D1%80%D1%8B%D1%86%D0%BA%D1%96_%28XVIII%29.jpg'},
{'ludz': 'Ławrentij Zyzanij-Tustanowski', 'opis': 'Ławrentij Zyzanij-Tustanowski, w wersji spolszczonej Wawrzyniec Zyzani-Tustanowski (ur. ok. 1560, zm. ok. 1634) – ruski językoznawca, pisarz, tłumacz, nauczyciel, teolog i protojerej. Autor podręczników do nauki języka cerkiewnosłowiańskiego. Napisał jego gramatykę i elementarz, który został uzupełniony o pierwszy słownik cerkiewnosłowiańsko-ruski Leksis syricz reczenija wkratci sobrany i iz słowenskaho jazyk na prostyj ruskij dialekt istołkowany (Wilno 1596)', 'url_portretu': 'https://upload.wikimedia.org/wikipedia/commons/d/dd/Zizaniy_Lavrrntiy.jpg'},
{'ludz': 'Zachariasz Kopysteński', 'opis': 'Zachariasz Kopysteński (ukr. Захарія Копистенський; ur. w Przemyślu, rok nieznany, zm. 21 marca 1627 w Kijowie) – ukraiński pisarz, polemista, działacz środowisk prawosławnych. Urodzony w Przemyślu w szlacheckiej rodzinie herbu Leliwa. Wykształcenie zdobył w szkole Bractwa Lwowskiego. Absolwent Akademii Ostrogskiej. Władał biegle greką i łaciną. W 1616 r. przeniósł się do Kijowa i wstąpił do Bractwa Kijowskiego, gdzie rozwinął działalność i polemiczno-literacką, i wydawniczą. W 1616 r. napisał przedmowę do „Czasoslova” («Часослова») – pierwszej księgi wydanej przez drukarnię kijowsko-peczerską. 20 listopada 1624 r. został archimandrytą ławry Kijowsko-Pieczerskiej. Knyha pro prawdywu jednist prawosławnych chrystyjan (Книга про правдиву єдність православних християн, 1623), tj. Księga o prawdziwej jedności składa się z 2 rozdziałów i rozstrzyga kwestię zasad zjednoczenia wyznaniowego, które nie powinno być krzywdzące dla żadnej ze stron. Autor oskarża projekt unijny w Brześciu, w wyniku którego świat prawosławny utracił jedność.', 'url_portretu': 'https://upload.wikimedia.org/wikipedia/commons/4/46/Zaharia_kopystensky.jpg'},
{'ludz': 'Pamwo Berynda', 'opis': 'Pamwo Berynda (ukr. Па́мво Бери́нда), imię świeckie Pawło (ur. 1555–1560 w Jezupolu, zm. 13 lipca/ 23 lipca 1632 w Kijowie) – działacz rusko-ukraińskiej kultury i oświaty, leksykograf, pisarz, poeta, grawer. Był jednym z prekursorów poezji i szkolnego dramatu na Ukrainie. W 1616 r. wydrukował we Lwowie świąteczny, wierszowany dialog – На Рождєство Христа вєршє для утєхи православним христіанам. Do dialogu dodane były inne wiersze dotyczące Cerkwi.', 'url_portretu': 'https://upload.wikimedia.org/wikipedia/commons/3/37/%D0%9F%D0%B0%D0%BC%D0%B2%D0%B0_%D0%91%D1%8F%D1%80%D1%8B%D0%BD%D0%B4%D0%B0.jpg'},]
    wylosowany = random.choice(ludzie)
    return render_template('biografia.html', **wylosowany)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_dla_ukrainy.html")

@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    with open('dane/characters.json', 'r') as f:
        characters_data = json.load(f)
    chosen_characters = random.sample(characters_data, 3)
    chosen_characters.sort(key=lambda x: x[3], reverse=True)
    return render_template("ciekawe-postacie.html", characters=chosen_characters)

@app.route('/htmx_examples')
def htmx_examples():
    return render_template('htmx_examples.html')

# -------------- HTMX FUNCTIONALITY ------------------ #

@app.route('/fruits', methods=["POST", "GET"])
def fruits():
    if request.method == "GET":
        try:
            with open('dane/fruits.json') as f:
                fruit_list = json.load(f)
        except FileNotFoundError:
            fruit_list = []
            return "No fruits file detected"
        return fruit_list
    else:
        try:
            new_fruit = request.form.get('new_fruit')
            try:
                with open('dane/fruits.json') as f:
                    fruit_list = json.load(f)
            except FileNotFoundError:
                fruit_list = []
            fruit_list.append(new_fruit)
            with open('dane/fruits.json', 'w') as f:
                json.dump(fruit_list, f)
            return redirect(url_for('htmx_examples'))
        except RateLimitException as e:
            return repr(e)


@app.route('/check_fruit', methods=["POST"])
def check_fruit():
    try:
        with open('dane/fruits.json') as f:
            fruit_list = json.load(f)
    except FileNotFoundError:
        fruit_list = []
    new_fruit = request.form.get('new_fruit')
    if new_fruit in fruit_list:
        return '<p id="fruit-label" style="color: red;">This fruit was already added</p>'
    else:
        return '<p id="fruit-label" style="color: green;">This fruit can be added</p>'


if __name__=="__main__":
    app.run()
