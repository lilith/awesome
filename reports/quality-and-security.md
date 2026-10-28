# Quality and security

Image codecs take bytes from strangers and turn them into pixels, usually on a server that also holds other people's data. A bug in a decoder is a security hole. All of this work is shaped by that fact, and it is also the reason frontier AI models can write so much of the code.

**Memory and concurrency safety the compiler checks.** Our crates compile with `#![forbid(unsafe_code)]`, so the compiler rules out out-of-bounds writes, use-after-free and data races. SIMD goes through two small primitive crates, [archmage](https://imazen.github.io/archmage/) and magetypes, that wrap the intrinsics once; a few older crates still carry unsafe code, and we treat it as debt.

**Limits on everything.** Decoders and encoders take resource limits (dimensions, pixel counts, memory) and fail cleanly instead of taking the process down. Long jobs accept cooperative cancellation ([enough](https://crates.io/crates/enough)), and CPU cost is predicted before the work starts.

**Bytes in, bytes out.** The domain is bytes and configuration in, bytes out, which makes it unusually testable. When a C reference exists we test against it bit for bit; where pixels may differ, perceptual metrics tell us whether a person would see it.

**Fuzzing, continually, on every platform**, with minimized regression files every later build must pass.

**Metrics we can trust.** [zensim](https://github.com/imazen/zensim) is our perceptual metric; to build it we ported 141 image-quality metrics to Rust ([what each costs to run](https://metric-brief.imazen.org/#models)), gathered over a terabyte of IQA datasets, and scored millions of encodes.

**What it replaces.** ImageMagick has [913 published vulnerabilities](https://app.opencve.io/cve/?vendor=imagemagick) (OpenCVE, checked 2026-10-28). This toolset is built to replace it on servers: memory-safe, faster, with better compression.

**Measured test data.** [imazen-26](https://github.com/imazen/imazen-26), our real-world corpus, holds 2,115 original images in 21 categories (12,672 megapixels) and 25,766 registered renditions of them; the corpus builder has collected 148,177 image files in 16 groups (formats, animation, wide gamut, edge cases); the IQA research library holds 230 datasets with 799,030 human-labelled test rows. Counted from the corpora themselves, each figure in its own unit.

**Executed in CI.** The newest successful run of each workflow executed 390,079 tests (6 failed, 9,417 of them doctests) in 1,135 jobs across 65 repositories, on Linux, macOS and Windows; 272 of those jobs ran on ARM64. GitHub keeps job logs for 90 days, so this counts one run per workflow, not a year.

*The owner's account; figures without a link are the owner's statements. The live version is chapter 05 of [https://stats.lilith.now/](https://stats.lilith.now/).*
