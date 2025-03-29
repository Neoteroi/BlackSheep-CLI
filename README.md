# BlackSheep-CLI
🛠️ CLI to start BlackSheep projects.

- Interactive project scaffolding
- Support for configuring more `cookiecutter` project templates

```bash
pip install blacksheep-cli
```

```bash
blacksheep --help

blacksheep create --help
```

## Official project templates

- `api`, to scaffold Web API projects.
- `mvc`, to scaffold Web Apps projects with Model, View, Controller
   architecture, including Server Side Rendering of HTML views (SSR).

## Creating a new project

```bash
blacksheep create
```

Create a project pinned to a specific tag:

```bash
blacksheep create Example --template mvc --checkout v1.0.2
```

Tags refer to the project template repository. To see the list of tags, use the
`blacksheep templates details` and navigate to the URL of the template
repository.

## Listing the project templates

```bash
blacksheep templates list
```

See details about the templates:

```bash
blacksheep templates details
```

## How to contribute

- clone this repository
- create a Python virtual environment
- install in development mode `pip install -e .`
- add new commands, test
