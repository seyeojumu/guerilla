#!/usr/bin/env bash

echo "update .profile per brew directions"
echo "export PATH=~/bin:/usr/local/bin:/usr/local/sbin:$PATH"
while true; do
    read -p "Do you wish to continue program?" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
xcode-select --install
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
brew doctor
brew install node
brew install python
pip install plumbum
pip install sh
brew upgrade
brew cleanup
exit 0

