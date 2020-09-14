# Downstream-Analysis

## Pipeline followed   
Gene Expression using Trim-galore, STAR, RSEM for Patient, Xenograft and Cell-line data.

## Run Command 
```bash
bash reference_prepare.sh
python fastq_download.py PE/SE subtypeAnnotationData.txt
```

### Info
1. *reference_prepare.sh* will process the human and mouse references for preparing chimeric reference and annotation which will be used for PDX data. It will then perform *rsem-prepare-reference* for both human and chimeric reference using parameter --STAR. 
2. *fastq_download.py* take the readtype - paired ended or single ended, and the subtype information as argument. It will then perform quality check using Trimgalore, STAR alignment and RSEM read quantification on the sample data. 
3. *subtype.txt* is a tab-seperated file which contain sample information in the format -  
<(sample Acccession number) (sample subtype)>

  Example:<br />
    SRR8528473	Cell line <br />
    SRR8528517	Patient data <br />
    SRR9842107	PDX <br />





