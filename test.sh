#!/bin/bash

PYTHONPATH=$PWD:$PWD/viewpassdemo:$PYTHONPATH DJANGO_SETTINGS_MODULE=viewpassdemo.settings django-admin test

