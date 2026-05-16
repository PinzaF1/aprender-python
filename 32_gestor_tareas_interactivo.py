#!/usr/bin/env python3
"""
Gestor de Tareas Interactivo
Una aplicación para gestionar tareas pendientes, completadas y eliminarlas.

Características:
- Agregar nuevas tareas
- Marcar tareas como completadas
- Listar todas las tareas
- Eliminar tareas
- Interfaz de menú interactiva

Autor: Sistema de Aprendizaje Python
Versión: 1.0
"""

class GestorTareas:
    """Clase para gestionar una lista de tareas con operaciones CRUD básicas."""
    
    def __init__(self):
        """Inicializa el gestor de tareas con lista vacía."""
        self.tareas = []
        self.contador_id = 1
    
    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea."""
        tarea = {
            'id': self.contador_id,
            'descripcion': descripcion,
            'completada': False
        }
        self.tareas.append(tarea)
        self.contador_id += 1
        print(f"✅ Tarea agregada: '{descripcion}'")
    
    def listar_tareas(self):
        """Lista todas las tareas."""
        if not self.tareas:
            print("📋 No hay tareas registradas")
            return
        
        print("\n" + "="*60)
        print("LISTA DE TAREAS")
        print("="*60)
        for tarea in self.tareas:
            estado = "✓ Completada" if tarea['completada'] else "⏳ Pendiente"
            print(f"[{tarea['id']}] {tarea['descripcion']:<40} {estado}")
        print("="*60 + "\n")
    
    def completar_tarea(self, id_tarea):
        """Marca una tarea como completada."""
        for tarea in self.tareas:
            if tarea['id'] == id_tarea:
                tarea['completada'] = True
                print(f"✅ Tarea '{tarea['descripcion']}' marcada como completada")
                return
        print(f"❌ No se encontró la tarea con ID {id_tarea}")
    
    def eliminar_tarea(self, id_tarea):
        """Elimina una tarea."""
        for i, tarea in enumerate(self.tareas):
            if tarea['id'] == id_tarea:
                descripcion = tarea['descripcion']
                self.tareas.pop(i)
                print(f"🗑️  Tarea '{descripcion}' eliminada")
                return
        print(f"❌ No se encontró la tarea con ID {id_tarea}")
    
    def obtener_estadisticas(self):
        """Obtiene estadísticas de las tareas."""
        total = len(self.tareas)
        completadas = sum(1 for t in self.tareas if t['completada'])
        pendientes = total - completadas
        
        print("\n" + "="*60)
        print("ESTADÍSTICAS")
        print("="*60)
        print(f"Total de tareas: {total}")
        print(f"Tareas completadas: {completadas}")
        print(f"Tareas pendientes: {pendientes}")
        if total > 0:
            porcentaje = (completadas / total) * 100
            print(f"Progreso: {porcentaje:.1f}%")
        print("="*60 + "\n")
    
    def limpiar_completadas(self):
        """Elimina todas las tareas completadas."""
        cantidad_eliminadas = len([t for t in self.tareas if t['completada']])
        self.tareas = [t for t in self.tareas if not t['completada']]
        print(f"🧹 Se eliminaron {cantidad_eliminadas} tarea(s) completada(s)")

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "="*60)
    print("GESTOR DE TAREAS INTERACTIVO")
    print("="*60)
    print("1. Agregar tarea")
    print("2. Listar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Ver estadísticas")
    print("6. Limpiar tareas completadas")
    print("7. Salir")
    print("="*60)

def main():
    """Función principal del gestor de tareas."""
    gestor = GestorTareas()
    
    # Tareas de ejemplo
    gestor.agregar_tarea("Aprender Python")
    gestor.agregar_tarea("Hacer un proyecto")
    gestor.agregar_tarea("Estudiar Git")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ").strip()
            if descripcion:
                gestor.agregar_tarea(descripcion)
            else:
                print("❌ La descripción no puede estar vacía")
        
        elif opcion == '2':
            gestor.listar_tareas()
        
        elif opcion == '3':
            gestor.listar_tareas()
            try:
                id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
                gestor.completar_tarea(id_tarea)
            except ValueError:
                print("❌ Ingrese un ID válido")
        
        elif opcion == '4':
            gestor.listar_tareas()
            try:
                id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
                gestor.eliminar_tarea(id_tarea)
            except ValueError:
                print("❌ Ingrese un ID válido")
        
        elif opcion == '5':
            gestor.obtener_estadisticas()
        
        elif opcion == '6':
            gestor.limpiar_completadas()
        
        elif opcion == '7':
            print("\n👋 ¡Gracias por usar el Gestor de Tareas!")
            break
        
        else:
            print("❌ Opción inválida. Por favor, seleccione una opción válida (1-7)")

if __name__ == "__main__":
    main()
