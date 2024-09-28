<p align="center">
  <img src="img/logo-uniovi.png" alt="University of Oviedo Logo" width="200"/>
</p>

# Replication package for the thesis "Resource Characterization and Optimization for End-to-End Testing"

This repository contains the replication package of the thesis Resource Characterization and Optimization for End-to-End Testing

The replication package comprises the test scripts, Jenkinsfiles and configuration files used during the evaluation revision of the Chapter IV. The replication package is organized as follows:

## CHAPTER IV: RETORCH – End-to-End optimization through the smart characterization of the resources Evaluation.

Located in `/chapterIV` folder contains all the evaluation data and scripting of this chapter. The folder is composed by  three different subfolders

- `/chapterIV/jenkinsfiles`: contains the Jenkinsfiles of the different schedullings: [baseline](chapterIV/jenkinsfiles/Jenkinsfile_baseline), [sequential](chapterIV/jenkinsfiles/Jenkinsfile_sequential), [3-parallel](chapterIV/jenkinsfiles/Jenkinsfile_3parallel), [4-parallel](chapterIV/jenkinsfiles/Jenkinsfile_4parallel),  and the [RETORCH](chapterIV/jenkinsfiles/Jenkinsfile_RETORCH).
- `/chapterIV/envfiles` contains the  `.env` files used to deploy the SUTS in the [RETORCH's  schedullings](chapterIV/envfiles/retorch/) and the [baseline](chapterIV/envfiles/baseline)
-`/chapterIV/monitoring` contains the docker-compose to deploy and monitor the SUT as well as the python scripting to convert the prometheus API output to a Excel-format compatible output.




