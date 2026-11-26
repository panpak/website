+++
title = "How it works"
description = "Follow a Linux app from source or AppImage to a signed Panpak package, then see how Panpak verifies, installs and runs it."
+++

<div class="workflow-intro">
<div>

# How it works

[From app to package](#from-app-to-package) · [From package to user](#from-package-to-user) · [When an app does not start](#when-an-app-does-not-start)

</div>
<img class="mascot" src="/images/box-420.webp" width="420" height="420" alt="The Panpak mascot coming out of a cardboard box.">
</div>

## From app to package

{{ workflow(slug="from-app-to-package", title="From app to package", width=1858, height=3700) }}

1. For a first release, the author or curator prepares a recipe. For a new upstream release, start with the previous recipe. Build a candidate, check its libraries with `panpak doctor`, and use the module report to identify plug-ins. A planned command, `panpak trace`, would record permissions used during a real task.
2. Test the features people need. If a test fails, use the report to correct the recipe, rebuild and try again. When the tests pass, the publisher reviews the results or the changes since the last release. A planned `panpak diff` would highlight new permissions and libraries.
3. The author signs with the key for the app’s domain-based ID. Community signing policy is still open: a curator might use their own ID and credit, or use the author’s ID with verified delegation. The signed release includes a software bill of materials, release history and module report. Independent rebuild verification is planned.

## From package to user

{{ workflow(slug="from-package-to-user", title="From package to user", width=2014, height=4200) }}

1. Get the signed package from the author’s website or release page. General catalogs, distribution-tested channels and store integration are planned. Panpak verifies the signature, then checks the publisher’s key against the app’s domain or a key supplied with `--expect-key`. Confirmation through a distribution catalog is planned.
2. The publisher check has three results: **contradicted (install stops)**, **not confirmed (the key is shown and the user decides)**, **confirmed**. Review the publisher, permissions and update source before accepting. If you decline, installation ends. If you accept, Panpak installs the app and records where to get updates.
3. Panpak looks for updates at the recorded source and checks the signature, publisher and permissions. It asks before granting new permissions. A failed check or a declined change keeps the installed version. An accepted update takes effect when the app closes.

## When an app does not start

If an app closes right after you start it, crashes while starting, or is stopped by the system, Panpak tells you with a notification titled “App didn’t start”. The notification says why in one sentence (for example “The app closed right after starting (error code 3).”). The reason is always Panpak’s own words, never text taken from the app.

If the app wrote something before it stopped, the notification has a button **Show details** that opens the last part of what it wrote. That file can contain personal data: read it before you send it to anyone. The notification is a banner and does not stay in your list.

If the same version fails twice in a row and an earlier version had been working, Panpak asks whether to go back to the earlier version or try again. Going back keeps your documents as they are.

**Known limits.** If you start the app from a terminal, the reason is written in the terminal and there is no “didn’t start” notification, but the question about going back can still appear. A problem inside the sandbox setup is shown as “closed right after starting (error code 1)”, and the real reason is in the details. “Show details” opens the file with your desktop’s default program: on GNOME it is chosen by the file name; on a desktop that looks at the content, an app could make its log open in another program, such as a browser.

[Source: dialogs and notifications](https://github.com/panpak/panpak/blob/ee58ce53e8806208a7109ae922d448f63dc4879e/docs/DIALOGS.md#an-app-that-did-not-start-a-notification-with-or-without-those-tools)
