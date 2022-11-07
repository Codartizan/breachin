# FWA Automated Test Suite

## Table of Content
* [General Information](#general-info)
* [Environment](#environment)
* [Usage](#usage)
* [Project Structure](#project-structure)

## General info
This project includes scripts and output data that used in research paper: 
An Investigation of Breaking Changes in Python Software Programs

## Environment
* phase1_data_selection : Python 3.10
* phase2_extract_diffs1 : Python 3.10
* phase3_extract_diffs2 : Java 11

## Usage
This project only records the scripts that are used in the steps of data collection and dependency change pattern extraction.
Breaking change detection was done manually in docker environments which are not included in this repository. All the data 
outcome and scripts here are intended to answer research question 1. Three sub-projects were included in this project. 
The first project is phase1_data_selection which includes all the scripts for extracting Python dependencies and dependent 
packages by consuming Libraries.io APIs. phase2_extract_diffs1 project includes all the scripts to extract file-level changes 
between the benchmark and target versions of dependencies. Also, extracted functions change, class change, and module change 
from changed Python files and output file diffs for unchanged Python files. phase3_extract_diffs2 based on the output of 
unchanged Python files diffs, extracted all function, class, and module changes. (unchanged Python files here means the 
Python file that remained the same file name and relative path in the benchmark and target version).


## Project structure
<pre>
|-- breachin  
|    |-- output  
|        |-- ResearchData.numbers # data and figures used in the paper
|    |-- phase1_data_selection
|        |-- .pytest_cache
|        |-- Archive # data output
|        |-- bin # Browser driver binary
|        |-- docs # data output
|        |-- pylint # data output
|        |-- src
|                |-- dependency # scripts for extracting dependency projects
|                |-- dependent # scripts for extracting dependent packages
|                |-- util # general utilities
|                |-- __init__.py
|        |-- test # extraction entry
|        |-- .travis.yml
|        |-- Dockerfile
|        |-- Dockerfile-perfect-python
|        |-- entrypoint.sh
|        |-- note.txt
|        |-- requirements.txt
|    |-- phase2_extract_diffs1 #Gmail API tokens
|        |-- libraries_io_api # scripts for package extraction from Libraries.io
|        |-- output # dependency diffs output
|        |-- project_diff
|                |-- __init__.py
|                |-- code_parser.py
|                |-- constant.py
|                |-- file_diff.py
|                |-- import_diff.py
|                |-- output_func_claz_change.py # get functions and classes diffs from changed python files
|                |-- output_module_changes.py # get module diffs from changed python files
|                |-- output_unchanged_file_diff.py # get file diffs from unchanged python files
|                |-- project_diff.py
|                |-- regex.py
|                |-- __init__.py
|        |-- __init__.py
|        |-- generic.py
|        |-- requirements.txt
|    |-- phase3_extract_diffs2 #Selenoid browser images definition
|        |-- src
|                |-- main
|                        |-- java
|                                |-- org.example 
|                                        |-- Dependent.java # get all dependent package for a dependency
|                                        |-- DiffCompare.java # get all funcs, claz, mod diffs from unchanged python files
|                                        |-- ExtractImport.java # get all import diffs
|                                        |-- GetAllCodeUnitsFromFolder.java # Utility for get all code unit stats from a project
|                                        |-- GetAllCodeUnitsFromList.java # Utility for get all code unit stats from a list of files
|                                        |-- searchCode # plain java objs for extracting dependent response
|                        |-- resources
|                |-- test
|        |-- pom.xml
|    |-- readme.md
 </pre>
  