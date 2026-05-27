# Primary Source Dossier

This folder documents the legal and institutional sources behind the simplified
rules used in the simulation.

The app is not a legal interpretation engine. It translates selected legal and
technical criteria into pedagogical classifiers so that their precision/recall
trade-offs can be observed. The sources below should be read as the evidentiary
backbone for that translation, not as a substitute for official wetland
delimitation, jurisdictional determination, or environmental legal advice.

## How The Sources Are Used

- Official links are preferred over vendored PDFs, because laws, guidance pages,
  and technical manuals can be updated.
- Short excerpts are included only to identify the relevant legal or technical
  anchor.
- The project distinguishes between a formal legal process and a simplified
  decision rule.
- Chile and the United States support relatively direct abstractions.
- Colombia is treated more cautiously: the 2-of-3 rule is a pedagogical model
  inspired by multicriteria institutional guidance, not a literal statutory
  threshold.

## Source Matrix

| Framework | Primary or institutional source | Relevant anchor | Simulation mapping | Confidence |
|---|---|---|---|---|
| Ramsar | [Convention on Wetlands: present text](https://www.ramsar.org/document/present-text-convention-wetlands) and [current English PDF](https://www.ramsar.org/sites/default/files/documents/library/current_convention_text_e.pdf) | Article 1.1 and Article 2.1-2.2 | International baseline: wetlands are broad, spatially delimited, and ecologically multidimensional. | High for conceptual framing. |
| Chile | [Law 21.202, BCN Ley Chile](https://www.leychile.cl/navegar?idNorma=1141461&idParte=10095363&idVersion=2020-01-23), [Decree 15/2020, BCN Ley Chile](https://www.bcn.cl/leychile/navegar?i=1152029), and [Decree 15/2020, Diario Oficial PDF](https://www.diariooficial.interior.gob.cl/publicaciones/2020/11/24/42813/01/1850809.pdf) | Decree 15, Article 8 | `OR / 1 of 3`: hydrology OR hydric soil OR hydrophytic vegetation. | High for the simplified delimitation criterion; medium for broader legal consequences. |
| United States | [EPA CWA Section 404 jurisdictional delineation page](https://www.epa.gov/cwa-404/what-jurisdictional-delineation-under-cwa-section-404), [USACE regional supplements page](https://www.usace.army.mil/Missions/Civil-Works/Regulatory-Program-and-Permits/reg_supp/), and [USACE 1987 Wetlands Delineation Manual](https://www.sac.usace.army.mil/Portals/43/docs/regulatory/1987_wetland_delineation_manual_reg.pdf) | EPA summary and USACE manual | `AND / 3 of 3`: hydric soils AND hydrophytic vegetation AND hydrology. | High for routine delineation logic; medium for jurisdictional status. |
| Colombia | [MinAmbiente humedales page](https://www.minambiente.gov.co/direccion-de-bosques-biodiversidad-y-servicios-ecosistemicos/generalidades-humedales/), [Resolution 196/2006 PDF](https://www.minambiente.gov.co/wp-content/uploads/2021/10/Resolucion-196-de-2006.pdf), and [Law 2478/2025, Funcion Publica](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=260799) | Resolution 196/2006 and Law 2478/2025 | `2 of 3` concurrence model inspired by a functional, multicriteria approach. | Medium: institutionally grounded, but not a literal legal formula. |

## Ramsar: International Baseline

Ramsar is used as the conceptual baseline for the project. It shows that a
wetland is not only a permanent visible water body. The Convention includes
systems that may be natural or artificial, permanent or temporary, static or
flowing, fresh, brackish, saline, and shallow marine.

Relevant short excerpts:

- "natural or artificial, permanent or temporary"
- "delimited on a map"

Methodological use:

Ramsar supports the broad framing of wetlands as a legal-ecological category
that can include temporary and less visually obvious systems. It does not define
the Chilean OR rule, the USACE AND rule, or the Colombian concurrence model.

## Chile: Urban Wetlands Regulation

The Chilean rule in the app is anchored in Law 21.202 and, more specifically,
Decree 15/2020. Article 8 of the regulation states that a municipal request for
recognition must include cartographic representation of the proposed polygon and
that wetland delimitation must consider at least one of three technical criteria.

Relevant short excerpt:

- "al menos uno de los siguientes criterios"

Simulation mapping:

```text
Chile = hydrology OR hydric soil OR hydrophytic vegetation
```

Responsible interpretation:

For simulation purposes, Chile is modeled as a 1-of-3 rule because Article 8 of
the regulation allows delimitation to be supported by at least one of the three
criteria. This is a strong basis for the pedagogical OR logic.

Important caveat:

This does not mean that any parcel automatically becomes a legally recognized
urban wetland when one indicator appears. The formal process still requires an
administrative file, review by the environmental authority, urban-boundary
requirements, publication, and a ministerial decision.

## United States: USACE/EPA Wetland Delineation

The U.S. rule is modeled from the USACE three-parameter approach used in wetland
delineation and summarized by EPA guidance for Clean Water Act Section 404.

Relevant short excerpts:

- "hydric soils, hydrophytic vegetation, and hydrology"
- "one positive wetland indicator from each parameter"

Simulation mapping:

```text
United States = hydrology AND hydric soil AND hydrophytic vegetation
```

Responsible interpretation:

This represents routine technical delineation logic, not the full legal status
of waters under federal jurisdiction. Jurisdictional determinations can depend on
case-specific records, regional supplements, normal circumstances, current
Waters of the United States implementation, and litigation.

## Colombia: Multicriteria Institutional Approach

Colombia is the most delicate case. The official and institutional sources
support a multicriteria approach to wetland management, identification,
delimitation, monitoring, and planning. They do not establish a national rule
that literally says "2 of 3".

Relevant short excerpts:

- "delimitación, caracterización y zonificación"
- "criterios biofísicos, ecológicos, geográficos y socioeconómicos"
- "características ecológicas, hidrológicas, geomorfológicas"

Simulation mapping:

```text
Colombia = at least 2 of 3 criteria
```

Responsible interpretation:

The app represents Colombia as a pedagogical concurrence model. The goal is to
show an institutional middle point between Chile's broad sensitivity and the
U.S. three-parameter concurrence logic. It should be described as
Colombia-inspired, not as a literal legal formula.

## Recommended Language For The README Or Interviews

Use this wording when explaining the legal translation:

> The rules are simplified classifiers inspired by official legal and technical
> sources. Chile is modeled as a 1-of-3 delimitation rule, the U.S. as a
> three-parameter concurrence rule, and Colombia as a pedagogical multicriteria
> concurrence model.

Avoid this wording:

> These are the exact wetland laws of Chile, the United States, and Colombia.

## Why Full PDFs Are Not Vendored Here

The project links to official source pages instead of storing full copies of the
legal documents in the repository. This keeps the repository lighter and reduces
the risk of presenting stale legal material as authoritative. If a future version
needs archival reproducibility, the recommended path is to add a `raw/` folder
with official PDFs plus a checksum file and retrieval date.
