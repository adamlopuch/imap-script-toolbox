# imap-script-toolbox
Collection of python scripts for running several tasks on IMAP mail and mailboxen.

### Requirements ###
Required libraries
* IMAPClient: wrapper for IMAP manipulations
* pandas: dataframe methods used for munging

### Configuration ###
TBD (each script should take a config file)

### References ###
* IMAPClient documentation: https://imapclient.readthedocs.org/en/latest/

## Roadmap ##
1. Folder list
  * output all folder names, # of messages, size of messages
  * used to check for bad folder names
    - e.g. extra spaces, or end in space
  * used to hash and verify that destination has it, too
2. Message metadata
  * TBD

# 1. imap-list-folders.py #
Returns all folders within IMAP server. Includes # of messages per folder and size of messages per folder.
