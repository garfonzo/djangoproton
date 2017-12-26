# Pip and ZSH Shell on a Mac

One issue you may run into is trying to install a pip package on a mac, while using the zsh shell - specifically, when trying to install a package that has square brackets in the name, such as:

`pip install -e .[test]`

Because Zsh will try to interpret the square brackets, the pip install command fails. So, if you are using the Zsh shell on a Mac, and need to install something with square brackets in the name, trying installing like this:

`noglob pip install -e .[test]`

or

`pip install -e '.[test]'`

Thanks to [this SO question](https://stackoverflow.com/questions/30539798/zsh-no-matches-found-requestssecurity).