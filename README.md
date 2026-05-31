# Personal Website

This repository deploys my personal website.
It uses a Pelican for static site generation.

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate it:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Local Development

Build the site with live reload:

```bash
pelican content -s pelicanconf.py -l -r
```

## Deploy

The GitHub Actions workflow in [.github/workflows/deploy.yml](.github/workflows/deploy.yml) builds the site with `publishconf.py` and pushes the generated `output/` directory to the `gh-pages` branch.

You can also do the same build locally with:

```bash
pelican content -s publishconf.py -o output
```

## Project Files

- `pelicanconf.py` contains the development settings and shared publication data.
- `publishconf.py` contains production overrides.
- `content/pages/` contains the page content.
- `content/images/` and `content/pdfs/` contain static assets.
