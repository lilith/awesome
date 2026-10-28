# Open-source program fit

Measured on 2026-10-28 against each program's published criteria. Every figure links to a page where it can be checked; the GitHub and OpenSSF measurements and their commands are in [data/](../data/). Live numbers: [https://stats.lilith.now/](https://stats.lilith.now/).

## Anthropic: Claude for Open Source

Criteria from [claude.com/contact-sales/claude-for-oss](https://claude.com/contact-sales/claude-for-oss) (checked 2026-10-28); any one track qualifies.

| Track | Status | Evidence |
|---|---|---|
| Maintainer: 500+ dependent repositories | Meets | [imazen/resizer](https://github.com/imazen/resizer/network/dependents) (ImageResizer): 2,569 dependent repositories on GitHub's dependency graph (2026-10-27) |
| Maintainer: 200,000+ combined monthly downloads | Meets | 913,218 a month across 66 crates: crates.io's 90-day downloads (2,739,653) divided by three. [enough](https://crates.io/crates/enough) alone: 190,981 a month |
| Maintainer: 100+ dependent packages | Approaches | ImageResizer: 81 dependent packages; 521 summed over all our packages |
| Critical infrastructure: OpenSSF criticality score 0.4+ | Meets | [imazen/imageflow](https://github.com/imazen/imageflow) 0.466; [imazen/resizer](https://github.com/imazen/resizer) 0.411 (scored 2026-10-28 without the deps.dev dependents signal, which can only raise a score) |
| Active contributor: 100+ merged PRs to repositories you don't own, 12 months | Approaches | 72 merged since 2025-10-28, into [image-rs/image-tiff](https://github.com/image-rs/image-tiff/pulls?q=is%3Apr+author%3Alilith+is%3Amerged), [pdf-rs/fax](https://github.com/pdf-rs/fax/pulls?q=is%3Apr+author%3Alilith+is%3Amerged), [awxkee/moxcms](https://github.com/awxkee/moxcms/pulls?q=is%3Apr+author%3Alilith+is%3Amerged), [image-rs/weezl](https://github.com/image-rs/weezl/pulls?q=is%3Apr+author%3Alilith+is%3Amerged), [libjxl/jxl-rs](https://github.com/libjxl/jxl-rs/pulls?q=is%3Apr+author%3Alilith+is%3Amerged), [inflation/jpegxl-rs](https://github.com/inflation/jpegxl-rs/pulls?q=is%3Apr+author%3Alilith+is%3Amerged), [etemesi254/zune-image](https://github.com/etemesi254/zune-image/pulls?q=is%3Apr+author%3Alilith+is%3Amerged), [kornelski/rust-rgb](https://github.com/kornelski/rust-rgb/pulls?q=is%3Apr+author%3Alilith+is%3Amerged) and others |
| Community builder: a repository with 20+ external contributors, 12 months | Not met | at most 3 on one repository; 13 people across imazen |

## OpenAI: Codex for Open Source

From [developers.openai.com/community/codex-for-oss](https://developers.openai.com/community/codex-for-oss) (checked 2026-10-28): for core maintainers of public projects and people who run widely used public projects; projects that do not fit the criteria but matter to the ecosystem are asked to apply and explain why. The [Codex open source fund](https://github.com/openai/codex/blob/main/docs/open-source-fund.md) gives API credits (up to $25,000) to projects that use Codex in pull request review, maintainer automation and release work.

| Criterion | Evidence |
|---|---|
| Core maintainer of public projects | lilith maintains the [imazen](https://github.com/imazen) and [lilith](https://github.com/lilith) repositories listed in [projects.md](projects.md); on GitHub since 2009 |
| Widely used | [imazen/imageflow](https://github.com/imazen/imageflow) 4,457 stars; 45,592,280 crates.io and NuGet downloads; 2,569+ dependent repositories |
| Uses Codex in maintainer work | Codex reviews designs and changes in the agent workflow described in [ai-assisted-development.md](ai-assisted-development.md) |

## Why these programs matter here

- **Decoders parse hostile input.** Every codec here reads bytes from strangers. Security tooling (Codex Security, and access to the models' cybersecurity capabilities) goes straight at the riskiest code; today even safe-Rust codec work trips model safety filters often.
- **The work runs on agents every day.** 58,076 instructions went to AI agents in 2026, across more than 2,798 unpaid hours. AI services are the largest part of the project's cloud spend: $9,011 of $16,167 from January 1 to 2026-10-12 (the books' charges; hosting and software make up the rest).
- **Review and release automation.** Codex already reviews designs and changes; API credits would run that review on every pull request and release in the public repositories.
- **The fixes travel upstream.** Work here regularly lands in other projects: 72 merged pull requests in the last 12 months, in image-rs, jxl-rs, moxcms, zune-image and others.

## Projects nearest each criterion

- [imazen/imageflow](https://github.com/imazen/imageflow): 4,457 stars, OpenSSF criticality 0.466
- [imazen/resizer](https://github.com/imazen/resizer): 583 stars, OpenSSF criticality 0.411
- [imazen/imageflow-server](https://github.com/imazen/imageflow-server): 317 stars, OpenSSF criticality 0.337
- [imazen/imageflow-dotnet](https://github.com/imazen/imageflow-dotnet): 167 stars, OpenSSF criticality 0.345
- [imazen/libwebp-net](https://github.com/imazen/libwebp-net): 145 stars
- [enough](https://crates.io/crates/enough) ([imazen/enough](https://github.com/imazen/enough)): 572,944 downloads in 90 days, 35 crates.io reverse dependencies
- [webpx](https://crates.io/crates/webpx) ([imazen/webpx](https://github.com/imazen/webpx)): 416,658 downloads in 90 days, 3 crates.io reverse dependencies
- [archmage](https://crates.io/crates/archmage) ([imazen/archmage](https://github.com/imazen/archmage)): 246,513 downloads in 90 days, 40 crates.io reverse dependencies
- [archmage-macros](https://crates.io/crates/archmage-macros) ([imazen/archmage](https://github.com/imazen/archmage)): 246,432 downloads in 90 days, 1 crates.io reverse dependency
- [magetypes](https://crates.io/crates/magetypes) ([imazen/archmage](https://github.com/imazen/archmage)): 176,697 downloads in 90 days, 22 crates.io reverse dependencies
- [linear-srgb](https://crates.io/crates/linear-srgb) ([imazen/linear-srgb](https://github.com/imazen/linear-srgb)): 145,447 downloads in 90 days, 17 crates.io reverse dependencies
- [zenyuv](https://crates.io/crates/zenyuv) ([imazen/zenjpeg](https://github.com/imazen/zenjpeg)): 100,185 downloads in 90 days, 2 crates.io reverse dependencies
- [mozjpeg-rs](https://crates.io/crates/mozjpeg-rs) ([imazen/mozjpeg-rs](https://github.com/imazen/mozjpeg-rs)): 95,483 downloads in 90 days, 10 crates.io reverse dependencies
