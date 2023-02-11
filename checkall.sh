#!/bin/sh
echo "-- Checking import sorting"
isort .

echo "-- Checking python formating"
black .

echo "-- Checking python with static checking"
flake8

echo "-- Checking type annotations"
mypy ./myapp  --ignore-missing-imports

echo "-- Checking for dead code"
vulture ./myapp

echo "-- Checking security issues"
bandit -r ./myapp