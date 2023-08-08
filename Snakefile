configfile: "config/config_test.yml"

rule all:
   input:
         expand("results/ERA5land.nc")
                
# Rules #
include: "rules/retrieve.py"
include: "rules/merge_year.py"
include: "rules/merge_all.py"
