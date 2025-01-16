# demo-datasets

Demo datasets suitable for direct upload to a Blind Insight instance. These datasets are designed to be used with the `blind` CLI for the purpose of testing, development, and demonstration.

## Structure

- `datasets/` is the top-level directory containing all datasets.
- Each subdirectory therein represents a dataset name.
- Each individual dataset contains `data` and `schemas` directories.

```bash
datasets
├── medical
│   ├── data
│   │   ├── condition_data.json
│   │   ├── medication_data.json
│   │   ├── patient_data.json
│   │   ├── procedure_data.json
│   │   └── wearable_data.json
│   └── schemas
│       ├── condition.json
│       ├── medication.json
│       ├── patient.json
│       ├── procedure.json
│       └── wearable.json
```

Therefore you can use the `blind` CLI to easily create a dataset from the top-level directory name:

Hint: For this example, the Organization slug is `demo`.

```bash
blind dataset create --organization demo --name medical
```

And then for each dataset, you can create each schema:

```bash
blind schema create --organization demo --dataset medical --name condition --file datasets/medical/schemas/condition.json
```

And then for each schema, you can upload the data:

```bash
blind record create --organization demo --dataset medical --schema condition --file datasets/medical/data/condition_data.json
```

Good luck and have fun!

## Further Reading

If you get stuck or need help, please checkout the [Getting Started](https://docs.blindinsight.io/getting-started/) guide on the official [Blind Insight documentation](https://docs.blindinsight.io/).

## Scripts

[!NOTE] You need to have the `faker`, `faker-datasets` and `pytz` Python packages installed to use the `generate` script. They are not required to use the `blind` CLI. You may install the script dependencies with:

```bash
pip install -r requirements.txt
```

If you want to use the `generate` script to create a dataset, you can run it like this:

```bash
python scripts/generate datasets/medical/schemas/wearable.json 100 > datasets/medical/data/wearable_data.json
```

This will generate 100 rows of data and save it to `datasets/medical/data/wearable_data.json`.

You can then upload the data using the `blind` CLI:

```bash
blind record create --organization demo --dataset medical --schema wearable --file datasets/medical/data/wearable_data.json
```
