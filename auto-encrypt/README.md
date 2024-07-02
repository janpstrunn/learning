# Auto Encrypt

A really simple way to easily archive, hash, split and encrypt files and folders by just giving it's path.

## auto-encrypt.sh

Simply archives, hashes, split and encrypt a given file or folder, using:

``tar``  ``sha512sum``  ``split``  ``gocryptfs``

Plus all unused files are shreded and deleted, remaining only the necessary.

This script have been configured to only accept one file/folder at once! 

It's recommended to throw everything you need to encrypt in a folder if you need to encrypt multiple files!

## auto-decrypt.sh

This script does the exact opposite, just for convenience, and also checks the stored hash.sha512 automatically to make sure it wasn't tampered.

## Step by Step

### Executing the Encrypt Script

```./auto-encrypt.sh path/to/file or path/to/folder```

If there is no folder called: 'mount' and 'Encrypted_Vault' in the __working directory__, it's automatically created.

After that, the file/folder is archived into a .tar.gz file, and it's hashed using sha512 and stored in a 'hash.sha512' file in the __working directory__.

Then, the archived file is split in fifteen chunks (by default) of same size. The archived file is shreded and deleted.

The command 'gocryptfs -init' is ran to generate the encrypted folder (asking you to prompt a password) and mount it to the 'mount' folder, then move all the split files to it, and finally it's unmounted.

### Executing the Decrypt Script

```./auto-decrypt.sh Encrypted_Vault```

Again, if there is no 'mount' folder in the __working directory__, it's automatically created.

The encrypted folder is unlocked and mounted to the 'mount' folder.

Now the split files are moved to the __working directory__ and are concatenated generating a .tar.gz file. 

The split files are shreded and delete, and the archived file is extracted, hashed and shreded as well.

The file/folder is unencrypted in the __working directory__, and the stored hash and previous generated hash are compared, warning you if they are identical or different.

## Dependencies:
- tar
- gocryptfs

### ALWAYS HAVE GOOD PASSWORDS PRACTICES

### "The biggest threat is, and will always be, the user." - *Arch Linux*.
