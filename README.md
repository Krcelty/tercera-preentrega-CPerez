# Tercera Pre-Entrega Constanza Perez

## Acerca del proyecto

El proyecto se basa en una aplicación de gestión de fichas de pacientes en una veterinaria. Permite ingresar nuevas fichas de pacientes, buscar fichas existentes por el nombre de la mascota y mostrar los detalles de las fichas encontradas.

## Aplicaciones

tienda: Contiene las vistas, modelos, formularios y plantillas relacionadas con la gestión de las fichas de pacientes.

## Modelos

En models.py se definen los siguientes modelos:

Mascota: Representa a una mascota con un nombre.
Dueño: Representa a un dueño con un nombre.
Especie: Representa a una especie con un nombre.
Ficha: Representa una ficha de paciente que contiene un número de ficha, una referencia a una mascota, un dueño y una especie.

## Mejoras Futuras

Las mejoras futuras seran:
1-Implementar la capacidad de editar y eliminar fichas existentes.
2-Añadir validaciones adicionales a los formularios para garantizar la integridad de los datos.
3-Mejorar la interfaz de usuario para hacerla más intuitiva y fácil de usar.
4-Implementar autenticación de usuarios para permitir que solo usuarios autorizados accedan a las funcionalidades de gestión de fichas.
5-Agregar mas datos a la ficha.

## Problemas conocidos

-La búsqueda de fichas actualmente solo se realiza por nombre de mascota, lo que podría causar problemas si hay mascotas con nombres similares o duplicados.
-No se está manejando adecuadamente el caso en el que se ingrese un nombre de mascota que no coincide con ninguna ficha existente. Esto puede resultar en una respuesta vacía sin indicación clara al usuario.