<h1 align="center">
  <img src="data/logo.png" alt="Magnus">
  <br />
  Magnus
</h1>

<p align="center"><b>A very simple screen magnifier.</b></p>

![Magnus Screenshot](data/screenshot.png?raw=true)

<p align="center">Made with 💝 for <img src="https://raw.githubusercontent.com/anythingcodes/slack-emoji-for-techies/gh-pages/emoji/tux.png" align="top" width="24" /></p>

## Building, Testing, and Installation

### Ubuntu

A [PPA for Magnus](https://launchpad.net/~flexiondotorg/+archive/ubuntu/magnus) is published by [Martin Wimpress](https://github.com/flexiondotorg).

```bash
sudo add-apt-repository ppa:flexiondotorg/magnus
sudo apt update
sudo apt install magnus
```

There's also an Ansible deployment by Taha Ahmed at [codeberg](https://codeberg.org/ansible/magnus).

### Source

You'll need the following dependencies:

  * `gir1.2-gdkpixbuf-2.0`
  * `gir1.2-glib-2.0`
  * `gir1.2-gtk-3.0`
  * `gir1.2-keybinder-3.0`
  * `python3`
  * `python3-gi`
  * `python3-setproctitle`

Run `setup.py` to build and install Magnus:

```bash
sudo python3 setup.py install
```
