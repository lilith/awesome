#!/usr/bin/env python3
"""Build this repository's README, SVG cards and reports from the public data behind https://stats.lilith.now/.

Usage: python3 tools/build.py [DATA]   (DATA: a path or URL to data.json; default https://stats.lilith.now/data.json)

Standard library only. Every number written comes from that data file or from data/measurements-*.json, which
records the GitHub and OpenSSF measurements with the commands that produced them. Nothing here estimates.
"""
import datetime
import glob
import html
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://stats.lilith.now/'
FONT = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
BG, LINE, INK, MUTED, AMBER, GREEN = '#0b1016', '#28313a', '#f0eee8', '#929ca8', '#ffd88f', '#9be38f'
FAMILY_COLORS = {'codecs': '#f5bd68', 'pixels': '#f08fb5', 'processing': '#7fc8f8', 'compression': '#9be38f', 'quality': '#80d5d0',
                 'ml': '#ae9bdf', 'foundations': '#d9d27c', 'products': '#f29b6b', 'tools': '#8fa0b3', 'other': '#6b7785'}
# The page's file-type palette: the dataviz categorical order, validated on #0b1016.
FILE_COLORS = ['#3987e5', '#d95926', '#199e70', '#c98500', '#d55181', '#008300', '#9085e9', '#e66767']
FILE_LABELS = {'rust': 'Rust', 'markdown': 'Markdown', 'json_yaml': 'JSON/YAML', 'python': 'Python', 'shell': 'Shell', 'c_cpp': 'C/C++',
               'js_ts': 'JS/TS', 'html_css': 'HTML/CSS', 'toml': 'TOML', 'other': 'Everything else'}


def load(source):
    if source.startswith('http'):
        with urllib.request.urlopen(urllib.request.Request(source, headers={'User-Agent': 'lilith-awesome-build'}), timeout=60) as r:
            return json.load(r)
    with open(source) as f:
        return json.load(f)


def fmt(n):
    return f'{round(n):,}'


def big(n):
    return f'{n / 1e9:.1f}B' if n >= 1e9 else f'{n / 1e6:.1f}M' if n >= 1e6 else f'{n / 1e3:.0f}K' if n >= 1e4 else fmt(n)


def esc(s):
    return html.escape(str(s), quote=True)


def wrap(text, chars):
    lines, line = [], ''
    for word in text.split():
        if line and len(line) + 1 + len(word) > chars:
            lines.append(line)
            line = word
        else:
            line = f'{line} {word}'.strip()
    return lines + ([line] if line else [])


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}" '
            f'font-family="{FONT}"><title>{esc(title)}</title><rect width="{w}" height="{h}" rx="14" fill="{BG}" stroke="{LINE}"/>{body}</svg>\n')


def header(title, sub, w):
    return (f'<text x="28" y="40" fill="{AMBER}" font-size="12" font-weight="700" letter-spacing="2">{esc(title.upper())}</text>'
            f'<text x="{w - 28}" y="40" fill="{MUTED}" font-size="12" text-anchor="end">{esc(sub)}</text>')


# ---------- cards ----------

def goals_card(d, asof):
    g = d['directive']
    w, pad, gap, ph = 1200, 28, 8, 30
    cell = [0.0]
    body = header('Goal', f'{SITE.rstrip("/").replace("https://", "")} · as of {asof}', w)
    y = 76
    for line in wrap(g['directive'], 98):
        body += f'<text x="{pad}" y="{y}" fill="{INK}" font-size="19" font-weight="600">{esc(line)}</text>'
        y += 26
    y += 10

    def pill(x, y, item, label, arrow, cw=None):
        cw = cw or cell[0]
        dashed = item.get('source') in ('fork', 'wrapper', 'dependencies')
        stroke = '#5b6672' if dashed else '#ffd88f80'
        fill = 'none' if dashed else '#1a1610'
        dash = ' stroke-dasharray="4 3"' if dashed else ''
        out = f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="{ph}" rx="7" fill="{fill}" stroke="{stroke}"{dash}/>'
        mx, my = x + 11, y + ph / 2
        if item.get('shipped'):
            out += (f'<rect x="{mx - 6:.1f}" y="{my - 6:.1f}" width="12" height="12" rx="3" fill="{GREEN}"/>'
                    f'<path d="M{mx - 3:.1f} {my:.1f} l2.2 2.3 l4 -4.6" fill="none" stroke="{BG}" stroke-width="2" stroke-linecap="round"/>')
        elif item.get('status') in ('done', 'in-progress'):
            out += (f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="6.5" fill="{AMBER}"/>'
                    f'<path d="M{mx - 3:.1f} {my:.1f} l2.2 2.3 l4 -4.6" fill="none" stroke="{BG}" stroke-width="2" stroke-linecap="round"/>')
        tx = x + 24
        if item.get('source') == 'fork':
            # The fork mark, drawn (system fonts lack a fork glyph).
            out += (f'<g transform="translate({tx:.1f},{my - 6:.1f}) scale(.5)" fill="none" stroke="#aab3bc" stroke-width="2.2" stroke-linecap="round">'
                    '<circle cx="7" cy="5" r="2"/><circle cx="17" cy="5" r="2"/><circle cx="12" cy="19" r="2"/>'
                    '<path d="M7 7v1.5c0 2 1.5 3 5 3s5-1 5-3V7m-5 4.5V17"/></g>')
            tx += 15
        elif item.get('source') in ('wrapper', 'dependencies'):
            out += f'<rect x="{tx:.1f}" y="{my - 5:.1f}" width="10" height="10" rx="2" fill="none" stroke="#aab3bc"/><rect x="{tx + 3:.1f}" y="{my - 2:.1f}" width="4" height="4" fill="#aab3bc"/>'
            tx += 15
        color = '#c9d1d9' if dashed else INK
        out += f'<text x="{tx:.1f}" y="{my + 4.5:.1f}" fill="{color}" font-size="13" font-weight="{600 if arrow else 400}">{esc(label)}</text>'
        if arrow:
            out += f'<text x="{x + cw - 10:.1f}" y="{my + 4.5:.1f}" fill="{MUTED}" font-size="13" text-anchor="end">{arrow}</text>'
        return out

    for title, items, cols in (('Formats', g['codecs'], 6), ('Processing, manipulation and enhancement', g['media'], 5)):
        cw = cell[0] = (w - 2 * pad - (cols - 1) * gap) / cols
        body += f'<text x="{pad}" y="{y + 12}" fill="{MUTED}" font-size="11" font-weight="700" letter-spacing="1.5">{esc(title.upper())}</text>'
        y += 22
        for n, item in enumerate(items):
            x = pad + (n % cols) * (cw + gap)
            row = y + (n // cols) * (ph + gap)
            if 'encode' in item:
                arrow = '↔' if item['encode'] and item['decode'] else '→' if item['encode'] else '←'
                body += pill(x, row, item, item['label'], arrow)
            else:
                body += pill(x, row, item, item['label'], '')
        y += ((len(items) + cols - 1) // cols) * (ph + gap) + 10
    shipped = sum(1 for x in g['codecs'] + g['media'] if x.get('shipped'))
    done = sum(1 for x in g['codecs'] + g['media'] if not x.get('shipped') and x.get('status') == 'done')
    keys = [f'Green square: shipped on crates.io ({shipped}). Amber circle: done, shipping with the unified codec API ({done}).',
            'Solid border: original code. Dashed: our fork of, or our crate around, another project\'s library. ↔ encode and decode, ← decode only.']
    for k, key in enumerate(keys):
        body += f'<text x="{pad}" y="{y + 8 + 17 * k}" fill="{MUTED}" font-size="11.5">{esc(key)}</text>'
    h = y + 46
    return svg(w, h, body, 'Goals achieved: formats and processing, with what has shipped')


def tiles_card(title, tiles, cols, asof, note=''):
    w, pad, gap, th = 1200, 28, 1, 92
    rows = (len(tiles) + cols - 1) // cols
    cw = (w - 2 * pad) / cols
    body = header(title, f'{SITE.rstrip("/").replace("https://", "")} · as of {asof}', w)
    top = 60
    body += f'<rect x="{pad}" y="{top}" width="{w - 2 * pad}" height="{rows * th}" fill="{LINE}"/>'
    for n, (value, label, color) in enumerate(tiles):
        x, y = pad + (n % cols) * cw, top + (n // cols) * th
        body += f'<rect x="{x + gap:.1f}" y="{y + gap}" width="{cw - 2 * gap:.1f}" height="{th - 2 * gap}" fill="#0d131a"/>'
        body += f'<text x="{x + 16:.1f}" y="{y + 46}" fill="{AMBER if color else INK}" font-size="30" font-weight="700">{esc(value)}</text>'
        body += f'<circle cx="{x + 20:.1f}" cy="{y + 68}" r="3.5" fill="{color or MUTED}"/>'
        body += f'<text x="{x + 30:.1f}" y="{y + 72}" fill="#d5dbe1" font-size="13">{esc(label)}</text>'
    h = top + rows * th + (40 if note else 24)
    if note:
        body += f'<text x="{pad}" y="{h - 16}" fill="{MUTED}" font-size="11.5">{esc(note)}</text>'
    return svg(w, h, body, title)


def year_card(d, asof):
    m, wk, f = d['metrics'], d['work']['totals'], d['focus']
    hist = d.get('timeline') or []
    cases = next((t['test_cases'] for t in reversed(hist) if t.get('test_cases') is not None), None)
    stock = next((t['stock'] for t in reversed(hist) if t.get('stock')), {})
    tiles = [
        (fmt(m['commits']), 'Commits', '#f0eee8'),
        ('>' + fmt(d['prompts']['ledger']['total']), 'Instructions sent to AI', '#7fc8f8'),
        (fmt(wk['feat'] + wk.get('refactor', 0)), 'Features & refactoring', '#f5bd68'),
        (fmt(wk['fix']), 'Fixes', '#80d5d0'),
        (fmt(wk['perf'] + wk.get('bench', 0)), 'Perf work', '#9be38f'),
        ('>' + fmt(cases) if cases else '—', 'Test cases', '#ae9bdf'),
        ('>' + f"{stock.get('production', 0) / 1000:,.1f}K", 'Production lines', '#d95926'),
        ('>' + f"{stock.get('tests', 0) / 1000:,.1f}K", 'Test lines', '#199e70'),
        ('>' + f"{stock.get('docs', 0) / 1000:,.1f}K", 'Docs lines', '#9085e9'),
        (fmt(d['github']['issues_closed']), 'Issues closed', '#80d5d0'),
        (fmt(d['github']['upstream_pulls_merged']), 'Upstream PRs merged', '#9be38f'),
        (fmt(d['reviewed']['lines']) if (d.get('reviewed') or {}).get('lines') is not None else '—', 'Human-reviewed lines', '#c9b3f5'),
        ('>' + fmt(f['worked_hours']), 'Unpaid hours on OSS', '#f08fb5'),
        (fmt(d['crates']['releases_in_year']), 'crates.io releases', '#ffffff'),
        (fmt(d['crates']['first_published_in_year']), 'New crates', '#fff3d6'),
    ]
    return tiles_card(f"{d['year']} so far", tiles, 5, asof,
                      "'>' marks a lower bound (only reconciled histories, or only the minutes before each typed prompt). Commit figures are lilith's own commits in public repositories.")


def adoption_card(d, asof):
    u, a, m = d['usage'], d['adoption'], d['metrics']
    dep, cf = u['dependents'], m.get('contribution_forks') or {}
    tiles = [
        (fmt(u['crates_downloads_total']), 'crates.io downloads, all time', None),
        (fmt(u['package_downloads_total']), 'crates.io + NuGet downloads', None),
        ('≥' + fmt(dep['repositories']['at_least']), f"repositories depending on {dep['repositories']['largest']['package']}", None),
        (fmt(a['nuget']['downloads_total']), 'NuGet downloads, all time', None),
        (fmt(u['reverse_dependencies_summed']), 'crates.io reverse dependencies', None),
        (fmt(d['crates']['published']), 'crates published', None),
        (fmt(a['github']['stars_total']), 'GitHub stars', None),
        (fmt(cf.get('total', 0)), 'repositories forked to contribute upstream', None),
    ]
    return tiles_card('Adoption', tiles, 4, asof, f"Captured {dep['captured']} from crates.io, NuGet and GitHub's dependency graph; links to check each figure are in reports/adoption.md.")


def lines_card(d, asof):
    ch = d['churn']
    langs, days = ch['languages'], ch['language_days']
    year = d['year']
    jan1 = datetime.date(year, 1, 1)
    n_days = (datetime.date(year, 12, 31) - jan1).days + 1
    cum = [[0.0] * n_days for _ in langs]
    for date, values in days:
        i = (datetime.date.fromisoformat(date) - jan1).days
        if 0 <= i < n_days:
            for k, v in enumerate(values):
                cum[k][i] += v
    for row in cum:
        for i in range(1, n_days):
            row[i] += row[i - 1]
    last = max(i for i in range(n_days) if any(r[i] != r[i - 1] for r in cum if i > 0)) if days else 0
    w, pad, ph, top = 1200, 28, 220, 104
    total = sum(r[last] for r in cum) or 1
    x = lambda i: pad + i / (n_days - 1) * (w - 2 * pad)
    y = lambda v: top + ph - v / total * ph
    body = header(f'File lines committed, {year}', f'{SITE.rstrip("/").replace("https://", "")} · as of {asof}', w)
    lx = pad
    for k, lang in enumerate(langs):
        label = f"{FILE_LABELS.get(lang, lang)} {cum[k][last] / 1000:,.0f}K"
        body += f'<rect x="{lx}" y="58" width="11" height="11" rx="2" fill="{FILE_COLORS[k]}"/><text x="{lx + 16}" y="68" fill="#d5dbe1" font-size="12.5">{esc(label)}</text>'
        lx += 24 + len(label) * 7.2
    base = [0.0] * (last + 1)
    for k in range(len(langs)):
        topline, bottom = [], []
        for i in list(range(0, last, 3)) + [last]:
            bottom.append(f'{x(i):.1f},{y(base[i]):.1f}')
            topline.append(f'{x(i):.1f},{y(base[i] + cum[k][i]):.1f}')
        for i in range(last + 1):
            base[i] += cum[k][i]
        body += f'<polygon points="{" ".join(topline)} {" ".join(reversed(bottom))}" fill="{FILE_COLORS[k]}" fill-opacity=".88" stroke="{BG}" stroke-width="1"/>'
    for mth in range(12):
        i = (datetime.date(year, mth + 1, 1) - jan1).days
        body += f'<line x1="{x(i):.1f}" x2="{x(i):.1f}" y1="{top}" y2="{top + ph}" stroke="#ffffff" stroke-opacity=".06"/>'
        body += f'<text x="{x(i) + 3:.1f}" y="{top + ph + 16}" fill="{MUTED}" font-size="11">{datetime.date(year, mth + 1, 1).strftime("%b")}</text>'
    note = (f"Every line of every text file lilith's commits added, as git counts them (blank lines, data and vendored files included), "
            f"in {ch['repositories']} reconciled repository histories; merge commits left out.")
    body += f'<text x="{pad}" y="{top + ph + 40}" fill="{MUTED}" font-size="11.5">{esc(note)}</text>'
    return svg(w, top + ph + 56, body, f'File lines committed in {year}, by file type, accumulated')


def activity_card(d, asof):
    year = d['year']
    jan1 = datetime.date(year, 1, 1)
    weeks = 53
    fams = [f for f in d['families'] if f['id'] != 'other']
    counts = {f['id']: [0] * weeks for f in fams}
    for p in d['projects']:
        fam = p.get('family') or 'other'
        if fam not in counts:
            continue
        for date, n in p.get('commit_days') or []:
            i = (datetime.date.fromisoformat(date[:10]) - jan1).days // 7
            if 0 <= i < weeks:
                counts[fam][i] += n
    w, pad, label_w, rh = 1200, 28, 200, 22
    cell = (w - 2 * pad - label_w) / weeks
    peak = max(max(v) for v in counts.values()) or 1
    body = header(f'Commits by week and family, {year}', f'{SITE.rstrip("/").replace("https://", "")} · as of {asof}', w)
    top = 64
    for r, f in enumerate(fams):
        y = top + r * rh
        total = sum(counts[f['id']])
        body += f'<text x="{pad}" y="{y + 15}" fill="#e8e6e0" font-size="12.5" font-weight="600">{esc(f["label"])}</text>'
        body += f'<text x="{pad + label_w - 8}" y="{y + 15}" fill="{MUTED}" font-size="11.5" text-anchor="end">{fmt(total)}</text>'
        for i, n in enumerate(counts[f['id']]):
            if n:
                op = 0.18 + 0.82 * (n / peak) ** 0.5
                body += f'<rect x="{pad + label_w + i * cell:.1f}" y="{y + 3}" width="{cell - 1.5:.1f}" height="{rh - 6}" rx="2" fill="{FAMILY_COLORS.get(f["id"], MUTED)}" fill-opacity="{op:.2f}"/>'
    h = top + len(fams) * rh + 34
    body += f'<text x="{pad}" y="{h - 14}" fill="{MUTED}" font-size="11.5">lilith\'s commits in public repositories, grouped by family; brighter cells are busier weeks.</text>'
    return svg(w, h, body, f'Commits by week and family in {year}')


# ---------- reports ----------

def measurements():
    files = sorted(glob.glob(os.path.join(ROOT, 'data', 'measurements-*.json')))
    return json.load(open(files[-1])) if files else None


def ai_line(d):
    """AI services against the other cloud spend in the owner's books, when the data carries them."""
    ai = d.get('ai_spend') or {}
    if not ai.get('through'):
        return ''
    a = ai['max20'] + ai['other']
    rest = (ai.get('cloud') or {}).get('total', 0) + (ai.get('software') or {}).get('total', 0)
    return (f"AI services are the largest part of the project's cloud spend: ${fmt(a)} of ${fmt(a + rest)} "
            f"from January 1 to {ai['through']} (the books' charges; hosting and software make up the rest).")


def program_fit(d, meas):
    u, a = d['usage'], d['adoption']
    by = a['crates']['by_crate']
    per_month = sum(c.get('downloads_90d') or 0 for c in by) / 3
    top_crate = max(by, key=lambda c: c.get('downloads_90d') or 0)
    dep = u['dependents']
    stars = sorted(a['github']['by_repository'].items(), key=lambda kv: -(kv[1].get('stars') or 0))
    rows_a = [
        ('Maintainer: 500+ dependent repositories', 'Meets',
         f"[{dep['repositories']['largest']['repository']}](https://github.com/{dep['repositories']['largest']['repository']}/network/dependents) "
         f"({dep['repositories']['largest']['package']}): {fmt(dep['repositories']['largest']['count'])} dependent repositories on GitHub's dependency graph ({dep['captured']})"),
        ('Maintainer: 200,000+ combined monthly downloads', 'Meets',
         f"{fmt(per_month)} a month across {len(by)} crates: crates.io's 90-day downloads ({fmt(per_month * 3)}) divided by three. "
         f"[{top_crate['crate']}](https://crates.io/crates/{top_crate['crate']}) alone: {fmt((top_crate.get('downloads_90d') or 0) / 3)} a month"),
        ('Maintainer: 100+ dependent packages', 'Approaches',
         f"{dep['packages']['largest']['package']}: {fmt(dep['packages']['largest']['count'])} dependent packages; {fmt(dep['packages']['reported_sum'])} summed over all our packages"),
    ]
    if meas:
        up = meas['upstream_merged_pull_requests_12_months']
        ex = meas['external_contributors_12_months']
        sc = meas['openssf_criticality_score']['scores']
        top = sorted(sc.items(), key=lambda kv: -kv[1])
        rows_a.append(('Critical infrastructure: OpenSSF criticality score 0.4+', 'Meets',
                       '; '.join(f"[{r}](https://github.com/{r}) {s:.3f}" for r, s in top if s >= 0.4) +
                       f" (scored {meas['measured_on']} without the deps.dev dependents signal, which can only raise a score)"))
        rows_a.append(('Active contributor: 100+ merged PRs to repositories you don\'t own, 12 months', 'Approaches',
                       f"{up['count']} merged since {up['since']}, into " + ', '.join(f"[{r}](https://github.com/{r}/pulls?q=is%3Apr+author%3Alilith+is%3Amerged)" for r in list(up['by_repository'])[:8]) + ' and others'))
        rows_a.append(('Community builder: a repository with 20+ external contributors, 12 months', 'Not met',
                       f"at most {ex['most_on_one_repository']} on one repository; {ex['unique_people_across_imazen']} people across imazen"))
    out = ['# Open-source program fit', '',
           f"Measured on {meas['measured_on'] if meas else 'the date of the data'} against each program's published criteria. "
           f"Every figure links to a page where it can be checked; the GitHub and OpenSSF measurements and their commands are in "
           f"[data/]({'../data/'}). Live numbers: [{SITE}]({SITE}).", '',
           '## Anthropic: Claude for Open Source', '',
           'Criteria from [claude.com/contact-sales/claude-for-oss](https://claude.com/contact-sales/claude-for-oss) (checked 2026-10-28); any one track qualifies.', '',
           '| Track | Status | Evidence |', '|---|---|---|']
    out += [f'| {t} | {s} | {e} |' for t, s, e in rows_a]
    out += ['', '## OpenAI: Codex for Open Source', '',
            'From [developers.openai.com/community/codex-for-oss](https://developers.openai.com/community/codex-for-oss) (checked 2026-10-28): '
            'for core maintainers of public projects and people who run widely used public projects; projects that do not fit the criteria '
            'but matter to the ecosystem are asked to apply and explain why. The [Codex open source fund](https://github.com/openai/codex/blob/main/docs/open-source-fund.md) '
            'gives API credits (up to $25,000) to projects that use Codex in pull request review, maintainer automation and release work.', '',
            '| Criterion | Evidence |', '|---|---|',
            f"| Core maintainer of public projects | lilith maintains the [imazen](https://github.com/imazen) and [lilith](https://github.com/lilith) repositories listed in [projects.md](projects.md); on GitHub since {d['profile']['joined'][:4]} |",
            f"| Widely used | [{stars[0][0]}](https://github.com/{stars[0][0]}) {fmt(stars[0][1]['stars'])} stars; {fmt(u['package_downloads_total'])} crates.io and NuGet downloads; {fmt(dep['repositories']['at_least'])}+ dependent repositories |",
            '| Uses Codex in maintainer work | Codex reviews designs and changes in the agent workflow described in [ai-assisted-development.md](ai-assisted-development.md) |',
            '', '## Why these programs matter here', '',
            '- **Decoders parse hostile input.** Every codec here reads bytes from strangers. Security tooling (Codex Security, and access to the models\' '
            'cybersecurity capabilities) goes straight at the riskiest code; today even safe-Rust codec work trips model safety filters often.',
            f"- **The work runs on agents every day.** {fmt(d['prompts']['ledger']['total'])} instructions went to AI agents in {d['year']}, across more than "
            f"{fmt(d['focus']['worked_hours'])} unpaid hours. " + ai_line(d),
            '- **Review and release automation.** Codex already reviews designs and changes; API credits would run that review on every pull request and '
            'release in the public repositories.',
            '- **The fixes travel upstream.** Work here regularly lands in other projects: ' +
            (f"{meas['upstream_merged_pull_requests_12_months']['count']} merged pull requests in the last 12 months" if meas else 'see the active-contributor row') +
            ', in image-rs, jxl-rs, moxcms, zune-image and others.',
            '', '## Projects nearest each criterion', '']
    for r, v in stars[:5]:
        out.append(f"- [{r}](https://github.com/{r}): {fmt(v['stars'])} stars" + (f", OpenSSF criticality {meas['openssf_criticality_score']['scores'][r]:.3f}" if meas and r in meas['openssf_criticality_score']['scores'] else ''))
    for c in sorted(by, key=lambda c: -(c.get('downloads_90d') or 0))[:8]:
        out.append(f"- [{c['crate']}](https://crates.io/crates/{c['crate']}) ([{c['repository']}](https://github.com/{c['repository']})): "
                   f"{fmt(c['downloads_90d'])} downloads in 90 days, {c.get('reverse_dependencies') or 0} crates.io reverse "
                   f"{'dependency' if (c.get('reverse_dependencies') or 0) == 1 else 'dependencies'}")
    return '\n'.join(out) + '\n'


def projects_report(d):
    proj = {p['repository']: p for p in d['projects']}
    by_crate = {}
    for c in d['adoption']['crates']['by_crate']:
        by_crate.setdefault(c['repository'], []).append(c)
    stars = d['adoption']['github']['by_repository']
    out = ['# Projects', '', f"Every public repository counted on [{SITE}]({SITE}), in the page's topics. "
           f"Commits are lilith's in {d['year']}; downloads are crates.io's last 90 days.", '']
    for topic in d['guide']['topics']:
        seen, lines = set(), []
        for item in topic['items']:
            repo = item.get('repository')
            if not repo or repo in seen or repo not in proj:
                continue
            seen.add(repo)
            p = proj[repo]
            facts = []
            if p.get('commits'):
                facts.append(f"{fmt(p['commits'])} commits")
            dl = sum(c.get('downloads_90d') or 0 for c in by_crate.get(repo, []))
            if dl:
                facts.append(f"{fmt(dl)} downloads/90d")
            if (stars.get(repo) or {}).get('stars'):
                facts.append(f"{fmt(stars[repo]['stars'])} stars")
            desc = (p.get('description') or '').replace('|', '/').strip()
            lines.append(f"| [{repo.split('/')[1]}](https://github.com/{repo}) | {esc(desc)[:160]} | {' · '.join(facts)} |")
        if lines:
            out += [f"## {topic['label']}", '', '| Repository | What it is | This year |', '|---|---|---|'] + lines + ['']
    return '\n'.join(out)


def adoption_report(d):
    u, a = d['usage'], d['adoption']
    dep = u['dependents']
    out = ['# Adoption', '', f"Captured {dep['captured']}. Each figure links to the page that lists it.", '',
           '| Figure | Value | Check it |', '|---|---|---|',
           f"| crates.io downloads, all time | {fmt(u['crates_downloads_total'])} | [crates.io/users/lilith](https://crates.io/users/lilith?sort=downloads) |",
           f"| NuGet downloads, all time | {fmt(a['nuget']['downloads_total'])} | [nuget.org/profiles/imazen](https://www.nuget.org/profiles/imazen) |",
           f"| Repositories depending on {dep['repositories']['largest']['package']} | ≥{fmt(dep['repositories']['at_least'])} | [GitHub dependents](https://github.com/{dep['repositories']['largest']['repository']}/network/dependents) |",
           f"| Packages depending on {dep['packages']['largest']['package']} | {fmt(dep['packages']['largest']['count'])} | [GitHub dependent packages](https://github.com/{dep['packages']['largest']['repository']}/network/dependents?dependent_type=PACKAGE) |",
           f"| crates.io reverse dependencies, summed | {fmt(u['reverse_dependencies_summed'])} | [crates.io](https://crates.io/users/lilith?sort=downloads) |",
           f"| GitHub stars, public repositories | {fmt(a['github']['stars_total'])} | [imazen by stars](https://github.com/orgs/imazen/repositories?type=public&sort=stargazers) |",
           '', '## Most downloaded crates (last 90 days)', '', '| Crate | Repository | 90 days | All time | Reverse dependencies |', '|---|---|---|---|---|']
    for c in sorted(a['crates']['by_crate'], key=lambda c: -(c.get('downloads_90d') or 0))[:25]:
        out.append(f"| [{c['crate']}](https://crates.io/crates/{c['crate']}) | [{c['repository']}](https://github.com/{c['repository']}) | {fmt(c['downloads_90d'])} | {fmt(c['downloads_total'])} | [{c.get('reverse_dependencies') or 0}](https://crates.io/crates/{c['crate']}/reverse_dependencies) |")
    out += ['', '## Most downloaded NuGet packages', '', '| Package | All time |', '|---|---|']
    for p in a['nuget']['packages'][:15]:
        out.append(f"| [{p['package']}](https://www.nuget.org/packages/{p['package']}) | {fmt(p['downloads_total'])} |")
    return '\n'.join(out) + '\n'


def ai_report(d):
    led, f, w = d['prompts']['ledger'], d['focus'], d['token_ledger']['window']
    totals = w['totals']
    tok = sum(t['input'] + t['cache_read'] + t['output'] for t in totals.values())
    words = (f.get('words') or {}).get('total')
    return '\n'.join([
        '# AI-assisted development', '',
        'Most code here is written with frontier AI agents (Claude Code, Codex, Devin and others) running on six development machines with different CPUs and '
        'operating systems. The agents work under rules that keep the output checkable: `#![forbid(unsafe_code)]`, resource limits on every decoder, bit-exact '
        'tests against C reference implementations where they exist, continual fuzzing, and perceptual metrics where pixels may differ. '
        'Codex reviews designs and changes; [quality-and-security.md](quality-and-security.md) has the details.', '',
        '| Measured | Value |', '|---|---|',
        f"| Instructions sent to AI agents in {d['year']} (input-history entries, every agent and host) | {fmt(led['total'])} |",
        f"| Prompts lilith typed | {fmt(f['prompts'])}" + (f" ({fmt(words)} words)" if words else '') + ' |',
        f"| Unpaid hours on open source (the {f['reading_minutes']} minutes before each typed prompt, overlaps merged; a lower bound) | >{fmt(f['worked_hours'])} |",
        f"| Tokens processed {w['start']} to {w['end']} ({w['days']} days of complete records, every agent) | {big(tok)} |",
        '', f"Prompt text is never kept: the inventory counts entries and words. Live figures and their scopes: [{SITE}]({SITE}).", ''])


def quality_report():
    return '\n'.join([
        '# Quality and security', '',
        "Image codecs take bytes from strangers and turn them into pixels, usually on a server that also holds other people's data. A bug in a decoder is a "
        'security hole. All of this work is shaped by that fact, and it is also the reason frontier AI models can write so much of the code.', '',
        '**Memory and concurrency safety the compiler checks.** Our crates compile with `#![forbid(unsafe_code)]`, so the compiler rules out out-of-bounds writes, '
        "use-after-free and data races. SIMD goes through two small primitive crates, [archmage](https://imazen.github.io/archmage/) and magetypes, that wrap the "
        'intrinsics once; a few older crates still carry unsafe code, and we treat it as debt.', '',
        '**Limits on everything.** Decoders and encoders take resource limits (dimensions, pixel counts, memory) and fail cleanly instead of taking the process '
        'down. Long jobs accept cooperative cancellation ([enough](https://crates.io/crates/enough)), and CPU cost is predicted before the work starts.', '',
        '**Bytes in, bytes out.** The domain is bytes and configuration in, bytes out, which makes it unusually testable. When a C reference exists we test '
        'against it bit for bit; where pixels may differ, perceptual metrics tell us whether a person would see it.', '',
        '**Fuzzing, continually, on every platform**, with minimized regression files every later build must pass.', '',
        '**Metrics we can trust.** [zensim](https://github.com/imazen/zensim) is our perceptual metric; to build it we ported 141 image-quality metrics to Rust '
        '([what each costs to run](https://metric-brief.imazen.org/#models)), gathered over a terabyte of IQA datasets, and scored millions of encodes.', '',
        '**What it replaces.** ImageMagick has [913 published vulnerabilities](https://app.opencve.io/cve/?vendor=imagemagick) (OpenCVE, checked 2026-10-28). '
        'This toolset is built to replace it on servers: memory-safe, faster, with better compression.', '',
        "*The owner's account; figures without a link are the owner's statements. The live version is chapter 05 of "
        f"[{SITE}]({SITE}).*", ''])


TOPIC_NOTES = {
    'Codecs': 'encode and decode, in safe Rust', 'AV1 and codec internals': 'the AV1 encoders, decoder and containers under AVIF',
    'Processing': 'resize, quantize, blend, tone-map, enhance', 'Pixels & color': 'pixel formats, transfer functions, color',
    'Pipeline & framework': 'streaming pipeline, codec traits, layout', 'Compression': 'DEFLATE, Zopfli, Zstandard',
    'Psychovisual metrics': 'perceptual quality, to tune the codecs', 'Pickers & ML': 'the right codec and quality per image',
    'Test corpora': 'images to test and train on', 'SIMD & Rust foundations': 'safe SIMD, cancellation, errors, benchmarks',
    'Developer tools': 'workspace, release and API tooling', 'Products': 'image servers and their bindings',
    'Other tools': 'everything else in use', 'Earlier work': 'the .NET and C years',
}


def readme_map(d, asof):
    """The README map, the way the "Image tech I maintain" block at the end of many of these READMEs lists it, with
    the page's topics and live counts: repositories, crates on crates.io and commits this year per topic; the most
    used entries in bold."""
    proj = {p['repository']: p for p in d['projects']}
    published = {c['name'] for p in d['projects'] for c in p.get('crates') or [] if (c.get('crates_io') or {}).get('first_published')}
    dl = {c['crate']: c.get('downloads_90d') or 0 for c in d['adoption']['crates']['by_crate']}
    stars = {r: v.get('stars') or 0 for r, v in d['adoption']['github']['by_repository'].items()}
    # Stars belong to a repository: they bold its main entry (named after it, or its only entry in the topic).
    popular = lambda label, repo, sole: dl.get(label, 0) >= 10000 or bool(
        repo and stars.get(repo, 0) >= 100 and (repo.split('/')[1].lower() == label.lower() or sole))
    rows, refs = [], {}
    for topic in d['guide']['topics']:
        items, seen, repos = [], set(), set()
        for it in topic['items']:
            label, repo = it['label'], it.get('repository')
            if label in seen or (repo and repo not in proj):
                continue
            seen.add(label)
            if repo:
                repos.add(repo)
            refs.setdefault(label, it.get('url') or f'https://github.com/{repo}')
            items.append((label, repo, it.get('parent')))
        if not items:
            continue
        commits = sum((proj[r].get('commits') or 0) for r in repos)
        crates = sum(1 for label, _, _ in items if label in published)
        shown = items
        if topic['label'] == 'Earlier work':  # the long tail: the ones people still star
            shown = sorted([x for x in items if stars.get(x[1], 0) >= 20], key=lambda x: -stars.get(x[1], 0))
        per_repo = {}
        for _, repo, _ in shown:
            per_repo[repo] = per_repo.get(repo, 0) + 1
        link = lambda label, repo: f'**[{label}]**' if popular(label, repo, per_repo.get(repo) == 1) else f'[{label}]'
        # Entries with a parent (the Imageflow bindings) sit in brackets after it, as in the README map.
        children = {}
        for label, repo, parent in shown:
            if parent:
                children.setdefault(parent, []).append(link(label, repo))
        cells = ' · '.join(link(label, repo) + (f" ({' · '.join(children[label])})" if label in children else '')
                           for label, repo, parent in shown if not parent)
        if len(shown) < len(items):
            cells += f' · [and {len(items) - len(shown)} more](reports/projects.md)'
        facts = [f"{len(repos)} repo{'s' if len(repos) != 1 else ''}"] + ([f'{crates} on crates.io'] if crates else []) + ([f'{fmt(commits)} commits'] if commits else [])
        rows.append(f"| **{topic['label']}**<br><sub>{esc(TOPIC_NOTES.get(topic['label'], ''))}</sub> | {cells} | <sub>{' · '.join(facts)}</sub> |")
    links = ' · '.join(f"[{l['label']}]({l['url']})" for l in d['guide'].get('profile_links') or [])
    block = ['| | | |', '|:--|:--|:--|', *rows, '',
             f"<sub>**Bold**: the most used, with 10,000+ crates.io downloads in the last 90 days or 100+ GitHub stars. Commits are lilith's in {d['year']}. "
             f"As of {asof}; live on [stats.lilith.now]({SITE}).</sub>", '', links, '']
    return block, refs


def readme(d, asof, meas):
    u, a = d['usage'], d['adoption']
    dep = u['dependents']
    per_month = sum(c.get('downloads_90d') or 0 for c in a['crates']['by_crate']) / 3
    sc = (meas or {}).get('openssf_criticality_score', {}).get('scores', {})
    crit = ', '.join(f'{r.split("/")[1]} {s:.2f}' for r, s in sorted(sc.items(), key=lambda kv: -kv[1]) if s >= 0.4)
    stars = sorted(a['github']['by_repository'].items(), key=lambda kv: -(kv[1].get('stars') or 0))
    g = d['directive']
    feature = [
        ('imazen/imageflow', 'image server engine and the C API behind the imageflow bindings'),
        ('imazen/resizer', 'ImageResizer, the .NET image server'),
        ('imazen/zenjpeg', 'JPEG encoder and decoder (a jpegli port) in safe Rust'),
        ('imazen/zenwebp', 'WebP, lossy and lossless'),
        ('imazen/zenavif', 'AVIF on owned AV1 encoders and a safe decoder'),
        ('imazen/jxl-encoder', 'JPEG XL encoder'),
        ('imazen/zenpipe', 'the streaming pipeline that ties the codecs together'),
        ('imazen/zensim', 'the perceptual metric that tunes the codecs'),
        ('imazen/archmage', 'safe SIMD through capability tokens'),
        ('imazen/enough', 'cooperative cancellation for long-running Rust work'),
    ]
    map_block, refs = readme_map(d, asof)
    lines = [
        '# awesome', '',
        f"Lilith River's open-source imaging work, in one place: what it is for, what is done, who depends on it, and how it is built. "
        f"Live numbers: **[{SITE.replace('https://', '').rstrip('/')}]({SITE})**.", '',
        *map_block,
        f"> {g['directive']}", '',
        f'[![Goals: formats and processing, with what has shipped]({"assets/goals.svg"})]({SITE})', '',
        f"I've published open source on GitHub since {d['profile']['joined'][:4]}; {d['year']} is my {d['profile']['oss_year']}th year there, as "
        '[@lilith](https://github.com/lilith) and through [imazen](https://github.com/imazen). That work includes ImageResizer and Imageflow, and now a '
        'pure-Rust imaging stack written with frontier AI agents under rules that make their work checkable.', '',
        '## Who depends on it', '',
        f"- **{fmt(u['package_downloads_total'])} downloads** across [crates.io](https://crates.io/users/lilith?sort=downloads) and "
        f"[NuGet](https://www.nuget.org/profiles/imazen); **{fmt(per_month)} crates.io downloads a month** over the last 90 days.",
        f"- **{fmt(dep['repositories']['at_least'])}+ repositories** depend on [{dep['repositories']['largest']['package']}](https://github.com/{dep['repositories']['largest']['repository']}/network/dependents).",
        f"- **{fmt(a['github']['stars_total'])} GitHub stars**; [{stars[0][0]}](https://github.com/{stars[0][0]}) has {fmt(stars[0][1]['stars'])}.",
    ]
    if crit:
        lines.append(f"- **OpenSSF criticality score** of 0.4 or more: {crit} ([how it was measured](data/)).")
    lines += ['', f'[![Adoption]({"assets/adoption.svg"})]({SITE})', '',
              '## Open-source programs', '',
              "Against [Anthropic's Claude for Open Source](https://claude.com/contact-sales/claude-for-oss) criteria this work meets the maintainer track "
              '(500+ dependent repositories; 200,000+ monthly downloads) and the critical-infrastructure track (OpenSSF criticality 0.4+), and approaches the '
              "active-contributor track. For [OpenAI's Codex for Open Source](https://developers.openai.com/community/codex-for-oss) it is a set of widely used "
              'public projects whose maintainer work already runs through Codex review. Evidence for each criterion: **[reports/program-fit.md](reports/program-fit.md)**.', '',
              f"## {d['year']} so far", '', f'[![The year in numbers]({"assets/year.svg"})]({SITE})', '',
              f'[![Commits by week and family]({"assets/activity.svg"})]({SITE})', '',
              f'[![File lines committed, by file type]({"assets/lines-by-file-type.svg"})]({SITE})', '',
              '## Where to start', '']
    for repo, what in feature:
        lines.append(f"- [{repo.split('/')[1]}](https://github.com/{repo}): {what}")
    lines += ['', f"All {len(d['projects'])} public projects by topic: [reports/projects.md](reports/projects.md). Interactive dashboards: "
              '[metrics](https://metrics.imazen.org/), [metric cost](https://metric-brief.imazen.org/#models), [gigapixels](https://gigapixels.imazen.org/), '
              '[JPEG AI in the browser](https://jpegai.imazen.org/), [squintly](https://squintly.imazen.org/), [imazen-26](https://imazen-26-review.pages.dev/), '
              '[archmage docs](https://imazen.github.io/archmage/).', '',
              '## How it is built', '',
              'Safety the compiler checks (`#![forbid(unsafe_code)]`), resource limits and cancellation in every codec, bit-exact tests against C references, '
              'continual fuzzing, and perceptual metrics: [reports/quality-and-security.md](reports/quality-and-security.md). How AI agents fit in, with measured '
              'figures: [reports/ai-assisted-development.md](reports/ai-assisted-development.md).', '',
              '## Reports', '',
              '- [Program fit](reports/program-fit.md): Anthropic and OpenAI open-source program criteria, with evidence',
              '- [Projects](reports/projects.md): every public project by topic',
              '- [Adoption](reports/adoption.md): downloads and dependents, with links to check each',
              '- [Quality and security](reports/quality-and-security.md)',
              '- [AI-assisted development](reports/ai-assisted-development.md)', '',
              '## Reproduce', '',
              f"`python3 tools/build.py` rebuilds every card and report from the public data behind [{SITE}]({SITE}) ({SITE}data.json); "
              'the GitHub and OpenSSF measurements are in [data/](data/) with their commands. Standard library only.', '',
              f"*Generated {asof} from data revision {d['revision'][:12]}.*", '']
    lines += [f'[{label}]: {url}' for label, url in refs.items()] + ['']
    return '\n'.join(lines)


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else SITE + 'data.json'
    d = load(source)
    asof = d['generated_at'][:10]
    meas = measurements()
    files = {
        'assets/goals.svg': goals_card(d, asof),
        'assets/year.svg': year_card(d, asof),
        'assets/adoption.svg': adoption_card(d, asof),
        'assets/lines-by-file-type.svg': lines_card(d, asof),
        'assets/activity.svg': activity_card(d, asof),
        'reports/program-fit.md': program_fit(d, meas),
        'reports/projects.md': projects_report(d),
        'reports/adoption.md': adoption_report(d),
        'reports/ai-assisted-development.md': ai_report(d),
        'reports/quality-and-security.md': quality_report(),
        'README.md': readme(d, asof, meas),
    }
    for name, text in files.items():
        path = os.path.join(ROOT, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(text)
        print(f'{name}: {len(text):,} bytes')


if __name__ == '__main__':
    main()
