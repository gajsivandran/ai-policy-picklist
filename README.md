# SEFS Course Delivery dashboard

A password-protected copy of the SEFS course-delivery dashboard (SEFS compared with the rest of the College of the Environment, 2004-05 to 2024-25), rebuilt from archived UW Time Schedule pages.

> **Preliminary data, not QA/QC'd.** Use it for larger trends only. Any fine-resolution analysis (individual courses, instructors or quarters) needs to be redone with verified registrar data.

## How the protection works

GitHub Pages can only serve static files, so it cannot check a password on a server. Instead, `index.html` contains the dashboard **encrypted** (AES-256-GCM, key derived from the password with PBKDF2-SHA256, 600,000 iterations). The page shows a password box and decrypts the dashboard in the browser only when the right password is entered.

- The repository and the page can be public: without the password, the file holds only unreadable data.
- The protection is only as strong as the password. Use a long one (the tool requires 12+ characters).
- "Remember on this device" stores the decryption key in that browser's local storage. Anyone using that browser profile can open the page without typing the password.
- Anyone who has the password can view, save or forward the decrypted page. Share the password separately from the link, and only with people who should see it.

## Files

| File | Put on GitHub? | Purpose |
|---|---|---|
| `index.html` | Yes | The encrypted dashboard with its password page |
| `encrypt-tool.html` | Yes (optional) | Re-encrypts the dashboard with a new password, entirely in your browser |
| `README.md` | Yes | This file |
| `.nojekyll` | Yes | Tells GitHub Pages to serve files as they are |
| `.gitignore` | Yes | Stops the unencrypted file and name keys from being committed by accident |
| `dashboard-plain.html` | **No** | The unencrypted dashboard. Keep it on your computer only |

Never upload `dashboard-plain.html` or any `faculty_key_PRIVATE*.csv` file.

## Publish on GitHub Pages (web interface, no command line)

1. On github.com, click **New repository**. Give it a name (for example `sefs-dashboard`) and create it.
2. Click **Add file → Upload files**. Drag in `index.html`, `encrypt-tool.html`, `README.md`, `.nojekyll` and `.gitignore`, then click **Commit changes**.
   - Files starting with a dot can be hidden in Windows Explorer. They are optional; the site works without them.
3. Go to **Settings → Pages**. Under **Build and deployment**, set **Source** to *Deploy from a branch*, choose branch `main` and folder `/ (root)`, and click **Save**.
4. After a minute or two, the page appears at `https://<your-username>.github.io/<repository-name>/`.

A private repository can also host Pages on some paid GitHub plans. On a free plan the repository must be public, which is fine because the dashboard is encrypted.

## Change the password

1. Open `encrypt-tool.html` from your computer (double-click it).
2. Choose `dashboard-plain.html`, type the new password twice, and click **Create index.html**.
3. Upload the downloaded `index.html` to the repository, replacing the old one.

Changing the password does not remove copies anyone has already saved, and devices that chose "Remember" will be asked for the new password.

## Update the dashboard

To publish a newer version of the dashboard, replace `dashboard-plain.html` with the new unencrypted file and repeat **Change the password** (you can reuse the same password).
