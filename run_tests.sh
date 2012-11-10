#!/bin/bash

echo "** Running Unit Tests **"


echo "** WRITING COVERAGE **"
coverage html -d ./reports/coverage_html
coverage -r -m >./reports/coverage_report.txt
