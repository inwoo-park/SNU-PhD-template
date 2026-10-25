# SNU-PhD-template

Latex template for PhD dissertation at SNU (Seoul National University)

This repository is inspired by PUT ANOTHER similar tempaltes for PhD dissertation


# vscode settings

* You can find some vscode settings for excluding temporary and auxiliary LaTeX files in the `.vscode/settings.json` file.

```json
{
    ...
    "files.exclude": {
        // Latex related temporary and auxiliary files to exclude from the file explorer
        "*.aux": true,
        "*.bbl": true,
        "*.blg": true,
        "*.fdb_latexmk": true,
        "*.fls": true,
        "*.log": true,
        "*.lof": true,
        "*.lot": true,
        "*.out": true,
        "*.toc": true,
        "*.synctex.gz": true,
    }
    ...
}
```