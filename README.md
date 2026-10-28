# awesome

Lilith River's open-source imaging work, in one place: what it is for, what is done, who depends on it, and how it is built. Live numbers: **[stats.lilith.now](https://stats.lilith.now/)**.

| | | |
|:--|:--|:--|
| **JPEG**<br><sub>encoders, decoder and YUV, in safe Rust</sub> | [zenjpeg] · **[zenyuv]** · **[mozjpeg-rs]** · [browser-jpeg-support] | <sub>3 repos · 3 on crates.io · 3,267 commits</sub> |
| **WebP**<br><sub>lossy and lossless, plus libwebp bindings</sub> | **[zenwebp]** · **[webpx]** · **[libwebp-net]** | <sub>3 repos · 2 on crates.io · 1,922 commits</sub> |
| **AVIF & AV1**<br><sub>the container, three AV1 encoders and a decoder</sub> | [zenavif] · [zenavif-parse] · [zenavif-serialize] · [zenravif] · [zenrav1e] · [rav1d-safe] · [zenav1-svt] · [zenav1-aom] | <sub>6 repos · 4 on crates.io · 7,061 commits</sub> |
| **JPEG XL**<br><sub>encoder, decoder, GPU kernels, inspector</sub> | [zenjxl] · [zenjxl-decoder] · **[jxl-encoder]** · [jxl-gpu] · [jxl-inspect] | <sub>5 repos · 3 on crates.io · 4,476 commits</sub> |
| **PNG & GIF**<br><sub>PNG and animated GIF</sub> | **[zenpng]** · [zengif] | <sub>2 repos · 2 on crates.io · 1,093 commits</sub> |
| **HDR & gain maps**<br><sub>Ultra HDR gain maps and tone mapping</sub> | [ultrahdr] · **[zentone]** · [gainmap-spec-status] · [browser-hdr-test] | <sub>4 repos · 1 on crates.io · 537 commits</sub> |
| **Learned codecs**<br><sub>JPEG AI and Cool-chic in safe Rust</sub> | [zenjpegai] · [zencoolchic] | <sub>2 repos · 210 commits</sub> |
| **HEIC, RAW & more formats**<br><sub>HEIC, camera RAW, TIFF, PDF, SVG, JPEG 2000, bitmaps</sub> | **[heic]** · [zenraw] · [zenbitmaps] · [zentiff] · [zenpdf] · [zensvg] · [zenjp2] | <sub>4 repos · 4 on crates.io · 1,567 commits</sub> |
| **Codec API & pipeline**<br><sub>shared codec traits and the streaming pipeline</sub> | **[zencodec]** · [zencodecs] · [zenpipe] · [zenlayout] · [zennode] · [zenwasm] · [zentract] | <sub>5 repos · 2 on crates.io · 2,818 commits</sub> |
| **Processing**<br><sub>resize, filter, blend, quantize, crop, enhance</sub> | **[zenresize]** · [zenfilters] · **[zenblend]** · [zenquant] · [zensally] · [zensr] | <sub>6 repos · 4 on crates.io · 2,833 commits</sub> |
| **Pixels & color**<br><sub>pixel formats, transfer functions, color</sub> | **[zenpixels]** · **[zenpixels-convert]** · **[linear-srgb]** · **[garb]** | <sub>3 repos · 4 on crates.io · 1,108 commits</sub> |
| **Compression**<br><sub>DEFLATE, Zopfli, Zstandard, xxHash</sub> | **[zenflate]** · [zenzop] · [zenzstd] · [zenhash] | <sub>4 repos · 2 on crates.io · 687 commits</sub> |
| **Quality metrics**<br><sub>perceptual quality, to tune the codecs</sub> | [zensim] · **[fast-ssim2]** · **[butteraugli]** · [zenmetrics] · [resamplescope-rs] · [squintly] · [evif] | <sub>7 repos · 4 on crates.io · 11,872 commits</sub> |
| **Codec pickers**<br><sub>the right codec and quality per image</sub> | [zenanalyze] · [zenpredict] · [zenpicker] · [zenanalyze-api] | <sub>1 repo · 2 on crates.io · 1,365 commits</sub> |
| **Test corpora**<br><sub>images to test and train on</sub> | **[codec-corpus]** · [imazen-26] · [imazen-26-jxl-p3] · [imazen-26-jxl-srgb] · [imazen-26-originals] · [imazen-xl-26] · [all-the-images] · [zentrain-corpus] | <sub>8 repos · 1 on crates.io · 342 commits</sub> |
| **SIMD & Rust foundations**<br><sub>safe SIMD, cancellation, errors, benchmarks</sub> | **[archmage]** · **[magetypes]** · [multiversed] · **[winarm-cpufeatures]** · **[enough]** · [how-far] · [whereat] · **[zenbench]** | <sub>7 repos · 7 on crates.io · 2,443 commits</sub> |
| **Developer tools**<br><sub>workspace, release and API tooling</sub> | [cargo-copter] · [cargo-read] · [crate-mcp] · [cargo-superwork] · [zenutils] · [efficient-ui] | <sub>6 repos · 2 on crates.io · 183 commits</sub> |
| **Products**<br><sub>image servers and their bindings</sub> | **[Imageflow]** (**[.NET]** · **[Node]** · [Go]) · **[ImageResizer]** · **[imageflow-server]** · [resizer-web] · [imageflow-fuzz] | <sub>8 repos · 807 commits</sub> |
| **Other tools**<br><sub>everything else in use</sub> | [astro-broken-link-checker] · [folioxml] · [interleaved-site] | <sub>3 repos · 21 commits</sub> |
| **Earlier work**<br><sub>the .NET and C years</sub> | [keyhub] · [hardwired] · [and 8 more](reports/projects.md) | <sub>10 repos</sub> |

<sub>**Bold**: the most used, with 10,000+ crates.io downloads in the last 90 days or 100+ GitHub stars. Commits are lilith's in 2026. As of 2026-10-28; live on [stats.lilith.now](https://stats.lilith.now/).</sub>

[Open source](https://www.imazen.io/open-source) · [@imazen](https://github.com/imazen) · [@lilith](https://github.com/lilith) · [lib.rs/~lilith](https://lib.rs/~lilith)

> Open-source, server-grade, robust codecs that shift the Pareto front for every major image and video format, and the full image processing, manipulation and enhancement stack around them, in 100% safe Rust, for every major platform.

[![Goals: formats and processing, with what has shipped](assets/goals.svg)](https://stats.lilith.now/)

I've published open source on GitHub since 2009; 2026 is my 18th year there, as [@lilith](https://github.com/lilith) and through [imazen](https://github.com/imazen). That work includes ImageResizer and Imageflow, and now a pure-Rust imaging stack written with frontier AI agents under rules that make their work checkable.

## Who depends on it

- **45,592,280 downloads** across [crates.io](https://crates.io/users/lilith?sort=downloads) and [NuGet](https://www.nuget.org/profiles/imazen); **913,218 crates.io downloads a month** over the last 90 days.
- **2,569+ repositories** depend on [ImageResizer](https://github.com/imazen/resizer/network/dependents).
- **6,185 GitHub stars**; [imazen/imageflow](https://github.com/imazen/imageflow) has 4,457.
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

All 98 public projects by topic: [reports/projects.md](reports/projects.md). Interactive dashboards: [metrics](https://metrics.imazen.org/), [metric cost](https://metric-brief.imazen.org/#models), [gigapixels](https://gigapixels.imazen.org/), [JPEG AI in the browser](https://jpegai.imazen.org/), [squintly](https://squintly.imazen.org/), [imazen-26](https://imazen-26-review.pages.dev/), [archmage docs](https://imazen.github.io/archmage/).

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

*Generated 2026-10-28 from data revision 39d1a17ada37.*

[zenjpeg]: https://github.com/imazen/zenjpeg
[zenyuv]: https://github.com/imazen/zenjpeg
[mozjpeg-rs]: https://github.com/imazen/mozjpeg-rs
[browser-jpeg-support]: https://github.com/lilith/browser-jpeg-support
[zenwebp]: https://github.com/imazen/zenwebp
[webpx]: https://github.com/imazen/webpx
[libwebp-net]: https://github.com/imazen/libwebp-net
[zenavif]: https://github.com/imazen/zenavif
[zenavif-parse]: https://github.com/imazen/zenavif
[zenavif-serialize]: https://github.com/imazen/zenavif
[zenravif]: https://github.com/imazen/cavif-rs
[zenrav1e]: https://github.com/imazen/zenrav1e
[rav1d-safe]: https://github.com/imazen/rav1d-safe
[zenav1-svt]: https://github.com/imazen/zenav1-svt
[zenav1-aom]: https://github.com/imazen/zenav1-aom
[zenjxl]: https://github.com/imazen/zenjxl
[zenjxl-decoder]: https://github.com/imazen/zenjxl-decoder
[jxl-encoder]: https://github.com/imazen/jxl-encoder
[jxl-gpu]: https://github.com/imazen/jxl-gpu
[jxl-inspect]: https://github.com/imazen/jxl-inspect
[zenpng]: https://github.com/imazen/zenpng
[zengif]: https://github.com/imazen/zengif
[ultrahdr]: https://github.com/imazen/ultrahdr
[zentone]: https://github.com/imazen/zentone
[gainmap-spec-status]: https://github.com/imazen/gainmap-spec-status
[browser-hdr-test]: https://github.com/lilith/browser-hdr-test
[zenjpegai]: https://github.com/imazen/zenjpegai
[zencoolchic]: https://github.com/imazen/zencoolchic
[heic]: https://github.com/imazen/heic
[zenraw]: https://github.com/imazen/zenraw
[zenbitmaps]: https://github.com/imazen/zenbitmaps
[zentiff]: https://github.com/imazen/zenextras
[zenpdf]: https://github.com/imazen/zenextras
[zensvg]: https://github.com/imazen/zenextras
[zenjp2]: https://github.com/imazen/zenextras
[zencodec]: https://github.com/imazen/zencodec
[zencodecs]: https://github.com/imazen/zenpipe
[zenpipe]: https://github.com/imazen/zenpipe
[zenlayout]: https://github.com/imazen/zenpipe
[zennode]: https://github.com/imazen/zennode
[zenwasm]: https://github.com/imazen/zenwasm
[zentract]: https://github.com/imazen/zentract
[zenresize]: https://github.com/imazen/zenresize
[zenfilters]: https://github.com/imazen/zenpipe
[zenblend]: https://github.com/imazen/zenblend
[zenquant]: https://github.com/imazen/zenquant
[zensally]: https://github.com/imazen/zensally
[zensr]: https://github.com/imazen/zensr
[zenpixels]: https://github.com/imazen/zenpixels
[zenpixels-convert]: https://github.com/imazen/zenpixels
[linear-srgb]: https://github.com/imazen/linear-srgb
[garb]: https://github.com/imazen/garb
[zenflate]: https://github.com/imazen/zenflate
[zenzop]: https://github.com/imazen/zenzop
[zenzstd]: https://github.com/imazen/zenzstd
[zenhash]: https://github.com/imazen/zenhash
[zensim]: https://github.com/imazen/zensim
[fast-ssim2]: https://github.com/imazen/fast-ssim2
[butteraugli]: https://github.com/imazen/butteraugli
[zenmetrics]: https://github.com/imazen/zenmetrics
[resamplescope-rs]: https://github.com/imazen/resamplescope-rs
[squintly]: https://github.com/imazen/squintly
[evif]: https://github.com/imazen/evif
[zenanalyze]: https://github.com/imazen/zenanalyze
[zenpredict]: https://github.com/imazen/zenanalyze
[zenpicker]: https://github.com/imazen/zenanalyze
[zenanalyze-api]: https://github.com/imazen/zenanalyze
[codec-corpus]: https://github.com/imazen/codec-corpus
[imazen-26]: https://github.com/imazen/imazen-26
[imazen-26-jxl-p3]: https://github.com/imazen/imazen-26-jxl-p3
[imazen-26-jxl-srgb]: https://github.com/imazen/imazen-26-jxl-srgb
[imazen-26-originals]: https://github.com/imazen/imazen-26-originals
[imazen-xl-26]: https://github.com/imazen/imazen-xl-26
[all-the-images]: https://github.com/imazen/all-the-images
[zentrain-corpus]: https://github.com/imazen/zentrain-corpus
[archmage]: https://github.com/imazen/archmage
[magetypes]: https://github.com/imazen/archmage
[multiversed]: https://github.com/imazen/multiversed
[winarm-cpufeatures]: https://github.com/imazen/winarm-cpufeatures
[enough]: https://github.com/imazen/enough
[how-far]: https://github.com/imazen/how-far
[whereat]: https://github.com/lilith/whereat
[zenbench]: https://github.com/imazen/zenbench
[cargo-copter]: https://github.com/imazen/cargo-copter
[cargo-read]: https://github.com/imazen/cargo-read
[crate-mcp]: https://github.com/imazen/crate-mcp
[cargo-superwork]: https://github.com/imazen/cargo-superwork
[zenutils]: https://github.com/imazen/zenutils
[efficient-ui]: https://github.com/imazen/efficient-ui
[Imageflow]: https://github.com/imazen/imageflow
[.NET]: https://github.com/imazen/imageflow-dotnet
[Node]: https://github.com/imazen/imageflow-node
[Go]: https://github.com/imazen/imageflow-go
[ImageResizer]: https://github.com/imazen/resizer
[imageflow-server]: https://github.com/imazen/imageflow-server
[resizer-web]: https://github.com/imazen/resizer-web
[imageflow-fuzz]: https://github.com/imazen/imageflow-fuzz
[astro-broken-link-checker]: https://github.com/imazen/astro-broken-link-checker
[folioxml]: https://github.com/imazen/folioxml
[interleaved-site]: https://github.com/imazen/interleaved-site
[imageci]: https://github.com/imazen/imageci
[imageflow-web]: https://github.com/imazen/imageflow-web
[srcset-checker]: https://github.com/imazen/srcset-checker
[imageflow-now]: https://github.com/lilith/imageflow-now
[bank-csv]: https://github.com/imazen/bank-csv
[hardwired]: https://github.com/imazen/hardwired
[keyhub]: https://github.com/imazen/keyhub
[repositext]: https://github.com/imazen/repositext
[suspension]: https://github.com/imazen/suspension
[load_image]: https://github.com/lilith/load_image
