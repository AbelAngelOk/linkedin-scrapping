# Scrapper
Dado un perfil de linkedin devuelve un excel con la informacion de la lista de empresas que contiene el perfil.

## Índice

- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Instalación
no requiere instalacion

## Uso
Para ejecutar el proyecto debe ejecutar

```bash
$ python Scrapper.py
```

## Personalizacion

Para activar/desactivar el modo headless se debe especificar  el parametro con True o False respectivamente
al crear el Objeto Scrapper, si no se especifica el default es True.

```bash
$ unScrapper = Scrapper(handlessMode=False)
```

Para elegir las columnas de datos que quiere generar en el excel debe ir a Scrapper.py y cambiar el parametro de 
seleccionarDatos por True o False respectivamente. 

```bash
unScrapper = Scrapper()
unScrapper.run(seleccionarDatos=False)
```

## mejoras e incidencias

a. El limite de empresas extraidas es 10. Se debe quitar el limite de empresas extraidas. ✔
b. Al fallar el login genera el excel vacio. Al fallar el login deberia cancelarse la ejecucion. 🆗
c. No puede generar mas de un excel. ✔
d. paginas de empresas que resultan en no_found rompen el codigo. ✔
e. que se realice el proceso de extrasion de datos en paralelo