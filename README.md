# BlackSheep-CLI
🛠️ CLI to start BlackSheep projects.

- Interactive project scaffolding
- Support for configuring more `cookiecutter` project templates

```bash
pip install blacksheep-cli
```

## Official project templates

- `api`, to scaffold Web API projects
- `mvc`, to scaffold Web Apps projects with Model, View, Controller
   architecture, including Server Side Rendering of HTML views (SSR)

## Creating a new project

```bash
blacksheep create
```

## Listing the project templates

```bash
blacksheep templates list
```

With details:

```bash
blacksheep templates details
```

## How to contribute

- clone this repository
- create a Python virtual environment
- install in development mode `pip install -e .`
- add new commands, test
