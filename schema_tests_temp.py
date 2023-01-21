import yaml
from jsonschema import validate


def main() -> None:
    with open("demo-org.yml", "r") as file:
        obj = yaml.safe_load(file)

    with open("organisation-schema.json", "r") as file:
        schema = yaml.safe_load(file)

    validate(instance=obj, schema=schema)


if __name__ == '__main__':
    main()