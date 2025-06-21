def calcular_imposto_renda(renda_mensal):
    # Base de cálculo anual
    renda_anual = renda_mensal * 12

    # Faixas de cálculo baseadas na tabela de 2024
    if renda_anual <= 28559.70:
        aliquota = 0
        deducao = 0
    elif renda_anual <= 42675.06:
        aliquota = 0.075
        deducao = 2144.40
    elif renda_anual <= 55949.40:
        aliquota = 0.15
        deducao = 4288.80
    elif renda_anual <= 55949.40 * 1.5:
        aliquota = 0.225
        deducao = 9648.36
    else:
        aliquota = 0.275
        deducao = 13130.51

    imposto = (renda_anual * aliquota) - deducao

    # Evita imposto negativo
    imposto = max(0, imposto)

    print(f"Renda Anual: R$ {renda_anual:.2f}")
    print(f"Alíquota: {aliquota * 100:.1f}%")
    print(f"Deduções: R$ {deducao:.2f}")
    print(f"Imposto a pagar: R$ {imposto:.2f}")

# Exemplo de uso:
renda = float(input("Informe sua renda mensal: R$ "))
calcular_imposto_renda(renda)
