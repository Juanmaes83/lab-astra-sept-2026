# Reference Media

Store benchmark/reference media here with provenance notes.

## Suggested structure

```text
references/
├── solace-astra/
│   ├── images/
│   ├── videos/
│   └── MANIFEST.md
└── torrevieja/
    ├── images/
    ├── maps/
    └── MANIFEST.md
```

## SOLACE / Thomas-Astra

Upload the original 7 images + 2 videos used in the benchmark analysis.

Keep originals whenever practical. Do not rename manually unless needed; update `MANIFEST.md` after upload with:
- filename;
- media type;
- purpose;
- source/origin note;
- date received;
- whether it is a benchmark/reference only;
- checksum if available.

## Torrevieja / geospatial

Store only reference media/data that is permitted for the intended use.

Google Photorealistic 3D Tiles should not be copied into this repository as extracted assets. Keep Google as a live visualization/reference layer under its platform terms.

## Secrets

Never upload API keys, tokens, auth files or `.env` files alongside references.
