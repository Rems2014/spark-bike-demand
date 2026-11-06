"""Create GitHub-friendly SVG charts from the small Spark result tables."""
from html import escape
import json
from pathlib import Path


def render(report):
    data = json.loads((report / 'results.json').read_text(encoding='utf-8'))
    specs = [
        ('03_peak_hours', 'hour', 'average_rentals', 'Average rentals by hour', 'hourly_demand.svg'),
        ('02_monthly_trend', 'month', 'total_rentals', 'Monthly rental totals', 'monthly_demand.svg'),
    ]
    for table, label, value, title, filename in specs:
        rows = sorted(data[table], key=lambda row: row[label])
        top = max(float(row[value]) for row in rows) * 1.1
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 440" role="img" aria-label="{title}">',
               '<rect width="1000" height="440" fill="#f8fafc"/>',
               '<g font-family="Arial, sans-serif" fill="#0f172a">',
               f'<text x="70" y="35" font-size="24" font-weight="bold">{title}</text>',
               '<text x="70" y="58" font-size="13">Capital Bikeshare | 2011–2012 | Source: UCI Bike Sharing dataset</text>']
        for tick in range(6):
            y = 340 - tick * 50
            svg += [f'<path d="M70 {y}H970" stroke="#cbd5e1"/>',
                    f'<text x="60" y="{y+4}" text-anchor="end" font-size="12">{top*tick/5:,.0f}</text>']
        width = 900 / len(rows)
        for i, row in enumerate(rows):
            height = float(row[value]) / top * 250
            x = 70 + i * width
            text = escape(str(row[label]))
            svg += [f'<rect x="{x+4:.1f}" y="{340-height:.1f}" width="{width-8:.1f}" height="{height:.1f}" fill="#0f766e"><title>{text}: {row[value]}</title></rect>',
                    f'<text transform="translate({x+width/2:.1f},355) rotate(60)" font-size="11">{text}</text>']
        svg += ['<text x="70" y="425" font-size="12">Descriptive historical data. Missing hours are not treated as zero.</text>', '</g></svg>']
        (report / filename).write_text('\n'.join(svg), encoding='utf-8')


if __name__ == '__main__':
    render(Path(__file__).resolve().parents[1] / 'reports')
