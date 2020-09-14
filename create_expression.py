import sys
import csv
import time
import os
#USAGE:   python fastq_download.py PE/SE subtypeData.txt 


start = time.time()
readtype = sys.argv[1]
filename = sys.argv[2]



with open(filename,'r') as csv_file:
    reader =csv.reader(csv_file, delimiter='\t')
    if readtype == "PE" :
        print("PE")
        for row in reader:
            print("Downloading "+row[1]+" data "+row[0]+"...")
            os.system(" fastq-dump -I --split-files "+row[0]+" ")
            print("Trimming sample"+row[0]+"...")
            os.system("~/TrimGalore-0.6.6/trim_galore --fastqc --illumina --length 25 --fastqc --cores 8  --paired "+row[0]+"_1.fastq "+row[0]+"_2.fastq ")
            if row[1]== "PDX":
                print ("Mapping PDX sample",row[0],"...")
                os.system("STAR --genomeDir ./hg_mm --runMode alignReads --runThreadN 16 --readFilesIn "+row[0]+"_1_val_1.fq "+row[0]+"_2_val_2.fq --readFilesType Fastx --limitBAMsortRAM 80000000000 --quantMode TranscriptomeSAM --twopassMode Basic --alignIntronMax 1000000 --alignIntronMin 20 --alignMatesGapMax 1000000 --alignSJDBoverhangMin 10 --alignSJstitchMismatchNmax 5 -1 5 5 --chimJunctionOverhangMin 12 --chimNonchimScoreDropMin 10 --chimMultimapNmax 20  --chimMultimapScoreRange 3 --chimOutJunctionFormat 1 --chimSegmentMin 12 --chimScoreJunctionNonGTAG -4 --peOverlapMMp 0.1 --peOverlapNbasesMin 12 --outFilterMismatchNmax 999 --outFilterMismatchNoverReadLmax 0.04 --outFilterMultimapNmax 20 --outFilterType BySJout --outReadsUnmapped Fastx --outSAMattrRGline ID:GRPundef --outSAMtype BAM SortedByCoordinate --outWigNorm None --outWigType wiggle --outSAMunmapped Within --outSAMstrandField intronMotif --outFileNamePrefix  "+row[0]+" ")
                
                print("Read quantification"+row[0]+"...")
                os.system("rsem-calculate-expression --paired-end --alignments --bam --no-bam-output --seed 12345 -p 8 "+row[0]+"Aligned.toTranscriptome.out.bam  ./hg_mm/GRChg_mm "+row[0]+" ")
            elif row[1]== "Cell line":
                print ("Mapping Cell line sample",row[0],"...")
                os.system("STAR --genomeDir ./hg --runMode alignReads --runThreadN 16 --readFilesIn "+row[0]+"_1_val_1.fq "+row[0]+"_2_val_2.fq --readFilesType Fastx --limitBAMsortRAM 80000000000 --quantMode TranscriptomeSAM --twopassMode Basic --alignIntronMax 1000000 --alignIntronMin 20 --alignMatesGapMax 1000000 --alignSJDBoverhangMin 10 --alignSJstitchMismatchNmax 5 -1 5 5 --chimJunctionOverhangMin 12 --chimNonchimScoreDropMin 10 --chimMultimapNmax 20  --chimMultimapScoreRange 3 --chimOutJunctionFormat 1 --chimSegmentMin 12 --chimScoreJunctionNonGTAG -4 --peOverlapMMp 0.1 --peOverlapNbasesMin 12 --outFilterMismatchNmax 999 --outFilterMismatchNoverReadLmax 0.04 --outFilterMultimapNmax 20 --outFilterType BySJout --outReadsUnmapped Fastx --outSAMattrRGline ID:GRPundef --outSAMtype BAM SortedByCoordinate --outWigNorm None --outWigType wiggle --outSAMunmapped Within --outSAMstrandField intronMotif --outFileNamePrefix  "+row[0]+" ")
                os.system("rsem-calculate-expression --paired-end --alignments --bam --no-bam-output --seed 12345 -p 8 "+row[0]+"Aligned.toTranscriptome.out.bam  ./hg/GRCh38 "+row[0]+" ")
            elif row[1]== "Patient data":
                print ("Mapping Patient data sample"+row[0]+"...")
                os.system("STAR --genomeDir ./hg --runMode alignReads --runThreadN 16 --readFilesIn "+row[0]+"_1_val_1.fq "+row[0]+"_2_val_2.fq --readFilesType Fastx --limitBAMsortRAM 80000000000 --quantMode TranscriptomeSAM --twopassMode Basic --alignIntronMax 1000000 --alignIntronMin 20 --alignMatesGapMax 1000000 --alignSJDBoverhangMin 10 --alignSJstitchMismatchNmax 5 -1 5 5 --chimJunctionOverhangMin 12 --chimNonchimScoreDropMin 10 --chimMultimapNmax 20  --chimMultimapScoreRange 3 --chimOutJunctionFormat 1 --chimSegmentMin 12 --chimScoreJunctionNonGTAG -4 --peOverlapMMp 0.1 --peOverlapNbasesMin 12 --outFilterMismatchNmax 999 --outFilterMismatchNoverReadLmax 0.04 --outFilterMultimapNmax 20 --outFilterType BySJout --outReadsUnmapped Fastx --outSAMattrRGline ID:GRPundef --outSAMtype BAM SortedByCoordinate --outWigNorm None --outWigType wiggle --outSAMunmapped Within --outSAMstrandField intronMotif --outFileNamePrefix  "+row[0]+" ")
                print("Read quantification"+row[0]+"...")
                os.system("rsem-calculate-expression --paired-end --alignments --bam --no-bam-output --seed 12345 -p 8 "+row[0]+"Aligned.toTranscriptome.out.bam ./hg/GRCh38 "+row[0]+" ")
            else:
                print ("Error: Fault in processing"+row[0]+"...")
                exit    
    elif readtype == "SE" :
        print("SE")
        for row in reader:
            print("Downloading "+row[1]+" data "+row[0]+"...")
            os.system(" fastq-dump "+row[0]+" ")
            print("Trimming sample"+row[0]+"...")
            os.system("~/TrimGalore-0.6.6/trim_galore --fastqc --illumina --length 25 --fastqc --cores 8  --paired "+row[0]+".fastq ")
            if row[1]== "PDX":
                print ("Mapping PDX sample"+row[0]+"...")
                os.system("STAR --genomeDir ./hg_mm --runMode alignReads --runThreadN 16 --readFilesIn "+row[0]+"_trimmed.fq --readFilesType Fastx --limitBAMsortRAM 80000000000 --quantMode TranscriptomeSAM --twopassMode Basic --alignIntronMax 1000000 --alignIntronMin 20 --alignMatesGapMax 1000000 --alignSJDBoverhangMin 10 --alignSJstitchMismatchNmax 5 -1 5 5 --chimJunctionOverhangMin 12 --chimNonchimScoreDropMin 10 --chimMultimapNmax 20  --chimMultimapScoreRange 3 --chimOutJunctionFormat 1 --chimSegmentMin 12 --chimScoreJunctionNonGTAG -4 --peOverlapMMp 0.1 --peOverlapNbasesMin 12 --outFilterMismatchNmax 999 --outFilterMismatchNoverReadLmax 0.04 --outFilterMultimapNmax 20 --outFilterType BySJout --outReadsUnmapped Fastx --outSAMattrRGline ID:GRPundef --outSAMtype BAM SortedByCoordinate --outWigNorm None --outWigType wiggle --outSAMunmapped Within --outSAMstrandField intronMotif --outFileNamePrefix  "+row[0]+" ")
                print("Read quantification"+row[0]+"...")
                os.system("rsem-calculate-expression --alignments --bam --no-bam-output --seed 12345 -p 8 "+row[0]+"Aligned.toTranscriptome.out.bam  ./hg_mm/GRChg_mm "+row[0]+" ")
            elif row[1]== "Cell line":
                print ("Mapping Cell line sample"+row[0]+"...")
                os.system("STAR --genomeDir ./hg --runMode alignReads --runThreadN 16 --readFilesIn "+row[0]+"_trimmed.fq --readFilesType Fastx --limitBAMsortRAM 80000000000 --quantMode TranscriptomeSAM --twopassMode Basic --alignIntronMax 1000000 --alignIntronMin 20 --alignMatesGapMax 1000000 --alignSJDBoverhangMin 10 --alignSJstitchMismatchNmax 5 -1 5 5 --chimJunctionOverhangMin 12 --chimNonchimScoreDropMin 10 --chimMultimapNmax 20  --chimMultimapScoreRange 3 --chimOutJunctionFormat 1 --chimSegmentMin 12 --chimScoreJunctionNonGTAG -4 --peOverlapMMp 0.1 --peOverlapNbasesMin 12 --outFilterMismatchNmax 999 --outFilterMismatchNoverReadLmax 0.04 --outFilterMultimapNmax 20 --outFilterType BySJout --outReadsUnmapped Fastx --outSAMattrRGline ID:GRPundef --outSAMtype BAM SortedByCoordinate --outWigNorm None --outWigType wiggle --outSAMunmapped Within --outSAMstrandField intronMotif --outFileNamePrefix  "+row[0]+" ")
                print("Read quantification"+row[0]+"...")
                os.system("rsem-calculate-expression --alignments --bam --no-bam-output --seed 12345 -p 8 "+row[0]+"Aligned.toTranscriptome.out.bam  ./hg/GRCh38 "+row[0]+" ")
            elif row[1]== "Patient data":
                print ("Mapping pdx sample"+row[0]+"...")
                os.system("STAR --genomeDir ./hg --runMode alignReads --runThreadN 16 --readFilesIn "+row[0]+"_trimmed.fq --readFilesType Fastx --limitBAMsortRAM 80000000000 --quantMode TranscriptomeSAM --twopassMode Basic --alignIntronMax 1000000 --alignIntronMin 20 --alignMatesGapMax 1000000 --alignSJDBoverhangMin 10 --alignSJstitchMismatchNmax 5 -1 5 5 --chimJunctionOverhangMin 12 --chimNonchimScoreDropMin 10 --chimMultimapNmax 20  --chimMultimapScoreRange 3 --chimOutJunctionFormat 1 --chimSegmentMin 12 --chimScoreJunctionNonGTAG -4 --peOverlapMMp 0.1 --peOverlapNbasesMin 12 --outFilterMismatchNmax 999 --outFilterMismatchNoverReadLmax 0.04 --outFilterMultimapNmax 20 --outFilterType BySJout --outReadsUnmapped Fastx --outSAMattrRGline ID:GRPundef --outSAMtype BAM SortedByCoordinate --outWigNorm None --outWigType wiggle --outSAMunmapped Within --outSAMstrandField intronMotif --outFileNamePrefix  "+row[0]+" ")
                os.system("rsem-calculate-expression  --alignments --bam --no-bam-output --seed 12345 -p 8 "+row[0]+"Aligned.toTranscriptome.out.bam ./hg/GRCh38 "+row[0]+" ")
            else:
                print ("Error: Fault in processing"+row[0]+"...")
                exit  
    else :
        print("Error: Enter a valid readtype...")
    

#os.system("mkdir readFile")
#os.system("mv SRR* ./readFile/"

end = time.time()
print("total time required : ",(end-start))