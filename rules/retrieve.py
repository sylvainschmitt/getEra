rule retrieve:
    output:
        temp("results/raw/{year,[0-9]+}_{month,[0-9]+}.nc")
    log:
        "results/logs/{year}_{month}.log"
    benchmark:
        "results/benchmarks/{year}_{month}.benchmark.txt"
    singularity: 
        config["cdsapi"]
    threads: 1
    params:
        year="{year}",
        month="{month}"
    script:
        "../scripts/retrieve.py"
        
