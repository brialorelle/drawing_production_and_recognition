# "Parallel devleopmental changes in children's production and recognition of line drawings of visual concepts" 

This repository is designed to share the data, code, and figures that support the above paper. 

## Overview
The repository is organized into the following sections:

*Data* - Contains both raw and preprocessed data for generating the anlayses.
Inside "Data", there are several notable folders:


Figures_out - contains the pdfs of the figures in the paper
Figures_csv - contains the preprocessed data for each figure
Drawings - contains .zip files with the pngs of the drawings
CSV files with all of the drawings and their stroke information are located in the OSF repository as they are too large to be hosted on GitHub (see link below.)

Note that for data storage efficiency, many of the larger data files are stored as .RData vs. csvs.

*Analysis* - Step by step anlaysis files that generate the figures and inferential statistics in the paper, written mostly in R and RMarkdown. At the end of each file are the exact versions of R and associated packages used to generate the figures and data.
HTML files show both the code and the rendered figures.

*Experiments*  - Javascript code for the main experiments listed in the main (production & recognition). These are designed to be hosted on a node.js webserver; backend code writes the data and images to a private mongodb server. 

A minimal working interface for collecting sketches with paper.js can be found:
https://github.com/cogtoolslab/sketch_min

*Preprocess drawings* - These folders contain code for pulling the full drawing datasets from the mongodb server and creating and sets of the data to be filtered by crowd-sourced, online experiments. The codebase for the filtering experiments can be found here: https://github.com/cogtoolslab/gallerize.

*Model classifications* - Contains code to obtain model classificatinos (preprocessed vgg and clip classifications are in the data folder, under *preprocessed_data*) for two different models were used to obtain classifications of the drawings in the larger dataset. Python code for obtanining feature activations and logistic regression classifications (regressions for VGG embeddings only; a .yml file is included for setup); this code is adapted to be run on two different large computing clusters. There are two separate sets of files as the classifications were obtained separately for the full dataset and the smaller dataset used for the drawing recognition experiments, and the filenaming conventions and metadata were slightly different. 


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

Please contact Bria Long (brialorelle@gmail.com) with questions about the proejct.
