+++
title = "How it works"
+++

# How it works

<img class="mascot" src="/images/box-420.webp" width="420" height="420" alt="The Panpak mascot coming out of a cardboard box.">

**Diagram legend.** Solid blue boxes exist today. Dashed yellow boxes are planned. Green boxes mark decisions about trust. Grey boxes show questions or events.

## From app to package

An author starts with the app’s existing build and records its inputs in a recipe and lockfile. Panpak collects libraries and reports modules. The author exercises a real task in the sandbox, adjusts the recipe if it fails and signs the package. Its release history, software bill of materials (SBOM) and module report travel with it.

A community recipe collection, permission tracing and a command to compare changes between releases are planned. [Source builds](https://github.com/panpak/panpak/blob/main/docs/SOURCE-BUILD.md) · [Package format](https://github.com/panpak/panpak/blob/main/PANPAK-FORMAT.md)

<a href="/diagrams/to-package.svg"><img class="diagram" src="/diagrams/to-package.svg" alt="Packaging flow from source through build, sandbox test and signing. Open the full-size diagram."></a>

## From package to user

Today you can download a signed file directly. At first install you review the permissions and decide whether to trust the publisher’s key. Panpak can check a key against the publisher’s domain or a key you already know. Updates follow the recorded origin and new permissions require confirmation.

Distribution channels, store integration and catalog search are planned. In that design, a distribution can identify the build it tested while preserving the publisher’s signature. [Publisher trust and updates](https://github.com/panpak/panpak/blob/main/PANPAK-FORMAT.md)

<a href="/diagrams/to-user.svg"><img class="diagram" src="/diagrams/to-user.svg" alt="Distribution flow from the publisher to direct download, install and updates, alongside planned stores and search. Open the full-size diagram."></a>
