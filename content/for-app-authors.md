+++
title = "For app authors"
+++

# For app authors

**Pre-beta.** Use trusted inputs and disposable test data. Please hold off on publishing packages while the format and review process are still in development.

## Prepare the tools

From a checkout of the [Panpak source](https://github.com/panpak/panpak), build the command and its companion stub. On the documented x86-64 build path, run the following in the same shell. Create your personal signing key once and keep the recovery phrase on paper.

```sh
./build.sh
export PATH="$PWD/target/x86_64-unknown-linux-musl/release:$PATH"
panpak key new
```

## From an AppImage

Substitute your local AppImage filename and app ID. Conversion packs and signs the result with your key. Inspect it to see its permissions. The recorded origin identifies the input AppImage, and the signature identifies you as the converter.

```sh
panpak convert Etcher.AppImage --id io.example.app -o app.panpak
panpak inspect app.panpak
```

If you already have an unpacked tree and manifest, the quick start builds an example directory called `hello` with a separate key called `hello.key`. After preparing those inputs, pack it directly.

```sh
panpak pack hello --stub ./target/x86_64-unknown-linux-musl/release/panpak-stub --secret-file hello.key -o hello.panpak
panpak inspect hello.panpak
```

[Quick start, including the tree and manifest](https://github.com/panpak/panpak/blob/main/QUICKSTART.md)

## From source

Use the GNOME Text Editor recipe in the [project README](https://github.com/panpak/panpak#simple-for-developers). Save it as `panpak.toml` in a recipe directory and run the following from that directory. The first build needs network access for the build environment and sources.

```sh
panpak build . -o editor.panpak
panpak inspect editor.panpak
```

The source-build notes describe the recipes tested for GNOME Text Editor, qBittorrent and Ghostty, including how the builds collect libraries and plug-ins. [Source-build notes](https://github.com/panpak/panpak/blob/main/docs/SOURCE-BUILD.md)
