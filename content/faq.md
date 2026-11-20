+++
title = "FAQ"
+++

# Frequently asked questions

## Why another format?

Panpak explores whether an author can ship a signed file directly, let people review its permissions and reuse content when updating it. The project judges those choices by what people can actually do with an app. [Guiding principles](/principles/)

## How does it differ from Flatpak, Snap and AppImage?

Panpak shares AppImage’s direct-file distribution and uses desktop portals familiar to Flatpak users. It bundles the app’s libraries, checks a publisher signature and installs in the user’s home. Flatpak, Snap and AppImage have mature ecosystems with many more apps available today. Flathub also has a submission review process. Panpak is pre-beta and has no equivalent review service. [Project status](https://github.com/panpak/panpak#panpak) · [Flathub submission process](https://docs.flathub.org/docs/for-app-authors/submission/)

## Is it safe to use today?

Use it for experiments with trusted software and disposable data. The format is still changing, and protection depends on your host and the permissions you grant. [Security and known limits](/security/)

## Do I need root?

Panpak installs apps, data and its runtime in your home. It needs no Panpak system service. Host tools such as bubblewrap provide parts of the sandbox. [Host requirements](https://github.com/panpak/panpak/blob/main/docs/REQUIREMENTS.md)

## Does it work on atomic distributions?

Installing in your home leaves the system image untouched. The project reports real-app tests on Bluefin. A reproducible comparison with Flatpak on Fedora Silverblue is coming soon. [Distribution support and tests](https://github.com/panpak/panpak#any-distribution-and-perfect-for-atomic-ones)

## How do I know who published a package?

Read the domain at first install and check whether it confirms the key. You can also supply a key you already trust with `--expect-key`. Panpak pins the accepted key. For a converted AppImage, the signature belongs to whoever performed the conversion. [Publisher trust](https://github.com/panpak/panpak/blob/main/PANPAK-FORMAT.md#321-confirmation-of-the-domain-normative) · [Conversion](https://github.com/panpak/panpak/blob/main/QUICKSTART.md)
