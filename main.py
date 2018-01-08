import csv
import json

import config
from transfer import transfer_pst

if __name__ == '__main__':
    tx = []
    with open(config.csv_file) as f:
        tx = list(transfer_pst([row for row in csv.DictReader(f)]))

    print("\n\n", json.dumps(tx, sort_keys=True, indent=2))
