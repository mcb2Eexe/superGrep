# superGrep

Written by: McB

This script was written to allow me to regex search large data more efficiently,

It is designed to be run on Linux systems (Tested on Ubuntu 16.10 with python3.5),

This script is designed to take a regular expression input and conduct a search across large data sets using multiprocessing,
It will then output the results into a single results file.

The script can take either a dir or a file:

  - If a dir is provided, the script will create a queue of files within the dir. It will then search 1 file per logical core of the host machine. It will ensure that all cores are active as long as there are files in the queue. The results will be outputed to the parent dir,

  - If a file is provided, the script will break the file down into chunks and allocate chunks to each core until the file is complete. The results will be outputed to the file's dir.

Points to note:

  - The results are stored in memory until all searchers are complete,
  - There is no support included for Windows systems at this time (there was issues with how Windows handled the multiprocessing), 
  - Regex searches are pre-compiled so escaping characters must be double-slashed (\\),
  - single file's must be processed with -f (in development).
  
Installation:

  - Edit first line to match the version of Python3.* you are currently running, 
  - Drop the file into a location that is included in your $PATH (use cmd "echo $PATH" to display if needed),
  - Ensure script is executable (use cmd "sudo chmod +x superGrep"),
  - run from any location within a shell terminal by typing the cmd "superGrep".
  
This will continue to be developed when time permits.
