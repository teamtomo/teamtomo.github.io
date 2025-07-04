# Contributing Guidelines

Want to work with us to add a package here? Great!

As a first step, please reach out in the 
[TeamTomo zulip channel](https://imagesc.zulipchat.com/#narrow/channel/426493-TeamTomo)
and let us know what you'd like to add.

If you get stuck with any of the following just ask in the Zulip! 
We've probably run into whatever issue you're having before and are happy to help.

**Imposter syndrome disclaimer**:
> We want your help. No, really. There may be a little voice inside your head that is telling you that you're not ready,
> that you aren't skilled enough to contribute. We assure you that the little voice in your head is wrong. Most
> importantly, there are many valuable ways to contribute besides writing code.


## Package Scope

Packages should:

- do one thing and do it well
- have a simple Python API
- be easy to install
- be [tested](https://docs.pytest.org/en/7.1.x/)

Small packages which compose well make it easy to find and
depend on only the functionality which is relevant for your own work.
In our experience, having small packages that are easy to reason about also makes it more 
likely that motivated users will try to submit patches when things aren't quite working for them.

## Package Template

We use the fantastic Python project template from 
[pydev-guide.github.io](https://pydev-guide.github.io/quickstart/) 
maintained by [Talley Lambert](https://bsky.app/profile/talley.codes). 

This template provides:

- a modern Python packaging setup
- automated testing in GitHub Actions
- automated deployment to PyPI

When setting up, please select the *fully featured* version of the template.

## Documentation

We use [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) for our 
documentation sites. Sites deployed to GitHub pages from repositories within the 
teamtomo organization on GitHub will be available at *teamtomo.org/<repo_name>*.

As a starting point, try running `mkdocs new .` then replacing your config with something like
this from [torch-find-peaks](https://github.com/teamtomo/torch-find-peaks).

```yaml
site_name: torch-find-peaks
site_author: jojoelfe
site_description: >-
  Documentation for torch-find-peaks
repo_name: jojoelfe/torch-find-peaks
repo_url: https://github.com/jojoelfe/torch-find-peaks
edit_uri: edit/main/docs/

copyright: Copyright &copy; 2022 - 2022 teamtomo


# Custom navigation can be specified
#nav:
#  - Overview: index.md
#  - Section:
#      - Title: directory/file.md

theme:
  icon:
    logo: material/cube-outline
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: blue
      accent: blue

  features:
    - navigation.instant
    - search.highlight
    - search.suggest
    - content.tabs.link

markdown_extensions:
  - admonition
  - tables
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
  - md_in_html
  - pymdownx.arithmatex:
      generic: true

plugins:
  - search
  - mkdocs-jupyter
  - mkdocstrings:
      handlers:
        python:
          paths: [src]
          options:
            docstring_style: numpy
```

### Deploying Documentation
The following GitHub Actions config should build your site and deploy it to a branch 
called *gh-pages* in your repository.

Once the *gh-pages* branch is present, you can configure the site to deploy from it 
at *github.com/teamtomo/<repo_name>/settings/pages*.

```yaml
name: docs

on:
  push:
    branches:
      - main

# This job installs dependencies, builds the book, and pushes it to
# the `gh-pages` branch of the same repository.
jobs:
  deploy-book:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          # pip install -e .
          pip install mkdocs mkdocs-material mkdocs-jupyter mkdocstrings[python]

      # Build the book
      - name: Build the book
        run: |
          mkdocs build

      # Push the site to github-pages
      - name: GitHub Pages action
        uses: peaceiris/actions-gh-pages@v4
        with:
          publish_dir: ./site
          github_token: ${{ secrets.GITHUB_TOKEN }}

```
