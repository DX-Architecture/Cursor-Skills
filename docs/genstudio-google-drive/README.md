# GenStudio Google Drive documents

Word files you can upload to Google Drive, then open as Google Docs. Each file maps to one GenStudio guideline type.

| File | GenStudio destination |
|------|------------------------|
| `GenStudio-Brand-guidelines.docx` | Brand → Tone of voice, Brand values, Editorial guidelines, Editorial restrictions, Channel → Email |
| `GenStudio-Products.docx` | Products (one product per heading) |
| `GenStudio-Personas.docx` | Personas (WIP list) |

## Upload to Drive

1. Open [Google Drive](https://drive.google.com).
2. Drag the three `.docx` files into a folder (for example **GenStudio guidelines**).
3. Right-click each file → **Open with** → **Google Docs**.
4. Optional: **File → Save as Google Docs** so the working copy is native Docs, not Word.

Do **not** upload an entire document into a single GenStudio field. Copy each heading’s bullets into the matching field. If you upload the whole Brand file to GenStudio’s “add brand via document,” Adobe may extract intro notes and Channel lines into Tone of voice and lower Brand scores.

## Rebuild after skill edits

From this folder, with `python-docx` installed:

```bash
python3 build_docs.py
```

Source of truth remains `.cursor/skills/genstudio-email-prompts/` (`brand-guidelines.md`, `channel-guidelines.md`, `products.md`, `personas.md`).
