import logging
logging.basicConfig(filename=snakemake.log[0], level=logging.DEBUG)

import cdsapi
c = cdsapi.Client()

month = int(snakemake.params.month)
if (month<10):
  month2 = '0' + str(month)
else:
  month2 = str(month)

c.retrieve(
snakemake.config["resource"],

{
  "area": snakemake.config["area"],
  "dataset_short_name": snakemake.config["dataset_short_name"],
  "day": snakemake.config["day"],
  "format": snakemake.config["format"],
  "month": month2,
  "time": snakemake.config["time"],
  "variable": snakemake.config["variables"],
  "year": snakemake.params.year
}

,
snakemake.output[0]
)
