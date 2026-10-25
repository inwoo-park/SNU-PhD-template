# SNU-PhD-template

LaTeX template for PhD dissertation at SNU (Seoul National University). Officially, SNU does not provide an official LaTeX template for dissertations. Lots of students have created their own templates.

This repository is inspired by similar LaTeX templates for PhD dissertation. You can find another example SNU PhD templates at [SNU PhD Dissertation Templates](https://github.com/snu-phd-templates). Feel free to choose the template that best fits your needs and preferences :blush:.

> [!NOTE] Other SNU PhD Dissertation Templates
> * Sungju Moon's SNU PhD Dissertation Template in overleaf : [Overleaf link](https://www.overleaf.com/latex/templates/snu-dissertation-template/fxvtwvxzdpvp)
> * Yoonsoo P. Bach's SNU PhD Dissertation Template in overleaf : [Overleaf link](https://github.com/ysBach/snu-dissertation-template)

> [!NOTE]
> If you have any questions or suggestions regarding this template, feel free to open an issue or submit a pull request on this repository. Your feedback and contributions are always welcome! :satisfied:

# Gettings started with Visual Studio Code (vscode)

* I used to work with Latex in both `vscode` and `overleaf`. If someone is new to working with latex in `vscode`, this section will provide some recommended settings and extensions to get started.

## Download vscode

* You can download and install `Visual Studio Code` from the official website.
    * Link for `Visual Studio Code` website : [Visual Studio Code download](https://code.visualstudio.com/download)

## Recommended extension for LaTeX in VSCode

* Especially, I am window guy, so I recommend using `Miktex` as the TeX distribution for Windows.

**Required packages:**

* **`Latex Workshop` in VSCODE**: A recommended VSCode extension for working with LaTeX files.
    * Link for `Latex workshop` extension : [Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
* `Miktex` : A TeX distribution for Windows.
    * `Latex Workshop` requires external latex distribution for compiling LaTeX documents.
    * Link for `Miktex` website : [Miktex download](https://miktex.org/howto/install-miktex)
* `git` : A version control system for tracking changes in source code.
    * Link for `git` website : [Git download](https://git-scm.com/downloads)

## Excluding temporary and auxiliary LaTeX files

* If you cannot find any temporary or auxiliary Latex files in your vscode's `file explorer`, it might be because they are excluded by the settings.
* You can find some vscode settings for excluding temporary and auxiliary `LaTeX` files from the file explorer in the `.vscode/settings.json` file.

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