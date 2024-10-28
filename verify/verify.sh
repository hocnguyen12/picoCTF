#!/bin/bash
# Checks if files in a directory have the same sha256 hash as the reference checksum provided

if [ "$#" -ne 2 ]; then
    echo "Expected usage: $0 <directory> <reference checksum>"
    exit 1
fi

dir="$1"
ref_checksum="$2"

# Vérifie que le dossier existe
if [ ! -d "$dir" ]; then
    echo "Error: The directory does not exist."
    exit 1
fi

if [ ! -f "$ref_checksum" ]; then
    echo "Error: The file containing the reference checksum does not exist."
    exit 1
fi

checksum=$(cat "$ref_checksum" | tr -d ' \n')

# Parcourt chaque fichier du dossier
for file in "$dir"/*; do
    # Vérifie que l'élément est bien un fichier
    if [ -f "$file" ]; then
        # Calcule le hash du fichier
        hash_file=$(sha256sum "$file" | awk '{ print $1 }')

        # Compare le hash du fichier avec le hash de référence
        if [ "$hash_file" == "$checksum" ]; then
            echo "$file has the same hash as the reference checksum."
        fi
    fi
done
