#!/usr/bin/env bash

# Get and save latest data
curl -k --ciphers 'DEFAULT:!DH' https://www.epicentro.iss.it/coronavirus/open-data/covid_19-iss.xlsx --output data/latest/data.xlsx 