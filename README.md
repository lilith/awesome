# awesome

Lilith River's open-source imaging work, in one place: what it is for, what is done, who depends on it, and how it is built. Live numbers: **[stats.lilith.now](https://stats.lilith.now/)**.

> Open-source, server-grade, robust codecs that shift the Pareto front for every major image and video format, and the full image processing, manipulation and enhancement stack around them, in 100% safe Rust, for every major platform.

[![Goals: formats and processing, with what has shipped](assets/goals.svg)](https://stats.lilith.now/)

I've published open source on GitHub since 2009; 2026 is my 18th year there, as [@lilith](https://github.com/lilith) and through [imazen](https://github.com/imazen). That work includes ImageResizer and Imageflow, and now a pure-Rust imaging stack written with frontier AI agents under rules that make their work checkable.

## Who depends on it

- **45,605,234 downloads** across [crates.io](https://crates.io/users/lilith?sort=downloads) and [NuGet](https://www.nuget.org/profiles/imazen); **914,754 crates.io downloads a month** over the last 90 days.
- **2,569+ repositories** depend on [ImageResizer](https://github.com/imazen/resizer/network/dependents).
- **6,629 GitHub stars**; [imazen/imageflow](https://github.com/imazen/imageflow) has 4,457.
- **OpenSSF criticality score** of 0.4 or more: imageflow 0.47, resizer 0.41 ([how it was measured](data/)).

[![Adoption](assets/adoption.svg)](https://stats.lilith.now/)

## Open-source programs

Against [Anthropic's Claude for Open Source](https://claude.com/contact-sales/claude-for-oss) criteria this work meets the maintainer track (500+ dependent repositories; 200,000+ monthly downloads) and the critical-infrastructure track (OpenSSF criticality 0.4+), and approaches the active-contributor track. For [OpenAI's Codex for Open Source](https://developers.openai.com/community/codex-for-oss) it is a set of widely used public projects whose maintainer work already runs through Codex review. Evidence for each criterion: **[reports/program-fit.md](reports/program-fit.md)**.

## 2026 so far

[![The year in numbers](assets/year.svg)](https://stats.lilith.now/)

[![Commits by week and family](assets/activity.svg)](https://stats.lilith.now/)

[![File lines committed, by file type](assets/lines-by-file-type.svg)](https://stats.lilith.now/)

## Where to start

- [imageflow](https://github.com/imazen/imageflow): image server engine and the C API behind the imageflow bindings
- [resizer](https://github.com/imazen/resizer): ImageResizer, the .NET image server
- [zenjpeg](https://github.com/imazen/zenjpeg): JPEG encoder and decoder (a jpegli port) in safe Rust
- [zenwebp](https://github.com/imazen/zenwebp): WebP, lossy and lossless
- [zenavif](https://github.com/imazen/zenavif): AVIF on owned AV1 encoders and a safe decoder
- [jxl-encoder](https://github.com/imazen/jxl-encoder): JPEG XL encoder
- [zenpipe](https://github.com/imazen/zenpipe): the streaming pipeline that ties the codecs together
- [zensim](https://github.com/imazen/zensim): the perceptual metric that tunes the codecs
- [archmage](https://github.com/imazen/archmage): safe SIMD through capability tokens
- [enough](https://github.com/imazen/enough): cooperative cancellation for long-running Rust work

All 154 public projects by topic: [reports/projects.md](reports/projects.md). Interactive dashboards: [metrics](https://metrics.imazen.org/), [metric cost](https://metric-brief.imazen.org/#models), [gigapixels](https://gigapixels.imazen.org/), [JPEG AI in the browser](https://jpegai.imazen.org/), [squintly](https://squintly.imazen.org/), [imazen-26](https://imazen-26-review.pages.dev/), [archmage docs](https://imazen.github.io/archmage/).

## How it is built

Safety the compiler checks (`#![forbid(unsafe_code)]`), resource limits and cancellation in every codec, bit-exact tests against C references, continual fuzzing, and perceptual metrics: [reports/quality-and-security.md](reports/quality-and-security.md). How AI agents fit in, with measured figures: [reports/ai-assisted-development.md](reports/ai-assisted-development.md).

## Reports

- [Program fit](reports/program-fit.md): Anthropic and OpenAI open-source program criteria, with evidence
- [Projects](reports/projects.md): every public project by topic
- [Adoption](reports/adoption.md): downloads and dependents, with links to check each
- [Quality and security](reports/quality-and-security.md)
- [AI-assisted development](reports/ai-assisted-development.md)

## Reproduce

`python3 tools/build.py` rebuilds every card and report from the public data behind [https://stats.lilith.now/](https://stats.lilith.now/) (https://stats.lilith.now/data.json); the GitHub and OpenSSF measurements are in [data/](data/) with their commands. Standard library only.

*Generated 2026-10-28 from data revision c49a8707ec92.*
