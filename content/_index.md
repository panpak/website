+++
title = "Panpak"
+++

# A signed package for Linux apps

A `.panpak` file carries the app, its permissions and a signed index of its contents. Panpak checks the publisher’s signature at every start and runs the app in a layered sandbox, without root privileges or a separate runtime download.

<section id="status" aria-labelledby="status-title">
<h2 id="status-title">Project status <small>Pre-beta</small></h2>

### What works today

- Before you install an app, Panpak shows the permissions it requests and pins the publisher’s key when you accept. On a first install, Panpak can confirm that key against the keys the publisher lists for the app on their domain. [Install permissions](https://github.com/panpak/panpak#what-an-app-can-ask-for) · [Domain confirmation](https://github.com/panpak/panpak/blob/main/PANPAK-FORMAT.md#321-confirmation-of-the-domain-normative)
- Apps run in a layered sandbox. Bubblewrap gives each app an isolated view of the filesystem, Landlock restricts file access, and seccomp filters system calls. [Sandbox and its limits](https://github.com/panpak/panpak/blob/main/THREAT-MODEL.md)
- The store keeps one copy of each identical file, and updates reuse chunks already on disk. On 20 November 2026, a local HTTP server counted the bytes it sent to update Simplenote from 2.27.0 to 2.27.1. Panpak fetched 1.1% of the new package. [Update benchmark and method](https://github.com/panpak/panpak/blob/main/docs/BENCHMARKS.md#update-size)
- You can use `panpak convert` to turn an existing AppImage into a Panpak package that you sign yourself. [AppImage conversion guide](https://github.com/panpak/panpak/blob/main/QUICKSTART.md)
- Publishers use `panpak key new` to create a signing key and a separate recovery key. The command shows the recovery key once as a 24-word phrase. [Publisher keys](https://github.com/panpak/panpak#quick-start)
- You can build GNOME Text Editor, qBittorrent and Ghostty from source using the example recipes and their lockfiles. [Source build guide](https://github.com/panpak/panpak/blob/main/docs/SOURCE-BUILD.md)

### What to expect

The format can change. There are no releases, registry or package review process yet. Please keep experiments away from important data and untrusted software, and hold off on publishing packages.

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
