# panpak.org

The Panpak project website uses Zola. Run `zola build` to generate `public/`, or `zola serve` for a local preview. The home page is in `content/_index.md`.

GitHub Actions builds pull requests with Zola v0.20.0. A push to `main` builds and deploys the site to GitHub Pages.

## Images
The Panpak logo was designed by fabrizio (fabx-dev). The mascot images were generated with an AI image model for the Panpak project. The name "Panpak" and the logo are trademarks of the Panpak project: see TRADEMARKS.md in the main repository for how they may be used.

## Workflow diagrams

Edit the Mermaid sources in `static/images/diagrams/`, then run `python3 scripts/render-diagrams.py` with Docker and Python 3 with Pillow installed. The script runs a pinned Mermaid CLI and regenerates the full-size and 1120-pixel PNG and WebP files used on “How it works”. The shared renderer settings are in `scripts/mermaid-config.json`.

For a planned feature that now exists, remove the “Planned” prefix and the `:::planned` class on its source line to use the default blue box. Review any planned connections and update the walk-through in `content/how-it-works.md` in the same change.
