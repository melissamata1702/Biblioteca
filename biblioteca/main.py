from library import Library

# Funciones auxiliares para imprimir datos
def print_book(b):
    estado = "Disponible" if b.available else "Prestado"
    print(f"  [{b.book_id}] {b.title} — {b.author} ({b.year}) · {estado}")

def print_member(m):
    print(f"  [{m.member_id}] {m.name}")

def main():
    lib = Library()  # Creamos la biblioteca vacía

    while True:
        # Menú principal
        print("\n=== Mini Biblioteca ===")
        print("1) Agregar libro")
        print("2) Buscar libros")
        print("3) Listar disponibles")
        print("4) Agregar miembro")
        print("5) Prestar libro")
        print("6) Devolver libro")
        print("7) Listar miembros")
        print("0) Salir")
        opt = input("Opción: ").strip()

        try:
            if opt == "1":
                # Agregar libro
                t = input("Título: ")
                a = input("Autor: ")
                y = int(input("Año: "))
                b = lib.add_book(t, a, y)
                print("Libro agregado:")
                print_book(b)

            elif opt == "2":
                # Buscar libros
                q = input("Buscar por título/autor: ")
                results = lib.search_books(q)
                if not results:
                    print("Sin resultados.")
                else:
                    print("Resultados:")
                    for b in results:
                        print_book(b)

            elif opt == "3":
                # Listar libros disponibles
                av = lib.list_available()
                if not av:
                    print("No hay libros disponibles.")
                else:
                    print("Libros disponibles:")
                    for b in av:
                        print_book(b)

            elif opt == "4":
                # Agregar miembro
                n = input("Nombre del miembro: ")
                m = lib.add_member(n)
                print("Miembro agregado:")
                print_member(m)

            elif opt == "5":
                # Prestar libro
                book_id = int(input("ID del libro: "))
                member_id = int(input("ID del miembro: "))
                lib.lend_book(book_id, member_id)
                print("¡Préstamo registrado!")

            elif opt == "6":
                # Devolver libro
                book_id = int(input("ID del libro: "))
                lib.return_book(book_id)
                print("¡Libro devuelto!")

            elif opt == "7":
                # Listar miembros
                if not lib.members:
                    print("No hay miembros.")
                else:
                    print("Miembros:")
                    for m in lib.members:
                        print_member(m)

            elif opt == "0":
                # Salir del programa
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()