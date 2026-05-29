import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""
    a=np.array(v1)
    b=np.array(v2)
    c = a @ b
    print(c)
    return c

def rango_matrice(m: list) -> int:
    """Sub-task 2: Calcola il rango di una matrice."""
    rank=np.linalg.matrix_rank(m, tol=None, hermitian=False)
    return rank

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 3: Risolvere un Sistema Lineare."""
    equation1=np.array(A)
    equation2=np.array(b)
    solution=np.linalg.solve(equation1,equation2)
    return solution

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""
    matrix_1=np.array(m1)
    matrix_2=np.array(m2)
    correlation_matrix=np.corrcoef(matrix_1,matrix_2)
    return correlation_matrix

def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    v1_array=np.array(v1)
    array_sin=np.sin(v1_array)
    array_cos=np.cos(v1_array)
    array_arcsin=np.arcsin(v1_array)
    array_arccos=np.arccos(v1_array)
    return (array_sin, array_cos, array_arcsin, array_arccos)


def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 2:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print(f"Sub-task 5:{ operazioni_elemento_per_elemento([0, 0.5, 1, -0.5])}")

if __name__ == "__main__":
    main()
