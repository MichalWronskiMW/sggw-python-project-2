# SQLAlchemy – Ćwiczenia II–V

Projekt realizuje kolejne etapy pracy z SQLAlchemy i Alembic w ramach ćwiczeń 2–5.

Plik **`cwiczenie_2_3_4.py`** zawiera definicję modeli `Experiment` i `DataPoint` oraz relację *jeden–do–wielu*.  
Skrypt tworzy bazę `lab.db`, dodaje dane przykładowe i prezentuje operacje CRUD (dodawanie, aktualizacja, usuwanie).

Plik **`cwiczenie_5.py`** stanowi rozszerzenie poprzedniego – dodaje tabelę `Subject` oraz relację *wiele–do–wielu* między `Subject` i `Experiment` poprzez tabelę pośrednią `subject_experiment`.  
Ten plik służy jako baza do wykonania migracji z użyciem **Alembica**.  
Migracja została wygenerowana i zastosowana przy użyciu komend:

```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```
Po wykonaniu tych poleceń w bazie utworzone zostały wszystkie wymagane tabele zgodnie z definicją modeli w pliku `cwiczenie_5.py`.

Autor: Michał Wroński
