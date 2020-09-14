# Downstream-Analysis

## Pipeline followed   
Gene Expression using Trim-galore, STAR, RSEM for Patient, Xenograft and Cell-line data.

## Run Command 
```bash
bash reference_prepare.sh
python fastq_download.py PE/SE subtypeAnnotationData.txt
```

*subtype.txt* is a tab-seperated file which contain sample information in the format -  
<(sample Acccession number) (sample subtype)>

Example:<br />
SRR8528473	Cell line <br />
SRR8528517	Patient data <br />
SRR9842107	PDX <br />





