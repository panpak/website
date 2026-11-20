+++
title = "Panpak"
+++

<section class="hero">
<div class="hero-copy">

# A signed package for Linux apps

A `.panpak` file carries the app, its permissions and a signed index of its contents.

<div class="actions"><a href="/how-it-works/">How it works</a><a href="/for-app-authors/">Try it</a></div>
</div>
<img class="mascot wave" src="/images/wave-420.webp" srcset="/images/wave-240.webp 240w, /images/wave-420.webp 420w, /images/wave-640.webp 640w" sizes="(max-width: 650px) 160px, (max-width: 1000px) 32vw, 360px" width="420" height="420" alt="The Panpak robot waves, with a package for a head and the Panpak logo on its chest.">
</section>

## Why Panpak

- Panpak works out library dependencies and reports plug-ins today, while automatic permission tracing is planned.
- The publisher signs the manifest and content index, so someone with the expected public key can check a downloaded package offline.
- A static website can serve the package, and Panpak installs it in your home without root or a Panpak system service.

<section id="status" aria-labelledby="status-title">
<h2 id="status-title">Project status <small>Pre-beta</small></h2>

<div class="status-columns">
<div class="today">

### What works today

- Before you install an app, Panpak shows the permissions it requests and pins the publisher’s key when you accept. On a first install, Panpak can confirm that key against the keys the publisher lists for the app on their domain. <span class="trust">[Install permissions](https://github.com/panpak/panpak#what-an-app-can-ask-for) · [Domain confirmation](https://github.com/panpak/panpak/blob/main/PANPAK-FORMAT.md#321-confirmation-of-the-domain-normative)</span>
- Panpak checks the publisher’s signature at every start and runs the app in a layered sandbox, without root privileges or a separate runtime download. Bubblewrap gives each app an isolated view of the filesystem, Landlock restricts file access, and seccomp filters system calls. [Sandbox and its limits](https://github.com/panpak/panpak/blob/main/THREAT-MODEL.md)
- The store keeps one copy of each identical file, and updates reuse chunks already on disk. On 20 November 2026, a local HTTP server counted the bytes it sent to update Simplenote from 2.27.0 to 2.27.1. Panpak fetched 1.1% of the new package. [Update benchmark and method](https://github.com/panpak/panpak/blob/main/docs/BENCHMARKS.md#update-size)
- You can use `panpak convert` to turn an existing AppImage into a Panpak package that you sign yourself. [AppImage conversion guide](https://github.com/panpak/panpak/blob/main/QUICKSTART.md)
- Publishers use `panpak key new` to create a signing key and a separate recovery key. The command shows the recovery key once as a phrase to keep on paper. <span class="trust">[Publisher keys](https://github.com/panpak/panpak#quick-start)</span>
- You can build GNOME Text Editor, qBittorrent and Ghostty from source using the example recipes and their lockfiles. [Source build guide](https://github.com/panpak/panpak/blob/main/docs/SOURCE-BUILD.md)

</div>
<div class="roadmap">

### On the roadmap

| Planned support | Project step |
| --- | --- |
| Graphical Panpak app | 10b |
| Apps with embedded browsers | 12 |
| Terminal programs | 14 |

These steps describe the order of work. They have no promised release dates.

</div>
</div>

### What to expect

The format can change. There are no releases, registry or package review process yet. Please keep experiments away from important data and untrusted software, and hold off on publishing packages.

</section>

## Explore the project

App authors can start with the [source build guide](https://github.com/panpak/panpak/blob/main/docs/SOURCE-BUILD.md). For reviewers, the [threat model](https://github.com/panpak/panpak/blob/main/THREAT-MODEL.md) describes the sandbox and its known limits. Volunteers can explore the [guiding principles](https://github.com/panpak/panpak/blob/main/docs/PRINCIPLES.md) and [project roadmap](https://github.com/panpak/panpak#roadmap).

## Coming soon

A reproducible comparison with Flatpak on Fedora Silverblue and a guide to the package specification are planned.
