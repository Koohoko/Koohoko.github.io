---
title: "Deploying web-based code editor and Github Copilot on my local machine"
date: 2024-11-14
permalink: /posts/2024-11-14/coder_copilot
categories:
  - Misc
tags:
  - code-server
  - Github copilot
toc: true
# last_modified_at: 2024-09-01
---

I have been used [code-server](https://github.com/coder/code-server) for a while, but I never been successful in deploying Github Copilot Chat on it. Recently, Github copilot has been [upgraded](https://github.blog/news-insights/product-news/bringing-developer-choice-to-copilot/) and support Claude 3.5 Sonnet, o1-preview and o1-mini models, I am using some tricks to let it work on the code-server environment.

## Code-server

I like code-server a lot because it is a web-based code editor, once I bind it to a domain, I can access it from anywhere, using any device (including ipad and iphone!). The code-server is like a third-party fork of the official VSCode, so it makes it lack of official support of some features, like you are not able to download the Github Copilot Chat from the marketplace. 

Let's first update the code-server to the latest version following the [official guide](https://coder.com/docs/code-server/install#installsh):

```bash
# update the code-server
curl -fsSL https://code-server.dev/install.sh | sh

# start the code-server
sudo systemctl enable --now code-server@$USER
sudo systemctl restart code-server@$USER
sudo systemctl status code-server@$USER
```

You may also need to bind it to a domain, I am using cloudflared to do this, not going to detail here.

## Github Copilot and Github Copilot Chat

The [Github Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) is available on the marketplace. Just download it via `Download Extension` and drag and install it on your code-server extension panel. 

Unfortunately, the [Github Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) can not be installed in this way. But we can still use it by following the steps below:
1. Download the Github Copilot Chat from the marketplace.
2. Unzip the downloaded file, go into the extension folder.
3. Edit the `package.json` file, change the required version number, as referred [here](https://github.com/coder/code-server/issues/6625#issuecomment-1893288400)
4. Repack the extension folder, you need to use vsce to do this (`vsce package`), but you may need to install it first (`npm install -g @vscode/vsce`). Afterwards you will get the `.vsix` file.
5. Install it on the code-server and login Github account.

## Usage

Enable Anthropic Claude 3.5 Sonnet in Copilot on the [Github settings](https://github.com/settings/copilot).

Some useful shortcuts:
- `Cmd+Shift+I` to open the Github Copilot Chat
- `Cmd+I` to open the Github Copilot inline suggestions

---
