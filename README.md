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

    TUO,1,1ASR
    FUW,3,1ASR
    IMW,4,2ASR
    BAE,6,1DAM
    PGL,3,2DAM
    PRO,7,1DAW
    DSW,5,2DAW
    FCT,4,2DAM

> 💡 &nbsp;No se espera ninguna cabecera.

Por defecto, se espera que el nombre del fichero de datos sea `subjects.csv` (alojado en el directorio de trabajo del proyecto) aunque puede modificarse mediante argumentos de línea de comandos.

## Modo de uso

```console
$ python main.py --help
Usage: main.py [OPTIONS]

Options:
  -f, --filename PATH        Subjects filename (csv format)  [default:
                             subjects.csv]
  -h, --hours INTEGER        Number of hours to reach within each schedule
                             [default: 18]
  -r, --hours-range INTEGER  Schedules will be in [hours - hours-range, hours
                             + hours-range]  [default: 0]
  -s, --max-size INTEGER     Maximum number of subjects within each schedule.
                             If -1 all sizes are valid.  [default: -1]
  --gmin INTEGER             Minimum number of (different) groups within each
                             schedule.  [default: 1]
  --gmax INTEGER             Maximum number of (different) groups within each
                             schedule. If -1 no restriction is applied.
                             [default: -1]
  --smin INTEGER             Minimum number of hours for each subject in
                             schedule.   [default: 1]
  --smax INTEGER             Maximum number of hours for each subject in
                             schedule.   [default: 30]
  -i, --include TEXT         Include this subject, group or subject-group
  -x, --exclude TEXT         Exclude this subject, group or subject-group
  --color / --no-color       [default: color]
  -o, --output PATH          Output schedules to this filename in csv format.
  --help                     Show this message and exit.
```

## Ejecución sin parámetros

En una ejecución sin parámetros, la herramienta buscará **todas las combinaciones posibles de las asignaturas de entrada** (`subjects.csv`) que cumplan con los **valores por defecto**:

```console
$ python main.py
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ S5           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ BAE-1DAM (6) │ PRO-1DAW (7) │ DSW-2DAW (5) │              │              │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │              │ 4 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 18 │
│ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 3 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 4 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
15 available schedules!
```

> 💡 &nbsp;`G` representa el número de grupos y `H` representa el número total de horas.

Dentro de cada fila las asignaturas se ordenan por grupo, y cada combinación se ordena por el número total de horas `H`.

### `-f`, `--filename`

Permite especificar un fichero de datos de entrada distinto al esperado `subjects.csv`.

```console
$ python main.py -f /tmp/subjects-data.csv
```

### `-h`, `--hours`

Permite especificar el número de horas totales que deben tener las combinaciones generadas.

```console
$ python main.py -h17
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ S5           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │              │              │ 3 │ 17 │
│ BAE-1DAM (6) │ PRO-1DAW (7) │ FCT-2DAM (4) │              │              │ 3 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PRO-1DAW (7) │              │ 3 │ 17 │
│ TUO-1ASR (1) │ PRO-1DAW (7) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 17 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ PGL-2DAM (3) │              │ 4 │ 17 │
│ TUO-1ASR (1) │ PRO-1DAW (7) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 17 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ 4 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ IMW-2ASR (4) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 3 │ 17 │
│ TUO-1ASR (1) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 17 │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
15 available schedules!
```

### `-r`, `--hours-range`

Permite especificar un rango de horas "alrededor" de `-h` para ampliar las posibles combinaciones.

```console
$ python main.py -r1
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ S5           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │              │              │ 3 │ 17 │
│ BAE-1DAM (6) │ PRO-1DAW (7) │ FCT-2DAM (4) │              │              │ 3 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PRO-1DAW (7) │              │ 3 │ 17 │
│ TUO-1ASR (1) │ PRO-1DAW (7) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 17 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ PGL-2DAM (3) │              │ 4 │ 17 │
│ TUO-1ASR (1) │ PRO-1DAW (7) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 17 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 17 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ 4 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ IMW-2ASR (4) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 17 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 3 │ 17 │
│ TUO-1ASR (1) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 17 │
│ BAE-1DAM (6) │ PRO-1DAW (7) │ DSW-2DAW (5) │              │              │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │              │ 4 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 18 │
│ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 3 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 4 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ DSW-2DAW (5) │              │ 4 │ 19 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 19 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ PRO-1DAW (7) │ PGL-2DAM (3) │              │ 4 │ 19 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 19 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 19 │
│ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 19 │
│ PRO-1DAW (7) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 3 │ 19 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │ 4 │ 19 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ FCT-2DAM (4) │ 4 │ 19 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 19 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 19 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 5 │ 19 │
│ TUO-1ASR (1) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 4 │ 19 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 19 │
│ FUW-1ASR (3) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 19 │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
45 available schedules!
```

> 💡 &nbsp;`-r1` busca combinaciones con horas totales en el rango `[18 - 1, 18 + 1] = [17, 19]`.

### `-s`, `--max-size`

Permite especificar el tamaño máximo de cada combinación de asignaturas.

```console
$ python main.py -s4
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ BAE-1DAM (6) │ PRO-1DAW (7) │ DSW-2DAW (5) │              │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │ 4 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ FCT-2DAM (4) │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ FCT-2DAM (4) │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
│ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 3 │ 18 │
│ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 3 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
10 available schedules!
```

### `--gmin`, `--gmax`

Permiten especificar el número mínimo y/o máximo de grupos distintos que aparecen en las combinaciones generadas.

```console
$ python main.py --gmin 3 --gmax 4
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ S5           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ BAE-1DAM (6) │ PRO-1DAW (7) │ DSW-2DAW (5) │              │              │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │              │ 4 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 18 │
│ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 3 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 4 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
15 available schedules!
```

### `--smin`, `--smax`

Permiten especificar el número mínimo y/o máximo de horas para cada asignatura de las combinaciones generadas.

```console
$ python main.py --smin 3 --smax 6
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 4 │ 18 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
│ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 3 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
4 available schedules!
```

### `-i`, `--include`

Permite especificar patrones que deben existir en las combinaciones generadas.

```console
$ # incluir la asignatura FUW y el grupo 2DAW
$ python main.py -i FUW -i 2DAW
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ S5           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
4 available schedules!
```

```console
$ # incluir la asignatura concreta de IMW que se imparte en el grupo 2ASR
$ python main.py -i IMW-2ASR
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ S5           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ 4 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 4 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
8 available schedules!
```

```console
$ # incluir los grupos de ASR (en este caso 1ASR y 2ASR)
$ python main.py -i ASR
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ S5           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ IMW-2ASR (4) │              │ 4 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ PRO-1DAW (7) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ FCT-2DAM (4) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ BAE-1DAM (6) │ FCT-2DAM (4) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ DSW-2DAW (5) │              │ 4 │ 18 │
│ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │              │ 3 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ IMW-2ASR (4) │ FCT-2DAM (4) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ IMW-2ASR (4) │ PGL-2DAM (3) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ BAE-1DAM (6) │ PGL-2DAM (3) │ DSW-2DAW (5) │ 4 │ 18 │
│ TUO-1ASR (1) │ FUW-1ASR (3) │ PRO-1DAW (7) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 3 │ 18 │
│ TUO-1ASR (1) │ BAE-1DAM (6) │ IMW-2ASR (4) │ PGL-2DAM (3) │ FCT-2DAM (4) │ 4 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
13 available schedules!
```

> 💡 &nbsp;La búsqueda de patrones se realiza a nivel de subcadenas de caracteres lo que nos da flexibilidad a la hora de usar estos filtros.

### `-x`, `--exclude`

Permite especificar patrones que no deben existir en las combinaciones generadas.

```console
$ python main.py -x ASR
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━┳━━━━┓
┃ S1           ┃ S2           ┃ S3           ┃ S4           ┃ G ┃ H  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━╇━━━━┩
│ BAE-1DAM (6) │ PRO-1DAW (7) │ DSW-2DAW (5) │              │ 3 │ 18 │
│ BAE-1DAM (6) │ PGL-2DAM (3) │ FCT-2DAM (4) │ DSW-2DAW (5) │ 3 │ 18 │
└──────────────┴──────────────┴──────────────┴──────────────┴───┴────┘
2 available schedules!
```

### `--color`, `--no-color`

Permite especificar si la salida estará coloreada o no.

### `-o`, `--output`

Permite especificar una ruta a un fichero de salida donde se guardarán las combinaciones generadas en formato csv.

### Combinando argumentos

Todos estos argumentos se pueden combinar para conseguir filtros más potentes:

```console
$ python main.py -i PRO -s4 --gmax 3 --smin 5
```

## Tests

Existen [tests](tests) para comprobar el correcto funcionamiento de la herramienta:

```console
$ pip install pytest
$ pytest
```
