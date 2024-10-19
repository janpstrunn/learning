#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path/to/file or path/to/folder>"
    exit 1
fi
file2enc="$1"
chuck_prefix="chuck"
encrypted_folder="Encrypted_Vault"
if [ ! -d "mount" ]; then
    mkdir "mount"
fi
if [ ! -d "Encrypted_Vault" ]; then
    mkdir "Encrypted_Vault"
fi
if [ -d "$encrypted_folder" ]; then
    if [ ! -f "$encrypted_folder/gocryptfs.conf" ]; then
        gocryptfs -init "$encrypted_folder"
    fi
fi
tar -czvf "${chuck_prefix}.tar.gz" "$file2enc"
sha512sum "${chuck_prefix}.tar.gz" > "hash.sha512"
split -n l/15 "${chuck_prefix}.tar.gz" "${chuck_prefix}_"
shred -u "${chuck_prefix}.tar.gz"
gocryptfs "$encrypted_folder" mount
for file in "${chuck_prefix}"_*; do
    mv "$file" "mount/$(basename "$file")"
done
sleep 1
fusermount -u mount
