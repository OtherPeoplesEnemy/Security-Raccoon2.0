# 🦝 Security Raccoon Installer

A modular, menu-driven Python installer for building your own Fedora-based pentesting distro — inspired by Kali Linux, but fully customizable.

---

## 🚀 Features

- 🔹 Interactive CLI (powered by [rich](https://github.com/Textualize/rich))
- 🔹 Install core tools like `nmap`, `sqlmap`, `ffuf`, `john`, etc.
- 🔹 Active Directory tools like `CrackMapExec`, `ldapsearch`, `kerbrute`, `BloodHound`, `Rubeus`, and more
- 🔹 Cloud tools like `CloudFox`, `Sublist3r`, `httpx`
- 🔹 C2 Frameworks: Sliver and Empire
- 🔹 Optional KDE desktop setup with raccoon-themed customization
- 🔹 Modular Python code (easy to maintain or extend)

---

## 🛠 Installation

### Step 1: Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/security-raccoon.git
cd security-raccoon
```

### Step 2: Run the setup script

```bash
chmod +x setup.sh
./setup.sh
```

### Step 3: Launch the installer

```bash
python3 installer.py
```

---

## 📁 Modules

| Module        | Description                      |
|---------------|----------------------------------|
| `core_tools`  | Basic pentesting tools           |
| `ad_tools`    | Active Directory enumeration     |
| `cloud_tools` | Recon and AWS-focused tooling    |
| `c2s`         | C2 Frameworks (Empire, Sliver)   |
| `kde_setup`   | Desktop, wallpaper, prompt setup |

---

## ✅ Dependencies

- Fedora 38/39/40+
- Python 3.8+
- `dnf`, `pip`, `go`, `git`, `wget`

---

## 📦 License

MIT – Customize and share freely. Built by and for hackers, sysadmins, and raccoons. 🦝

---

> Pull requests and new module suggestions welcome!
