# demo-datasets

Demo datasets suitable for direct upload.

## Structure

- Each top-level directory represents a dataset name.
- Each inner directory contains `data` and `schemas` directories and should be named as such:

```bash
medical
├── data
│   ├── condition_data.json
│   ├── medication_data.json
│   ├── patient_data.json
│   ├── procedure_data.json
│   └── wearable_data.json
└── schemas
    ├── condition.json
    ├── medication.json
    ├── patient.json
    ├── procedure.json
    └── wearable.json

2 directories, 10 files
```

Therefore you can use the `blind` CLI to easily create a dataset from the top-level directory name:

Hint: For this example, the Organization slug is `example`.

```bash
blind dataset create --organization example --name medical
```

And then for each dataset, you can create each schema

```bash
blind dataset --organization example create --dataset medical --name condition --file medical/schemas/condition.json
```

And then for each schema, you can upload the data:

```bash
blind record create --organization example --dataset medical --schema condition -f medical/data/condition_data.json
```

Good luck and have fun!

## Further Reading

If you get stuck or need help, please checkout the [Getting Started](https://docs.blindinsight.io/getting-started/) guide on the official [Blind Insight documentation](https://docs.blindinsight.io/).

## Scripts

[!NOTE] You need to have the `faker` and `pytz` Python packages installed to use the `generate` script. They are not required to use the `blind` CLI. You may install the script dependencies with:

```bash
pip install -r requirements.txt
```

If you want to use the `generate` script to create a dataset, you can run it like this:

```bash
python scripts/generate medical/schemas/wearable.json 100 > medical/data/wearable_data.json
```

This will generate 100 rows of data and save it to `medical/data/wearable_data.json`.

You can then upload the data using the `blind` CLI:

```bash
blind record create -O demo -D medical -n wearable -f medical/data/wearable_data.json
```
