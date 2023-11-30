Alan Gaines
* Tasks
  * Bandit Git Hook:
    * Requires command before functioning `git config core.hooksPath bandit_scanning`
  * Fuzzing:
    * GitHub Actions to run fuzz.py
    * parser.py - getKeyRecursively - no type checking or enforcement beyond input dictionary
    * parser.py - update_json_paths - no type checking for input or on data contained within the input if it is an iterable container
    * parser.py - getSingleDict4MultiDocs - just a lack of checking for whether the input is iterable that I could find
    * scanner.py - getYAMLFiles - doesn't handle if input isn't a valid directory path
    * scanner.py - getItemFromSecret - no type checking of inputs or contents thereof, doesn't ensure position is within range
  * Logging:
    * scanner.py - runScanner
    * scanner.py - scanForOverPrivelages
    * parser.py - checkParseError
    * parser.py - loadMultiYAML
    * parser.py - show_line_for_paths
* Lessons
  * Git Hook
    * In the default directory, Git hooks aren't committed to a repository
    * Git has a command to change the directory checked for hooks to execute
    * Bandit has command line settings to automatically output to a CSV
  * Logging
    * Logging is useful for both identifying the point at which a program crashes but also finding when a series of commands executed all call the same function individually
  * Fuzzing
    * Some methods don't check to verify correct assumptions or naming conventions, and it isn't always clear when those assumptions are present
    * Also, failing gracefully upon assumptions proving false or requirements going unchecked is useful