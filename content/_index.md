+++
title = "Panpak"
+++

# A signed package for Linux apps

A `.panpak` file carries the app, its permissions and a signed index of its contents. Panpak checks the publisher’s signature at every start and runs the app in a layered sandbox, without root privileges or a separate runtime download.

<section id="status" aria-labelledby="status-title">
<h2 id="status-title">Project status <small>Pre-beta</small></h2>

### What works today

App authors can explore source builds for GNOME Text Editor, qBittorrent and Ghostty. A recipe and lockfile describe the build. At install, Panpak shows the permissions and pins the publisher’s key.

### What to expect

The format can change. There are no releases, registry, key policy or package review process yet. Please keep experiments away from important data and untrusted software, and hold off on publishing packages.

### On the roadmap

| Planned support | Project step |
| --- | --- |
| Graphical Panpak app | 10b |
| Apps with embedded browsers | 12 |
| Terminal programs | 14 |

These steps describe the order of work. They have no promised release dates.

</section>

## Explore the project

App authors can start with the [source build guide](https://github.com/panpak/panpak/blob/main/docs/SOURCE-BUILD.md). For reviewers, the [threat model](https://github.com/panpak/panpak/blob/main/THREAT-MODEL.md) describes the sandbox and its known limits. Volunteers can explore the [guiding principles](https://github.com/panpak/panpak/blob/main/docs/PRINCIPLES.md) and [project roadmap](https://github.com/panpak/panpak#roadmap).
