from modelo import obtener_libros
# from template import renderizar_template


def renderizar_template(libros):
    # Simular la renderizacion de un template de libros
    html = "<h1>Lista de libros<h1>"
    for libro in libros:
        html += f"<p>ID: {libro["id"]}, <br>Titulo: {libro["titulo"]}, <br>Autor : {libro["Autor"]}</p>"
    return html 


#Integrar la vista y el template


def mostrar_libros_con_template():
    libros = obtener_libros()
    html = renderizar_template(libros)
    print(html)

if __name__ == "__main__":
    mostrar_libros_con_template()

