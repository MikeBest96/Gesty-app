# CRUD básico con archivo JSON

Este proyecto implementa un CRUD simple en Python con separación clara:

- `data_store.py`: acceso y persistencia de datos en `data.json`.
- `crud.py`: lógica de negocio (create, read, update, delete).
- `app.py`: interfaz CLI y orquestación.

## Uso

```bash
python3 app.py create "Tarea 1" "Primera tarea"
python3 app.py list
python3 app.py get 1
python3 app.py update 1 --name "Tarea actualizada"
python3 app.py delete 1
```
