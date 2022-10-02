// returns a color pallette from img file

const path = require("path");
const fs = require("fs/promises");
const { promisify } = require("util");
const getPixels = promisify(require("get-pixels"));
const { createCanvas } = require("canvas");
const Color = require("canvas-sketch-util/color");
const { quantize } = require("gifenc");

(async () => {
  const outdir = path.resolve(process.cwd(), "output");
  const outfile = `outfile.png`;
  const pixels = await getPixels(path.resolve(outdir, outfile));

  const n = 8;
  const palette = quantize(pixels.data, n);

  const canvas = createCanvas(512, 512);
  const tileWidth = canvas.width / n;
  const context = canvas.getContext("2d");

  for (let i = 0; i < palette.length; i++) {
    const color = palette[i];
    const hex = Color.parse(color).hex;
    context.fillStyle = hex;
    context.fillRect(i * tileWidth, 0, tileWidth, canvas.height);
  }

  const buf = canvas.toBuffer();
  await fs.writeFile(path.join(outdir, `palette.png`), buf);
})();
