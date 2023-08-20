import pytest
from click.testing import CliRunner

from blacksheepcli.cli.main import main
from blacksheepcli.templates.domain import Template

# from blacksheepcli.templates.data.default import JSONTemplatesDataProvider


def test_list_templates():
    runner = CliRunner()
    result = runner.invoke(main, ["templates", "list"])
    assert result.exit_code == 0
    assert result.output == "api\nmvc\n"


@pytest.mark.parametrize(
    "source,expected_tag",
    [
        ["~/projects/github/blacksheep-api", ""],
        ["~/projects/github/blacksheep-api$v2", "v2"],
        ["https://github.com/Neoteroi/BlackSheep-API", ""],
        ["https://github.com/Neoteroi/BlackSheep-API$", ""],
        ["https://github.com/Neoteroi/BlackSheep-API$v2", "v2"],
    ],
)
def test_template_source_tag(source, expected_tag):
    template = Template("test", source)
    assert template.tag == expected_tag
