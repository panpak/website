+++
title = "Security"
+++

# Security

## What the signature tells you

Panpak checks the signature on the manifest and file index. It checks the contents against that index when preparing the app and checks the signature and pinned key again at launch. A signature identifies a signing key. A publisher can still sign harmful software.

On first install, check the domain shown or supply an expected key obtained independently. Accepting an unfamiliar key pins it for later use. A look-alike domain or a compromised publisher website can mislead you. A process already running as you outside the sandbox can change your local store. [Threat model](https://github.com/panpak/panpak/blob/main/THREAT-MODEL.md)

## What the sandbox limits

Bubblewrap limits the folders an app can see. Landlock restricts access to files, seccomp blocks selected system calls, and a private desktop message bus limits which services the app can reach. Where supported, the document portal gives the app access to files you choose.

The protection depends on the host and on the permissions you accept. Without bubblewrap, the isolated filesystem view is missing. X11 access can expose other windows and keystrokes. Audio access includes the microphone, and a writable folder lets the app change its contents. Use `panpak doctor` to see which layers are available. [Full list of known limits](https://github.com/panpak/panpak/blob/main/THREAT-MODEL.md#5-known-limitations)

## Report a vulnerability

Send a private report to [security@panpak.org](mailto:security@panpak.org). Include the affected version, the setup and what you observed so maintainers can investigate. [Reporting policy](https://github.com/panpak/panpak/blob/main/SECURITY.md) · [Machine-readable contact](/.well-known/security.txt)
