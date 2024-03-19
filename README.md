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

Therefore you can use the `bi` CLI to easily create a dataset from the top-level directory name:

```bash
bi dataset create --name medical`
```

And then for each dataset, you can create each schema

```bash
bi dataset create -D medical -n condition -f medical/schemas/condition.json
```

And then for each schema, you can upload the data:

```bash
bi record create -n condition -f medical/data/condition_data.json
```

Good luck and have fun!
