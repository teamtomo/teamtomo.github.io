"""Generate cite page with authors fetched from Zenodo."""

from typing import List

import requests


ZENODO_CONCEPT_ID = "18405652"
ZENODO_CONCEPT_DOI = "10.5281/zenodo.18405652"


def fetch_zenodo_authors(concept_id: str) -> List[str]:
    """Fetch author names from the latest Zenodo record for a concept ID.

    Returns a list of author names in 'Last, First' format suitable for BibTeX.
    """
    response = requests.get(f"https://zenodo.org/api/records/{concept_id}")
    response.raise_for_status()
    creators = response.json()["metadata"]["creators"]
    authors = []
    for creator in creators:
        name = creator["name"]
        # Zenodo stores names as "Last, First" or occasionally "First Last"
        if "," not in name:
            parts = name.strip().split()
            if len(parts) >= 2:
                name = f"{parts[-1]}, {' '.join(parts[:-1])}"
        authors.append(name)
    return authors


def generate_cite_page(concept_id: str, concept_doi: str) -> str:
    """Generate the cite.md page content with authors fetched from Zenodo."""
    authors = fetch_zenodo_authors(concept_id)

    # BibTeX author string: names joined with " and "
    bibtex_authors = " and\n                      ".join(authors)

    # APA author string: e.g. "Burt, A., & Giammar, M."
    def apa_name(name: str) -> str:
        if "," in name:
            last, first = name.split(",", 1)
            initials = ". ".join(p[0] for p in first.strip().split()) + "."
            return f"{last.strip()}, {initials}"
        return name

    apa_name_list = [apa_name(a) for a in authors]
    if len(apa_name_list) == 1:
        apa_authors = apa_name_list[0]
    elif len(apa_name_list) == 2:
        apa_authors = f"{apa_name_list[0]}, & {apa_name_list[1]}"
    else:
        apa_authors = ", ".join(apa_name_list[:-1]) + f", & {apa_name_list[-1]}"

    return f"""# Cite teamtomo

If you use teamtomo packages in your research, please cite the project using the reference below.

The DOI is a concept DOI that represents the teamtomo project as a whole, independent of any specific version.
To cite a specific version, follow the DOI link and use the citation provided on that Zenodo page.

[![DOI](https://zenodo.org/badge/DOI/{concept_doi}.svg)](https://doi.org/{concept_doi})

=== "BibTeX"

    ```bibtex
    @software{{teamtomo,
      author       = {{{bibtex_authors}}},
      title        = {{{{teamtomo: modular Python packages for cryo-EM and cryo-ET}}}},
      publisher    = {{Zenodo}},
      doi          = {{{concept_doi}}},
      url          = {{https://doi.org/{concept_doi}}}
    }}
    ```

=== "APA"

    {apa_authors} *teamtomo*. Zenodo. https://doi.org/{concept_doi}
"""


def main():
    print("Fetching Zenodo authors and generating cite page...")
    cite_markdown = generate_cite_page(ZENODO_CONCEPT_ID, ZENODO_CONCEPT_DOI)
    with open("src/site/cite.md", "w") as f:
        f.write(cite_markdown)
    print("Cite page generated successfully!")


main()
