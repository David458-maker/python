from flask import Flask
import random
import string  # Do generowania haseł

app = Flask(__name__)

# Strona główna
@app.route("/")
def home():
    return '''<h1>Witaj na stronie głównej!</h1>
              <a href="/random_fact">Zobacz losowy fakt!</a><br>
              <a href="/generate_password">Wygeneruj losowe hasło!</a><br>
              <a href="/coin_flip">Rzuć monetą!</a>'''

# Strona z losowym faktem
@app.route("/random_fact")
def random_fact():
    facts_list = [
        "Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.",
        "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.",
        "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.",
        "Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.",
        "Jednym ze sposobów walki z uzależnieniem od technologii jest poszukiwanie zajęć, które sprawiają przyjemność i poprawiają nastrój.",
        "Elon Musk twierdzi, że sieci społecznościowe są zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.",
        "Elon Musk opowiada się także za regulacją sieci społecznościowych i ochroną danych osobowych użytkowników. Twierdzi, że sieci społecznościowe gromadzą o nas ogromną ilość informacji, które następnie można wykorzystać do manipulowania naszymi myślami i zachowaniami.",
        "Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi."
    ]
    return f'<p>{random.choice(facts_list)}</p><br><a href="/">Wróć do strony głównej</a>'

# Strona generująca hasła
@app.route("/generate_password")
def generate_password():
    length = 12  # Długość hasła
    characters = string.ascii_letters + string.digits + string.punctuation  # Znaki do użycia
    password = ''.join(random.choice(characters) for _ in range(length))
    return f'<h2>Twoje losowe hasło:</h2><p><strong>{password}</strong></p><br><a href="/">Wróć do strony głównej</a>'

# Strona rzutu monetą
@app.route("/coin_flip")
def coin_flip():
    result = random.choice(["Orzeł", "Reszka"])
    return f'<h2>Wynik rzutu monetą:</h2><p><strong>{result}</strong></p><br><a href="/">Wróć do strony głównej</a>'

# Uruchomienie aplikacji
if __name__ == "__main__":
    app.run(debug=True)
