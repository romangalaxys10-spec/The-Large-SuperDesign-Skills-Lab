#!/usr/bin/env python3
"""Validates The Large SuperDesign Skills Lab.

Checks:
 1. Every folder under skills/ has a SKILL.md with name+description frontmatter.
 2. skills-index.json is in sync with the filesystem (slugs + families).
 3. No broken internal markdown links inside skills/*/SKILL.md (relative refs).
Exit code 1 on any failure.
"""
import os, re, json, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
errors = []

# --- 1. SKILL.md presence + frontmatter ---
folders = sorted(d for d in os.listdir(SKILLS)
                 if os.path.isdir(os.path.join(SKILLS, d)))
for d in folders:
    sk = os.path.join(SKILLS, d, "SKILL.md")
    if not os.path.exists(sk):
        # family packs may nest; search one level deep
        found = any(os.path.exists(os.path.join(r, "SKILL.md"))
                    for r, _, fs in os.walk(sk if os.path.exists(sk) else os.path.join(SKILLS, d))
                    for f in fs) or \
                 any("SKILL.md" in fs for _, _, fs in os.walk(os.path.join(SKILLS, d)))
        if not found:
            errors.append(f"skills/{d}: no SKILL.md anywhere in folder")
        continue
    head = open(sk, encoding="utf-8", errors="replace").read(900)
    if not head.startswith("---"):
        errors.append(f"skills/{d}/SKILL.md: missing YAML frontmatter")
        continue
    fm_end = head.find("---", 3)
    fm = head[3:fm_end] if fm_end > 0 else head
    if not re.search(r"^name:", fm, re.M):
        errors.append(f"skills/{d}/SKILL.md: frontmatter missing 'name'")
    if not re.search(r"^description:", fm, re.M):
        errors.append(f"skills/{d}/SKILL.md: frontmatter missing 'description'")

# --- 2. index sync ---
idx_path = os.path.join(ROOT, "skills-index.json")
idx = json.load(open(idx_path))
indexed = {e["slug"] for e in idx}
missing_in_index = [d for d in folders if d not in indexed]
stale_in_index = [s for s in indexed if s not in folders]
if missing_in_index:
    errors.append(f"skills-index.json missing slugs: {missing_in_index[:10]}")
if stale_in_index:
    errors.append(f"skills-index.json stale slugs: {stale_in_index[:10]}")

# --- 3. internal md links inside top-level SKILL.md files ---
link_re = re.compile(r"\]\((?!http|#/|mailto)([^)#]+?)(?:#[^)]*)?\)")
checked = 0
for d in folders:
    sk = os.path.join(SKILLS, d, "SKILL.md")
    if not os.path.exists(sk):
        continue
    base = os.path.dirname(sk)
    for m in link_re.finditer(open(sk, encoding="utf-8", errors="replace").read()):
        rel = m.group(1).strip()
        checked += 1
        target = os.path.normpath(os.path.join(base, rel))
        if not os.path.exists(target):
            errors.append(f"skills/{d}/SKILL.md: broken link -> {rel}")
print(f"checked {len(folders)} skill folders, {checked} internal links")
if errors:
    print("\n".join("FAIL: " + e for e in errors))
    sys.exit(1)
print("ALL VALID ✔")
