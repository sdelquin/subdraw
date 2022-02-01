# ✨ subdraw

Elección de materias para horarios de secundaria.

sub|draw = **subject** | **draw**

> Esta herramienta permite generar combinaciones de asignaturas que sumen un determinado número de horas semanales. Útil para proyectar el horario personal en el reparto de materias sobre departamentos didácticos de secundaria y formación profesional.

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

    FUW,3,1ASR
    IMW,4,2ASR
    BAE,6,1DAM
    PGL,3,2DAM
    PRO,7,1DAW
    DSW,5,2DAW

> 💡 &nbsp;No se espera ninguna cabecera.

Por defecto, se espera que el nombre del fichero de datos sea `subjects.csv` (alojado en el directorio de trabajo del proyecto) aunque puede modificarse mediante argumentos de línea de comandos.

## Modo de uso

```console
$ python main.py --help
Usage: main.py [OPTIONS]

Options:
  -f, --filename TEXT     Subjects filename (csv format)  [default:
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

BAE-1DAM(6) + PRO-1DAW(7) + DSW-2DAW(5) = 18h
FUW-1ASR(3) + BAE-1DAM(6) + IMW-2ASR(4) + DSW-2DAW(5) = 18h
FUW-1ASR(3) + PRO-1DAW(7) + PGL-2DAM(3) + DSW-2DAW(5) = 18h
BAE-1DAM(6) + IMW-2ASR(4) + PGL-2DAM(3) + DSW-2DAW(5) = 18h
```

Obtener todas las combinaciones que sumen 20 horas:

```console
$ python main.py -h20

FUW-1ASR(3) + BAE-1DAM(6) + PRO-1DAW(7) + IMW-2ASR(4) = 20h
BAE-1DAM(6) + PRO-1DAW(7) + IMW-2ASR(4) + PGL-2DAM(3) = 20h
```

Obtener todas las combinaciones que tengan, como máximo, 3 asignaturas:

```console
$ python main.py -s3

BAE-1DAM(6) + PRO-1DAW(7) + DSW-2DAW(5) = 18h
```

Obtener todas las combinaciones que incluyan la asignatura FUW:

```console
$ python main.py -i FUW

FUW-1ASR(3) + BAE-1DAM(6) + IMW-2ASR(4) + DSW-2DAW(5) = 18h
FUW-1ASR(3) + PRO-1DAW(7) + PGL-2DAM(3) + DSW-2DAW(5) = 18h
```

Obtener todas las combinaciones que incluyan la asignatura BAE de 1ºDAM y además, que incluyan todas las asignaturas del grupo 2ºASR:

```console
$ python main.py -i BAE-1DAM -i 2ASR

FUW-1ASR(3) + BAE-1DAM(6) + IMW-2ASR(4) + DSW-2DAW(5) = 18h
BAE-1DAM(6) + IMW-2ASR(4) + PGL-2DAM(3) + DSW-2DAW(5) = 18h
```

Obtener todas las combinaciones excluyendo la asignatura PRO:

```console
$ python main.py -x PRO

FUW-1ASR(3) + BAE-1DAM(6) + IMW-2ASR(4) + DSW-2DAW(5) = 18h
BAE-1DAM(6) + IMW-2ASR(4) + PGL-2DAM(3) + DSW-2DAW(5) = 18h
```

Usar otro fichero de entrada:

```console
$ python main.py -f funny-subjects.csv
```

Todos estos parámetros se pueden combinar para conseguir filtros más potentes:

```console
$ python main.py -f mydata.csv -s3 -h17 -i PRO -x 2DAM

BAE-1DAM(6) + PRO-1DAW(7) + IMW-2ASR(4) = 17h
```
