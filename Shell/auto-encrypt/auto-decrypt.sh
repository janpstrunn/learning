#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <Encrypted Folder>"
    exit 1
fi
encrypted_folder="$1"
chuck_prefix="chuck"
if [ ! -d "mount" ]; then
    mkdir "mount"
fi
gocryptfs "$encrypted_folder" mount
for file in mount/${chuck_prefix}_*; do
    mv "$file" "$(basename "$file")"
done
cat ${chuck_prefix}_* > "${chuck_prefix}.tar.gz"
shred -u ${chuck_prefix}_*
tar -xzvf "${chuck_prefix}.tar.gz"
computed_hash=$(sha512sum "${chuck_prefix}.tar.gz" | awk '{print $1}')
stored_hash=$(cat "hash.sha512" | awk '{print $1}')
shred -u "${chuck_prefix}.tar.gz"
fusermount -u mount
if [ "$computed_hash" == "$stored_hash" ]; then
    echo "Integrity check passed. Hashes match."
else
    echo "WARNING: Integrity check failed. Hashes do not match."
fi
