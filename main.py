class Board:
    def __init__(self, n=8, debug=False):
        self.n = n
        self.queens = []
        self.debug = debug   # flaga sterująca printami

    def place(self, row, col):
        if self.debug: print(f"\t️->  Stawiam hetmana na ({row}, {col})")
        self.queens.append((row, col))

    def remove(self, row, col):
        if self.debug:
            print(f"\t<- Usuwam hetmana z ({row}, {col})")
        self.queens.remove((row, col))

    def is_safe(self, row, col):
        for r, c in self.queens:
            if c == col or r == row or abs(r - row) == abs(c - col):
                if self.debug: print(f"\tX - ({row}, {col}) koliduje z ({r}, {c})")
                return False
        if self.debug: print(f"\tV - ({row}, {col}) jest bezpieczne")
        return True

    def solve(self):
        solutions = []

        def backtrack(row=0):
            if self.debug: print(f"\nPoczątek backtrack({row})")
            if row == self.n:
                if self.debug:
                    print(f"!!! - Znaleziono rozwiązanie: {self.queens}")
                    print(self.__str__())
                solutions.append(self.queens.copy())
                return
            if self.debug: print(f"\n~~~~~~Wiersz {row}: Próbuję wszystkie kolumny")
            for col in range(self.n):
                if self.debug: print(f"Wiersz {row}: Sprawdzamy kolumnę {col}")
                if self.is_safe(row, col):
                    self.place(row, col)
                    backtrack(row + 1)
                    self.remove(row, col)
                    if self.debug: print(f"\tCofam się do poprzedniego wiersza!")

        backtrack()
        return solutions

    def __str__(self):
        board = [["#" for _ in range(self.n)] for _ in range(self.n)]
        for r, c in self.queens:
            board[r][c] = "Q"
        return "\n".join(" ".join(row) for row in board)

    def __repr__(self):
        return f"Board(n={self.n}, queens={self.queens})"

    def __len__(self):
        return len(self.queens)

    def __iter__(self):
        yield from self.queens

    def __contains__(self, pos):
        return pos in self.queens


def solve(n=8, debug=False):
    solutions_count = len(Board(n,debug=debug).solve())
    print(f"\nDla n = {n} znaleziono {solutions_count} rozwiązania")
    return solutions_count


if __name__ == '__main__':
    solve(n=1, debug=True) # pokazuje działanie flagi debug na krótkim przykładzie
    solve(n=2)
    solve(n=3)
    solve(n=4)
    solve(n=8)