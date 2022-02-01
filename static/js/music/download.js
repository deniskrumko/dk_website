function downloadFile(filename, url) {
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
}
