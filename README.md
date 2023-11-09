# Algorytm Needlemana-Wunscha
## Opis

Program implementuje algorytm Needleman-Wunsch do globalnego dopasowania sekwencji nukleotydowych. Sekwencje do dopasowania przekazywane są w jednym pliku FASTA, a wyniki do 10 dopasowań z maksymalnym scorem zapisywane do pliku txt. Pozwala użytkownikowi na dostosowywanie punktacji match, mismatch i gap. W repozytorium znajduje się przykładowy plik FASTA. Jeżeli w podanym na wejściu pliku FASTA będa się znajdować więcej niż 2 sekwencje to przeanalizowane zostaną pierwsze dwie.

## Sposób użycia

### Instalacja

1. Upewnij się, że masz zainstalowanego Pythona w wersji 3.x.
2. Zainstaluj wymagane biblioteki, uruchamiając poniższą komendę w terminalu:

    ```bash
    pip install biopython
    ```

3. Pobierz repozytorium lub skopiuj pliki programu na swój lokalny komputer.

### Uruchamianie

Aby uruchomić program, użyj terminala i wpisz:

```bash
python main.py --f sekwencje.fasta --o wyniki.txt --match 2 --mismatch -1 --gap -2
```
### Flagi

* `--f:` Ścieżka do pliku FASTA zawierającego dwie sekwencje nukleotydowe.
* `--o` (Opcjonalne) Ścieżka do pliku, do którego zostaną zapisane wyniki. Domyślnie: "output.txt".
* `--match` (Opcjonalne) Punktacja za match. Domyślnie: 2.
* `--mismatch` (Opcjonalne) Kara za mismatch. Domyślnie: -1.
* `--gap` (Opcjonalne) Kara za gap. Domyślnie: -2.

## Przykład użycia

### Przykładowe sekwencje w pliku przykladowaSekwencja.fasta
```fasta
>sequence1
ATGCTAGCTAGCTAGCTAGCTAGC

>sequence2
ATGCTAGCTAGGTAGTTTTAGA
```

### Uruchomienie
```bash
python main.py --f przykladowaSekwencja.fasta --o wyniki.txt
```

### Wynik w konsoli
```bash
Score (Match=2, Mismatch=-1, Gap=-2): 28
Alignments:
Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAG-T-TTTAGA

Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAG-TT-TTAGA

Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAGTT--TTAGA

Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAG-TTT-TAGA

Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAGTT-T-TAGA

Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAGTTT--TAGA

Results saved to wyniki.txt
```

### Wynik w pliku wyniki.txt
```txt
Score: 28
Alignments:

Alignment 1:
Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAG-T-TTTAGA

Alignment 2:
Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAG-TT-TTAGA

Alignment 3:
Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAGTT--TTAGA

Alignment 4:
Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAG-TTT-TAGA

Alignment 5:
Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAGTT-T-TAGA

Alignment 6:
Alignment 1: ATGCTAGCTAGCTAGCTAGCTAGC
Alignment 2: ATGCTAGCTAGGTAGTTT--TAGA
```
