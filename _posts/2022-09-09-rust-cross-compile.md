---
title: "Cross-compiling Rust programs (for Linux and Windows) on Mac OS"
date: 2022-09-09
permalink: /posts/2022-09-09/rust-cross-compile
categories:
  - Programming
tags:
  - Rust
# last_modified_at: 2022-09-01
---

This post records the essential steps for cross-compiling Rust programs (for Linux and Windows) on Mac OS.

### Install prerequisites
```shell
rustup target add x86_64-unknown-linux-musl
brew install filosottile/musl-cross/musl-cross
ln -s /usr/local/bin/x86_64-linux-musl-gcc /usr/local/bin/musl-gcc

rustup target add x86_64-pc-windows-gnu
brew install mingw-w64
```

### Add config
add to `~/.cargo/config`
```
[target.x86_64-unknown-linux-musl]
linker = "x86_64-linux-musl-gcc"
[target.x86_64-pc-windows-gnu]
linker = "x86_64-w64-mingw32-gcc"
ar = "x86_64-w64-mingw32-gcc-ar"
```

### Compiling

```
# Linux
CROSS_COMPILE=x86_64-linux-musl- cargo build --release --target x86_64-unknown-linux-musl
# Windows
cargo build --release --target x86_64-pc-windows-gnu
```
