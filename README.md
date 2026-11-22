# Preentrega 14 - Análisis visual de distribuciones categóricas y outliers

Notebook de Jupyter que caracteriza un dataset de propinas de restaurante: gráficos de barras, boxplots, violin plots, asimetría, curtosis y detección de outliers con IQR.

## Origen de los datos
`data/propinas.csv`: dataset **simulado** con la misma estructura que `tips` de Seaborn (cuenta_total, propina, sexo, fumador, dia, momento, personas). Se genera con `generar_dataset.py` con semilla fija. Si querés usar el original: `sns.load_dataset("tips")`.

## Contenido
```
analisis_distribuciones.ipynb  -> notebook ejecutable con todo el análisis
generar_dataset.py             -> crea los datos
data/propinas.csv
requirements.txt
```

## Cómo ejecutarlo
1. `pip install -r requirements.txt`
2. `jupyter notebook analisis_distribuciones.ipynb`
3. Menú **Kernel → Restart & Run All**

## Resultados principales
- `cuenta_total`: asimetría **1.06** (positiva, cola a la derecha) y curtosis **1.07**.
- Método IQR: **9 outliers** (2.2% de los registros), todos por encima del límite superior.
- Sin outliers, la media baja de 20.78 a 19.84.

## Decisión sobre los outliers
No se eliminan: son cuentas reales de grupos grandes y no errores de carga. Para modelado se recomienda **transformarlos** (logaritmo) o usar estadísticos robustos (mediana, IQR). Solo se eliminarían si el análisis visual mostrara errores de medición.
