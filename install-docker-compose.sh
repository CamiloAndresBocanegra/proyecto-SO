#!/usr/bin/env bash
#
#D Este script permite la instalacion del comando docker-compose en el 
#D directorio actual
#
#A Autor: John Sanabria - john.sanabria@correounivalle.edu.co
#F Fecha: 11-01-2023 
#
OUTPUT_FILE="./docker-compose"
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o ${OUTPUT_FILE}
chmod +x ${OUTPUT_FILE}
