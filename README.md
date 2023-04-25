## FARM-Stack Tutorial

```
Back and frontend running on different env.

Backend file strucutre:
.
├── backend              # "backend" is a Python package
│   ├── __init__.py      # this file makes "backend" a "Python package"
│   ├── main.py          # "main" module, e.g. import backend.main
│   ├── dependencies.py  # "dependencies" module, e.g. import backend.dependencies
|   └── models.py        # "models" 
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   └── users.py     # "users" submodule, e.g. import backend.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import backend.internal.admin

```
