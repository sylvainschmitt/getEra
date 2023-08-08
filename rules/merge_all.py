rule merge_all:
    input:
        expand("results/raw/{year}.nc", year=config["year"])
    output:
        "results/ERA5land.nc"
    log:
        "results/logs/all.log"
    benchmark:
        "results/benchmarks/all.benchmark.txt"
    singularity: 
        "docker://alexgleith/cdo"
    threads: 1
    shell:
        "cdo -b F64 mergetime {input} {output}"
