# Magic Square Solver
Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square, or "impossible" if no valid number exists.

A magic square is a grid where every row, column, and diagonal adds up to the same number.

# Pruebas:
Esperando:1. solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]) should return 5.
Esperando:2. solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]) should return 4.
Esperando:3. solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) should return "impossible".
Esperando:4. solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]) should return 39.
Esperando:5. solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]) should return "impossible".