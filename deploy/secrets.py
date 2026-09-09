# This file lets you store secrets that you can then refer to from your djevops
# config. For example:
#
# DJANGO_SECRET_KEY = '1234...'
#
# The motivation for keeping secrets in a separate file is that you usually do
# not want to commit them to Git. One approach you can use is to hard-code your
# secrets here and only store djevops' djevops.yml file in Git.
#
# Another approach is to read secrets from environment variables. For example:
#
# import os
# MY_SECRET = os.environ['MY_SECRET']
#
# This works if the environment variables are available when you execute
# `djevops deploy`. The produced values are uploaded as constants to your
# server. If all your secrets are read from environment variables in this way,
# then you can consider committing this file to Git.
#
# (Feel free to remove these comments once you are done reading them.)
