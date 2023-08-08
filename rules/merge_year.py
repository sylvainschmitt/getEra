rule merge_year:
    input:
        expand("results/raw/{year}_{month}.nc", month=config["month"], allow_missing=True)
    output:
        temp("results/raw/{year}.nc")
    log:
        "results/logs/{year}.log"
    benchmark:
        "results/benchmarks/{year}.benchmark.txt"
    singularity: 
        "docker://alexgleith/cdo"
    threads: 1
    shell:
        "cdo -b F64 mergetime {input} {output}"
