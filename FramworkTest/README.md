#### This is a framework using selenium and bdd with python

## Selenium

Is a framework for automating browser interactions
## Behave

Is a framework for BDD .It is a common language syntax which can be used to define steps for end to end tests. 

## Getting Started
Install python
Install selenium
Install drivers
Install Allure

## To run test
py -m behave -f allure_behave.formatter::AllureFormatter -o reports/

## to transform json report to html run
py -m allure serve reports/

