# SQLAlchemy – Ćwiczenia II–V

Projekt realizuje kolejne etapy pracy z SQLAlchemy i Alembic w ramach ćwiczeń 2–5.

Plik **`cwiczenie_2_3_4.py`** zawiera definicję modeli `Experiment` i `DataPoint` oraz relację *jeden–do–wielu*.  
Skrypt tworzy bazę `lab.db`, dodaje dane przykładowe i prezentuje operacje CRUD (dodawanie, aktualizacja, usuwanie).

Plik **`cwiczenie_5.py`** rozszerza modele o relację *wiele–do–wielu* między `Experiment` i `Subject` (przez tabelę pośrednią `subject_experiment`).  
Ten plik stanowi podstawę do tworzenia migracji przy użyciu **Alembica** – poprawnie reaguje na komendy migracyjne (`revision`, `upgrade`), generując strukturę bazy na podstawie zdefiniowanych modeli.

Struktura plików i sposób działania odpowiada wymaganiom z poleceń ćwiczeń II–V.
