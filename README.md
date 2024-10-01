# US Political Polarization
Politics has become a large societal concern in the United States and the polarizing stances on common issues has given way to social unrest, tension, and distrust. Utilizing data from [VoteView](https://www.voteview.com) and similar analysis from [Kaggle](https://www.kaggle.com/code/justin2028/political-polarization-us-congress-data-analysis), this report expands to the next stage from determining the existance of political polarity to identification of trends and influencing factors within the contained bodies of Congress.

We acknowledge the myriad existance of factors, both significant and inferred, beyond the scope any single analysis can ascertain; instead we hope to build a foundation for expansion and insight.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [References](#references)
- [License](#license)
- [Contact](#contact)

## Introduction
This report was built for academic subission in my Data Science Tools class at the University of Denver and is retained as part of my personal portfolio.

## Installation
This repository is written in `Python 3.12` with supporting packages defined in the `requirements.txt` file. Independent installation is not required and encapsulated virtual environments are not included.

### Prerequisites
This project was built using Python 3.12 and is not compatibility-tested with other versions. Python packages used are identified in the `requirements.txt` file and is formatted for direct installation via `pip`.

```
pip install -r requirements.txt
```
## Usage
This GitHub is a self-contained data science project and designed to be accessed via folder and file tree. The source information and generating files are located in the `root` folder with report extracts, including HTML and PDF documents, located in the `reports` subfolder.

### Analysis Files
the python notebook files are independent analysis depending on the aspect or function of the analysis. Because each notebook is a self-contained group of analysis, there may be overlap or duplicity in the content from one notebook to another.

### Initializing Datasets
> <span style="color: red;">Initializing data is not required to view any outputs of this report, see `reports` subfolder for self-contained and pre-generated outputs.</span>

Due to large file size constraints with GitHub, the source data is not directly included with this repository. To initialize the data files, execute the `Initialize Environment` block in any of the analysis `nb*` notebook files.

## Data
Primary datasets were obtained from [VoteView](https://www.voteview.com) as of 2024-09-29. Supplemental datasets were compiled manually via accumulated public information sources including:

- [BBC News](https://www.bbc.com/news/world-us-canada-16759233)
- [Library of Congress: US History](https://www.loc.gov/classroom-materials/united-states-history-primary-source-timeline/)
- [Library of Congress: President History](https://guides.loc.gov/presidents-portraits/chronological)

### References
Additional resource references supplemental to data processing and analysis:
- [*Substance and Change in Congressional Ideology* by Devin Caughey and Eric Schickler](http://hdl.handle.net/1721.1/105926)
- [*Broken Contract?* by Stephen C Craig](https://doi.org/10.4324/9780429502002)
- [*The Punishment of Negationism* by Emanuela Fronza](https://lawreview.vermontlaw.edu/wp-content/uploads/2012/02/fronza.pdf)
- [*The Red Scare* by the History Channel](https://www.history.com/topics/cold-war/red-scare)
- [*Spacial Modeling of Parliamentary Voting* by Keith T Poole](https://doi.org/10.1017/CBO9780511614644)
- [*An Estimator of Mutual Information and its Application to Independence Testing* by Joe Suzuki](https://doi.org/10.3390/e18040109)

## License
[MIT License 2024](https://choosealicense.com/licenses/mit/)

## Contact
**AJ Marcus**<br>
[Copper Panda Consulting](http://www.copper-panda.consulting)<br>
[github@copper-panda.consulting](mailto:github@copper-panda.consulting)