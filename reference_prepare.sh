#Download Refrence
echo -e "Downloading Human Reference and Annotation\n"
wget ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_33/GRCh38.primary_assembly.genome.fa.gz
wget ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_33/gencode.v33.primary_assembly.annotation.gtf.gz 
echo -e "Downloading Mouse Reference and Annotation\n"
wget ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M24/GRCm38.primary_assembly.genome.fa.gz
wget ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M24/gencode.vM24.primary_assembly.annotation.gtf.gz
echo -e "Unzipping Reference and Annotation\n"
gunzip *.gz

#change chr to mchr in mm
echo -e "Processing mouse Chromosome\n"
sed -i 's/chr/mchr/' GRCm38.primary_assembly.genome.fa
sed -i 's/chr/mchr/' gencode.vM24.primary_assembly.annotation.gtf
##Chimeric

if [ ! -d "./hg_mm" ]
  then
     mkdir hg_mm
     cd hg_mm/
	 echo -e "Preparing Chimeric Reference\n"
     cat  ../GRCh38.primary_assembly.genome.fa ../GRCm38.primary_assembly.genome.fa > GRC.human_mouse.fa
     cat  ../gencode.v33.primary_assembly.annotation.gtf ../gencode.vM24.primary_assembly.annotation.gtf > gencode.human_mouse.gtf
     rsem-prepare-reference --gtf gencode.human_mouse.gtf --star --star-path  /usr/bin -p 16 GRC.human_mouse.fa GRChg_mm
     cd ..
fi
##Hg
echo -e "Preparing Human Reference\n"
if [ ! -d "./hg" ]
  then
     mkdir hg	
     cd hg/
     rsem-prepare-reference --gtf ../gencode.v33.primary_assembly.annotation.gtf --star --star-path /usr/bin -p 16 ../GRCh38.primary_assembly.genome.fa GRCh38
     cd ..
fi