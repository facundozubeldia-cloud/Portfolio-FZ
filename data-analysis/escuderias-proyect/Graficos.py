import os
import pandas as pd
import matplotlib.pyplot as plt

# Rutas
output_dir   = r"C:\Github\fz-dataworks\data-analysis\escuderias-proyect"
excel_esc    = os.path.join(output_dir, "podio_escuderias.xlsx")
excel_rapida = os.path.join(output_dir, "vueltas_rapidas_por_piloto.xlsx")

# Gráfico: Puntos Totales por Escudería
df_esc = pd.read_excel(excel_esc)
df_esc_sorted = df_esc.sort_values(by="Puntos Totales", ascending=False)

plt.figure(figsize=(8, 5))
bars = plt.bar(df_esc_sorted["Escudería"], df_esc_sorted["Puntos Totales"])
plt.xticks(rotation=45, ha="right")
plt.title("Puntos Totales por Escudería (ordenado por ganador)")
plt.xlabel("Escudería")
plt.ylabel("Puntos Totales")

for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h + 1, f"{int(h)}", ha="center", va="bottom")

max_p = df_esc_sorted["Puntos Totales"].max()
plt.ylim(0, max_p * 1.15)

out1 = os.path.join(output_dir, "puntos_por_escuderia_ordenado.png")
plt.tight_layout()
plt.savefig(out1)
plt.close()
print(f"📌 Gráfico generado: {out1}")

# Gráfico de Vuelta Más Rápida por Piloto
df_vr = pd.read_excel(excel_rapida)
# Se ordena de menor a mayor porque quien menos tarda es el “mejor”
df_vr_sorted = df_vr.sort_values(by="Vuelta Más Rápida (s)", ascending=True)

plt.figure(figsize=(10, 6))
bars2 = plt.bar(df_vr_sorted["Piloto"], df_vr_sorted["Vuelta Más Rápida (s)"])
plt.xticks(rotation=90, ha="right")
plt.title("Vuelta Más Rápida por Piloto")
plt.xlabel("Piloto")
plt.ylabel("Tiempo de Vuelta (s)")

for bar in bars2:
    w = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, w + 0.5, f"{w:.0f}", ha="center", va="bottom")

max_vr = df_vr_sorted["Vuelta Más Rápida (s)"].max()
plt.ylim(0, max_vr * 1.10)

out2 = os.path.join(output_dir, "vuelta_mas_rapida_por_piloto.png")
plt.tight_layout()
plt.savefig(out2)
plt.close()
print(f"📌 Gráfico generado: {out2}")