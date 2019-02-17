import base64
import os
import subprocess
import sys
import tempfile

from .term import term


def get_latex_image(latex, width=120, height="auto", color=(22, 22, 22)):
    doc = "\n".join(
        [
            r"\documentclass[10pt]{article}",
            r"\usepackage{geometry}",
            r"\geometry{paperwidth=15cm, paperheight=4cm, margin=0cm}",
            r"\usepackage{amsmath,amsfonts,amsthm,pagecolor,xcolor}",
            r"\begin{document}",
            r"\definecolor{bgcolor}{RGB}{%d,%d,%d}" % color,
            r"\pagecolor{bgcolor}\color{white}",
            r"\begin{center}",
            latex,
            r"\end{center}",
            r"\end{document}",
        ]
    )

    workdir = tempfile.mkdtemp()
    texfile = os.path.join(workdir, "texput.tex")
    with open(texfile, "w") as f:
        f.write(doc)

    subprocess.check_output(["pdflatex", "-output-directory=" + workdir, texfile])
    pdffile = os.path.join(workdir, "texput.pdf")
    pngfile = os.path.join(workdir, "texput.png")
    subprocess.check_output(
        ["convert", "-quiet", "-density", "300", pdffile, "-quality", "90", pngfile]
    )
    with open(pngfile, "rb") as f:
        png = f.read()

    IMAGE_CODE = "\033]1337;File=name={name};inline={inline};size={size};width={width};height={height};preserveAspectRatio={preserve_aspect_ratio}:{base64_img}\a"
    data = {
        "name": base64.b64encode("Unnamed file".encode("utf-8")).decode("ascii"),
        "inline": 1,
        "size": len(png),
        "base64_img": base64.b64encode(png).decode("ascii"),
        "width": width,
        "height": height,
        "preserve_aspect_ratio": 1,
    }
    s = IMAGE_CODE.format(**data).encode("ascii")
    return b" " * ((term.width - 120) // 2) + s


def print_image(image):
    sys.stdout.buffer.write(image)
    print()
