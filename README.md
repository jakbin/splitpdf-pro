# splitpdf-pro

A python package for split pdf.

[![Python package](https://github.com/jakbin/splitpdf-pro/actions/workflows/publish.yml/badge.svg)](https://github.com/jakbin/splitpdf-pro/actions/workflows/publish.yml)
[![PyPI version](https://badge.fury.io/py/splitpdf-pro.svg)](https://badge.fury.io/py/splitpdf-pro)
[![Downloads](https://pepy.tech/badge/splitpdf-pro/month)](https://pepy.tech/project/splitpdf-pro)
[![Downloads](https://static.pepy.tech/personalized-badge/splitpdf-pro?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/splitpdf-pro)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/jakbin/splitpdf-pro)
![GitHub last commit](https://img.shields.io/github/last-commit/jakbin/splitpdf-pro)

## Introduction

Using "splitpdf-pro", you can split pdf into multiple parts by given ranges or numbers at once.

## Compatability

Python 3.6+ is required.

## Installation

```sh
pip install splitpdf-pro
```

## Usage

```sh
splitpdf-pro -h
splitpdf-pro file.pdf
splitpdf-pro file.pdf -r 2,4-6,8
```
or 

```sh
splitpdf -h
splitpdf file.pdf
splitpdf file.pdf -r 2,4-6,8
```