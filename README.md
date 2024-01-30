# "Parallel developmental changes in children's production and recognition of line drawings of visual concepts" 

This repository is designed to share the data, code, and figures that support the above paper. 

## Overview
The repository is organized into the following sections:

* *Experiments*  - Javascript code for the main experiments listed in the main (production & recognition). These are designed to be hosted on a node.js webserver; backend code writes the data and images to a private mongodb server. 

  * A minimal working interface for collecting sketches with paper.js can be found:
https://github.com/cogtoolslab/sketch_min

* *Preprocess drawings* - These folders contain code for pulling the full drawing datasets from the mongodb server and creating and sets of the data to be filtered by crowd-sourced, online experiments. The codebase for the filtering experiments can be found here: https://github.com/cogtoolslab/gallerize.

* *Model classifications* - Contains code to obtain model classificatinos (preprocessed vgg and clip classifications are in the data folder, under *preprocessed_data*) for two different models were used to obtain classifications of the drawings in the larger dataset. Python code for obtanining feature activations and logistic regression classifications (regressions for VGG embeddings only; a .yml file is included for setup); this code is adapted to be run on two different large computing clusters. There are two separate sets of files as the classifications were obtained separately for the full dataset and the smaller dataset used for the drawing recognition experiments, and the filenaming conventions and metadata were slightly different. 

* *Data* - Contains both raw and preprocessed data for generating the anlayses.
Inside "Data", there are several notable folders:

  * Figures_out - contains the pdfs of the figures in the paper
  * Figures_csv - contains the preprocessed data for each figure
  * Drawings - contains .zip files with the pngs of the drawings

CSV files with all of the drawings and their stroke information are located in the OSF repository as they are too large to be hosted on GitHub (see link below.)
Note that for data storage efficiency, many of the larger data files are stored as .RData vs. csvs.

* *Analysis* - Step by step anlaysis files that generate the figures and inferential statistics in the paper, written mostly in R and RMarkdown. At the end of each file are the exact versions of R and associated packages used to generate the figures and data.
HTML files show both the code and the rendered figures.

  * step0_preprocess_clip_classification.Rmd - preprocessees the CLIP classification outputs (from model classifications)
  * step0a_merge_metadata.Rmd - merges metadata from different datasources
  * step1_preprocess_and_merge_datasets.Rmd - merges all of the different drawing classification datasets
  * step2_part_annotations_preprocess.Rmd - pre-processess the semantic part annotation data
  * step3_classifications_by_age.Rmd - Shows drawing classifications by children's age; outputs figures in main text and appendix.
  * step4_production_main_analyses.Rmd - Runs main analyses understanding changes in drawing classification accuracy across development
  * step5_recognition_main_analysis.Rmd - Runs main analyses understanding changes in drawing recognition accuracy across development
  * step6_recognition_figures_and_part_analyses.Rmd - Outputs additional analyses of children's drawing recognition, including relating recognition to the presence of annotated semantic parts.
  * step7_recognition_with_clip.Rmd - Reruns recognition analyses using CLIP classifications as a robustness check.
  * step8_production_vs_recognition.Rmd - Relates drawing production vs. recognition at the item level as an exploratory analysis.

## Associated repositories
Two other repositories are associated with this proejct:

Part annotations experiment and preprocessing code: https://github.com/cogtoolslab/kiddraw_annotations_public2022
Tracing experiment and preprocessing code: https://github.com/cogtoolslab/visuomotor_model_in_drawing
Filtering experiments were run using a verion of https://github.com/cogtoolslab/gallerize

## Links to papers and resources:
This repository is linked to the associated OSF page:
https://osf.io/qymjr/

and the following preprint:
https://psyarxiv.com/5yv7x/

## Installation
The following repository integrates tools from open-source software packages to create the dataset and anlayses described in the paper; this is not a software package.

If you wish to run the analyses in these notebooks on preprocessed data, 
–clone this repository
–download R and RStudio (see https://posit.co/download/rstudio-desktop/)
–install the required packages in each script (many are shared across scripts, and a list of the most common libraries are in the anlaysis directory.)
–Click the "knit" icon in RSTudio to generate html files with the analyses from scratch.
–The entire run time of all 8 notebooks should be approprimately 10-20 minutes.

Re-extracting the model embeddings for these datasets takes considerably more time and access to specialized hardware (GPUs). The preprocessed model embeddings are thus provided in the repository for re-use.

The main statistical software has been tested in RStudio with R Version R version 4.1.3 on MacOX 13.4.1, but these open-source distributions of RStudio and standard packages are reliably maintained and tend to be backwards compatible.


Please contact Bria Long (brialorelle@gmail.com) with questions.
