# subdraw

Elección de materias para horarios de secundaria.

sub|draw = **subject** | **draw**

## Instalación

Cree un entorno virtual Python e instale los requerimientos:

```console
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Opcionalmente, puede crear un fichero `.env` en el directorio del proyecto y sobreescribir las configuraciones de [settings.py](settings.py).

## Datos de entrada

Los datos de entrada estarán en un fichero csv con el siguiente formato:

    ASIGNATURA,HORAS_SEMANALES,GRUPO

Por ejemplo:

    BAE,6,1DAM
    ETS,3,1DAM
    LND,4,1DAM
    PRO,7,1DAM
    ...

> 💡 &nbsp;No se espera ninguna cabecera.

Por defecto, el nombre del fichero de datos será `subjects.csv`, aunque puede ser cualquier otro.

## Modo de uso

```console
$ python main.py --help
Usage: main.py [OPTIONS]

Options:
  -i, --filename TEXT     Subjects filename (csv format)  [default:
                          subjects.csv]
  -h, --hours INTEGER     Number of hours to reach within each schedule
                          [default: 18]
  -s, --max-size INTEGER  Maximum number of subjects within each schedule. If
                          -1 all sizes are valid.  [default: -1]
  -i, --include TEXT      Include this subject, group or subject-group
  -x, --exclude TEXT      Exclude this subject, group or subject-group
  --help                  Show this message and exit.
```

Obtener todas las combinaciones (_que sumen 18 horas por defecto_):

```console
$ python main.py
```

Obtener todas las combinaciones que sumen 19 horas:

```console
$ python main.py -h19
```

Obtener todas las combinaciones que tengan, como máximo, 4 asignaturas:

```console
$ python main.py -s4
```

Obtener todas las combinaciones que incluyan la asignatura DPL:

```console
$ python main.py -i DPL
```

Obtener todas las combinaciones que incluyan la asignatura DPL de 1ºDAM y además, que incluyan todas las asignaturas del grupo 2ºDAM:

```console
$ python main.py -i DPL-1DAM -i 2DAM
```

Obtener todas las combinaciones excluyendo la asignatura FCT:

```console
$ python main.py -x FCT
```

Usar otro fichero de entrada:

```console
$ python main.py -f funny-subjects.csv
```

Todos estos parámetros se pueden combinar para conseguir filtros más potentes:

```console
$ python main.py -f mydata.csv -s3 -h17 -i PRO -x ETS-1DAM
```
