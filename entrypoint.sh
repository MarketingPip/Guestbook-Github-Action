#!/bin/sh
set -e

sh -c "git config --global user.name '${GITHUB_ACTOR}' \
      && git config --global user.email '${GITHUB_ACTOR}@users.noreply.github.com' \
      && git add -A && git commit -m "Updated Static Content" --allow-empty \
      && git push -u origin HEAD"
