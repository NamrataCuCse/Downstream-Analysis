# Downstream-Analysis

## Pipeline followed   
Gene Expression using Trim-galore, STAR, RSEM

## Run Command 
```bash
bash DEpipeline1_v2.sh
python fastq_download.py PE/SE subtypeData.txt
```

*subtype.txt* is a tab-seperated file which contain sample information in the format -  
<(sample Acccession number) (sample subtype)>

Example:
SRR8528473	Cell line <br />
SRR8528517	Patient data <br />
SRR9842107	PDX <br />





