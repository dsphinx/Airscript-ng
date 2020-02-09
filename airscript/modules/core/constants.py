#!/usr/bin/env python3

from os import environ, path
from pathlib import Path as FilePath
from typing import List


# Pathlib file paths.
BASE_PATH = FilePath(environ.get("BASE_PATH", path.expanduser("~/.cache/airscript-ng")))
STORAGE_DIR = BASE_PATH / "storage"
AIRCRACK_BASE_PATH = BASE_PATH / "air"
MDK_BASE_PATH = BASE_PATH / "mdk"
REAVER_BASE_PATH = BASE_PATH / "wps"
PIXIEWPS_BASE_PATH = BASE_PATH / "pixiewps"
AIRODUMP_PATH = AIRCRACK_BASE_PATH / "src" / "airodump-ng"
AIRCRACK_PATH = AIRCRACK_BASE_PATH / "src" / "aircrack-ng"
AIRMON_PATH = AIRCRACK_BASE_PATH / "scripts" / "airmon-ng"
AIREPLAY_PATH = AIRCRACK_BASE_PATH / "src" / "aireplay-ng"
MDK_PATH = MDK_BASE_PATH / "src" / "mdk4"
CSV_POSTFIX = "-01.csv"
CAP_POSTFIX = "-01.cap"

# URLs of required software.
AIRCRACK_GH_URL = "https://github.com/aircrack-ng/aircrack-ng.git"
MDK_GH_URL = "https://github.com/aircrack-ng/mdk4.git"
REAVER_GH_URL = "https://github.com/t6x/reaver-wps-fork-t6x.git"
PIXIEWPS_GH_URL = "https://github.com/wiire-a/pixiewps.git"

# Static system locations
IFACES = FilePath("/sys/class/net/")

# Required Packages
DEBPKGS: List[str] = [
    "xterm",
    "gawk",
    "reaver",
    "aircrack-ng",
    "wireless-tools",
    "ethtool",
    "apt-transport-https",
    "iproute2",
    "git",
    "wget",
    "curl",
    "p7zip-full",
    "libnl-3-dev",
    "autoconf",
    "automake",
    "libtool",
    "pkg-config",
    "libsqlite3-dev",
    "libpcre3-dev",
    "shtool",
    "rfkill",
    "libc-bin",
    "openssl",
    "libgcrypt20-dev",
    "build-essential",
    "libssl-dev",
    "libpcap-dev",
    "isc-dhcp-server",
    "python3-tk",
    "python3-requests",
    "dsniff",
    "driftnet",
    "bzip2",
    "hostapd",
    "psmisc",
    "coreutils",
    "iw",
    "libcmocka-dev",
    "libhwloc-dev",
    "libnl-genl-3-dev",
    "screen",
    "tcpdump",
    "usbutils",
    "wpasupplicant",
    "zlib1g-dev"
]

# Instructions to compile
COMPILATION_STEPS: List[str] = [
    "apt",
    "apt update",
    "apt install -y {DEBPKGS}", # TODO: SORT!
    f"git clone {AIRCRACK_GH_URL} {AIRCRACK_BASE_PATH}",
    f"git clone {REAVER_GH_URL} {REAVER_BASE_PATH}",
    f"git clone {PIXIEWPS_GH_URL} {PIXIEWPS_BASE_PATH}",
    f"git clone {MDK_GH_URL} {MDK_BASE_PATH}",
    (f"cd {AIRCRACK_BASE_PATH} && autoreconf -i && "
     " ./configure --with-gcrypt && make -j$(nproc)"),
    (f"cd {REAVER_BASE_PATH / 'src'} && ./configure && "
     " make -j$(nproc)"),
    (f"cd {PIXIEWPS_BASE_PATH} && "
     " make -j$(nproc) && make install"),
    (f"cd {MDK_BASE_PATH} && "
     " make -j$(nproc)"),

]