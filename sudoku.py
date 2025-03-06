class Tablica:
    def __init__(self, tablica):
        self.tablica = tablica

    def __str__(self):
        tablica_str = ''
        for rzad in self.tablica:
            rzad_tablicy = ['*' if i == 0 else str(i) for i in rzad]
            tablica_str += " ".join(rzad_tablicy)
            tablica_str += "\n"
        return tablica_str

    def czy_liczba_w_rzedzie(self, rzad, liczba):
        if liczba in self.tablica[rzad]:
            return True
        return False

    def czy_liczba_w_kolumnie(self, kolumna, liczba):
        for rzad in range(9):
            if liczba == self.tablica[rzad][kolumna]:
                return True
        return False

    def czy_liczba_w_kwadracie(self, rzad, kolumna, liczba):
        n_rzedu = (rzad // 3) * 3
        n_kolumny = (kolumna // 3) * 3

        for r in range(n_rzedu, n_rzedu + 3):
            for k in range(n_kolumny, n_kolumny + 3):
                if liczba == self.tablica[r][k]:
                    return True
        return False

    def czy_mozna_wpisac_liczbe(self, puste_miejsce, liczba):
        rzad, kolumna = puste_miejsce

        czy_liczba_w_rzedzie = self.czy_liczba_w_rzedzie(rzad, liczba)
        czy_liczba_w_kolumnie = self.czy_liczba_w_kolumnie(kolumna, liczba)
        czy_liczba_w_kwadracie = self.czy_liczba_w_kwadracie(rzad, kolumna, liczba)

        czy_wpisac = all([not czy_liczba_w_rzedzie, not czy_liczba_w_kolumnie, not czy_liczba_w_kwadracie])
        return czy_wpisac

    def znajdz_puste_miejsca(self):
        for rzad, wartosci in enumerate(self.tablica):
            try:
                kolumna = wartosci.index(0)
                return rzad, kolumna
            except:
                pass
        return None

    def rozwiaz(self):
        puste_miejsce = self.znajdz_puste_miejsca()
        if puste_miejsce is None:
            return True

        for liczba in range(1, 10):
            if self.czy_mozna_wpisac_liczbe(puste_miejsce, liczba):
                rzad, kolumna = puste_miejsce
                self.tablica[rzad][kolumna] = liczba
                if self.rozwiaz():
                    return True
                self.tablica[rzad][kolumna] = 0
        return False


def rozwiaz_sudoku(problem_sudoku):
    sudoku = Tablica(problem_sudoku)
    print(f"Sudoku do rozwiązania:\n{sudoku}")
    if sudoku.rozwiaz():
        print(f"Rozwiazane sudoku:\n{sudoku}")
    else:
        print("Nie da się rozwiązać danego sudoku.")







puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

rozwiaz_sudoku(puzzle)

#print(sudoku.tablica)
#print(sudoku.czy_liczba_w_rzedzie(0, 1))
#print(sudoku.czy_liczba_w_kolumnie(0, 4))
#print(sudoku.czy_liczba_w_kwadracie(3, 2, 3))
#print(sudoku.znajdz_zero())
#print(sudoku.czy_mozna_wpisac_liczbe([0, 0], 1))