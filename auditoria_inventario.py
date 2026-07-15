# ============================================================================
# Programa: Auditoría de inventario y reabastecimiento
# Curso:    Fundamentos de Programación - 213022A_2202
# Fase:     5 - Evaluación Final POA
# Problema: 3 - Banco de problemas
# Autor:    George Eiver Chamorro Patiño
# Fecha:    15 de julio de 2026
# Universidad Nacional Abierta y a Distancia - UNAD
# Escuela de Ciencias Básicas, Tecnología e Ingeniería - ECBTI
# ============================================================================
# Descripción:
# Este programa audita un inventario almacenado en una matriz con el
# formato [Código, Nombre, Stock Actual, Stock Mínimo]. Calcula la
# cantidad exacta a solicitar por cada artículo y muestra una lista
# de pedidos. Si el stock actual es menor que el mínimo, la cantidad
# a pedir es la diferencia; si el stock es suficiente, la cantidad
# a pedir es cero.
# ============================================================================

# -----------------------------------------------------------------------------
# CONSTANTES: índices de columna de la matriz de inventario
# Se usan para evitar "números mágicos" al acceder a cada artículo.
# -----------------------------------------------------------------------------
INDICE_CODIGO = 0
INDICE_NOMBRE = 1
INDICE_STOCK_ACTUAL = 2
INDICE_STOCK_MINIMO = 3


def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Determina la cantidad exacta que debe pedirse de un artículo.

    Parámetros:
        stock_actual (int): unidades disponibles actualmente.
        stock_minimo (int): umbral mínimo requerido en inventario.

    Retorna:
        int: cantidad a solicitar. Si hay déficit retorna la diferencia;
                si el stock es suficiente retorna 0.
    """
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        # El stock actual es mayor o igual al mínimo requerido.
        cantidad_pedir = 0

    return cantidad_pedir


def mostrar_encabezado():
    """Imprime el encabezado visual del informe de auditoría."""
    print("=" * 72)
    print(" AUDITORÍA DE INVENTARIO Y LISTA DE PEDIDOS ".center(72, "="))
    print("=" * 72)
    print("Formato de matriz: [Código, Nombre, Stock Actual, Stock Mínimo]")
    print("-" * 72)


def mostrar_lista_pedidos(inventario):
    """
    Recorre la matriz de inventario, calcula la cantidad a pedir de cada
    artículo y muestra el nombre junto con dicha cantidad.

    Parámetros:
        inventario (list): matriz (lista de listas) con los artículos.

    Retorna:
        tuple: (total_articulos, total_unidades_pedir, articulos_con_deficit)
    """
    total_articulos = 0
    total_unidades_pedir = 0
    articulos_con_deficit = 0

    # Encabezado de la tabla de salida (mejora visual; no altera la lógica).
    print(f"{'Nombre del artículo':<35}{'Cantidad a solicitar':>20}")
    print("-" * 72)

    for articulo in inventario:
        nombre = articulo[INDICE_NOMBRE]
        stock_actual = articulo[INDICE_STOCK_ACTUAL]
        stock_minimo = articulo[INDICE_STOCK_MINIMO]

        cantidad_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

        print(f"{nombre:<35}{cantidad_pedir:>20}")

        total_articulos = total_articulos + 1
        total_unidades_pedir = total_unidades_pedir + cantidad_pedir

        if cantidad_pedir > 0:
            articulos_con_deficit = articulos_con_deficit + 1

    return total_articulos, total_unidades_pedir, articulos_con_deficit


def mostrar_resumen(total_articulos, total_unidades_pedir, articulos_con_deficit):
    """
    Muestra un resumen opcional del proceso de auditoría.

    Parámetros:
        total_articulos (int): cantidad de artículos evaluados.
        total_unidades_pedir (int): suma de unidades a solicitar.
        articulos_con_deficit (int): artículos con cantidad_pedir > 0.
    """
    print("-" * 72)
    print("RESUMEN DE LA AUDITORÍA")
    print(f"Total de artículos evaluados:     {total_articulos}")
    print(f"Artículos con déficit de stock:   {articulos_con_deficit}")
    print(f"Total de unidades a solicitar:    {total_unidades_pedir}")
    print("=" * 72)


def crear_inventario():
    """
    Crea y retorna la matriz de inventario con al menos cinco artículos.

    Cada fila tiene el formato:
    [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]

    Retorna:
        list: matriz de inventario.
    """
    inventario = [
        ["A001", "Resma de papel carta", 8, 15],
        ["A002", "Tóner laser negro", 25, 20],
        ["A003", "Bolígrafo azul caja x12", 3, 10],
        ["A004", "Carpeta oficio", 40, 30],
        ["A005", "USB 32 GB", 6, 12],
    ]
    return inventario


def main():
    """
    Función principal: orquesta la creación del inventario, el cálculo
    de pedidos y la presentación de resultados.
    """
    mostrar_encabezado()

    inventario = crear_inventario()

    total_articulos, total_unidades_pedir, articulos_con_deficit = (
        mostrar_lista_pedidos(inventario)
    )

    mostrar_resumen(total_articulos, total_unidades_pedir, articulos_con_deficit)


# Punto de entrada del programa.
# Solo se ejecuta main() cuando este archivo se corre directamente.
if __name__ == "__main__":
    main()
