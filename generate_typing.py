"""Regenerate assets/typing.svg from the ROLES list.

Usage:  python3 scripts/generate_typing.py
Edit ROLES below, run the script, commit assets/typing.svg.
"""
import os

ROLES = [
    "Data Science Student",
    "Future Data Scientist",
    "Frontend Developer",
    "Web & App Developer",
    "DSA Learner",
    "AI Enthusiast",
]
SECONDS_PER_ROLE = 3

MONO = "'Fira Code','JetBrains Mono','SF Mono',Consolas,'Courier New',monospace"
C, B, P = "#22d3ee", "#3b82f6", "#a855f7"
BRAND = (f'<linearGradient id="brand" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{C}"/>'
         f'<stop offset=".55" stop-color="{B}"/><stop offset="1" stop-color="{P}"/></linearGradient>')
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{l}">'
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "typing.svg")


def w(_name, s):
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(s)

def typing(roles=ROLES, seconds_per_role=3):
    n, cyc, adv = len(roles), len(roles) * seconds_per_role, 17
    parts = []
    for i, r in enumerate(roles):
        wd = len(r) * adv
        x0 = (800 - wd) / 2
        s, wn = i / n, 1 / n
        kt = ";".join(f"{v:.4f}" for v in [0, s, s + 0.4 * wn, s + 0.85 * wn, s + 0.95 * wn, 1])
        t = r.replace("&", "&amp;")
        parts.append(
            f'<clipPath id="c{i}"><rect x="{x0}" y="0" height="60" width="0"><animate attributeName="width" values="0;0;{wd};{wd};0;0" keyTimes="{kt}" dur="{cyc}s" repeatCount="indefinite"/></rect></clipPath>'
            f'<text x="{x0}" y="39" clip-path="url(#c{i})" textLength="{wd}" lengthAdjust="spacing" font-family="{MONO}" font-size="28" font-weight="600" fill="url(#brand)">{t}</text>'
            f'<g opacity="0"><animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;{s:.4f};{s + 0.95 * wn:.4f}" dur="{cyc}s" repeatCount="indefinite"/>'
            f'<rect y="12" width="3" height="32" fill="{C}"><animate attributeName="x" values="{x0};{x0};{x0 + wd};{x0 + wd};{x0};{x0}" keyTimes="{kt}" dur="{cyc}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect></g>'
        )
    s = HEAD.format(w=800, h=60, l="Typing animation: " + ", ".join(roles).replace("&", "&amp;"))
    s += f'<defs>{BRAND}</defs><rect width="800" height="60" rx="14" fill="#0b1020"/><rect x=".5" y=".5" width="799" height="59" rx="14" fill="none" stroke="url(#brand)" stroke-opacity=".4"/>' + "".join(parts) + "</svg>"
    w("typing.svg", s)


if __name__ == "__main__":
    typing(ROLES, SECONDS_PER_ROLE)
    print("wrote", os.path.normpath(OUT))
