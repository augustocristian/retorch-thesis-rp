<p align="center">
  <img src="img/logo-uniovi.png" alt="University of Oviedo Logo" width="200"/>
</p>

# Replication package for the thesis "Resource Characterization and Optimization for End-to-End Testing"

This repository contains the replication package of the thesis Resource Characterization and Optimization for End-to-End
Testing

The replication package comprises the test scripts, Jenkinsfiles and configuration files used during the evaluation
revision of the Chapter IV. The replication package is organized as follows:

## CHAPTER IV: RETORCH – End-to-End optimization through the smart characterization of the resources Evaluation.

Located in `/chapterIV` folder contains all the evaluation data and scripting of this chapter. The folder is composed by
three different subfolders

- `/chapterIV/jenkinsfiles`: contains the Jenkinsfiles of the different execution
  plans: [baseline](chapterIV/jenkinsfiles/Jenkinsfile_baseline), [sequential](chapterIV/jenkinsfiles/Jenkinsfile_sequential), [3-parallel](chapterIV/jenkinsfiles/Jenkinsfile_3parallel), [4-parallel](chapterIV/jenkinsfiles/Jenkinsfile_4parallel),
  and the [RETORCH](chapterIV/jenkinsfiles/Jenkinsfile_RETORCH).
- `/chapterIV/envfiles` contains the  `.env` files used to deploy the SUTS in
  the [RETORCH's  schedullings](chapterIV/envfiles/retorch/) and the [baseline](chapterIV/envfiles/baseline)
- `/chapterIV/monitoring` contains the docker-compose to deploy and monitor the SUT as well as the python scripting to
  convert the prometheus API output to a Excel-format compatible output.

### Monitoring

The monitorization of the E2E test suite execution is done through prometheus and CAdvisor. After the execution plan is
executed, we got the memory and processor usage thrrough the prometheus API with the following requests:

#### Memory:

```url
http://[URL]:[PORT]/api/v1/query_range?query=rate(container_cpu_usage_seconds_total{id="/"}[1m])&start=[STARTUNIXTIME]&end=[ENDUNIXTIME]&step=1
```

#### Processor:

```url
http://[URL]:[PORT]/api/v1/query_range?query=container_memory_usage_bytes{id="/"}/1024/1024/1024&start=[STARTUNIXTIME]&end=[ENDUNIXTIME]&step=1
```

## Citing this work

Resource Characterization and Optimization for End-to-End Testing

- Cristian Augusto, *"Resource Characterization and Optimization for End-to-End Testing"*,
  University of Oviedo, pp. 1–TO-DO, Gijón,Asturias (Spain), TO-DO 2025,  [Thesis available](TO-DO) -
  [Download citation](TO-DO)

RETORCH: an approach for resource-aware orchestration of end-to-end test cases:

- Cristian Augusto, Jesús Morán, Antonia Bertolino, Claudio de la Riva, and Javier Tuya,
  *“RETORCH: an approach for resource-aware orchestration of end-to-end test cases”*,
  *Software Quality Journal*, vol. 28, no. 3, 2020.
  https://doi.org/10.1007/s11219-020-09505-2 - [Full Article available](https://link.springer.com/article/10.1007/s11219-020-09505-2) - [Authors version](https://digibuo.uniovi.es/dspace/bitstream/handle/10651/55405/RETORCHSQJExtension_BUO.pdf;jsessionid=0E661594C8732B8D2CA53636A31E4FD5?sequence=1) -
  [Download citation](https://citation-needed.springer.com/v2/references/10.1007/s11219-020-09505-2?format=refman&flavour=citation)

RETORCH*: A Cost and Resource aware Model for E2E Testing in the Cloud:

- Cristian Augusto, Jesús Morán, Antonia Bertolino, Claudio de la Riva, and Javier Tuya,
  *“RETORCH*: A Cost and Resource aware Model for E2E Testing in the Cloud”*,
  *Journal of Systems and Software*, vol. 221 , pages. 112237, 2025.
  https://doi.org/10.1016/j.jss.2024.112237 - [Full Paper available](https://www.sciencedirect.com/science/article/pii/S0164121224002814?via%3Dihub) - [Authors version](https://hdl.handle.net/10651/75794) -
  [Download citation](https://www.sciencedirect.com/science/article/pii/S0164121224002814?via%3Dihub#:~:text=Export%20citation%20to%20text)

Exploratory study of the usefulness of LLMs in System testing

- Cristian Augusto, Jesús Morán, Antonia Bertolino, Claudio de la Riva, and Javier Tuya, *"Exploratory study of the
  usefulness of LLMs in System testing"*, *Proceedings of the 36th International Conference on Testing Software and
  Systems*, pp. 1–17, Springer Cham,
  2025, https://doi.org/10.1007/978-3-031-80889-0_17 - [Full Article available](TO-DO) - [Authors version](TO-DO) -
  [Download citation](TO-DO)

## Acknowledgments

This work was supported in part by the project PID2022-137646OB-C32 under Grant MCIN/ AEI/10.13039/501100011033/FEDER,
UE (EQUAVEL) and the project TestBUS (PID2019-105455GB-C32) supported by
the [Ministry of Science and Innovation (SPAIN)](https://www.ciencia.gob.es/)