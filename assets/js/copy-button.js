document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre').forEach((codeBlock) => {
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.type = 'button';
    button.innerText = 'Copy';

    button.addEventListener('click', () => {
      const code = codeBlock.querySelector('code');
      navigator.clipboard.writeText(code.innerText).then(() => {
        button.innerText = 'Copied!';
        setTimeout(() => {
          button.innerText = 'Copy';
        }, 2000);
      });
    });

    codeBlock.appendChild(button);
  });
});