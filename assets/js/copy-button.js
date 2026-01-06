document.addEventListener('DOMContentLoaded', () => {
  // Add copy button to all code blocks
  document.querySelectorAll('div.highlighter-rouge, figure.highlight').forEach((codeBlock) => {
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.type = 'button';
    button.innerHTML = '<i class="fas fa-copy"></i> Copy';

    button.addEventListener('click', () => {
      const code = codeBlock.querySelector('code');
      if (code) {
        navigator.clipboard.writeText(code.innerText).then(() => {
          // Visual feedback
          button.innerHTML = '<i class="fas fa-check"></i> Copied!';
          button.classList.add('copied');
          setTimeout(() => {
            button.innerHTML = '<i class="fas fa-copy"></i> Copy';
            button.classList.remove('copied');
          }, 2000);
        }).catch(() => {
          // Fallback for older browsers
          const textArea = document.createElement('textarea');
          textArea.value = code.innerText;
          document.body.appendChild(textArea);
          textArea.select();
          document.execCommand('copy');
          document.body.removeChild(textArea);
          button.innerHTML = '<i class="fas fa-check"></i> Copied!';
          button.classList.add('copied');
          setTimeout(() => {
            button.innerHTML = '<i class="fas fa-copy"></i> Copy';
            button.classList.remove('copied');
          }, 2000);
        });
      }
    });

    codeBlock.style.position = 'relative';
    codeBlock.appendChild(button);
  });

  // Add line numbers to code blocks
  document.querySelectorAll('div.highlighter-rouge pre code, figure.highlight pre code').forEach((codeBlock) => {
    // Only add line numbers if there are multiple lines
    const lines = codeBlock.innerHTML.split('\n');
    if (lines.length > 3) {
      const numberedLines = lines.map((line, index) => {
        // Don't add number to the last empty line
        if (index === lines.length - 1 && line.trim() === '') {
          return line;
        }
        return `<span class="line-number">${index + 1}</span>${line}`;
      }).join('\n');
      codeBlock.innerHTML = numberedLines;
    }
  });
});