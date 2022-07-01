#!/bin/sh
set -e

sh -c "git config--global user.name "github-actions[bot]"' \
      && git config  --global user.email "41898282+github-actions[bot]@users.noreply.github.com"\
      && git add -A && git commit -m "Updated Static Content" --allow-empty \
      && git push -u origin HEAD"
