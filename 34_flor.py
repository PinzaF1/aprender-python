import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Crear figura
fig, ax = plt.subplots(figsize=(10, 10), facecolor='#87CEEB')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Colores
color_petalo = '#FFD700'      # Oro/Amarillo
color_petalo_oscuro = '#FFA500'  # Naranja oscuro
color_centro = '#FF8C00'      # Naranja oscuro para el centro
color_tallo = '#228B22'       # Verde oscuro
color_hoja = '#32CD32'        # Verde lima

# Número de pétalos
num_petalos = 12

# Crear lista para guardar los pétalos (para animarlos)
petalos = []
hojas = []

# Función para animar
def animar(frame):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#87CEEB')
    
    # Ángulo de rotación basado en el frame
    rotacion = frame * 3
    
    # Escala de tamaño oscilante
    escala = 0.8 + 0.2 * np.sin(np.radians(frame * 6))
    
    # Dibujar pétalos con movimiento
    for i in range(num_petalos):
        angulo = (i * 360 / num_petalos) + rotacion
        
        # Distancia oscilante desde el centro
        distancia = 0.9 * escala
        x = distancia * np.cos(np.radians(angulo))
        y = distancia * np.sin(np.radians(angulo))
        
        # Alternancia de color
        color = color_petalo if i % 2 == 0 else color_petalo_oscuro
        
        # Crear pétalo como elipse
        petalo = patches.Ellipse((x, y), 
                                width=0.5 * escala, 
                                height=1.0 * escala, 
                                angle=angulo, 
                                facecolor=color, 
                                edgecolor='#CC6600', 
                                linewidth=2,
                                alpha=0.9)
        ax.add_patch(petalo)
    
    # Dibujar centro con brillo oscilante
    tamaño_centro = 0.4 + 0.1 * np.sin(np.radians(frame * 4))
    centro = Circle((0, 0), tamaño_centro, 
                   color=color_centro, 
                   ec='#8B4513', 
                   linewidth=2,
                   alpha=0.95)
    ax.add_patch(centro)
    
    # Dibujar detalles en el centro
    num_detalles = 8
    for j in range(num_detalles):
        angulo_detalle = (j * 360 / num_detalles) + rotacion
        x = 0.18 * np.cos(np.radians(angulo_detalle))
        y = 0.18 * np.sin(np.radians(angulo_detalle))
        detalle = Circle((x, y), 0.07, 
                        color='#FFD700', 
                        alpha=0.8)
        ax.add_patch(detalle)
    
    # Dibujar tallo
    tallo_x = [0, 0]
    tallo_y = [0, -2.2]
    ax.plot(tallo_x, tallo_y, color=color_tallo, linewidth=6, zorder=1)
    
    # Dibujar hojas ondulantes
    # Hoja izquierda
    offset_hoja = 0.15 * np.sin(np.radians(frame * 3))
    hoja1 = patches.Ellipse((-0.35 + offset_hoja, -1.0), 
                           width=0.4, 
                           height=0.8, 
                           angle=-35, 
                           facecolor=color_hoja, 
                           edgecolor='#1a7a1a', 
                           linewidth=2,
                           alpha=0.9)
    ax.add_patch(hoja1)
    
    # Hoja derecha
    hoja2 = patches.Ellipse((0.35 - offset_hoja, -1.4), 
                           width=0.4, 
                           height=0.8, 
                           angle=35, 
                           facecolor=color_hoja, 
                           edgecolor='#1a7a1a', 
                           linewidth=2,
                           alpha=0.9)
    ax.add_patch(hoja2)
    
    # Título
    titulo = ax.text(0, 2.7, '🌻 FLOR AMARILLA ANIMADA 🌻', 
                    fontsize=22, ha='center', fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    
    return ax,

# Crear animación
ani = FuncAnimation(fig, animar, frames=120, interval=50, blit=False, repeat=True)

plt.tight_layout()
plt.show()
