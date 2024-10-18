import sqlite3

# Connexion à la base de données pour la bibliothèque
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Création de la table des livres
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT UNIQUE NOT NULL,
        genre TEXT,
        publication_year INTEGER,
        available INTEGER NOT NULL DEFAULT 1
    )
''')

# Création de la table des utilisateurs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('user', 'admin')),
        email TEXT
    )
''')

# Création de la table des emprunts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        loan_date DATE DEFAULT (DATE('now')),
        return_date DATE,
        returned INTEGER DEFAULT 0,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# Création de la table des stocks
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        total_quantity INTEGER NOT NULL,
        available_quantity INTEGER NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
''')

# Fermeture de la connexion
conn.commit()
conn.close()

print("Base de données de bibliothèque créée avec succès !")
