"""Genera data/propinas.csv: dataset simulado con la misma estructura que 'tips' de Seaborn."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(14)
n = 400
dia = rng.choice(["Jue", "Vie", "Sab", "Dom"], n, p=[0.2, 0.15, 0.35, 0.30])
momento = np.where(rng.random(n) < np.where(np.isin(dia, ["Jue", "Vie"]), 0.6, 0.15), "Almuerzo", "Cena")
personas = rng.choice([1, 2, 3, 4, 5, 6], n, p=[0.04, 0.55, 0.16, 0.17, 0.05, 0.03])
cuenta = (rng.gamma(2.6, 4.2, n) * (0.6 + 0.45 * personas)).round(2).clip(4)
cuenta[rng.choice(n, 6, replace=False)] *= rng.uniform(2.2, 3.0, 6)       # algunas cuentas muy altas
cuenta = cuenta.round(2)
propina = (cuenta * rng.normal(0.155, 0.04, n)).clip(0.5).round(2)
df = pd.DataFrame({"cuenta_total": cuenta, "propina": propina,
                   "sexo": rng.choice(["Mujer", "Hombre"], n, p=[0.36, 0.64]),
                   "fumador": rng.choice(["Si", "No"], n, p=[0.38, 0.62]),
                   "dia": dia, "momento": momento, "personas": personas})
df.to_csv("data/propinas.csv", index=False)
print("Creado data/propinas.csv", df.shape)
