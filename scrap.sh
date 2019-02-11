#!/usr/bin/env bash

function usage() {
    echo "usage: $0 [URL]"
}

[[ -z $1 ]] && usage && exit

url=$1
path=${url/http:\/\//.\/}

wget --convert-links --level=4 --no-parent --recursive --reject "*.html*,*.php*" --relative $url >&- 2>&-
echo $url

[[ $path == *"/README" ]] && echo >> matches $path: `cat $path` && exit

lines=`grep -E "^<a" $path | sed -Ee 's/.*href="([^"]*)".*/\1/'`
for line in $lines; do
    $0 ${line%/} 
done
