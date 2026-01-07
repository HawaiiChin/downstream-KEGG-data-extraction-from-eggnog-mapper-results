ko <-read.table("pathway_by_sample.tsv", header=TRUE, sep="\t", row.names = 1)
gene.data <-ko[,'emap40']                                                                                                                                                                  
library(pathview)
pathview(gene.data=gene.data, pathway.id = "ko01310", species = "ko", out.suffix="emap40", kegg.native = TRUE) #nitrogen cycling pathway

#if fail, diagnosis

library(KEGGREST)
keggGet("ko03020")
